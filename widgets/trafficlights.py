import remi
import os, sys, base64
import widgets

class Trafficlights(remi.gui.Widget, remi.gui.EventSource):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)         # Init with original Image size
        self.style['background-repeat'] = "no-repeat"               # No tiling of BG
        self.style['background-size'] = "cover"                     # Fit Image to Widget size
        self.style['background-position'] = "center center"         # Center Image in Widget
        self.style['border'] = '1px solid black'                    # Draw a border (for debugging)

        widget_folder = os.path.dirname(widgets.__file__)           # Get the path of the folder where the custom widgets live

        # Loading Images from disk and converting it to base64. We do not need to load them from static folder then
        green_file = open(f'{widget_folder}/trafficlights/traffic_green.gif', 'rb')       # Read jpg as binary
        green_binary = green_file.read()
        green_file.close()
        green_base64 = base64.b64encode(green_binary)                                   # Convert to Base64 (still bytes)
        green_base64_message = green_base64.decode('utf-8')                             # Decode Base64 to utf-8
        self.green = f"url('data:image/gif;base64,{green_base64_message}')"             # Save the Image for use in css background

        red_file = open(f'{widget_folder}/trafficlights/traffic_red.gif', 'rb')       # Read jpg as binary
        red_binary = red_file.read()
        red_file.close()
        red_base64 = base64.b64encode(red_binary)                                       # Convert to Base64 (still bytes)
        red_base64_message = red_base64.decode('utf-8')                                 # Decode Base64 to utf-8
        self.red = f"url('data:image/gif;base64,{red_base64_message}')"                 # Save the Image for use in css background

        yellow_file = open(f'{widget_folder}/trafficlights/traffic_yellow.gif', 'rb') # Read jpg as binary
        yellow_binary = yellow_file.read()
        yellow_file.close()
        yellow_base64 = base64.b64encode(yellow_binary)                                 # Convert to Base64 (still bytes)
        yellow_base64_message = yellow_base64.decode('utf-8')                           # Decode Base64 to utf-8
        self.yellow = f"url('data:image/gif;base64,{yellow_base64_message}')"           # Save the Image for use in css background

        self.state='green'                                                              # Set initial state of the traffic lights

        self.style['background-image'] = self.green                                     # Load the prepared image to Widget Background
        self.onclick.do(self.handleclick)                                               # Register handler for onclick event


    def set_state(self, state='green'):

        if state == 'green' or state == 'red' or state == 'yellow':
            self.state = state
            self.style['background-image'] = self.__dict__[state]


    def handleclick(self, emittingWidget):
        # Change the state of the traffic lights when clicking on it

        if self.state == 'green':
            self.state = 'yellow'
            print('Switch to yellow')
            self.style['background-image'] = self.yellow

        elif self.state == 'yellow':
            self.state = 'red'
            print('Switch to red')
            self.style['background-image'] = self.red

        elif self.state == 'red':
            self.state = 'green'
            print('switch to green')
            self.style['background-image'] = self.green
