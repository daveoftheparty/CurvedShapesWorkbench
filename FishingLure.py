import FreeCAD
import FreeCADGui

import Part
import CurvedShapes
from FreeCAD import Vector, Rotation, Placement
from PySide.QtCore import QT_TRANSLATE_NOOP


def make_Walk_the_Dog_Sketch(doc):
    Walk_the_Dog_Sketch = doc.addObject('Sketcher::SketchObject', 'Walk_the_Dog_Side_Profile')
    Walk_the_Dog_Sketch.Label = 'Walk the Dog Side Profile'
    Walk_the_Dog_Sketch.addGeometry(Part.ArcOfCircle(Part.Circle(Vector(23.76380626473026, 145.9709209274943, 0.0), Vector(0.0, 0.0, 1.0), 153.9709209274943), 4.59835586832567, 4.96793137941701))
    Walk_the_Dog_Sketch.addGeometry(Part.ArcOfCircle(Part.Circle(Vector(23.763806264730338, -145.9709209274943, 0.0), Vector(0.0, 0.0, 1.0), 153.9709209274943), 1.3152539277625774, 1.6848294388539173))
    Walk_the_Dog_Sketch.addGeometry(Part.ArcOfCircle(Part.Circle(Vector(7.045760331163319, 0.0, 0.0), Vector(0.0, 0.0, 1.0), 7.045760331163319), 1.6848294388539173, 4.59835586832567))
    Walk_the_Dog_Sketch.addGeometry(Part.ArcOfCircle(Part.Circle(Vector(61.89930920808833, 0.0, 0.0), Vector(0.0, 0.0, 1.0), 3.100690791911669), 4.96793137941701, 7.5984392349421634))

    Walk_the_Dog_Sketch.AttacherEngine = 'Engine Plane'
    Walk_the_Dog_Sketch.Placement = Placement(Vector(0.0, 0.0, 0.0), Rotation(0.5, 0.5, 0.5, 0.4999999999999999))
    Walk_the_Dog_Sketch.Visibility = False
    Walk_the_Dog_Sketch.ViewObject.Visibility = False
    return Walk_the_Dog_Sketch


def make_Circle_Front_Profile_Sketch(doc):
    Circle_Front_Profile = doc.addObject('Sketcher::SketchObject', 'Circle_Front_Profile')
    Circle_Front_Profile.Label = 'Circle Front Profile'
    Circle_Front_Profile.addGeometry(Part.Circle(Vector(0.0, 0.0, 0.0), Vector(0.0, 0.0, 1.0), 3.0))
    Circle_Front_Profile.AttacherEngine = 'Engine Plane'
    Circle_Front_Profile.Placement = Placement(Vector(0.0, 0.0, 0.0), Rotation(0.7071067811865476, 0.0, 0.0, 0.7071067811865475))
    Circle_Front_Profile.Visibility = False
    Circle_Front_Profile.ViewObject.Visibility = False
    return Circle_Front_Profile


def setup_sketches(doc):
    sketches_group = doc.addObject('App::DocumentObjectGroup', 'Sketches')
    sketches_group.addObject(make_Walk_the_Dog_Sketch(doc))
    sketches_group.addObject(make_Circle_Front_Profile_Sketch(doc))


def draw_FishingLure():
    if FreeCAD.ActiveDocument is not None and FreeCAD.ActiveDocument.Name == "FishingLure":
        FreeCAD.closeDocument(FreeCAD.ActiveDocument.Name)
        FreeCAD.setActiveDocument("")
        FreeCAD.ActiveDocument = None

    doc = FreeCAD.newDocument('FishingLure')

    setup_sketches(doc)

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
