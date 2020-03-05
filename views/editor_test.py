from remi.gui import *

class Container( Container ):

    def __init__(self, AppInst=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.AppInst = AppInst
        self.constructUI()
        self.userInit(args, kwargs)


    def constructUI(self):
        self.attr_editor_newclass = False
        self.css_border_style = "solid"
        self.css_border_width = "1px"
        self.css_height = "360.0px"
        self.css_left = "150px"
        self.css_margin = "0px"
        self.css_position = "relative"
        self.css_top = "150px"
        self.css_width = "645.0px"
        self.variable_name = "myContainer"
        myButton = Button()
        myButton.attr_editor_newclass = False
        myButton.css_height = "50px"
        myButton.css_left = "195.0px"
        myButton.css_position = "absolute"
        myButton.css_top = "270.0px"
        myButton.css_width = "255px"
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


    def userInit(self, *args, **kwargs):
        self.shownInMenu = 'My Menu Name'
        self.menuTitle = 'View created with REMI Editor'

        # Here we add custom styling with CSS templates. This time we use W3.CSS styling.
        self.children['myButton'].style.update({'font-weight': 'normal', 'display': 'block', 'line-height': self.children['myButton'].css_height})
        self.children['myButton'].add_class('w3-btn w3-yellow')


    def updateView(self):
        # Here you can update the view if it needs updates
        pass
