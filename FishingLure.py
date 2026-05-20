import FreeCAD
import FreeCADGui
import CurvedShapes
from PySide.QtCore import QT_TRANSLATE_NOOP


def draw_FishingLure():
    if FreeCAD.ActiveDocument is not None and FreeCAD.ActiveDocument.Name == "FishingLure":
        FreeCAD.closeDocument(FreeCAD.ActiveDocument.Name)
        FreeCAD.setActiveDocument("")
        FreeCAD.ActiveDocument = None

    doc = FreeCAD.newDocument('FishingLure')

    doc.recompute()
    FreeCADGui.activeDocument().activeView().viewIsometric()
    FreeCADGui.SendMsgToActiveView("ViewFit")


class FishingLure():
    def Activated(self):
        import FishingLure
        draw_FishingLure()

    def GetResources(self):
        import CurvedShapes
        import os
        return {'Pixmap'  : os.path.join(CurvedShapes.get_module_path(), "Resources", "icons", "curvedArray.svg"),
                'MenuText': QT_TRANSLATE_NOOP("FishingLure", "Fishing Lure"),
                'ToolTip' : QT_TRANSLATE_NOOP("FishingLure", "Example fishing lure shapes demonstrating the PreserveAspectRatio property of CurvedArray")}


FreeCADGui.addCommand('FishingLure', FishingLure())
