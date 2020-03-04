
from remi.gui import *

class Mytest( Container ):                                                                                                          #cheak:Maybe change class name to name of root container

    def __init__(self, AppInst=None, *args, **kwargs):
        super().__init__(*args, **kwargs)                                                                                                #cheak:remove Comments
        self.AppInst = AppInst                                                                                                           #cheak:remove Comments
        self.constructUI()                                                                                                               #cheak:instead we just call it
        self.userInit(args, kwargs)                                                                                                      #more. Register events. Add custom widgets. Add css classes etc.
                                                                                                                                         # pass kwargs to user init in case user needs it.

    def constructUI(self):
        self.attr_editor_newclass = False
        self.css_border_style = "solid"
        self.css_border_width = "1px"
        self.css_height = "360.0px"
        self.css_left = "20px"
        self.css_margin = "0px"
        self.css_position = "relative"
        self.css_top = "20px"
        self.css_width = "645.0px"
        self.variable_name = "myContainer"
        myButton = Button()
        myButton.attr_editor_newclass = False
        myButton.css_background_color = "rgb(110,0,0)"
        myButton.css_border_radius = "10px"
        myButton.css_border_style = "solid"
        myButton.css_border_width = "1px"
        myButton.css_height = "30px"
        myButton.css_left = "270.0px"
        myButton.css_margin = "0px"
        myButton.css_position = "absolute"
        myButton.css_top = "270.0px"
        myButton.css_width = "100px"
        myButton.text = "Click Me"
        myButton.variable_name = "myButton"
        self.append(myButton,'myButton')
        label0 = Label()
        label0.attr_editor_newclass = False
        label0.css_height = "30.0px"
        label0.css_left = "195.0px"
        label0.css_margin = "0px"
        label0.css_position = "absolute"
        label0.css_text_align = "center"
        label0.css_top = "105.0px"
        label0.css_width = "255.0px"
        label0.text = "This is a Test Label"
        label0.variable_name = "label0"
        self.append(label0,'label0')
        textinput0 = TextInput()
        textinput0.attr_editor_newclass = False
        textinput0.css_height = "30.0px"
        textinput0.css_left = "225.0px"
        textinput0.css_margin = "0px"
        textinput0.css_position = "absolute"
        textinput0.css_top = "165.0px"
        textinput0.css_width = "195.0px"
        textinput0.text = ""
        textinput0.variable_name = "textinput0"
        self.append(textinput0,'textinput0')
        
        pass

    def userInit(self, *args, **kwargs):
        self.shownInMenu = 'My Menu Name'
        self.menuTitle = 'My View Name'

    def updateView(self):
        # Here you can update the view if it needs updates
        pass
