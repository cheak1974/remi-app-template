import remi.gui


class Disabledmenu(remi.gui.Container):
# The name of the class has to be identical with the name of the file (view_template.py), but with capital first letter!
# The App stores an instance of the view in its views{} dictionary. key = filename of the view without '.py' / value = the view instance
# Files which have a Underscore at first place in filename will not be loaded (by renaming you can take them out for development easily).

    def __init__(self, AppInst=None, *args, **kwargs):

        super().__init__(*args, **kwargs)       # Initializes the Parent Object remi.gui.Container
        self.AppInst = AppInst                  # Holds the Instance of the App. We need it to access uiControl
        self.shownInMenu = 'Examples Gitter Chat'
        self.menuTitle = 'Disable/Enable Menus'
        self.constructUI()

    def constructUI(self):

        # Style the View by updating it style dictionary
        # margin: auto centers the element
        self.style.update({'width': '500px', 'height': '500px', 'margin': 'auto', 'border': '1px solid black', 'padding': '10px', 'margin-top': '50px'})

        self.menuActive = True

        # Style a navbar
        self.menubar = remi.gui.MenuBar(width='100%', height='30px', style={'background-color': 'yellow', 'border': 'none'})
        self.menu = remi.gui.Menu(height=self.menubar.style['height'], style={'background-color': self.menubar.style['background-color'], 'border': 'none'})
        self.menubar.append(key='menu', value=self.menu)
        self.disable = remi.gui.MenuItem('Disable Menubar', width='150px', height=self.menubar.style['height'],
                                         style={'background-color': self.menubar.style['background-color'], 'color': 'black', 'box-shadow': 'none'})
        self.menu.append(key='disable', value=self.disable)

        self.disable.onclick.do(self.handleMenuClicks)

        self.enable = remi.gui.Button('Enable Menubar', width='150px', height='30px')
        self.enable.onclick.do(self.enableMenu)

        # Append all Widgets to the Container Instance (self)
        self.append(key='menubar', value=self.menubar)
        self.append(key='enable', value=self.enable)


    def updateView(self):
        # Here you can update the view if it needs updates
        pass


    def handleMenuClicks(self, emittingWidget):

        print('Handle Event')

        if emittingWidget == self.disable and self.menuActive == True:
            self.menuActive = False
            self.menubar.style.update({'background-color': 'darkgrey'})
            self.menu.style.update({'background-color': 'darkgrey'})
            self.disable.style.update({'background-color': 'darkgrey'})

        # You can add all the Menu commands here


    def enableMenu(self, emittingWidget):
        self.menuActive = True
        self.menubar.style.update({'background-color': 'yellow'})
        self.menu.style.update({'background-color': 'yellow'})
        self.disable.style.update({'background-color': 'yellow'})



