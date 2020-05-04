
from remi.gui import *
import threading, random, time

class Container( Container ):                                                                                                          #cheak:Maybe change class name to name of root container

    def __init__(self, AppInst=None, *args, **kwargs):
        super().__init__(*args, **kwargs)                                                                                                #cheak:remove Comments
        self.AppInst = AppInst                                                                                                           #cheak:remove Comments
        self.constructUI()                                                                                                               #cheak:instead we just call it
        self.userInit(*args, **kwargs)                                                                                                   #more. Register events. Add custom widgets. Add css classes etc.
                                                                                                                                         # pass kwargs to user init in case user needs it.

    def constructUI(self):
        self.attr_editor_newclass = False
        self.css_height = "600px"
        self.css_left = "px"
        self.css_margin = "0px"
        self.css_position = "absolute"
        self.css_top = "px"
        self.css_width = "1024px"
        self.variable_name = "container0"
        image0 = Image()
        image0.attr_editor_newclass = False
        image0.attr_src = "/static:images/plant_view/visu_test.jpg"
        image0.css_height = "500px"
        image0.css_left = "75.0px"
        image0.css_margin = "0px"
        image0.css_position = "absolute"
        image0.css_top = "45.0px"
        image0.css_width = "px"
        image0.variable_name = "image0"
        self.append(image0,'image0')
        vl_temp = Label()
        vl_temp.attr_editor_newclass = False
        vl_temp.css_align_content = "stretch"
        vl_temp.css_background_color = "rgb(0,200,0)"
        vl_temp.css_border_color = "rgb(0,0,0)"
        vl_temp.css_border_style = "solid"
        vl_temp.css_border_width = "1px"
        vl_temp.css_direction = "none"
        vl_temp.css_font_family = ""
        vl_temp.css_font_size = "16px"
        vl_temp.css_font_weight = "bold"
        vl_temp.css_height = "30px"
        vl_temp.css_justify_content = "flex-start"
        vl_temp.css_left = "445.0px"
        vl_temp.css_margin = "0px"
        vl_temp.css_position = "absolute"
        vl_temp.css_text_align = "center"
        vl_temp.css_top = "540.0px"
        vl_temp.css_width = "50px"
        vl_temp.text = "6°C"
        vl_temp.variable_name = "vl_temp"
        self.append(vl_temp,'vl_temp')
        rl_temp = Label()
        rl_temp.attr_editor_newclass = False
        rl_temp.css_background_color = "rgb(0,200,0)"
        rl_temp.css_border_style = "solid"
        rl_temp.css_border_width = "1px"
        rl_temp.css_font_size = "16px"
        rl_temp.css_font_weight = "bold"
        rl_temp.css_height = "30px"
        rl_temp.css_left = "445.0px"
        rl_temp.css_margin = "0px"
        rl_temp.css_position = "absolute"
        rl_temp.css_text_align = "center"
        rl_temp.css_top = "375.0px"
        rl_temp.css_width = "50px"
        rl_temp.text = "12°C"
        rl_temp.variable_name = "r_temp"
        self.append(rl_temp,'rl_temp')
        p1_status = Label()
        p1_status.attr_editor_newclass = False
        p1_status.css_background_color = "rgb(0,200,0)"
        p1_status.css_border_style = "solid"
        p1_status.css_border_width = "1px"
        p1_status.css_font_size = "14px"
        p1_status.css_font_weight = "bold"
        p1_status.css_height = "20px"
        p1_status.css_left = "635.0px"
        p1_status.css_margin = "0px"
        p1_status.css_position = "absolute"
        p1_status.css_text_align = "center"
        p1_status.css_top = "495.0px"
        p1_status.css_width = "80px"
        p1_status.text = "AN (Auto)"
        p1_status.variable_name = "p1_status"
        self.append(p1_status,'p1_status')
        p2_status = Label()
        p2_status.attr_editor_newclass = False
        p2_status.css_background_color = "rgb(200,0,0)"
        p2_status.css_border_style = "solid"
        p2_status.css_border_width = "1px"
        p2_status.css_font_size = "14px"
        p2_status.css_font_weight = "bold"
        p2_status.css_height = "20px"
        p2_status.css_left = "775.0px"
        p2_status.css_margin = "0px"
        p2_status.css_position = "absolute"
        p2_status.css_text_align = "center"
        p2_status.css_top = "495.0px"
        p2_status.css_width = "80px"
        p2_status.text = "AUS (Auto)"
        p2_status.variable_name = "p2_status"
        self.append(p2_status,'p2_status')
        km2_status = Label()
        km2_status.attr_editor_newclass = False
        km2_status.css_background_color = "rgb(0,200,0)"
        km2_status.css_border_style = "solid"
        km2_status.css_border_width = "1px"
        km2_status.css_font_size = "16px"
        km2_status.css_font_weight = "bold"
        km2_status.css_height = "30px"
        km2_status.css_left = "350.0px"
        km2_status.css_margin = "0px"
        km2_status.css_position = "absolute"
        km2_status.css_text_align = "center"
        km2_status.css_top = "15.0px"
        km2_status.css_width = "150px"
        km2_status.text = "AN (Auto)"
        km2_status.variable_name = "km2_status"
        self.append(km2_status,'km2_status')
        km1_status = Label()
        km1_status.attr_editor_newclass = False
        km1_status.css_background_color = "rgb(200,0,0)"
        km1_status.css_border_style = "solid"
        km1_status.css_border_width = "1px"
        km1_status.css_font_size = "16px"
        km1_status.css_font_weight = "bold"
        km1_status.css_height = "30px"
        km1_status.css_left = "125.0px"
        km1_status.css_margin = "0px"
        km1_status.css_position = "absolute"
        km1_status.css_text_align = "center"
        km1_status.css_top = "15.0px"
        km1_status.css_width = "150px"
        km1_status.text = "AUS (Auto)"
        km1_status.variable_name = "km1_status"
        self.append(km1_status,'km1_status')
        km2_setup = Button()
        km2_setup.attr_editor_newclass = False
        km2_setup.css_background_color = "rgb(0,0,0)"
        km2_setup.css_height = "30px"
        km2_setup.css_left = "400.0px"
        km2_setup.css_margin = "0px"
        km2_setup.css_position = "absolute"
        km2_setup.css_top = "205.0px"
        km2_setup.css_width = "80px"
        km2_setup.text = "Einstellen"
        km2_setup.variable_name = "km2_setup"
        self.append(km2_setup,'km2_setup')
        km1_setup = Button()
        km1_setup.attr_editor_newclass = False
        km1_setup.css_background_color = "rgb(0,0,0)"
        km1_setup.css_height = "30px"
        km1_setup.css_left = "175.0px"
        km1_setup.css_margin = "0px"
        km1_setup.css_position = "absolute"
        km1_setup.css_top = "205.0px"
        km1_setup.css_width = "80px"
        km1_setup.text = "Einstellen"
        km1_setup.variable_name = "km1_setup"
        self.append(km1_setup,'km1_setup')
        p1_setup = Button()
        p1_setup.attr_editor_newclass = False
        p1_setup.css_background_color = "rgb(0,0,0)"
        p1_setup.css_height = "30px"
        p1_setup.css_left = "660.0px"
        p1_setup.css_margin = "0px"
        p1_setup.css_position = "absolute"
        p1_setup.css_top = "550.0px"
        p1_setup.css_width = "80px"
        p1_setup.text = "Einstellen"
        p1_setup.variable_name = "p1_setup"
        self.append(p1_setup,'p1_setup')
        p2_setup = Button()
        p2_setup.attr_editor_newclass = False
        p2_setup.css_background_color = "rgb(0,0,0)"
        p2_setup.css_height = "30px"
        p2_setup.css_left = "755.0px"
        p2_setup.css_margin = "0px"
        p2_setup.css_position = "absolute"
        p2_setup.css_top = "550.0px"
        p2_setup.css_width = "80px"
        p2_setup.text = "Einstellen"
        p2_setup.variable_name = "p2_setup"
        self.append(p2_setup,'p2_setup')


    def userInit(self, *args, **kwargs):
        self.shownInMenu = 'My Example Menu'
        self.menuTitle = 'Plant View'

        self.children['km1_setup'].onclick.do(self.handleButtons)
        self.children['km2_setup'].onclick.do(self.handleButtons)
        self.children['p1_setup'].onclick.do(self.handleButtons)
        self.children['p2_setup'].onclick.do(self.handleButtons)

        self.data = {}                      # Dict for Datapoints

        self.data_aquisition_thread_started = False



    def updateView(self):

        if self.data_aquisition_thread_started == False and self.AppInst.connection_established == True:
            # data Aquisition in own thread
            t = threading.Thread(target=self.dummy_values)
            t.daemon = True
            t.start()
            return

        # Update the UI controls with the new values if UI is idle

        # Update Temperatures
        self.children['vl_temp'].set_text(f"{self.data['vl_temp']:.1f}°C")
        self.children['rl_temp'].set_text(f"{self.data['rl_temp']:.1f}°C")

        # Update chiller status
        self.children['km1_status'].set_text(f"{self.data['km1_status']}")
        if self.data['km1_run'] == 'AUS':
            self.children['km1_status'].css_background_color = 'rgb(200,0,0)'
        else:
            self.children['km1_status'].css_background_color = 'rgb(0,200,0)'

        self.children['km2_status'].set_text(f"{self.data['km2_status']}")
        if self.data['km2_run'] == 'AUS':
            self.children['km2_status'].css_background_color = 'rgb(200,0,0)'
        else:
            self.children['km2_status'].css_background_color = 'rgb(0,200,0)'



    def handleButtons(self, emittingButton):

        if emittingButton == self.children['km1_setup']:
            self.AppInst.showDialog(emittingButton, 'setup_km', title='Setup KM 1', km='km1')

        if emittingButton == self.children['km2_setup']:
            self.AppInst.showDialog(emittingButton, 'setup_km', title='Setup KM 2', km='km2')



    def dummy_values(self):
        # Generate Random Values like data aquisition from Bus System
        # This is absolutely not needed for the UI

        self.data_aquisition_thread_started = True

        self.data['km1_run'] = 'AUS'
        self.data['km1_setting'] = 'AUTO'
        self.data['km1_setpoint'] = 6.0
        self.data['km2_run'] = 'AN'
        self.data['km2_setting'] = 'AUTO'
        self.data['km2_setpoint'] = 6.0

        # check if the Instance that opened the view is still alive. Stop the thread if its dead.
        while self.AppInst.connection_established == True:

            self.data['vl_temp'] = random.uniform(4.5, 8.5)
            self.data['rl_temp'] = random.uniform(8.0, 12.0)

            if self.data['km1_setting'] == 'AN MAN':
                self.data['km1_run'] = 'AN'
            if self.data['km1_setting'] == 'AUS MAN':
                self.data['km1_run'] = 'AUS'

            if self.data['km2_setting'] == 'AN MAN':
                self.data['km2_run'] = 'AN'
            if self.data['km2_setting'] == 'AUS MAN':
                self.data['km2_run'] = 'AUS'

            self.data['km1_status'] = self.data['km1_run'] + ' (' + self.data['km1_setting'] + ')'
            self.data['km2_status'] = self.data['km2_run'] + ' (' + self.data['km2_setting'] + ')'

            time.sleep(1.0)

        self.data_aquisition_thread_started = False     # Set the flag back for next visit