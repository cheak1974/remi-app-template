import time
import core.globals
import remi
import pygal


class Pygal(remi.gui.Widget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.style['background-repeat'] = "no-repeat"           # No tiling of BG
        self.style['background-size'] = "contain"                 # Fit Image to Widget size
        self.style['background-position'] = "center center"     # Center Image in Widget
        #self.style['border'] = '1px solid black'                # Draw a border (for debugging)

    def set_content(self, chart):
    # Method for throwing in new Pygal chart data. We don't care about the chart type. We just take the PyGal Object it and show it.
        self.data = chart.render_data_uri()                         # Build in function to render SVG images as URI in Base64
        self.style['background-image'] = f"url({self.data})"
