import remi.gui as gui

class Container(gui.Container):

    def __init__(self, AppInst=None, *args, **kwargs):
        super().__init__(*args, **kwargs)                                                # Initializes the Parent Object remi.gui.Container
        self.AppInst = AppInst                                                           # Instances of the REMI App Instance. Needed to call methods placed there.
        self.constructUI()                                                               # Call the Editor made constructUI method
        self.userInit(args, kwargs)                                                      # Call custom Usercode


    def constructUI(self):

        row1 = gui.Container()                          # Create a row
        row1.add_class('w3-row')
        row1.style.update({'position': 'relative'})
        self.append(row1)

        box_1_left = gui.Container()                    # Create a column
        box_1_left.add_class('w3-col l3 s12')
        row1.append(box_1_left)

        card = gui.Container()
        card.add_class('w3-card-4 w3-margin w3-white')
        card.style.update({'padding': '20px', 'margin': '10px'})
        box_1_left.append(card)

        title = gui.Container()
        title.add_class('w3-light-grey')
        title.add_child(key='title', value='<h4 class="w3-wide w3-center">User Details</h2>')
        card.append(title)

        dropdown1 = gui.DropDown()
        dropdown1.add_class('w3-input w3-tiny w3-white')
        for item in ['Option 1', 'Option 2', 'Option 3']:
            dropdown_item = gui.DropDownItem(item)
            dropdown1.append(dropdown_item)
        card.append(dropdown1)

        dropdown1.onchange.do(self.change_text)

        input1 = gui.Input()
        input1.add_class('w3-input w3-tiny')
        card.append(key='input1', value=input1)

        self.label1 = gui.Label(f'Enter your Name ({dropdown1.get_item().get_text()} selected)')
        self.label1.add_class('w3-tiny')
        card.append(self.label1)

        input2 = gui.Input()
        input2.add_class('w3-input w3-tiny')
        card.append(input2)

        label2 = gui.Label('Enter your City')
        label2.add_class('w3-tiny')
        card.append(label2)

        card.add_child(key='spacer1', value='<br><br>')

        btn1_ok = gui.Button('OK', width='30%')
        btn1_ok.add_class('w3-button w3-green w3-left')
        card.append(btn1_ok)

        btn1_cancel = gui.Button('Cancel', width='30%')
        btn1_cancel.add_class('w3-button w3-yellow w3-right')
        card.append(btn1_cancel)

        card.add_child(key='spacer2', value='<br><br>')


        ######## Right Container
        box_1_right = gui.Container()  # Create a column
        box_1_right.add_class('w3-col l3 s12')
        row1.append(box_1_right)

        self.card2 = gui.Container()
        self.card2.add_class('w3-card-4 w3-margin w3-padding w3-white w3-display-container')
        box_1_right.append(self.card2)

        title = gui.Container()
        title.add_class('w3-light-grey')
        title.add_child(key='title', value='<h4 class="w3-wide w3-center">Automatic Form</h2>')
        self.card2.append(title)

        for i in range(1,10):
            input = gui.Input()
            input.add_class('w3-input w3-small')
            self.card2.append(key=f'input_{i}', value=input)
            label = gui.Label(f'This is Label {i}')
            label.add_class('w3-small')
            self.card2.append(label)

        self.card2.add_child(key='spacer1', value='<br><br>')

        footer = gui.Container()
        footer.add_child(key='footer', value='<p class="w3-small w3-center">Created with REM and W3.CSS</p>')
        self.card2.append(footer)

        self.card2.add_child(key='spacer2', value='<br><br>')

        btn2_ok = gui.Button('Dialog', width='30%')
        btn2_ok.add_class('w3-button w3-green w3-display-bottommiddle')
        self.card2.append(btn2_ok)

        # Call method for gathering information and showing dialog
        btn2_ok.onclick.do(self.notify)


    def userInit(self, *args, **kwargs):
        # Here you can add Instance Attributes, do additional styling, register events etc.
        self.style.update({'width': '100%', 'position': 'relative', 'margin': 'auto'})  # Absolute Base configuration of the container. Use relative for proper Widget placement.
        self.shownInMenu = 'My Example Menu'                                               # Change to None if the View should not be visible in Menu, otherwise this is the Menu Name
        self.menuTitle = 'W3 CSS styled View'                                             # The View will appear with this name in the Menu above


    def updateView(self):
        # Here you can update the view if it needs updates. This method is called periodically if the App is idle.
        pass

    def change_text(self, emittingWidget, dropdown_value):
        self.label1.set_text(f'Enter your Name ({dropdown_value} selected)')

    def notify(self, emittingWidget):
        # We need a wrapper because the args cannot change when directly linked. The event registration is fixed.
        text = ''

        for i in range(1, 10):
            text = text + self.card2.children[f'input_{i}'].get_value() + '\n'

        self.AppInst.showDialog(emittingWidget=emittingWidget, dialogname='alert', title='A message from behind', message=text)
