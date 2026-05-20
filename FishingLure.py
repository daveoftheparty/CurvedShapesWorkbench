import FreeCAD
import FreeCADGui

import Part
import CurvedShapes
from FreeCAD import Vector, Rotation, Placement
from PySide.QtCore import QT_TRANSLATE_NOOP


def force_show(array):
    array.Solid = not array.Solid
    array.Solid = not array.Solid


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


def make_Crankbait_Side_Profile_Sketch(doc):
    Crankbait_Side_Profile = doc.addObject('Sketcher::SketchObject', 'Crankbait_Side_Profile')
    Crankbait_Side_Profile.Label = 'Crankbait Side Profile'
    geo0 = Crankbait_Side_Profile.addGeometry(Part.LineSegment(Vector(0.0, -13.91, 0.0), Vector(65.0, -13.91, 0.0)))
    Crankbait_Side_Profile.toggleConstruction(geo0)
    geo1 = Crankbait_Side_Profile.addGeometry(Part.LineSegment(Vector(65.0, -13.91, 0.0), Vector(65.0, 13.91, 0.0)))
    Crankbait_Side_Profile.toggleConstruction(geo1)
    geo2 = Crankbait_Side_Profile.addGeometry(Part.LineSegment(Vector(65.0, 13.91, 0.0), Vector(0.0, 13.91, 0.0)))
    Crankbait_Side_Profile.toggleConstruction(geo2)
    geo3 = Crankbait_Side_Profile.addGeometry(Part.Circle(Vector(65.0, -3.43055, 0.0), Vector(0.0, 0.0, 1.0), 1.0))
    Crankbait_Side_Profile.toggleConstruction(geo3)
    geo4 = Crankbait_Side_Profile.addGeometry(Part.Circle(Vector(46.8361, -3.79737, 0.0), Vector(0.0, 0.0, 1.0), 1.0))
    Crankbait_Side_Profile.toggleConstruction(geo4)
    geo5 = Crankbait_Side_Profile.addGeometry(Part.Circle(Vector(24.0673543043263, -21.158894372912883, 0.0), Vector(0.0, 0.0, 1.0), 1.0))
    Crankbait_Side_Profile.toggleConstruction(geo5)
    geo6 = Crankbait_Side_Profile.addGeometry(Part.Circle(Vector(-1.611741877324998, -2.521012393059014, 0.0), Vector(0.0, 0.0, 1.0), 1.0))
    Crankbait_Side_Profile.toggleConstruction(geo6)
    geo7 = Crankbait_Side_Profile.addGeometry(Part.Circle(Vector(-0.3498518594821344, 4.8227987530242125, 0.0), Vector(0.0, 0.0, 1.0), 1.0))
    Crankbait_Side_Profile.toggleConstruction(geo7)
    geo8 = Crankbait_Side_Profile.addGeometry(Part.Circle(Vector(20.613143091401366, 16.44234768240592, 0.0), Vector(0.0, 0.0, 1.0), 1.0))
    Crankbait_Side_Profile.toggleConstruction(geo8)
    geo9 = Crankbait_Side_Profile.addGeometry(Part.Circle(Vector(43.04429502805924, 12.750533643064612, 0.0), Vector(0.0, 0.0, 1.0), 1.0))
    Crankbait_Side_Profile.toggleConstruction(geo9)
    geo10 = Crankbait_Side_Profile.addGeometry(Part.Circle(Vector(65.0, 1.95716, 0.0), Vector(0.0, 0.0, 1.0), 1.0))
    Crankbait_Side_Profile.toggleConstruction(geo10)
    Crankbait_Side_Profile.addGeometry(Part.BSplineCurve([Vector(65.0, -3.43055, 0.0), Vector(46.8361, -3.79737, 0.0), Vector(24.0673543043263, -21.158894372912883, 0.0), Vector(-1.611741877324998, -2.521012393059014, 0.0), Vector(-0.3498518594821344, 4.8227987530242125, 0.0), Vector(20.613143091401366, 16.44234768240592, 0.0), Vector(43.04429502805924, 12.750533643064612, 0.0), Vector(65.0, 1.95716, 0.0)]))
    Crankbait_Side_Profile.AttacherEngine = 'Engine Plane'
    Crankbait_Side_Profile.Placement = Placement(Vector(0.0, 0.0, 0.0), Rotation(0.5, 0.5, 0.5, 0.4999999999999999))
    Crankbait_Side_Profile.Visibility = False
    Crankbait_Side_Profile.ViewObject.Visibility = False
    return Crankbait_Side_Profile


