# Icon steps, notes, helping hints

- [Icon steps, notes, helping hints](#icon-steps-notes-helping-hints)
	- [file history in this folder](#file-history-in-this-folder)
	- [getting an svg export of your 3d object](#getting-an-svg-export-of-your-3d-object)


## file history in this folder

| File | Notes |
| --- | --- |
| FishingLure_Page__.svg | inital working through how to do it, and colors (blue back/green belly)|
| FishingLure_Page__v1.svg | i chose a different camera angle other than straight ortho, this is the angle documented in [positioning-camera readme](./positioning-camera-for-techdraw-export.md) the rest of the files below are also based on this angle, unless otherwise noted |
| FishingLure_Page__v1-v1.svg | manual coloring and figuring out workflow of how to use shapebuilder to make a nice looking icon. this one is blue back, bass green flank, bone belly. not an icon candidate yet |
| FishingLure_Page__v1-v2.svg | here is where i really start to get a workflow going for the final icon. |
| FishingLure_Page__v1-v3.svg | in this file, i add a copy of the techdraw lines to help give the lure some visual shape. file size is big though, it has two copies of techdraw export. it also doesn't render nice outside of inkscape due to line sizes-- in inkscape when i switch stroke style from pixels to hairline, it doesn't actually update stroke size, so lines are massive. that and the two copies of techdraw makes the file too big. Also in this file, I get black pupil reflection shading nailed. |
| FishingLure_Page__v1-v4.svg | I start to reduce file size by getting rid of duplicate techdraw groups, and flattening the nested subgroups (using Claude) for easier editing. still has the stroke width problem on techdraw paths. |
| FishingLure_Page__v1-v5.svg | with help of Claude, further reduce file size by taking all the redundant path attributes and moving them to parent group |
| ***FishingLure_Page__v1-v6.svg*** | further reduce file size with Claude, getting rid of some inkscape metadata, including xml describing recently used gradients. this is the first icon i actually attach to the Examples menu in the workbench in FreeCAD and have a good visual look at in the GUI. it's kind of a baby bass color scheme with a brownish back, greenish flank, bone belly-- lots of gradients |
| ***FishingLure_Page__v1-v7.svg*** | working on coloring only. got a firetiger-style gradient, this time a three stop gradient between blue, yellow, orange. I forgot the top of firetiger should be green :D |



## getting an svg export of your 3d object

- Position the camera how you want. See [positioning-camera readme](./positioning-camera-for-techdraw-export.md)


- in the model view, select object[s] you want an svg of. you may have to fuse them together

- open techdraw workbench, choose menu TechDraw->Page->New Page

- choose menu TechDraw->TechDraw Views->New View

- a Task dialog appears with a 9 box with arrows, and a placement at the center. in the lower right (position 9) choose the camera icon, that will match your current Model/GUI 3D view

- menu TechDraw->Page->Export Page as SVG

- now, open the SVG. Size the techdraw export how you want it. For creating the icon on this workbench, I realized I wanted a 1px black outline around the shape, and a 1px white line around the black outline in order to have it stand off from either a light or dark theme. With a 64px target square and knowing the outlines would add 4 total pixes, I sized the main object to 58 pixels. That way, when done, the icon would be at 62 pixels wide max ***DO THIS BEFORE DOING ANY COSMETIC THINGS***

- in inkscape, use the shape builder to create things like a whole copy of your object, copies of subshapes, etc. important that the object is already sized correctly as noted above