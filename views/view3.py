import core.globals
import remi.gui

# Just arrange freely the elements for fixed sceen sizes.

class Container(remi.gui.Container):

    def __init__(self, AppInst=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.AppInst = AppInst
        self.constructUI()
        self.userInit(args, kwargs)


    def constructUI(self):

        self.base = remi.gui.Widget(width='1000px', height='600px',
                                               style={'overflow': 'auto', 'margin': 'auto',
                                                      'border': '1px solid black',
                                                      'padding': '10px', 'margin-top': '10px'})
        # margin: auto centers the element, class w3-display-container

        self.base.add_child('html', '<H1 style="position: relative; left: 10px;">Overview Heating System</H1>')
        self.append(self.base)


    def userInit(self, *args, **kwargs):
        self.shownInMenu = 'My Example Menu'
        self.menuTitle = 'Show View 3'


    def updateView(self):
        # Here you can update the view if it needs updates
        pass