def make_Crankbait_Top_Profile_Sketch(doc):
    Crankbait_Top_Profile = doc.addObject('Sketcher::SketchObject', 'Crankbait_Top_Profile')
    Crankbait_Top_Profile.Label = 'Crankbait Top Profile'
    geo0 = Crankbait_Top_Profile.addGeometry(Part.LineSegment(Vector(-2.693855, 65.0, 0.0), Vector(2.693855, 65.0, 0.0)))
    Crankbait_Top_Profile.toggleConstruction(geo0)
    geo1 = Crankbait_Top_Profile.addGeometry(Part.LineSegment(Vector(-18.0603, 21.330741289041082, 0.0), Vector(18.0603, 21.330741289041082, 0.0)))
    Crankbait_Top_Profile.toggleConstruction(geo1)
    geo2 = Crankbait_Top_Profile.addGeometry(Part.Point(Vector(-11.128, 21.330741289041082, 0.0)))
    Crankbait_Top_Profile.toggleConstruction(geo2)
    geo3 = Crankbait_Top_Profile.addGeometry(Part.Point(Vector(11.128, 21.330741289041082, 0.0)))
    Crankbait_Top_Profile.toggleConstruction(geo3)
    geo4 = Crankbait_Top_Profile.addGeometry(Part.Circle(Vector(-0.0215615665286176, -0.0065573777592247, 0.0), Vector(0.0, 0.0, 1.0), 1.0))
    Crankbait_Top_Profile.toggleConstruction(geo4)
    geo5 = Crankbait_Top_Profile.addGeometry(Part.Circle(Vector(-8.744147048549669, 0.0, 0.0), Vector(0.0, 0.0, 1.0), 1.0))
    Crankbait_Top_Profile.toggleConstruction(geo5)
    geo6 = Crankbait_Top_Profile.addGeometry(Part.Circle(Vector(-13.213326859405798, 21.330741289041082, 0.0), Vector(0.0, 0.0, 1.0), 1.0))
    Crankbait_Top_Profile.toggleConstruction(geo6)
    geo7 = Crankbait_Top_Profile.addGeometry(Part.Circle(Vector(-9.379940000000003, 33.6794, 0.0), Vector(0.0, 0.0, 1.0), 1.0))
    Crankbait_Top_Profile.toggleConstruction(geo7)
    geo8 = Crankbait_Top_Profile.addGeometry(Part.Circle(Vector(-2.6873074077592, 64.99938451935192, 0.0), Vector(0.0, 0.0, 1.0), 1.0))
    Crankbait_Top_Profile.toggleConstruction(geo8)
    Crankbait_Top_Profile.addGeometry(Part.BSplineCurve([Vector(-0.0215615665286176, -0.0065573777592247, 0.0), Vector(-8.744147048549669, 0.0, 0.0), Vector(-13.213326859405798, 21.330741289041082, 0.0), Vector(-9.379940000000003, 33.6794, 0.0), Vector(-2.6873074077592, 64.99938451935192, 0.0)]))
    geo13 = Crankbait_Top_Profile.addGeometry(Part.Circle(Vector(0.0, -1e-16, 0.0), Vector(0.0, 0.0, 1.0), 1.0))
    Crankbait_Top_Profile.toggleConstruction(geo13)
    geo14 = Crankbait_Top_Profile.addGeometry(Part.Circle(Vector(8.744147048549669, 0.0, 0.0), Vector(0.0, 0.0, 1.0), 1.0))
    Crankbait_Top_Profile.toggleConstruction(geo14)
    geo15 = Crankbait_Top_Profile.addGeometry(Part.Circle(Vector(13.213326859405798, 21.330741289041082, 0.0), Vector(0.0, 0.0, 1.0), 1.0))
    Crankbait_Top_Profile.toggleConstruction(geo15)
    geo16 = Crankbait_Top_Profile.addGeometry(Part.Circle(Vector(9.379940000000003, 33.6794, 0.0), Vector(0.0, 0.0, 1.0), 1.0))
    Crankbait_Top_Profile.toggleConstruction(geo16)
    geo17 = Crankbait_Top_Profile.addGeometry(Part.Circle(Vector(2.69386, 65.0, 0.0), Vector(0.0, 0.0, 1.0), 1.0))
    Crankbait_Top_Profile.toggleConstruction(geo17)
    Crankbait_Top_Profile.addGeometry(Part.BSplineCurve([Vector(0.0, -1e-16, 0.0), Vector(8.744147048549669, 0.0, 0.0), Vector(13.213326859405798, 21.330741289041082, 0.0), Vector(9.379940000000003, 33.6794, 0.0), Vector(2.69386, 65.0, 0.0)]))
    Crankbait_Top_Profile.AttacherEngine = 'Engine Plane'
    Crankbait_Top_Profile.Visibility = False
    Crankbait_Top_Profile.ViewObject.Visibility = False
    return Crankbait_Top_Profile


