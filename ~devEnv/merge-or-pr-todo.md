# Branch cleanup todo for fork pr

some things had to be done inline with code, etc. here is a list of things to clean up that may not be part of targeted feat: commits


## cleanup todos

- [ ] remove line `import debugpy; debugpy.trace_this_thread(True)` from CurvedArray:execute() method
- [ ] search for other debug code
- [ ] remove .editorconfig at root of repo
- [ ] remove folder devenv
- [ ] double check icon in FishingLure.py! for naming, etc. because i'm still playing with the svg
- [ ] check that the original examples either render correctly in fc 1.1, or they are broken and it's not my fault

## feature todos

- [ ] update readme with note about KeepAspectRatio 
- [ ] if appropriate, create new screenshots, examples, reasoning behind new parameter
- [ ] create an SVG icon for the FishingLure example
- [x] challenge the average note from PreserveAspectRatio-feature.md : `_applyAspectRatio` uses the **average** scale factor if somehow multiple constrained axes are present (shouldn't happen with a single hull curve, but defensive).


