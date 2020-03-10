import importlib
import sys
import os
import core.globals                                 # Globally accessible Dicts with config defaults -> create Dicts (import this in all views to have access to the data)
import config.config                                # User configuration with user specific config and additional User Data -> change Dicts
import core.webapi                                  # Functions that can be accessed via the address bar of the browser
import remi


class WebApp(remi.server.App):

    def __init__(self, *args, **kwargs):
        static_path = sys.path[0] + core.globals.config['rel_path_to_static']
        super().__init__(static_file_path={'static': static_path}, *args, **kwargs)


    def main(self):

        self.views = {}         # All views for the App Instance reside here

        # Insert the headdata from config
        self.page.children['head'].add_child('additional_headdata', core.globals.config['headdata'])

        # Insert the API Widget for access via HTML Links
        # The ID attribute tells the sub url where remi can find the API class. Next url part is method name: http://ip:port/api/method?para1=para?para2=para
        self.api = core.webapi.Webapi(attributes={'id': 'api'}, AppInst=self)

        # The base Widget is our absolute root of the GUI which is returned (Internal App root is self.root)
        # margin: 0px auto centers the view, padding: 10 px holds a distance of 10px around the screen for the views. box-sizing: border-box forces padding only to be active inside container
        self.base = remi.gui.Container(style={'margin': '0px auto' ,'padding': str(core.globals.config['base_padding']) + 'px', 'box-sizing': 'border-box'})

        # Load all views in Dict (-> key=name of view lowercase, value=instance of the view container)
        self.loadViews('views', self.views)

        # After reading all available views build up the navbar automatically
        # Every view contains attributes which define in which Menu it should be shown and with which Menu Text
        import views._navbar                                        # Import the navbar file
        self.navbar = views._navbar.Container(AppInst=self)         # Create a navbar Instance
        self.base.append(key='navbar', value=self.navbar)           # Add the navbar to the base widget

        # The content Widgets holds the view widget. The view Widget holds the Views.
        # When we switch the view, we just remove the actual view widget from content widget and add another one from self.views[name]
        heightdiff = str(core.globals.config['navbar_height'] + 4 * core.globals.config['base_padding']) + 'px'
        self.content = remi.gui.Container(style={'min-height': 'calc(100vh - ' + heightdiff + ')'})  # 100vh = Viewport height - navbar_height - 4 * base_padding

        # Append the content widget to base widget
        self.base.append(key='content', value=self.content)

        # Append the already created Start View to the content Container for Session Startup
        self.content.append(key='view', value=self.views['start'])

        # Return the base widget
        return self.base


    def idle(self):
        # Every View has to have an update Method. It can be left empty if not needed.
        # When App is idle the App keeps running this method again and again (useful for updates)
        self.content.children['view'].updateView()


    def uiControl(self, emittingWidget, view):
        # emittingWidgets is needed in Case that the method is bound to an widget event directly

        self.content.remove_child(self.content.children['view'])        # Remove the old view from content widget
        if view in self.views.keys():
            self.views['start'].hintbox.set_text('')
            self.content.append(key='view', value=self.views[view])     # If view is existent, show it (add to content widget)
        else:
            self.views['start'].hintbox.set_text('The requested View is not available!')
            self.content.append(key='view', value=self.views['start'])  # If view is not existent, switch to start view. You could also stay in actual view

    # todo: create arg for loading a fresh instance of a view and not the existing one.

    def loadViews(self, relative_src_folder, target_dict):

        # Load all Views from src folder
        filelist = os.listdir(sys.path[0] + '//' + relative_src_folder)
        i = len(filelist) - 1

        while i >= 0:
            if filelist[i][0:1] == '_':                                     # Remove Elements with leading Underscore (e.g. _underDevelopment.py)
                del filelist[i]
            i = i - 1

        for element in filelist:
            element = element.lower()                                                        # Standarize the filename to lowercase
            element = element.replace('.py', '')                                             # Remove .py ending
            #elementClassName = element[0].upper() + element[1:]                              # Dynamically build up Class name (First letter uppercase)
            elementClassName ="Container"                                                    # New Remi Editor Function exports Views always with Classname 'Container'
            importedView = importlib.import_module(relative_src_folder + '.' + element)      # Import the view module from views
            viewClass = getattr(importedView, elementClassName)                              # Get the Class by Name from the module (as an reference)
            target_dict[element] = viewClass(AppInst=self)                                   # Instanciate the view via the reference and store it in target dict. Pass App Instance as arg.


    def showDialog(self, emittingWidget, dialogname):
        # Shows a view as a dialog
        # Insert seperation layer with transparency over the actual view (append it on top of self.base container)
        self.layer = remi.gui.Container(width='100%', height='calc(100vh)', style={'position': 'absolute', 'top': '0px', 'left': '0px', 'background-color': 'rgba(255, 0, 0, 0.6)'})
        self.base.append(key='layer', value=self.layer)                         # Set layer on top of the base Container

        #dialogClassName = dialogname[0].upper() + dialogname[1:]               # Create a dynamic instance of the dialog. It will be thrown away after showing up
        dialogClassName = 'Container'                                           # You can draw dialogs with remi editor. The Class will be named always 'Container'
        viewmodule = importlib.import_module('dialogs.' + dialogname)
        viewclass = getattr(viewmodule, dialogClassName)
        self.layer.append(key=dialogname, value=viewclass(AppInst=self))        # Append the dynamic dialog on top of the layer


    def hideDialog(self):
        self.base.remove_child(self.layer)      # Remove the layer from the base Container
        del self.layer                          # Delete the layer and all of its children (=dialog)



############# Example Code for User examples. Not needed for the template.
    def printSentences(self, emittingWidget, amount):
        # This method belongs to view 'sentences' and is an example for using options in URLs and is called by webapi.Webapi.sentences(self, amount)
        output = ''
        sentence = 'THE QUICK BROWN FOX JUMPED OVER THE LAZY DOGS BACK 1234567890'
        i = 1

        while i <= int(amount):
            output = output + sentence + '\n'
            i = i + 1

        self.views['sentences'].textbox_sentences.set_value(output)         # All view Instances live in memory. You can change the value from here
        self.uiControl(emittingWidget, view='sentences')                    # Switch the view to sentences (in views/sentences.py)


def startApp():
    # Function that starts the REMI App. You can integrate the entire GUI by just calling this function. If you spawn a new thread its non blocking.
    remi.server.start(core.webapp.WebApp,
                      address=core.globals.config['address'],
                      port=core.globals.config['port'],
                      multiple_instance=core.globals.config['multiple_instance'],
                      debug=core.globals.config['debug'],
                      start_browser = core.globals.config['start_browser'],
                      enable_file_cache=core.globals.config['enable_file_cache'],
                      update_interval = core.globals.config['update_interval'],
                      certfile = core.globals.config['rel_path_to_ssl_certfile'],
                      keyfile = core.globals.config['rel_path_to_ssl_keyfile'],
                      ssl_version = core.globals.config['use_ssl_version'])

