import core.globals
import time
import random
import threading
from remi.gui import *

class Container(Container):

    def __init__(self, AppInst=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.AppInst = AppInst
        self.userInit(args, kwargs)
        self.constructUI()
        self.style.update({'width': '100%', 'height': '100%', 'position': 'relative',
                           'overflow': 'auto', 'margin': 'auto', 'border': '1px solid black',
                           'box-sizing': 'border-box', 'padding': '10px', 'margin-top': '10px'})
        # margin: auto centers the element, box-sizing: border-box forces padding settings just to be applied inside the box


    def constructUI(self):
        schema = Image('/static:images/plant_view/visu_test.jpg', width='1500px')
        self.append(schema, 'schema')

        rl_temp = Label(f"{self.data['rl_temp']:.1f}°C", style={'position': 'absolute', 'top': '630px', 'left': '500px', 'background-color': 'green', 'font-weight': 'bold'})
        vl_temp = Label(f"{self.data['vl_temp']:.1f}°C", style={'position': 'absolute', 'top': '790px', 'left': '500px', 'background-color': 'green', 'font-weight': 'bold'})
        self.append(rl_temp, 'rl_temp')
        self.append(vl_temp, 'vl_temp')

        # Add Button for Pump Control ON/OFF/AUTO


    def userInit(self, *args, **kwargs):
        self.shownInMenu = 'My Example Menu'
        self.menuTitle = 'Show View 3'

        self.data = {}

        # data Aquisition in own thread
        t = threading.Thread(target=self.dummy_values)
        t.daemon = True
        t.start()





    def updateView(self):
    # Update the UI controls with the new values if UI is idle

        self.children['vl_temp'].set_text(f"{self.data['vl_temp']:.1f}°C")
        self.children['rl_temp'].set_text(f"{self.data['rl_temp']:.1f}°C")



    def dummy_values(self):
    # Generate Random Values like data aquisition from Bus System

        while True:
            self.data['vl_temp'] = random.uniform(4.5, 8.5)
            self.data['rl_temp'] = random.uniform(8.0, 12.0)
            time.sleep(1.0)



