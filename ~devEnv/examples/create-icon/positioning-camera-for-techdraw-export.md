## getting camera state (freecad python console)

>>> print(FreeCADGui.ActiveDocument.ActiveView.getCamera())
#Inventor V2.1 ascii


OrthographicCamera {
  viewportMapping ADJUST_CAMERA
  position 247.20026 45.088905 131.76414
  orientation 0.59058809 0.52961832 0.60885984  1.4547983
  nearDistance 220.35733
  farDistance 339.08652
  aspectRatio 1
  focalDistance 250
  height 73.784966
}


## restoring camera state (freecad python console)

LURE_ICON_CAMERA = """#Inventor V2.1 ascii

OrthographicCamera {
	viewportMapping ADJUST_CAMERA
	position 247.20026 45.088905 131.76414
	orientation 0.59058809 0.52961832 0.60885984  1.4547983
	nearDistance 220.35733
	farDistance 339.08652
	aspectRatio 1
	focalDistance 250
	height 73.784966
}
"""

FreeCADGui.ActiveDocument.ActiveView.setCamera(LURE_ICON_CAMERA)

## versions I've tried to export so far

camera angle below used for `FishingLure_Page__v1.svg`

```
OrthographicCamera {
  viewportMapping ADJUST_CAMERA
  position 247.20026 45.088905 131.76414
  orientation 0.59058809 0.52961832 0.60885984  1.4547983
  nearDistance 220.35733
  farDistance 339.08652
  aspectRatio 1
  focalDistance 250
  height 73.784966
}
```