def make_Flat_Sided_Front_Profile_Sketch(doc):
    Flat_Sided_Front_Profile = doc.addObject('Sketcher::SketchObject', 'Flat_Sided_Front_Profile')
    Flat_Sided_Front_Profile.Label = 'Flat Sided Front Profile'
    geo0 = Flat_Sided_Front_Profile.addGeometry(Part.LineSegment(Vector(-4.0, -5.0, 0.0), Vector(4.0, -5.0, 0.0)))
    Flat_Sided_Front_Profile.toggleConstruction(geo0)
    geo1 = Flat_Sided_Front_Profile.addGeometry(Part.LineSegment(Vector(4.0, -5.0, 0.0), Vector(4.0, 5.0, 0.0)))
    Flat_Sided_Front_Profile.toggleConstruction(geo1)
    geo2 = Flat_Sided_Front_Profile.addGeometry(Part.LineSegment(Vector(4.0, 5.0, 0.0), Vector(-4.0, 5.0, 0.0)))
    Flat_Sided_Front_Profile.toggleConstruction(geo2)
    geo3 = Flat_Sided_Front_Profile.addGeometry(Part.LineSegment(Vector(-4.0, 5.0, 0.0), Vector(-4.0, -5.0, 0.0)))
    Flat_Sided_Front_Profile.toggleConstruction(geo3)
    geo4 = Flat_Sided_Front_Profile.addGeometry(Part.Point(Vector(-0.0, -0.0, 0.0)))
    Flat_Sided_Front_Profile.toggleConstruction(geo4)
    Flat_Sided_Front_Profile.addGeometry(Part.ArcOfCircle(Part.Circle(Vector(0.0, -1.7137884072761502, 0.0), Vector(0.0, 0.0, 1.0), 3.2862115927238498), 3.2901830214447942, 6.134594939324585))
    Flat_Sided_Front_Profile.addGeometry(Part.ArcOfCircle(Part.Circle(Vector(0.0, -3.5000000000000004, 0.0), Vector(0.0, 0.0, 1.0), 8.5), 1.2030598901251002, 1.9385327634634626))
    Flat_Sided_Front_Profile.addGeometry(Part.LineSegment(Vector(-4.0, 2.809938199485819, 0.0), Vector(-3.2499999999999996, -2.2002929110092886, 0.0)))
    Flat_Sided_Front_Profile.addGeometry(Part.LineSegment(Vector(4.0, 2.8099381994860955, 0.0), Vector(3.249999999999999, -2.200292911009289, 0.0)))
    Flat_Sided_Front_Profile.addGeometry(Part.ArcOfCircle(Part.Circle(Vector(-2.5165288775701584, 3.0320044709381633, 0.0), Vector(0.0, 0.0, 1.0), 1.5), 1.9385327634636262, 3.290183021444784))
    Flat_Sided_Front_Profile.addGeometry(Part.ArcOfCircle(Part.Circle(Vector(2.5165288775700403, 3.032004470937678, 0.0), Vector(0.0, 0.0, 1.0), 1.5), 6.13459493932511, 7.486245197298824))
    Flat_Sided_Front_Profile.AttacherEngine = 'Engine Plane'
    Flat_Sided_Front_Profile.Placement = Placement(Vector(0.0, 0.0, 0.0), Rotation(0.7071067811865476, 0.0, 0.0, 0.7071067811865475))
    Flat_Sided_Front_Profile.Visibility = False
    Flat_Sided_Front_Profile.ViewObject.Visibility = False
    return Flat_Sided_Front_Profile


