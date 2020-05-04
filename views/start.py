import logging
import remi.gui
import core.globals

class Container(remi.gui.Container):

    def __init__(self, AppInst=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.AppInst = AppInst
        self.constructUI()
        self.userInit(args, kwargs)


    def constructUI(self):

        self.vbox = remi.gui.VBox()

        self.spacer1 = remi.gui.Container(height='50px')
        self.vbox.append(self.spacer1)

        self.info = remi.gui.Label('Template for WebApps made with REMI (www.remigui.com) by Christian Kueken (github: cheak1974)')
        self.info.style.update({'font-family': 'Lobster', 'font-weight': 'bold', 'font-size': '20px', 'text-align': 'center'})
        self.vbox.append(self.info)

        self.info.add_child(key='link', value='<br><br><a href="https://github.com/cheak1974/remi-app-template" target="_blank">REMI App Template on github</a>')

        self.spacer2 = remi.gui.Container(height='50px')
        self.vbox.append(self.spacer2)

        self.picture = remi.gui.Image('/static:images/montypython.gif', style={'width': '300px'})
        self.vbox.append(self.picture)

        self.inputview = remi.gui.Input('', 'start', width='300px')
        self.inputbtn = remi.gui.Button('Go to view with the entered name', width='300px', height='60px', style={'font-style': 'normal', 'font-weight': 'normal', 'box-shadow': 'none'})
        self.inputbtn.onclick.do(self.goToEnteredView)
        self.vbox.append(self.inputview)
        self.vbox.append(self.inputbtn)

        self.hintbox = remi.gui.Label(' ', width='500px', style={'font-weight': 'bold', 'font-size': '14px', 'text-align': 'center'})
        self.vbox.append(self.hintbox)

        self.append(self.vbox)       # Append the container which holds the GUI to the View Instance


    def userInit(self, *args, **kwargs):
        self.shownInMenu = None             # Start Page should not be visible in any Menu
        self.menuTitle = ''                 # Because it is not in any Menu it doesn't need a menu title neither


    def updateView(self):
        self.hintbox.set_text('Number of Clients actually connected: ' + str(core.globals.config['number_of_connected_clients']))


    def goToEnteredView(self, emittingWidget):
        # Wrapper Function. If uiControl used when registering the event, the view is fixed but it should be dynamic depending on input
        enteredView = self.inputview.get_value()
        self.AppInst.uiControl(emittingWidget, enteredView)


