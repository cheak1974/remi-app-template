import core.globals
import remi.gui

class Navbar(remi.gui.Container):

    def __init__(self, AppInst=None, *args, **kwargs):

        super(Navbar, self).__init__(*args, **kwargs)
        self.AppInst = AppInst                          # Holds the Instance of the App. We need it to access uiControl

        # Define the look of the NavBar
        self.HEIGHT = str(core.globals.config['navbar_height']) + 'px'
        self.BACKGROUND = 'black'
        self.TEXT = 'white'
        self.CLASSES = 'w3-small w3-hover-yellow'
        self.MENUWIDTH = '200px'

        self.style.update({'height': self.HEIGHT, 'background-color': self.BACKGROUND, })

        # Create the NavBar and the contained Menu
        self.navbar = remi.gui.MenuBar(width='100%', height=self.HEIGHT, style={'background-color': self.BACKGROUND})
        self.menu = remi.gui.Menu(height=self.HEIGHT, style={'background-color': self.BACKGROUND})
        self.navbar.append(self.menu)

        # Define kind of home Menuitem which holds the AppName and Version
        self.title = remi.gui.MenuItem(core.globals.config['appname'] + ' ' + core.globals.config['version'], width=self.MENUWIDTH, height=self.HEIGHT,
                                       style={'color': self.TEXT, 'background-color': self.BACKGROUND})
        self.title.add_class(self.CLASSES)
        self.title.onclick.do(self.switchview, 'start')
        self.menu.append(self.title)


        # Create Menus for all Menus found in views of AppInst

        for viewname, viewobj in self.AppInst.views.items():

            # Search for Menu Names that are not already a MenuItem and make a Menuitem for them
            if viewobj.shownInMenu != None and ('menu_' + viewobj.shownInMenu) not in self.__dict__.keys():
                self.__dict__['menu_' + viewobj.shownInMenu] = remi.gui.MenuItem(viewobj.shownInMenu, width=self.MENUWIDTH, height=self.HEIGHT,
                                                                       style = {'color': self.TEXT, 'background-color': self.BACKGROUND})
                self.__dict__['menu_' + viewobj.shownInMenu].add_class(self.CLASSES)
                self.menu.append(self.__dict__['menu_' + viewobj.shownInMenu])

        # Add the views as menuItems to the previously created Menus
        for viewname, viewobj in self.AppInst.views.items():

            if viewobj.shownInMenu != None:

                self.__dict__['item_' + viewname] = remi.gui.MenuItem(viewobj.menuTitle, width=self.MENUWIDTH, height=self.HEIGHT,
                                                                  style={'color': self.TEXT, 'background-color': self.BACKGROUND})

                self.__dict__['item_' + viewname].add_class(self.CLASSES)
                self.__dict__['item_' + viewname].onclick.do(self.switchview, viewname)
                self.__dict__['menu_' + viewobj.shownInMenu].append(self.__dict__['item_' + viewname])


        self.append(self.navbar)


    def switchview(self, emittingWidget, view):
        self.AppInst.uiControl(emittingWidget, view)


    def updateView(self):
        # Here you can update the view if it needs updates
        pass