def setup_sketches(doc):
    walk_the_dog = make_Walk_the_Dog_Sketch(doc)
    circle_front = make_Circle_Front_Profile_Sketch(doc)
    crankbait_side = make_Crankbait_Side_Profile_Sketch(doc)
    crankbait_top = make_Crankbait_Top_Profile_Sketch(doc)
    flat_sided_front = make_Flat_Sided_Front_Profile_Sketch(doc)
    sketches_group = doc.addObject('App::DocumentObjectGroup', 'Sketches')
    for sketch in [walk_the_dog, circle_front, crankbait_side, crankbait_top, flat_sided_front]:
        sketches_group.addObject(sketch)
    return walk_the_dog, circle_front, crankbait_side, crankbait_top, flat_sided_front


def setup_curved_arrays(walk_the_dog, circle_front, crankbait_side, crankbait_top, flat_sided_front):
    array1 = CurvedShapes.makeCurvedArray(
        Base=circle_front,
        Hullcurves=[walk_the_dog],
        Items=50,
        OffsetStart=0.05,
        OffsetEnd=0.05,
        Solid=True,
        Distribution='x³',
        PreserveAspectRatio=False)
    array1.Label = 'CurvedArray: Walk the Dog, PreserveAspectRatio = False'
    array1.Placement = Placement(Vector(0, 0, 45), array1.Placement.Rotation)
    force_show(array1)

    array2 = CurvedShapes.makeCurvedArray(
        Base=circle_front,
        Hullcurves=[walk_the_dog],
        Items=50,
        OffsetStart=0.05,
        OffsetEnd=0.05,
        Solid=True,
        Distribution='x³',
        PreserveAspectRatio=True)
    array2.Label = 'CurvedArray: Walk the Dog, PreserveAspectRatio = True'
    array2.Placement = Placement(Vector(0, 100, 45), array2.Placement.Rotation)
    force_show(array2)

    array3 = CurvedShapes.makeCurvedArray(
        Base=flat_sided_front,
        Hullcurves=[crankbait_side],
        Items=50,
        Solid=True,
        Distribution='x³',
        PreserveAspectRatio=False)
    array3.Label = 'CurvedArray: Crankbait, PreserveAspectRatio = False'
    force_show(array3)

    array4 = CurvedShapes.makeCurvedArray(
        Base=flat_sided_front,
        Hullcurves=[crankbait_side],
        Items=50,
        Solid=True,
        Distribution='x³',
        PreserveAspectRatio=True)
    array4.Label = 'CurvedArray: Crankbait, PreserveAspectRatio = True'
    array4.Placement = Placement(Vector(0, 100, 0), array4.Placement.Rotation)
    force_show(array4)

    array5 = CurvedShapes.makeCurvedArray(
        Base=flat_sided_front,
        Hullcurves=[crankbait_side, crankbait_top],
        Items=50,
        OffsetStart=0.05,
        OffsetEnd=0.05,
        Solid=True,
        Distribution='x³')
    array5.Label = 'CurvedArray: Crankbait, Side & Top Hullcurves'
    array5.Placement = Placement(Vector(0, 50, -45), array5.Placement.Rotation)
    force_show(array5)


def draw_FishingLure():
    if FreeCAD.ActiveDocument is not None and FreeCAD.ActiveDocument.Name == "FishingLure":
        FreeCAD.closeDocument(FreeCAD.ActiveDocument.Name)
        FreeCAD.setActiveDocument("")
        FreeCAD.ActiveDocument = None

    doc = FreeCAD.newDocument('FishingLure')

    sketches = setup_sketches(doc)
    setup_curved_arrays(*sketches)

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
