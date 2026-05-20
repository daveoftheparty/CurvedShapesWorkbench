import FreeCAD as app
import Sketcher, Part

def createSketch_Sketch(doc):
    Eye_Revolve_Sketch = doc.addObject('Sketcher::SketchObject', 'Sketch')
    geo0 = Eye_Revolve_Sketch.addGeometry(Part.Point(Vector(3e-16, 1.3000000000000003, 0.0)))
    Eye_Revolve_Sketch.toggleConstruction(geo0)
    geo1 = Eye_Revolve_Sketch.addGeometry(Part.ArcOfCircle(Part.Circle(Vector(0.0, -2.8115384615384786, 0.0), Vector (0.0, 0.0, 1.0), 4.111538461538479), 1.5707963267948966, 2.388611984696748))
    Eye_Revolve_Sketch.toggleConstruction(geo1)
    geo2 = Eye_Revolve_Sketch.addGeometry(Part.LineSegment(Vector (3e-16, 0.0, 0.0), Vector (-3.000000000000014, -7.5e-15, 0.0)))
    Eye_Revolve_Sketch.toggleConstruction(geo2)
    geo3 = Eye_Revolve_Sketch.addGeometry(Part.ArcOfCircle(Part.Circle(Vector(0.0, -2.8115384615384786, 0.0), Vector (0.0, 0.0, 1.0), 4.111538461538479), 1.5707963267948966, 2.816929336448888))
    geo4 = Eye_Revolve_Sketch.addGeometry(Part.LineSegment(Vector (-3.8967442031284882, -1.5000000000000002, 0.0), Vector (0.0, -1.5000000000000002, 0.0)))
    geo5 = Eye_Revolve_Sketch.addGeometry(Part.LineSegment(Vector (0.0, -1.5000000000000002, 0.0), Vector (3e-16, 1.3000000000000005, 0.0)))
    Eye_Revolve_Sketch.addConstraint(Sketcher.Constraint('DistanceY', -1, 1, geo0, 1, 1.3))
    Eye_Revolve_Sketch.addConstraint(Sketcher.Constraint('Coincident', geo1, 2, -3, 2))
    Eye_Revolve_Sketch.addConstraint(Sketcher.Constraint('Coincident', geo1, 1, geo0, 1))
    Eye_Revolve_Sketch.addConstraint(Sketcher.Constraint('PointOnObject', geo1, 3, -2))
    Eye_Revolve_Sketch.addConstraint(Sketcher.Constraint('Coincident', geo2, 1, -1, 1))
    Eye_Revolve_Sketch.addConstraint(Sketcher.Constraint('Coincident', geo2, 2, geo1, 2))
    Eye_Revolve_Sketch.addConstraint(Sketcher.Constraint('PointOnObject', geo0, 1, -2))
    Eye_Revolve_Sketch.addConstraint(Sketcher.Constraint('Coincident', geo3, 1, geo0, 1))
    Eye_Revolve_Sketch.addConstraint(Sketcher.Constraint('PointOnObject', geo3, 3, -2))
    Eye_Revolve_Sketch.addConstraint(Sketcher.Constraint('Equal', geo3, geo1))
    Eye_Revolve_Sketch.addConstraint(Sketcher.Constraint('Distance', geo3, 1.5))
    Eye_Revolve_Sketch.addConstraint(Sketcher.Constraint('Coincident', geo4, 1, geo3, 2))
    Eye_Revolve_Sketch.addConstraint(Sketcher.Constraint('PointOnObject', geo4, 2, -2))
    Eye_Revolve_Sketch.addConstraint(Sketcher.Constraint('Coincident', geo5, 1, geo4, 2))
    Eye_Revolve_Sketch.addConstraint(Sketcher.Constraint('Coincident', geo5, 2, geo0, 1))
    Eye_Revolve_Sketch.addConstraint(Sketcher.Constraint('Horizontal', geo4))
    Eye_Revolve_Sketch.AttacherEngine = 'Engine Plane'
    Eye_Revolve_Sketch.ExternalGeo = [Part.LineSegment(Vector (0.0, 0.0, 0.0), Vector (1.0, 0.0, 0.0)), Part.LineSegment(Vector (0.0, 0.0, 0.0), Vector (0.0, 1.0, 0.0)), Part.LineSegment(Vector (2.999999999999986, -7.1e-15, 2e-16), Vector (-3.000000000000014, -7.1e-15, -2e-16))]
    Eye_Revolve_Sketch.Placement = Placement(Vector(8.299772852249232, 112.70000445296269, 0.8982695431404932), Rotation (0.8020100669887478, 0.5932624670562144, -0.05425347912061805, -0.04331348097748942))
    Eye_Revolve_Sketch.Visibility = False
    Eye_Revolve_Sketch.ViewObject.Visibility = False
    return Eye_Revolve_Sketch

def make_doc():
    doc = app.newDocument('FishingLure')
    Sketch = createSketch_Sketch(doc)
    doc.recompute()

make_doc()