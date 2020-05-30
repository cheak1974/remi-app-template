import sys
import core.globals
import remi
import jinja2


class Htmltemplate(remi.gui.Container):

    def __init__(self, templatefile, *args, **kwargs):
        super().__init__(*args, **kwargs)
        templatepath = sys.path[0] + core.globals.config['rel_path_to_static'] + '//templates//'


        # Jinja2 Magic
        self.file_loader = jinja2.FileSystemLoader(templatepath)     # Define Place where templates live
        self.env = jinja2.Environment(loader=self.file_loader)       # Make Jinja2 Environment with markup extension
        self.template = self.env.get_template(templatefile)          # Load template with filename from arg
        self.add_child('jinja', self.template.render(data=kwargs))   # render the template file


    def setTemplate(self, templatefile, *args, **kwargs):
        self.remove_child('jinja')
        self.template = self.env.get_template(templatefile)          # Load new template with filename from arg
        self.add_child('jinja', self.template.render(data=kwargs))              # render the new template file
