import core.globals                     # Gain access to global objects
from remi.gui import *                  # Import all REMI GUI Elements


class Container(Container):

    def __init__(self, AppInst=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.AppInst = AppInst
        self.constructUI()
        self.userInit()


    def constructUI(self):

        TITLE = 'My fancy Dialog Box'
        STYLE_WIDGETS = {'color': 'black', 'font-weight': 'bold', 'padding': '5px', 'background-color': 'rgba(0, 0, 0, 0.0)'}

        # The Container for Dialog is a Container. We add to VBox Containers (left / right) for easy placing of the Widgets

        self.row = HBox()
        self.row.style.update(STYLE_WIDGETS)
        self.left = VBox()
        self.left.style.update(STYLE_WIDGETS)
        self.right = VBox()
        self.right.style.update(STYLE_WIDGETS)
        self.row.append([self.left, self.right])
        self.add_child(key='title', value='<H2>' + TITLE + '</H2><BR>')
        self.append(self.row)


        self.label1 = Label('Testlabel 1')
        self.label1.style.update(STYLE_WIDGETS)
        self.left.append(self.label1)
        self.input1 = Input(width='150px', height='40px', default_value=core.globals.UserData['sample1'].field['lastname'])
        self.input1.style.update(STYLE_WIDGETS)
        self.right.append(self.input1)

        self.label2 = Label('Testlabel 2')
        self.label2.style.update(STYLE_WIDGETS)
        self.left.append(self.label2)
        self.input2 = Input(width='150px', height='40px', default_value='Some Value')
        self.input2.style.update(STYLE_WIDGETS)
        self.right.append(self.input2)



    def userInit(self, *args, **kwargs):
        self.style.update({'width':'80%', 'margin': '0px auto' ,'padding': '10px', 'margin-top': '50px', 'background-color': 'rgba(255, 255, 255, 0.8)'})

        self.ok = Button('OK', style={'width': '80px', 'left': '40%'})
        self.ok.add_class('w3-button')
        self.ok.onclick.do(self.handle)
        self.cancel = Button('Cancel', style={'width': '80px', 'left': '60%'})
        self.cancel.add_class('w3-button')
        self.cancel.onclick.do(self.handle)
        self.add_child(key='spacer', value='<br><br>')
        self.append(self.ok)
        self.append(self.cancel)


    def handle(self, emittingWidget):

        if emittingWidget == self.ok:
            print('CONFIRMED')
            core.globals.UserData['sample1'].field['lastname'] = self.input1.get_value()
            self.AppInst.hideDialog()                                                           # Code to close the dialog again is in the main App

        if emittingWidget == self.cancel:
            print('CANCELED')
            self.AppInst.hideDialog()                                                           # Code to close the dialog again is in the main App





