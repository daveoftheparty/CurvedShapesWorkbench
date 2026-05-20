import FreeCAD as app
import Sketcher, Part

def createSketch_Circle_Front_Profile(doc):
    Circle_Front_Profile = doc.addObject('Sketcher::SketchObject', 'Circle_Front_Profile')
    geo0 = Circle_Front_Profile.addGeometry(Part.Circle(Vector(0.0, 0.0, 0.0), Vector (0.0, 0.0, 1.0), 3.0))
    Circle_Front_Profile.addConstraint(Sketcher.Constraint('Diameter', geo0, 6.0))
    Circle_Front_Profile.addConstraint(Sketcher.Constraint('Coincident', geo0, 3, -1, 1))
    Circle_Front_Profile.AttacherEngine = 'Engine Plane'
    Circle_Front_Profile.Placement = Placement(Vector(0.0, 0.0, 0.0), Rotation (0.7071067811865476, 0.0, 0.0, 0.7071067811865475))
    Circle_Front_Profile.Visibility = False
    Circle_Front_Profile.ViewObject.Visibility = False
    return Circle_Front_Profile

def make_doc():
    doc = app.newDocument('bait_to_copy')
    Circle_Front_Profile = createSketch_Circle_Front_Profile(doc)
    doc.recompute()

make_doc()