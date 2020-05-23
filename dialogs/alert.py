import core.globals                     # Gain access to global objects
import remi.gui as gui                  # Import all REMI GUI Elements


class Container(gui.Container):

    def __init__(self, AppInst=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.AppInst = AppInst
        self.constructUI(**kwargs)
        self.userInit()


    def constructUI(self, **kwargs):

        card = gui.Container(width='400px')
        card.add_class('w3-card-4 w3-margin w3-white w3-display-middle')
        card.style.update({'padding': '20px', 'margin': '10px'})
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
        card.add_child(key='spacer1', value='<br><br>')
        card.append(ok)
        card.append(cancel)
        card.add_child(key='spacer2', value='<br><br>')

    def userInit(self, *args, **kwargs):
        pass

    def handle(self, emittingWidget):

        if emittingWidget.get_text() == "OK":
            print('CONFIRMED')
            self.AppInst.hideDialog()                                                           # Code to close the dialog again is in the main App

        if emittingWidget.get_text() == "Cancel":
            print('CANCELED')
            self.AppInst.hideDialog()                                                           # Code to close the dialog again is in the main App





