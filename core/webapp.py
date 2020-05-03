import importlib
import datetime
import time
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

        self.views = {}                             # All views for the App Instance reside here
        self.connection_established = False         # Connection Flag
        self.connect_time = None                    # Timestamp when a connection was established
        self.disconnect_time = None                 # Timestamp when a connection was closed

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
        # Every View has to have an update Method. It can be left empty if not needed.
        # When App is idle the App keeps running this method again and again (useful for updates)

        # Take care of the connection. It is only alive if the websocket still is active.
        # Check, if there is a new websocket connection for this App session (= Instance)
        if self.connection_established == False and len(self.websockets) == 1:

            for session_id, app_inst in remi.server.clients.items():
                if session_id == self.session:
                    print(f'New incoming Connection:')
                    print(f'---------------------------------------------------')
                    print(f'Session ID    : {self.session}')

                    for ws_client in app_inst.websockets:
                        print(f'ClientIP      : {ws_client.client_address} (type: {type(ws_client.client_address)})')
                        print(f'Client Headers:')
                        print(f'---------------------------------------------------')
                        print(f'{ws_client.headers} (type: {type(ws_client.headers)})')
                        print(f'---------------------------------------------------')

                        core.globals.config['connected_clients'][self.session] = ws_client.client_address
                        core.globals.config['number_of_connected_clients'] = core.globals.config['number_of_connected_clients'] + 1
                        print('Connected clients (' + str(core.globals.config['number_of_connected_clients']) + ' in total): ' + str(core.globals.config['connected_clients']))

            self.connect_time = datetime.datetime.now()
            self.connection_established = True                  # Set Flag. This can be used by other threads as end signal.

        # Check, if the websocket connection is still alive. REMI removes the Websocket from the List if dead.
        if len(remi.server.clients[self.session].websockets) == 0 and self.connection_established == True:
            print(f'Client for session <{self.session}> has disconnected.')
            self.connection_established = False                 # Set Flag. This can be used by other threads as end signal.
            self.disconnect_time = datetime.datetime.now()      # Store the disconnect time
            del core.globals.config['connected_clients'][self.session]
            core.globals.config['number_of_connected_clients'] = core.globals.config['number_of_connected_clients'] - 1

        # If connection is lost wait for a certain amount of time to be reconnected. If it takes too long stop the update idle loop (save CPU time).
        if self.connection_established == False and self.disconnect_time != None:
            now = datetime.datetime.now()               # Store the actual time
            timedelta = now - self.disconnect_time      # Subtraction of two datetime objects results in datetime.timedelta object
            print(f"Time until stop of idle loop of session <{self.session}> {core.globals.config['reconnect_timeout'] - timedelta.total_seconds()  :.0f} seconds.")

            if timedelta.total_seconds() >= core.globals.config['reconnect_timeout']:        # If the timeout is reached stop the idle Loop for the App Instance
                print(f'Stopped the idle loop for Session <{self.session}>')
                self._stop_update_flag = True                                               # The idle method is not called anymore
                print('Connected clients (' + str(core.globals.config['number_of_connected_clients']) + ' in total): ' + str(core.globals.config['connected_clients']))
                return                                                                      # End the idle method

        # Debug Info - Check idle loop
        # print(f'Update session <{self.session}>...')

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

