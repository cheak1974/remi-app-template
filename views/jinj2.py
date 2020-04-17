import remi.gui
import widgets.htmltemplate


class Container(remi.gui.Container):

    def __init__(self, AppInst=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.AppInst = AppInst
        self.constructUI()
        self.userInit(args, kwargs)


    def constructUI(self):

        # Here we use another base Container for GUI Design and append it in the end to self. We could also use directly self.
        self.base = remi.gui.Container(width='80%', style={'overflow': 'auto', 'margin': 'auto',
                                                        'padding': '5px', 'border': '1px solid black', 'margin-top': '10px'})

        # Typical REMI Table
        self.table = remi.gui.Table(width='90%', style={'border': '1px solid red'})
        self.r1 = remi.gui.TableRow()
        self.c11 = remi.gui.TableItem('Nur Text')
        self.c12 = remi.gui.TableItem('Nur Text 2')
        self.c13 = remi.gui.TableItem()
        self.testbtn = remi.gui.Button('Buttons can be inside Table :-)', style={'box-shadow': 'none', 'font-style': 'normal', 'font-weight': 'normal'})
        self.testbtn.add_class('w3-btn w3-green w3-hover-yellow')
        self.c13.append(self.testbtn)

        self.r1.append(self.c11)
        self.r1.append(self.c12)
        self.r1.append(self.c13)
        self.table.append(self.r1)

        self.base.append(self.table)

        # Test with "handmade" own html table.
        self.base.add_child('html1', '<table width="90%" , style="border: 1px solid orange;"><tr>')
        self.base.add_child('html2', '<td>')
        self.button = remi.gui.Button('This works also in "handmade" Tables', style={'font-style': 'normal', 'font-weight': 'normal'})
        self.button.add_class('w3-btn w3-hover-yellow w3-small w3-round-large')
        self.base.append(self.button)
        self.base.add_child('html3', '</td></tr></table>')

        self.append(self.base)


        # Test with manually added HTML Code
        self.div = remi.gui.Container(width='300px', height='300px', style={'margin': 'auto', 'border': '1px solid black',
                                                                         'margin-top': '10px', 'padding': '5px', 'text-align': 'justify'})

        self.div.add_child('html', """You can also insert simple HTML Documents into REMI Widgets. By doing this
                                   you can work with templates. With an API function you can also use usual
                                   HTML Links to link to other <a href="/api/switch?view=start">documents/views (Here: Start View)</a>.
                                   Or you can link to other api functions and give parameters <a href="/api/sentences?amount=50">Sentences Example</a>
                                   """)
        self.append(self.div)


        # Work with Jinja templates
        self.templatetest = widgets.htmltemplate.Htmltemplate(templatefile='jinja_example.html', width='80%',
                                                                           style={'margin': 'auto', 'border': '1px solid black', 'margin-top': '10px'},
                                                                           listofviews=str(self.AppInst.views.keys()))
        self.append(self.templatetest)


    def userInit(self, *args, **kwargs):
        self.shownInMenu = 'My Example Menu'
        self.menuTitle = 'Jinja2 Testing'


    def updateView(self):
        # Here you can update the view if it needs updates
        pass

