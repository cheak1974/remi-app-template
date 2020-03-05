import core.globals
import remi


class Container(remi.gui.Container):

    def __init__(self, AppInst=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.AppInst = AppInst
        self.constructUI()
        self.userInit(args, kwargs)


    def constructUI(self):

        margintop = 10
        heightdiff = str(core.globals.config['navbar_height'] + 2 * core.globals.config['base_padding'] + margintop) + 'px'

        self.base = remi.gui.Container(width='80%', height='calc(100vH - ' + heightdiff + ')',
                                       style={'overflow': 'auto', 'margin': 'auto',
                                              'border': '1px solid black',
                                              'padding': '10px', 'margin-top': str(margintop) + 'px'})
        # margin: auto centers the element, class w3-display-container

        self.textbox_sentences = remi.gui.TextInput(single_line=False, width='100%', height='100%', style={'scrolling': 'yes', 'resize': 'none'})
        self.textbox_sentences.set_value('Enter http://127.0.0.1:8080/api/sentences?amount=50 in address row of browser!')
        self.base.append(self.textbox_sentences)
        self.append(self.base)


    def userInit(self, *args, **kwargs):
        self.shownInMenu = 'Examples Gitter Chat'
        self.menuTitle = 'Control View Content with API'


    def updateView(self):
        # Here you can update the view if it needs updates
        pass

