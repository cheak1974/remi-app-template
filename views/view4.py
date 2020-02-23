import core.globals
import remi.gui

#Example with class from remi editor.
# We have to edit the editor output manually because it doesn't uses fully qualified namespace Widget() -> remi.gui.Widget()



class View4(remi.gui.Container):

    def __init__(self, AppInst=None, *args, **kwargs):

        super(View4, self).__init__(*args, **kwargs)
        self.AppInst = AppInst          # Holds the Instance of the App. We need it to access uiControl
        self.shownInMenu = 'My Example Menu'
        self.menuTitle = 'Show View 4'
        self.constructUI()


    def constructUI(self):

        ######### EDITOR SHOULD ONLY MAKE CHANGES TO THIS PART ##############

        base = remi.gui.Container()
        base.attributes.update({"class": "Widget", "editor_constructor": "()", "editor_varname": "base", "editor_tag_type": "widget",
             "editor_newclass": "False", "editor_baseclass": "Widget"})
        base.style.update({"margin": "0px", "width": "775.0px", "height": "430.0px", "top": "100px", "left": "20px",
                           "position": "absolute", "overflow": "auto", "border-width": "1px", "border-style": "solid"})
        medium = remi.gui.DropDown()
        medium.attributes.update({"class": "DropDown", "editor_constructor": "()", "editor_varname": "medium", "editor_tag_type": "widget",
             "editor_newclass": "False", "editor_baseclass": "DropDown"})
        medium.style.update(
            {"margin": "0px", "width": "580.0px", "height": "45.0px", "top": "30.0px", "left": "100.0px",
             "position": "absolute", "overflow": "auto"})
        wasser = remi.gui.DropDownItem('Wasser')
        wasser.attributes.update({"class": "DropDownItem", "editor_constructor": "('Wasser')", "editor_varname": "wasser",
             "editor_tag_type": "widget", "editor_newclass": "False", "editor_baseclass": "DropDownItem",
             "selected": "selected"})
        wasser.style.update({"margin": "0px", "overflow": "auto"})
        medium.append(wasser, 'wasser')
        wasser_glykol_35 = remi.gui.DropDownItem('Wasser-Ethylenglykol 35%')
        wasser_glykol_35.attributes.update({"class": "DropDownItem", "editor_constructor": "('Wasser-Ethylenglykol 35%')",
             "editor_varname": "wasser_glykol_35", "editor_tag_type": "widget", "editor_newclass": "False",
             "editor_baseclass": "DropDownItem"})
        wasser_glykol_35.style.update({"margin": "0px", "overflow": "auto"})
        medium.append(wasser_glykol_35, 'wasser_glykol_35')
        base.append(medium, 'medium')

        self.append(base)

        ############## EDITOR SHOULD MAKE NO CHANGES BEYOND THIS POINT ##########

        # Here could be user defined event signals



    def updateView(self):
        # Here you can update the view if it needs updates
        pass

