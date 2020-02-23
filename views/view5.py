import core.globals
import helpers.generatetable
import remi.gui

# Just arrange freely the elements for fixed sceen sizes.

class View5(remi.gui.Container):

    def __init__(self, AppInst=None, *args, **kwargs):

        super(View5, self).__init__(*args, **kwargs)
        self.AppInst = AppInst          # Holds the Instance of the App. We need it to access uiControl
        self.shownInMenu = 'My Example Menu'
        self.menuTitle = 'Show View 5'
        self.constructUI()


    def constructUI(self):

        self.base = remi.gui.Container(width='1000px', height='900px',
                                    style={'overflow': 'auto', 'margin': 'auto',
                                           'border': '1px solid black',
                                           'padding': '10px', 'margin-top': '10px'})
        # margin: auto centers the element, class w3-display-container

        self.MyTestTable = helpers.generatetable.generateTable(tableName='tab', tableWidth='800px',
                                                      noRows=4, noColumns=5,
                                                      tableStyle={'table-layout': 'fixed', 'border': '1px solid red', 'overflow': 'hidden', 'word-wrap': 'break-word'},
                                                      rowStyle={},
                                                      cellStyle={'height': '25px', 'background-color': 'cyan'},
                                                      testmode=False)

        self.base.append(self.MyTestTable['tab'])

        self.append(self.base)

        self.MyTestTable['tab-2,5'].set_text('Lirum Larum Ipsum Dolrem sit Lirum Larum Ipsum Dolrem sitLirum Larum Ipsum Dolrem sitLirum Larum Ipsum Dolrem sitLirum Larum Ipsum Dolrem sit')

        self.testbtn = remi.gui.Button('My Button')
        self.MyTestTable['tab-1,3'].append(self.testbtn)

        self.MyTestTable['tab-1,1'].style.update({'width': '10px'})
        self.MyTestTable['tab-1,2'].style.update({'width': '20px'})
        self.MyTestTable['tab-1,3'].style.update({'width': '40px'})
        self.MyTestTable['tab-1,4'].style.update({'width': '80px'})
        self.MyTestTable['tab-1,5'].style.update({'width': '160px'})


    def updateView(self):
        # Here you can update the view if it needs updates
        pass

