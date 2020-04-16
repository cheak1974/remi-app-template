import core.globals
import remi.gui
import remi.server


class Webapi(remi.gui.Widget):
    # To use the Web API just add the Widget Web_api to the main container

    def __init__(self, AppInst=None, **kwargs):
        super(Webapi, self).__init__(**kwargs)

        self.AppInst = AppInst          # get the Remi AppInst for Access on all members, methods, etc.


    ############ API FUNCTIONS ###################


    def confirm(self, user, conf):
        # Method that is called if you need to verify a user (e.g. after sending him an email with confirmation code)
        # url "http://127.0.0.1:8082/api/confirm?user=text1&conf=text2

        user = user.strip().lower()
        conf = conf.strip()
        print('Received: ' + user + ' ' + conf)

        # Your Code:  Check the conf code given against the parameter stored in user details

        headers = {'Content-type': 'text/plain'}
        return ['OK', headers]


    def switch(self, view):
        # Method for switching the App view via a html <a> link. You can use relative Links inside your app as well.
        # "http://127.0.0.1:8080/api/switch?view=view2
        # <a href="/api/switch?view=view1>Click here to get to View1</a>

        # Take the name of the view and call uiControl from AppInst
        self.AppInst.uiControl(self, view=view)

        # Get actual AppUrl (http://adresse:port) from active browserwindow address bar (_self)
        # Get complete Url Location and split along /
        # Build base Url of App with appurl and load it into active window
        # The Api isn't showing anything but returns text to the browser. After executing our command we have to refresh the app
        headers = {'Content-type': 'text/html'}
        html = """
                <html>
                <head></head>
                <body>
                <script language="javascript" type="text/javascript">
                    var url = window.location.href;                                         
                    var arr = url.split("/");
                    var appurl = arr[0] + "//" + arr[2];
                    app = window.open(appurl, '_self');
                </script>
                </body></html>
                """

        return [html, headers]


    def newswitch(self, view):
        # Method for switching the App view via a html <a> link. You can use relative Links inside your app as well.
        # "http://127.0.0.1:8080/api/newswitch?view=view2
        # <a href="/api/switch?view=view1>Click here to get to View1</a>    Use it as relative link.

        # Take the name of the view and call uiControl from AppInst
        self.AppInst.uiControl(self, view=view)
        # Build a small html page which reloads the origin address (http://url:port) into the same window.
        content = '<html><head></head><body><script language="javascript" type="text/javascript">window.open(window.location.origin, "_self");</script></body></html> '
        headers = {'Content-type': 'text/html'}
        return [content, headers]


    def sentences(self, amount):
        # Method from user question. This function forwards the parameter from api call to a method of the AppInstance
        # The method in AppInstance updates the view Instances 'sentences.py' along by using the parameter and switches to view sentences afterwards
        # "http://127.0.0.1:8080/api/sentences?amount=50"

        self.AppInst.printSentences(self, amount)

        # Load AppUrl (http://adresse:port) in active window (_self)
        headers = {'Content-type': 'text/html'}
        html = '<html><head></head><body><script language="javascript" type="text/javascript">window.open(window.location.origin, "_self");</script></body></html> '
        return [html, headers]

