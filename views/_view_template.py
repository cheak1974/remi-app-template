from remi.gui import *

class View_template(Container):

    def __init__(self, AppInst=None, *args, **kwargs):

        # Same __init__ Method for all Editor made containers. The __init__ method is never again touched by the editor again. Changes are not needed here.
        super().__init__(*args, **kwargs)                                                   # Initializes the Parent Object remi.gui.Container
        self.AppInst = AppInst
        self.style.update({'width': '100%', 'position': 'relative', 'margin': 'auto'})      # Absolute Base configuration of the container
        self.construct_ui()                                                                 # Call the Editor made constructUI method
        self.registerEventHandlers()                                                        # Optional: User can register event handlers here
        self.userDefinedAttributes()                                                        # Optional: Users can add Attributes to the container class for their application



###EDITOR_BEGIN
    def construct_ui(self):

        self.style.update({'height': '600px', 'border': '1px solid black', 'padding': '10px', 'margin-top': '20px'}  )
        self.variable_name = ''

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
        self.append(button0, 'button0')             # append to class instance

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
        self.append(textinput0, 'textinput0')       # append to class instance

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
        self.append(textinput1, 'textinput1')       # append to class instance

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
        self.append(label0, 'label0')              # append to class instance

###EDITOR_END##################################################################################

    def registerEventHandlers(self):
        self.children['button0'].onclick.do(self.buttonclick)


    def userDefinedAttributes(self):
        import core.globals                     # User imports
        self.shownInMenu = 'My Example Menu'    # Use None if it should not be visible in any Menu
        self.menuTitle = 'Text shown in Menu'

########## The registerEventHandlers and userDefinedAttributes methods are also just written when saving for the first time and never again touched.
########## All things below are userdefined and also never touched by the editor.


    def buttonclick(self, emittingWidget):
        print('Button was clicked!')
        self.AppInst.uiControl(emittingWidget, 'start')


    def updateView(self):
        # Here you can update the view if it needs updates
        pass

