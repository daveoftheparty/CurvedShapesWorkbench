import FreeCAD as app
import Sketcher, Part

def createSketch_Walk_the_Dog_Sketch(doc):
    Walk_the_Dog_Sketch = doc.addObject('Sketcher::SketchObject', 'Walk_the_Dog_Sketch')
    geo0 = Walk_the_Dog_Sketch.addGeometry(Part.LineSegment(Vector (0.0, -8.0, 0.0), Vector (65.0, -8.0, 0.0)))
    Walk_the_Dog_Sketch.toggleConstruction(geo0)
    geo1 = Walk_the_Dog_Sketch.addGeometry(Part.ArcOfCircle(Part.Circle(Vector(23.76380626473026, 145.9709209274943, 0.0), Vector (0.0, 0.0, 1.0), 153.9709209274943), 4.59835586832567, 4.96793137941701))
    geo2 = Walk_the_Dog_Sketch.addGeometry(Part.ArcOfCircle(Part.Circle(Vector(23.763806264730338, -145.9709209274943, 0.0), Vector (0.0, 0.0, 1.0), 153.9709209274943), 1.3152539277625774, 1.6848294388539173))
    geo3 = Walk_the_Dog_Sketch.addGeometry(Part.ArcOfCircle(Part.Circle(Vector(7.045760331163319, 0.0, 0.0), Vector (0.0, 0.0, 1.0), 7.045760331163319), 1.6848294388539173, 4.59835586832567))
    geo4 = Walk_the_Dog_Sketch.addGeometry(Part.ArcOfCircle(Part.Circle(Vector(61.89930920808833, 0.0, 0.0), Vector (0.0, 0.0, 1.0), 3.100690791911669), 4.96793137941701, 7.5984392349421634))
    geo5 = Walk_the_Dog_Sketch.addGeometry(Part.LineSegment(Vector (65.0, -8.0, 0.0), Vector (65.0, 0.0, 0.0)))
    Walk_the_Dog_Sketch.toggleConstruction(geo5)
    Walk_the_Dog_Sketch.addConstraint(Sketcher.Constraint('Distance', geo0, 65.0))
    Walk_the_Dog_Sketch.addConstraint(Sketcher.Constraint('Horizontal', geo0))
    Walk_the_Dog_Sketch.addConstraint(Sketcher.Constraint('PointOnObject', geo0, 1, -2))
    Walk_the_Dog_Sketch.addConstraint(Sketcher.Constraint('DistanceY', geo0, 1, 8.0))
    Walk_the_Dog_Sketch.addConstraint(Sketcher.Constraint('Tangent', geo1, 0, geo0))
    Walk_the_Dog_Sketch.addConstraint(Sketcher.Constraint('Equal', geo2, geo1))
    Walk_the_Dog_Sketch.addConstraint(Sketcher.Constraint('Tangent', geo1, 1, geo3, 2))
    Walk_the_Dog_Sketch.addConstraint(Sketcher.Constraint('Tangent', geo2, 2, geo3, 1))
    Walk_the_Dog_Sketch.addConstraint(Sketcher.Constraint('Tangent', geo3, 0))
    Walk_the_Dog_Sketch.addConstraint(Sketcher.Constraint('Tangent', geo1, 2, geo4, 1))
    Walk_the_Dog_Sketch.addConstraint(Sketcher.Constraint('Tangent', geo2, 1, geo4, 2))
    Walk_the_Dog_Sketch.addConstraint(Sketcher.Constraint('Coincident', geo5, 1, geo0, 2))
    Walk_the_Dog_Sketch.addConstraint(Sketcher.Constraint('PointOnObject', geo5, 2, -1))
    Walk_the_Dog_Sketch.addConstraint(Sketcher.Constraint('Vertical', geo5))
    Walk_the_Dog_Sketch.addConstraint(Sketcher.Constraint('Tangent', geo4, 0, geo5))
    Walk_the_Dog_Sketch.addConstraint(Sketcher.Constraint('PointOnObject', geo3, 3, -1))
    Walk_the_Dog_Sketch.addConstraint(Sketcher.Constraint('PointOnObject', geo4, 3, -1))
    Walk_the_Dog_Sketch.addConstraint(Sketcher.Constraint('Distance', geo1, 1, geo0, 1.0))
    Walk_the_Dog_Sketch.addConstraint(Sketcher.Constraint('Distance', geo1, 2, geo0, 5.0))
    Walk_the_Dog_Sketch.AttacherEngine = 'Engine Plane'
    Walk_the_Dog_Sketch.Placement = Placement(Vector(0.0, 0.0, 0.0), Rotation (0.5, 0.5, 0.5, 0.4999999999999999))
    Walk_the_Dog_Sketch.Visibility = False
    Walk_the_Dog_Sketch.ViewObject.Visibility = False
    return Walk_the_Dog_Sketch

def make_doc():
    doc = app.newDocument('bait_to_copy')
    Walk_the_Dog_Sketch = createSketch_Walk_the_Dog_Sketch(doc)
    doc.recompute()

make_doc()