import remi

class View_template(remi.gui.Container):
# The name of the class has to be identical with the name of the file (view_template.py), but with capital first letter!
# Files which have a Underscore at first place in filename will not be loaded (by renaming you can take them out for development easily).

    def __init__(self, AppInst=None, *args, **kwargs):

        super().__init__(*args, **kwargs)       # Initializes the Parent Object remi.gui.Container
        self.AppInst = AppInst                  # Holds the Instance of the App. We need it to access uiControl
        self.shownInMenu = 'Menu Name'          # Use None if it should not be visible in any Menu
        self.menuTitle = 'Text to show in Menu'
        self.constructUI()

    def constructUI(self):
        # The View (self) is a Container itself (inherited from Container)
        # You can append Containers or widgets directly to the self Instance
        # Style the View Container by updating it style dictionary
        # margin: auto centers the element
        self.style.update({'width': '500px', 'height': '500px', 'margin': 'auto', 'border': '1px solid black', 'padding': '10px', 'margin-top': '50px'})

        # Your Widget definitions go here
        self.myFirstLabel = remi.gui.Label('This is my first Widget')

        # Append all Widgets to the Container Instance (self)
        self.append(key='mylabel', value=self.myFirstLabel)     # You can access the child widgets with self.children('mylabel') or directly with self.myFirstLabel


    def updateView(self):
        # Here you can update the view if it needs updates
        pass

    # Add Event Handlers as needed
