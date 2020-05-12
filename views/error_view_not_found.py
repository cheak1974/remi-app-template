import logging
import remi.gui
import core.globals
import helpers.connections

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

        self.info = remi.gui.Label("That's an error. The requested view was not found on the server.")
        self.info.style.update({'font-family': 'Arial', 'font-weight': 'bold', 'font-size': '20px', 'text-align': 'center'})
        self.vbox.append(self.info)

        self.info.add_child(key='link', value='<br><br><a href="/start">Go to Start Page</a>')

        self.append(self.vbox)       # Append the container which holds the GUI to the View Instance


    def userInit(self, *args, **kwargs):
        self.shownInMenu = None             # Start Page should not be visible in any Menu
        self.menuTitle = ''                 # Because it is not in any Menu it doesn't need a menu title neither


    def updateView(self):
        pass
