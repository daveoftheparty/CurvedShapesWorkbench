# Branch cleanup todo for fork pr

some things had to be done inline with code, etc. here is a list of things to clean up that may not be part of targeted feat: commits


## cleanup todos

- [ ] remove line `import debugpy; debugpy.trace_this_thread(True)` from CurvedArray:execute() method
- [ ] search for other debug code
- [ ] remove .editorconfig at root of repo
- [ ] remove folder devenv
- [ ] double check icon in FishingLure.py! for naming, etc. because i'm still playing with the svg
- [ ] check that the original examples either render correctly in fc 1.1, or they are broken and it's not my fault
- [ ] run my fishing lure py example in freecad when i fell 100% done and save that .fcstd file to this dev branch
- [ ] investigate any .fcstd files in this branch, decide if i need to keep, delete, rename, write a readme, etc. do this AFTER saving an fcstd of fishing lure example menu, because future me will want to know where it is, what it is, how to find it
- [ ] cleanup every file/folder in ~devEnv, create a future me development readme, archive files in archive folders if necessary, delete or rename if better. make a nice clean branch that has everything future me needs if/when i need to revisit either this PreserveAspectRatio feature, this workbench, or want to refer to notes for working on future workbenches or programmatic FreeCad stuff.

## feature todos

- [ ] update readme with note about KeepAspectRatio 
- [ ] if appropriate, create new screenshots, examples, reasoning behind new parameter
- [ ] create an SVG icon for the FishingLure example
- [x] challenge the average note from PreserveAspectRatio-feature.md : `_applyAspectRatio` uses the **average** scale factor if somehow multiple constrained axes are present (shouldn't happen with a single hull curve, but defensive).


