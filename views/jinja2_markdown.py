import remi.gui
import widgets.htmltemplate



class Container(remi.gui.Container):

    def __init__(self, AppInst=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.AppInst = AppInst
        self.constructUI()
        self.userInit(args, kwargs)


    def constructUI(self):

        markdown="""

# Euler's Identity

In mathematics, **Euler's identity** is the equality
$$ e^{i \pi} + 1 = 0. $$

## Explanation

Euler's identity is a special case of Euler's formula from complex
analysis, which states that for any real number $ x $,
$$ e^{ix} = \cos x + i \sin x. $$

<script src="https://cdn.jsdelivr.net/npm/texme"></script>
     
"""

        # Work with Jinja templates, here loading a static page.
        self.templatetest = widgets.htmltemplate.Htmltemplate(templatefile='jinja_markdown.html')
        self.append(self.templatetest)

        # Here creating a container and loading the same html one more time
        self.test1 = remi.gui.Container(width='80%', style={'border': '1px black solid', 'margin': 'auto'})
        self.test1.add_child(key='direct', value=markdown)
        self.append(self.test1)


    def userInit(self, *args, **kwargs):
        self.shownInMenu = 'My Example Menu'
        self.menuTitle = 'Jinja2 Markdown testing'


    def updateView(self):
        # Here you can update the view if it needs updates
        pass

