import remi
import random
import threading
import time
import pygal
import widgets.pygal.pygal


class Container(remi.gui.Container):

    def __init__(self, AppInst=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.AppInst = AppInst
        self.constructUI()
        self.userInit(args, kwargs)


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

        self.pygalcanvasbar = widgets.pygal.pygal.Pygal(width='480px', height='350px', style={'margin-top': '20px'})
        self.pygalcanvasbar.set_content(myBarChart)
        # Append Graph to Container
        self.append(key='bargraph', value=self.pygalcanvasbar)     # You can access the child widgets with self.children('mylabel') or directly with self.myFirstLabel

        # Create data for dynamic Line Graph
        self.graphdata = [1,2,3,4,5]
        self.xlabels = [1,2,3,4,5]

        # Create Pygaldynamic Widget for the LineGraph
        self.pygalcanvasline = widgets.pygal.pygal.Pygal(width='480px', height='350px', style={'margin-top': '20px'})    # Empty Image Widget
        self.append(key='linegraph', value=self.pygalcanvasline)

        # data Aquisition in own thread
        t = threading.Thread(target=self.generateRandomData)
        t.daemon = True
        t.start()


    def userInit(self, *args, **kwargs):
        self.shownInMenu = 'My Example Menu'
        self.menuTitle = 'PyGal Example (dynamic)'

        self.generation_thread_started = False


    def updateView(self):

        if self.generation_thread_started == False and self.AppInst.connection_established == True:    # Flag is used to start the thread only once
            # Data Aquisition in own thread
            t = threading.Thread(target=self.generateRandomData)
            t.setDaemon(True)
            t.setName(str(self.AppInst.session) + '_pygal_thread')
            t.start()
            self.generation_thread_started = True

        self.refreshLineGraph()


    def refreshLineGraph(self):
        myLineChart = pygal.Line(fill=True, style=pygal.style.DarkSolarizedStyle, range=(0,100))
        myLineChart.add('Random Values', self.graphdata[-32:-1])    # Last 30 values
        myLineChart.x_labels = self.xlabels[-32:-1]                 # Last 30 values
        self.pygalcanvasline.set_content(myLineChart)               # send the new graph to the Pygal Widget


    def generateRandomData(self):

        while self.AppInst.connection_established == True:          # Run thread until the calling App Instance is disconnected
            self.graphdata.append(random.randrange(1, 100, 1))      # Add random Data
            self.xlabels.append(int(self.xlabels[-1])+1)            # Add new X axis label for this
            time.sleep(0.5)                                         # wait and loop forever

        self.generation_thread_started = False                      # Set Flag back to false when ending thread


        return

