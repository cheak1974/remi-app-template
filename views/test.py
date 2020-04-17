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

        # box-sizing: border-box forces padding to stay in the defined width of the <div> tag  (e.g. width 300px with padding 20px would be 340px wide otherwise
        # margin: 0 auto combined with width of 95% centers the box on the screen. Define the width to adjust the left/right border
        # margin-top: 20px sets the distance from top

        self.inner_container = remi.gui.Container()
        self.inner_container.add_child('html', """<b>Lirum Larum</b> Ipsum Dolorem <b>Lirum Larum</b> Ipsum Dolorem <b>Lirum Larum</b> Ipsum Dolorem <b>Lirum Larum</b> Ipsum Dolorem
                                                  <b>Lirum Larum</b> Ipsum Dolorem <b>Lirum Larum</b> Ipsum Dolorem <b>Lirum Larum</b> Ipsum Dolorem <b>Lirum Larum</b> Ipsum Dolorem 
                                                  <b>Lirum Larum</b> Ipsum Dolorem <b>Lirum Larum</b> Ipsum Dolorem <b>Lirum Larum</b> Ipsum Dolorem <b>Lirum Larum</b> Ipsum Dolorem 
                                                  <b>Lirum Larum</b> Ipsum Dolorem <b>Lirum Larum</b> Ipsum Dolorem <b>Lirum Larum</b> Ipsum Dolorem <b>Lirum Larum</b> Ipsum Dolorem 
                                                  <b>Lirum Larum</b> Ipsum Dolorem <b>Lirum Larum</b> Ipsum Dolorem <b>Lirum Larum</b> Ipsum Dolorem <b>Lirum Larum</b> Ipsum Dolorem 
                                                  <b>Lirum Larum</b> Ipsum Dolorem <b>Lirum Larum</b> Ipsum Dolorem <b>Lirum Larum</b> Ipsum Dolorem <b>Lirum Larum</b> Ipsum Dolorem  
                                                  <b>Lirum Larum</b> Ipsum Dolorem <b>Lirum Larum</b> Ipsum Dolorem <b>Lirum Larum</b> Ipsum Dolorem <b>Lirum Larum</b> Ipsum Dolorem """)

        self.outer_container.append(self.inner_container)
        self.append(self.outer_container)

        test_lights = widgets.trafficlights.trafficlights.Trafficlights()

        self.append(test_lights)


    def userInit(self, *args, **kwargs):
        self.shownInMenu = 'My Example Menu'
        self.menuTitle = 'Test with HTML added to View'


    def updateView(self):
        # Here you can update the view if it needs updates
        pass

