# Python Console Captures

- [Python Console Captures](#python-console-captures)
	- [doc purpose](#doc-purpose)
	- [creating sketches in the gui](#creating-sketches-in-the-gui)
		- [YZ sketch](#yz-sketch)
		- [XY sketch](#xy-sketch)
		- [XZ sketch](#xz-sketch)


## doc purpose
for understanding / hacking my way to a new example menu item

## creating sketches in the gui


### YZ sketch

```
 ### Begin command Sketcher_NewSketch
>>> App.activeDocument().addObject('Sketcher::SketchObject', 'Sketch')
>>> App.activeDocument().Sketch.Placement = App.Placement(App.Vector(0.000000, 0.000000, 0.000000), App.Rotation(0.500000, 0.500000, 0.500000, 0.500000))
>>> App.activeDocument().Sketch.MapMode = "Deactivated"
>>> # Gui.activeDocument().setEdit('Sketch')
>>> # import Show
>>> # ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
>>> # tv = Show.TempoVis(App.ActiveDocument, tag= ActiveSketch.ViewObject.TypeId)
>>> # ActiveSketch.ViewObject.TempoVis = tv
>>> # if ActiveSketch.ViewObject.EditingWorkbench:
>>> #   tv.activateWorkbench(ActiveSketch.ViewObject.EditingWorkbench)
>>> # if ActiveSketch.ViewObject.HideDependent:
>>> #   tv.hide(tv.get_all_dependent(App.getDocument('Unnamed').getObject('Sketch'), ''))
>>> # if ActiveSketch.ViewObject.ShowSupport:
>>> #   tv.show([ref[0] for ref in ActiveSketch.AttachmentSupport if not (ref[0].isDerivedFrom("App::Plane") or ref[0].isDerivedFrom("App::LocalCoordinateSystem"))])
>>> # if ActiveSketch.ViewObject.ShowLinks:
>>> #   tv.show([ref[0] for ref in ActiveSketch.ExternalGeometry])
>>> # tv.sketchClipPlane(ActiveSketch, ActiveSketch.ViewObject.SectionView)
>>> # tv.hide(ActiveSketch)
>>> # del(tv)
>>> # del(ActiveSketch)
>>> # 
>>> # ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
>>> # if ActiveSketch.ViewObject.RestoreCamera:
>>> #   ActiveSketch.ViewObject.TempoVis.saveCamera()
>>> #   if ActiveSketch.ViewObject.ForceOrtho:
>>> #     ActiveSketch.ViewObject.Document.ActiveView.setCameraType('Orthographic')
>>> # 
>>> ### End command Sketcher_NewSketch
>>> 
```



### XY sketch


```
>>> ### Begin command Sketcher_NewSketch
>>> App.activeDocument().addObject('Sketcher::SketchObject', 'Sketch001')
>>> App.activeDocument().Sketch001.Placement = App.Placement(App.Vector(0.000000, 0.000000, 0.000000), App.Rotation(0.000000, 0.000000, 0.000000, 1.000000))
>>> App.activeDocument().Sketch001.MapMode = "Deactivated"
>>> # Gui.activeDocument().setEdit('Sketch001')
>>> # ActiveSketch = App.getDocument('Unnamed').getObject('Sketch001')
>>> # tv = Show.TempoVis(App.ActiveDocument, tag= ActiveSketch.ViewObject.TypeId)
>>> # ActiveSketch.ViewObject.TempoVis = tv
>>> # if ActiveSketch.ViewObject.EditingWorkbench:
>>> #   tv.activateWorkbench(ActiveSketch.ViewObject.EditingWorkbench)
>>> # if ActiveSketch.ViewObject.HideDependent:
>>> #   tv.hide(tv.get_all_dependent(App.getDocument('Unnamed').getObject('Sketch001'), ''))
>>> # if ActiveSketch.ViewObject.ShowSupport:
>>> #   tv.show([ref[0] for ref in ActiveSketch.AttachmentSupport if not (ref[0].isDerivedFrom("App::Plane") or ref[0].isDerivedFrom("App::LocalCoordinateSystem"))])
>>> # if ActiveSketch.ViewObject.ShowLinks:
>>> #   tv.show([ref[0] for ref in ActiveSketch.ExternalGeometry])
>>> # tv.sketchClipPlane(ActiveSketch, ActiveSketch.ViewObject.SectionView)
>>> # tv.hide(ActiveSketch)
>>> # del(tv)
>>> # del(ActiveSketch)
>>> # 
>>> # ActiveSketch = App.getDocument('Unnamed').getObject('Sketch001')
>>> # if ActiveSketch.ViewObject.RestoreCamera:
>>> #   ActiveSketch.ViewObject.TempoVis.saveCamera()
>>> #   if ActiveSketch.ViewObject.ForceOrtho:
>>> #     ActiveSketch.ViewObject.Document.ActiveView.setCameraType('Orthographic')
>>> # 
>>> ### End command Sketcher_NewSketch
>>> 
```



### XZ sketch


```
Python 3.11.14 | packaged by conda-forge | (main, Oct 13 2025, 14:00:26) [MSC v.1944 64 bit (AMD64)] on win32
Type 'help', 'copyright', 'credits' or 'license' for more information.
>>> ### Begin command Sketcher_NewSketch
>>> App.activeDocument().addObject('Sketcher::SketchObject', 'Sketch002')
>>> App.activeDocument().Sketch002.Placement = App.Placement(App.Vector(0.000000, 0.000000, 0.000000), App.Rotation(0.707107, 0.000000, 0.000000, 0.707107))
>>> App.activeDocument().Sketch002.MapMode = "Deactivated"
>>> # Gui.activeDocument().setEdit('Sketch002')
>>> # ActiveSketch = App.getDocument('Unnamed').getObject('Sketch002')
>>> # tv = Show.TempoVis(App.ActiveDocument, tag= ActiveSketch.ViewObject.TypeId)
>>> # ActiveSketch.ViewObject.TempoVis = tv
>>> # if ActiveSketch.ViewObject.EditingWorkbench:
>>> #   tv.activateWorkbench(ActiveSketch.ViewObject.EditingWorkbench)
>>> # if ActiveSketch.ViewObject.HideDependent:
>>> #   tv.hide(tv.get_all_dependent(App.getDocument('Unnamed').getObject('Sketch002'), ''))
>>> # if ActiveSketch.ViewObject.ShowSupport:
>>> #   tv.show([ref[0] for ref in ActiveSketch.AttachmentSupport if not (ref[0].isDerivedFrom("App::Plane") or ref[0].isDerivedFrom("App::LocalCoordinateSystem"))])
>>> # if ActiveSketch.ViewObject.ShowLinks:
>>> #   tv.show([ref[0] for ref in ActiveSketch.ExternalGeometry])
>>> # tv.sketchClipPlane(ActiveSketch, ActiveSketch.ViewObject.SectionView)
>>> # tv.hide(ActiveSketch)
>>> # del(tv)
>>> # del(ActiveSketch)
>>> # 
>>> # ActiveSketch = App.getDocument('Unnamed').getObject('Sketch002')
>>> # if ActiveSketch.ViewObject.RestoreCamera:
>>> #   ActiveSketch.ViewObject.TempoVis.saveCamera()
>>> #   if ActiveSketch.ViewObject.ForceOrtho:
>>> #     ActiveSketch.ViewObject.Document.ActiveView.setCameraType('Orthographic')
>>> # 
>>> ### End command Sketcher_NewSketch
>>> 
```