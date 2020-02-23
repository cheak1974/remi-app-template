import time
import core.globals
import remi
import pygal


class Pygal(remi.gui.Container):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def set_content(self, chart):
        self.data = chart.render()      #_data_uri()
        i = int(time.time() * 1e6)      # ID
        self.style['background-image'] = "url('/%s/download?update_index=%d')" % (id(self), i)
        self.style['background-repeat'] = "no-repeat"

    def download(self, update_index=0):
        content = self.data
        headers = {'Content-type': 'image/svg+xml'}
        return [content, headers]


class Pygaldynamic(remi.gui.Container):

    def __init__(self, update_interval=1.0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.style['background-color'] = 'red'                        # just for testing
        self.style['background-repeat'] = "no-repeat"                  # CSS background command

    def set_content(self, chart):
    # Method for throwing in new chart data. We don't care about the chart type. We just take it and show it.
        self.data = str(chart.render())         # PyGal Method for creating SVG Data from the Chart Object (returns bytes)
        self.data = self.data[2:-1]             # remove the leading b' and the tailing ' in the end. CSS will not work with it correctly. Now it's a clear string
        self.data = self.data.strip().replace('"', "'")
        #print(self.data)                      # Debug
        imagedata = 'url("data:image/svg+xml;' + self.data + '");'
        #print(imagedata)
        #self.style['background-image'] = f'url("data:image/svg+xml;{self.data}")'  # Take the XML/SVG Data and set it as background without creating a file
        self.style['background-image'] = imagedata
