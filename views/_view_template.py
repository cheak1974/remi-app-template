from remi.gui import *

class Container(Container):

    def __init__(self, AppInst=None, *args, **kwargs):
        super().__init__(*args, **kwargs)                                                # Initializes the Parent Object remi.gui.Container
        self.AppInst = AppInst                                                           # Instances of the REMI App Instance. Needed to call methods placed there.
        self.constructUI()                                                               # Call the Editor made constructUI method
        self.userInit(args, kwargs)                                                      # Call custom Usercode


    def constructUI(self):
        # This method is reserved for the REMI Editor. You can also use it, but if you load it into the Editor your UI may break.
        myLabel = Label('This is a Test Label')                                         # Create a Label
        self.append(myLabel, 'myLabel')                                                 # Add it to the View Container


    def userInit(self, *args, **kwargs):
        # Here you can add Instance Attributes, do additional styling, register events etc.
        self.style.update({'width': '100%', 'position': 'relative', 'margin': 'auto'})  # Absolute Base configuration of the container. Use relative for proper Widget placement.
        self.shownInMenu = 'My Menu Name'                                               # Change to None if the View should not be visible in Menu, otherwise this is the Menu Name
        self.menuTitle = 'My View Template'                                             # The View will appear with this name in the Menu above


    def updateView(self):
        # Here you can update the view if it needs updates. This method is called periodically if the App is idle.
        pass

    # Rest of file is free for your own methods