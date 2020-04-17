import core.globals
import models.customer
import remi

# Form Variant 1: Positioning of widgets inside widget container with absolute coordinates

class Container(remi.gui.Container):

    def __init__(self, AppInst=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.AppInst = AppInst
        self.constructUI()
        self.userInit(args, kwargs)


    def constructUI(self):

        # Style the View
        self.style.update({'width': '600px', 'height': '500px', 'position': 'relative', 'margin': 'auto', 'border': '1px solid black', 'padding': '10px', 'margin-top': '20px'})
        # margin: auto centers the element

        # Add some stupid html to the view
        self.add_child('html', '<H1 style="position: absolute; top: 10px; left: 10px;">Customer Data</H1>')

        # Add some widgets and put position them with relative positioning

        self.label_first = remi.gui.Label('Firstname', style={'position': 'absolute', 'top': '100px', 'left': '10px'})
        self.label_first.add_class('w3-small')
        self.input_first = remi.gui.Input(width='400px', style={'position': 'absolute', 'top': '90px', 'left': '100px'})
        self.input_first.add_class('w3-input w3-small')
        self.append([self.label_first, self.input_first])

        self.label_last = remi.gui.Label('Lastname', width='30%', style={'position': 'absolute', 'top': '150px', 'left': '10px'})
        self.label_last.add_class('w3-small')
        self.input_last = remi.gui.Input(width='400px', style={'position': 'absolute', 'top': '140px', 'left': '100px'})
        self.input_last.add_class('w3-input w3-small')
        self.append([self.label_last, self.input_last])

        self.label_city = remi.gui.Label('City', width='30%', style={'position': 'absolute', 'top': '200px', 'left': '10px'})
        self.label_city.add_class('w3-small')
        self.input_city = remi.gui.Input(width='400px', style={'position': 'absolute', 'top': '190px', 'left': '100px'})
        self.input_city.add_class('w3-input w3-small')
        self.append([self.label_city, self.input_city])

        self.create_btn = remi.gui.Button('Create new Dataset', width='200px', style={'position': 'absolute', 'top': '250px', 'left': '10px', 'font-style': 'normal', 'font-weight': 'normal'})
        self.create_btn.add_class('w3-button')
        self.create_btn.onclick.do(self.createNewDataset)
        self.append(key='create_btn', value=self.create_btn)

        self.showdialog = remi.gui.Button('Show Dialog', width='200px', style={'position': 'absolute', 'top': '250px', 'left': '300px', 'font-style': 'normal', 'font-weight': 'normal'})
        self.showdialog.add_class('w3-button w3-display-bottom-right')
        self.showdialog.onclick.do(self.AppInst.showDialog, 'sample')
        self.append(key='showdialog', value=self.showdialog)


    def userInit(self, *args, **kwargs):
        self.shownInMenu = 'My Example Menu'
        self.menuTitle = 'Formular with custom dialog'


    def updateView(self):
        # Here you can update the view if it needs updates
        pass


    def createNewDataset(self, emittingWidget):

        # Just an example how to get the name from the emitting widget. We don't need it here.
        emitter = ''
        for widget_key, widget_obj in self.children.items():
            if widget_obj == emittingWidget:
                emitter = widget_key
        print(f'RECEIVED CLICK FROM {emittingWidget}')
        print(f'RECEIVED CLICK FROM {emitter}')

        # If there is data given in the form then process it
        if self.input_last.get_value() != '':
            # Create new customer and store it away (it will live only in memory). All other views can access this.
            core.globals.UserData[self.input_last.get_value()] = models.customer.Customer(lastname=self.input_last.get_value(),
                                                                                          firstname=self.input_first.get_value(),
                                                                                          city=self.input_city.get_value())
            # Access the freshly created customer object
            print(f"{core.globals.UserData[self.input_last.get_value()]}")



