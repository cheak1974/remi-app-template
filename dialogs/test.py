import core.globals
import remi.gui


class Test(remi.gui.Container):

    def __init__(self, AppInst=None, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.AppInst = AppInst          # Holds the Instance of the App. We need it to access uiControl
        self.constructUI()

    def constructUI(self):

        TITLE = 'My fancy Dialog Box'
        STYLE_DIALOG = {'width':'80%', 'margin': '0px auto' ,'padding': '10px', 'margin-top': '50px', 'background-color': 'rgba(255, 255, 255, 0.8)'}
        STYLE_WIDGETS = {'color': 'black', 'font-weight': 'bold', 'padding': '5px', 'background-color': 'rgba(0, 0, 0, 0.0)'}

        # The Container for Dialog is a Container. We add to VBox Containers (left / right) for easy placing of the Widgets

        self.style.update(STYLE_DIALOG)

        self.row = remi.gui.HBox()
        self.row.style.update(STYLE_WIDGETS)
        self.left = remi.gui.VBox()
        self.left.style.update(STYLE_WIDGETS)
        self.right = remi.gui.VBox()
        self.right.style.update(STYLE_WIDGETS)
        self.row.append([self.left, self.right])
        self.add_child(key='title', value='<H2>' + TITLE + '</H2><BR>')
        self.append(self.row)

        ############ Your Widgets go here

        self.label1 = remi.gui.Label('Testlabel 1')
        self.label1.style.update(STYLE_WIDGETS)
        self.left.append(self.label1)
        self.input1 = remi.gui.Input(width='150px', height='40px', default_value=core.globals.UserData['sample1'].field['lastname'])
        self.input1.style.update(STYLE_WIDGETS)
        self.right.append(self.input1)

        self.label2 = remi.gui.Label('Testlabel 2')
        self.label2.style.update(STYLE_WIDGETS)
        self.left.append(self.label2)
        self.input2 = remi.gui.Input(width='150px', height='40px', default_value='Some Value')
        self.input2.style.update(STYLE_WIDGETS)
        self.right.append(self.input2)



        ############ End your widget definition

        self.ok = remi.gui.Button('OK', style={'width': '80px', 'left': '40%'})
        self.ok.add_class('w3-button')
        self.ok.onclick.do(self.handle)
        self.cancel = remi.gui.Button('Cancel', style={'width': '80px', 'left': '60%'})
        self.cancel.add_class('w3-button')
        self.cancel.onclick.do(self.handle)
        self.add_child(key='spacer', value='<br><br>')
        self.append(self.ok)
        self.append(self.cancel)


    def handle(self, emittingWidget):

        if emittingWidget == self.ok:
            print('CONFIRMED')
            core.globals.UserData['sample1'].field['lastname'] = self.input1.get_value()
            self.AppInst.hideDialog()

        if emittingWidget == self.cancel:
            print('CANCELED')
            self.AppInst.hideDialog()

        # Code to close the dialog again is in the main App

