import os, sys, logging, importlib
import core.globals                                 # Globally accessible Dicts with config defaults -> create Dicts (import this in all views to have access to the data)
import config.config                                # User configuration with user specific config and additional User Data -> change Dicts
import core.webapi                                  # Functions that can be accessed via the address bar of the browser
import helpers.connections
import remi



class WebApp(remi.server.App):

    def __init__(self, *args, **kwargs):
        static_path = sys.path[0] + core.globals.config['rel_path_to_static']

        self.logger = logging.getLogger('remi.app')
        self.views = {}                                     # All views for the App Instance reside here
        self.connection_established = False                 # Connection Flag
        self.connect_time = None                            # Timestamp when a connection was established
        self.disconnect_time = None                         # Timestamp when a connection was closed

        super().__init__(static_file_path={'static': static_path}, *args, **kwargs)


    def _process_all(self, func):                   # Overload _process_all method for routing
        # print(f'{func}')                            # Debug log the Url Part after the origin Url

        # Skip Urls with : in it, because these are remi ressources like res:img/test.jpg etc.
        if not ':' in func:
            # Catch "naked" foreign identifier added to the url like 127.0.0.1:8080/?fbclid=135454635461321651321654
            if '?' in func:
                temp = func.split('?')
                if temp[0] == '/':
                    remi.server.App._process_all(self, '/')     # Call the original _process_all without all the url additions

                    for element in temp:                        # Handle variables in url
                        if 'fbclid' in element:
                            content = element.split('=')
                            self.logger.info(f'Facebook Click ID detected (content: {content[1]})')

                        if 'myvar' in element:
                            self.logger.info('Somebody triggered myvar')

            # Catch URLS and route them to views -> when we do this, the normal API widget isn't working anymore.
            temp = func.split('/')
            if temp[1] != '' and temp[1] != 'favicon.ico':

                if temp[1] == 'api':                                        # Skip URL parts starting with API for the API widget
                    remi.server.App._process_all(self, func)                # Pass the original url to the process all method
                else:
                    remi.server.App._process_all(self, '/')                 # Call the original _process_all without all the url additions
                    helpers.connections.client_route_url_to_view[self.session] = str(temp[1])   # Store the first part of url extension for later switching to view
                    return

        # For all other cases the origin URL stays untouched just call the original handler
        remi.server.App._process_all(self, func)


    def main(self):

        # Debug Infos
        # print(f'Session ID: {self.session}')        # Direct access to session id
        # print(f'{remi.server.clients.items()}')     # Dict with session id as key and WebApp instance as value

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

        helpers.connections.handle_connections(AppInst=self)                        # Manage incoming and terminating connections

        # Check if there is a pending view switch coming from URL routing
        if self.session in helpers.connections.client_route_url_to_view.keys() and self.connection_established == True:
            view = helpers.connections.client_route_url_to_view[self.session]       # Store the view given via URL
            del helpers.connections.client_route_url_to_view[self.session]          # Delete the switching request from Dict
            self.uiControl(self, view)                                              # Finally switch to the view

        if self.connection_established == True:                                     # Call the updateView method of the active view if connection is alive
            self.content.children['view'].updateView()


    def uiControl(self, emittingWidget, view):
        # emittingWidgets is needed in Case that the method is bound to an widget event directly

        if hasattr(self, 'base'):
            if 'view' in self.base.children.keys():
                self.content.remove_child(self.content.children['view'])        # Remove the old view from content widget

        if view in self.views.keys():
            self.logger.info(f'session <{self.session}> switched to view {view}')
            self.content.append(key='view', value=self.views[view])     # If view is existent, show it (add to content widget)
        else:
            self.logger.info(f'session <{self.session}> tried to switch to view {view} which is not available.')
            self.content.append(key='view', value=self.views['error_view_not_found'])  # If view is not existent, switch to start view. You could also stay in actual view


    def loadViews(self, relative_src_folder, target_dict):

        # Load all Views from src folder
        filelist = os.listdir(sys.path[0] + '/' + relative_src_folder)
        i = len(filelist) - 1

        while i >= 0:
            if filelist[i][0:1] == '_':                                     # Remove Elements with leading Underscore (e.g. _underDevelopment.py)
                del filelist[i]
            i = i - 1

        for element in filelist:
            element = element.lower()                                                        # Standarize the filename to lowercase
            element = element.replace('.py', '')                                             # Remove .py ending
            elementClassName ="Container"                                                    # New Remi Editor Function exports Views always with Classname 'Container'
            importedView = importlib.import_module(relative_src_folder + '.' + element)      # Import the view module from views
            viewClass = getattr(importedView, elementClassName)                              # get the Container class from module and store as reference
            target_dict[element] = viewClass(AppInst=self)                                   # Instanciate the view via the reference and store it in target dict. Pass App Instance as arg.


    def showDialog(self, emittingWidget, dialogname, **kwargs):
        # Shows a view as a dialog
        # Insert seperation layer with transparency over the actual view (append it on top of self.base container)
        self.layer = remi.gui.Container(width='100%', height='calc(100vh)', style={'position': 'absolute', 'top': '0px', 'left': '0px', 'background-color': 'rgba(255, 0, 0, 0.6)'})
        self.base.append(key='layer', value=self.layer)                                     # Set layer on top of the base Container
        dialogClassName = 'Container'                                                       # You can draw dialogs with remi editor. The Class will be named always 'Container'
        viewmodule = importlib.import_module('dialogs.' + dialogname)                       # Import the view module
        viewclass = getattr(viewmodule, dialogClassName)                                    # get the Container class from module and store as reference
        self.layer.append(key=dialogname, value=viewclass(AppInst=self, **kwargs))          # Append the dynamic dialog on top of the layer


    def hideDialog(self):
        self.base.remove_child(self.layer)                                                  # Remove the layer from the base Container
        del self.layer                                                                      # Delete the layer and all of its children (=dialog)



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

