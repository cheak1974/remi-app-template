import core.globals                     # Gain access to global objects
from remi.gui import *                  # Import all REMI GUI Elements


class Container(Container):

    def __init__(self, AppInst=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.AppInst = AppInst
        self.userInit(*args, **kwargs)
        self.constructUI()


    def constructUI(self):

        STYLE_WIDGETS = {'color': 'black', 'font-weight': 'bold', 'padding': '5px', 'background-color': 'rgba(0, 0, 0, 0.0)', 'text-align': 'left'}

        # The Container for Dialog is a Container. We add to VBox Containers (left / right) for easy placing of the Widgets

        self.row = HBox()
        self.row.style.update(STYLE_WIDGETS)
        self.left = VBox()
        self.left.style.update(STYLE_WIDGETS)
        self.right = VBox()
        self.right.style.update(STYLE_WIDGETS)
        self.row.append([self.left, self.right])
        self.add_child(key='title', value='<H2>' + self.TITLE + '</H2><BR>')
        self.append(self.row)


        self.label1 = Label('Kältemaschine Einstellung')
        self.label1.style.update(STYLE_WIDGETS)
        self.left.append(self.label1)
        #self.input1 = Input(width='150px', height='40px', default_value=self.AppInst.views['plant_view'].data[self.km + '_setting'])
        self.input1 = DropDown(width='150px', height='40px')
        self.input1.style.update(STYLE_WIDGETS)
        self.opt1 = DropDownItem('AUTO')
        self.opt2 = DropDownItem('AN MAN')
        self.opt3 = DropDownItem('AUS MAN')

        self.input1.append([self.opt1, self.opt2, self.opt3])

        self.right.append(self.input1)

        self.label2 = Label('Kältemaschine Status')
        self.label2.style.update(STYLE_WIDGETS)
        self.left.append(self.label2)
        self.input2 = Input(width='150px', height='40px', default_value=self.AppInst.views['plant_view'].data[self.km + '_status'])
        self.input2.attributes['readonly'] =''
        self.input2.style.update(STYLE_WIDGETS)
        self.right.append(self.input2)

        self.label3 = Label('Kältemaschine Sollwert')
        self.label3.style.update(STYLE_WIDGETS)
        self.left.append(self.label3)
        self.input3 = Input(width='150px', height='40px', default_value=self.AppInst.views['plant_view'].data[self.km + '_setpoint'])
        self.input3.style.update(STYLE_WIDGETS)
        self.right.append(self.input3)

        self.ok = Button('OK', style={'width': '80px', 'left': '40%'})
        self.ok.add_class('w3-button')
        self.ok.onclick.do(self.handle)
        self.cancel = Button('Cancel', style={'width': '80px', 'left': '60%'})
        self.cancel.add_class('w3-button')
        self.cancel.onclick.do(self.handle)
        self.add_child(key='spacer', value='<br><br>')
        self.append(self.ok)
        self.append(self.cancel)


    def userInit(self, *args, **kwargs):
        self.style.update({'width':'80%', 'margin': '0px auto' , 'border': '1px black solid', 'padding': '10px', 'margin-top': '50px', 'background-color': 'rgba(255, 255, 255)'})

        if 'title' in kwargs.keys():
            self.TITLE = kwargs['title']

        if 'km' in kwargs.keys():
            self.km = kwargs['km']
            if self.km + '_status' not in self.AppInst.views['plant_view'].data.keys():
                self.AppInst.hideDialog()


    def handle(self, emittingWidget):

        if emittingWidget == self.ok:
            print('CONFIRMED')
            self.AppInst.views['plant_view'].data[self.km + '_setting'] = self.input1.get_value()
            self.AppInst.views['plant_view'].data[self.km + '_setpoint'] = self.input3.get_value()
            self.AppInst.hideDialog()                                                           # Code to close the dialog again is in the main App

        if emittingWidget == self.cancel:
            print('CANCELED')
            self.AppInst.hideDialog()                                                           # Code to close the dialog again is in the main App





