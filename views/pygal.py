import core.globals
import remi
import random
import threading
import time
import pygal
import widgets.pygal


class Pygal(remi.gui.Container):
# The name of the class has to be identical with the name of the file (view_template.py), but with capital first letter!
# The App stores an instance of the view in its views{} dictionary. key = filename of the view without '.py' / value = the view instance
# Files which have a Underscore at first place in filename will not be loaded (by renaming you can take them out for development easily).

    def __init__(self, AppInst=None, *args, **kwargs):

        super().__init__(*args, **kwargs)       # Initializes the Parent Object remi.gui.Container
        self.AppInst = AppInst                  # Holds the Instance of the App. We need it to access uiControl
        self.shownInMenu = 'My Example Menu'
        self.menuTitle = 'PyGal Example (dynamic)'
        self.constructUI()


    def constructUI(self):

        # Style the View by updating it style dictionary
        # margin: auto centers the element
        self.style.update({'width': '500px', 'min-height': 'calc(100vh-70px', 'margin': 'auto', 'border': '1px solid black', 'padding': '10px', 'margin-top': '10px', 'overflow': 'auto'})

        self.fileno = 0     # Force the browser to update with different filenames

        # pygal docs: http://www.pygal.org/en/stable/documentation/index.html
        # Create a very simple static Bar Graph with the pygal library
        myBarChart = pygal.Bar()
        myBarChart.x_labels = [2001, 2002, 2003, 2004, 2005, 2006]
        myBarChart.add('My fancy Data', [3, 5, 1, 8, 10, 2])

        self.pygalcanvasbar = widgets.pygal.Pygal(width='480px', height='350px')
        self.pygalcanvasbar.set_content(myBarChart)
        # Append Graph to Container
        self.append(key='bargraph', value=self.pygalcanvasbar)     # You can access the child widgets with self.children('mylabel') or directly with self.myFirstLabel

        # Create data for dynamic Line Graph
        self.graphdata = [1,2,3,4,5]
        self.xlabels = [1,2,3,4,5]

        # Create Pygaldynamic Widget for the LineGraph
        self.pygalcanvasline = widgets.pygal.Pygaldynamic(width='480px', height='400px')    # Empty Image Widget
        self.append(key='linegraph', value=self.pygalcanvasline)

        # data Aquisition in own thread
        t = threading.Thread(target=self.generateRandomData)
        t.daemon = True
        t.start()


    def updateView(self):
        pass


    def refreshLineGraph(self):
        myLineChart = pygal.Line(fill=True, style=pygal.style.DarkSolarizedStyle, range=(0,100))
        myLineChart.add('Random Values', self.graphdata[-32:-1])    # Last 30 values
        myLineChart.x_labels = self.xlabels[-32:-1]                 # Last 30 values
        self.pygalcanvasline.set_content(myLineChart)               # send the new graph to the Pygal Widget


    def generateRandomData(self):
        while True:
            self.graphdata.append(random.randrange(1, 100, 1))    # Add random Data
            self.xlabels.append(int(self.xlabels[-1])+1)          # Add new X axis label for this
            self.refreshLineGraph()                               # refresh the Graph
            time.sleep(0.3)                                       # wait and loop forever
