import core.globals
import remi        # This doesn't work with files from remi
from remi.gui import *
from remi import start, App

class From_remi_editor2(remi.gui.Container):
# The name of the class has to be identical with the name of the file (view_template.py), but with capital first letter!
# Files which have a Underscore at first place in filename will not be loaded (by renaming you can take them out for development easily).

    def __init__(self, AppInst=None, *args, **kwargs):

        super().__init__(*args, **kwargs)       # Initializes the Parent Object remi.gui.Container
        self.AppInst = AppInst                  # Holds the Instance of the App. We need it to access uiControl
        self.shownInMenu = 'My Example Menu'          # Use None if it should not be visible in any Menu
        self.menuTitle = 'from REMI Editor container rel'
        self.style.update({'width': '100%', 'margin': 'auto', 'border': '1px solid black', 'padding': '10px', 'margin-top': '20px'})
        self.append(self.constructUI())
        self.registerEventHandlers()

######EDITOR OUTPUT BEGIN

    def constructUI(self):

        container0 = Container()
        container0.attr_editor_newclass = False
        container0.css_height = "330.0px"
        #container0.css_left = "20px"                           # not needed here
        container0.css_margin = "0px"
        container0.css_position = "relative"                    # EDITED this line from absolute to relative to make the Container from Editor work inside my views
        #container0.css_top = "20px"                            # not needed here
        container0.css_width = "630.0px"
        container0.variable_name = "container0"
        button0 = Button()
        button0.attr_editor_newclass = False
        button0.css_height = "30px"
        button0.css_left = "120.0px"
        button0.css_margin = "0px"
        button0.css_position = "absolute"
        button0.css_top = "30.0px"
        button0.css_width = "100px"
        button0.text = "button"
        button0.variable_name = "button0"
        container0.append(button0, 'button0')
        textinput0 = TextInput()
        textinput0.attr_editor_newclass = False
        textinput0.css_height = "30px"
        textinput0.css_left = "270.0px"
        textinput0.css_margin = "0px"
        textinput0.css_position = "absolute"
        textinput0.css_top = "30.0px"
        textinput0.css_width = "100px"
        textinput0.text = ""
        textinput0.variable_name = "textinput0"
        container0.append(textinput0, 'textinput0')
        textinput1 = TextInput()
        textinput1.attr_editor_newclass = False
        textinput1.css_height = "30px"
        textinput1.css_left = "270.0px"
        textinput1.css_margin = "0px"
        textinput1.css_position = "absolute"
        textinput1.css_top = "75.0px"
        textinput1.css_width = "100px"
        textinput1.text = ""
        textinput1.variable_name = "textinput1"
        container0.append(textinput1, 'textinput1')
        label0 = Label()
        label0.attr_editor_newclass = False
        label0.css_font_family = "Roboto"
        label0.css_font_size = "20px"
        label0.css_height = "30.0px"
        label0.css_left = "60.0px"
        label0.css_margin = "0px"
        label0.css_position = "absolute"
        label0.css_top = "225.0px"
        label0.css_width = "510.0px"
        label0.text = "Test View made with REMI Editor and saved as Container."
        label0.variable_name = "label0"
        container0.append(label0, 'label0')

        return container0                                           # add the Editor Container to the view

######EDITOR OUTPUT END

    def registerEventHandlers(self):
        for container in self.children.values():                    # Search for container0
            if container.variable_name == 'container0':
                for widget in container.children.values():          # Search for button0
                    if widget.variable_name == 'button0':
                        widget.onclick.do(self.buttonclick)         # register Event
                                                                    # Would really be easier when all widgets would be stored with a key

    def buttonclick(self, emittingWidget):
        print('Button was clicked!')


    def updateView(self):
        # Here you can update the view if it needs updates
        pass

