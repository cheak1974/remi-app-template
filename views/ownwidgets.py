import core.globals
import remi.gui
import widgets.trafficlights

class Container(remi.gui.Container):

    def __init__(self, AppInst=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.AppInst = AppInst
        self.constructUI()
        self.userInit(args, kwargs)


    def constructUI(self):

        ### UI Design
        self.height = '100%'
        self.outer_container = remi.gui.Container(width='95%', height='400px', style={'box-sizing': 'border-box', 'border': '1px solid black',
                                                                                      'margin': '0 auto', 'margin-top': '20px',
                                                                                      'padding': '15px', 'border-radius': '15px'})


        test_lights = widgets.trafficlights.Trafficlights(height='140px', width='60px')
        test_lights.style.update({'display': 'inline-block', 'position': 'relative', 'vertical-align': 'top'})
        self.outer_container.append(test_lights)

        test_lights2 = widgets.trafficlights.Trafficlights(height='100px', width='40px')
        test_lights2.style.update({'display': 'inline-block', 'position': 'relative', 'vertical-align': 'top', 'margin-left': '20px'})
        self.outer_container.append(test_lights2)

        self.append(self.outer_container)


    def userInit(self, *args, **kwargs):
        self.shownInMenu = 'My Example Menu'
        self.menuTitle = 'Testing of own Widgets'


    def updateView(self):
        # Here you can update the view if it needs updates
        pass

