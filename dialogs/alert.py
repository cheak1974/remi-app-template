import core.globals                     # Gain access to global objects
import remi.gui as gui                  # Import all REMI GUI Elements


class Container(gui.Container):

    def __init__(self, AppInst=None, *args, **kwargs):
        # Expects title and message as arguments.
        super().__init__(*args, **kwargs)
        self.AppInst = AppInst
        self.constructUI(**kwargs)          # Passing the kwargs of the view to constructUI
        self.userInit()


    def constructUI(self, **kwargs):

        card = gui.Container()
        card.add_class('w3-card-4 w3-margin w3-padding w3-white w3-display-middle w3-col l4 s12')
        card.style.update({'position': 'fixed'})        # Position is calculated dynamically but then the card stays fixed :-)
        self.append(card)

        title = gui.Container()
        title.add_child(key='title', value=f'<h4 class="w3-wide w3-center">{kwargs["title"]}</h2>')
        card.append(title)

        message = gui.Label(kwargs['message'])
        message.add_class('w3-small')
        card.append(message)

        ok = gui.Button('OK', style={'width': '30%'})
        ok.add_class('w3-button w3-green w3-left')
        ok.onclick.do(self.handle)

        cancel = gui.Button('Cancel', style={'width': '30%'})
        cancel.add_class('w3-button w3-yellow w3-right')
        cancel.onclick.do(self.handle)

        card.add_child(key='spacer', value='<br><br>')
        card.append(ok)
        card.append(cancel)
        #card.add_child(key='spacer2', value='<br><br>')

    def userInit(self, *args, **kwargs):
        pass

    def handle(self, emittingWidget):

        if emittingWidget.get_text() == "OK":
            print('CONFIRMED')
            self.AppInst.hideDialog()                                                           # Code to close the dialog again is in the main App

        if emittingWidget.get_text() == "Cancel":
            print('CANCELED')
            self.AppInst.hideDialog()                                                           # Code to close the dialog again is in the main App





