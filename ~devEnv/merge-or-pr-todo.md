# Branch cleanup todo for fork pr

some things had to be done inline with code, etc. here is a list of things to clean up that may not be part of targeted feat: commits


## cleanup todos

- [ ] remove line `import debugpy; debugpy.trace_this_thread(True)` from CurvedArray:execute() method
- [ ] search for other debug code
- [ ] remove .editorconfig at root of repo
- [ ] remove folder devenv

## feature todos

- [ ] update readme with note about KeepAspectRatio 
- [ ] if appropriate, create new screenshots, examples, reasoning behind new parameter
- [ ] challenge the average note from PreserveAspectRatio-feature.md : `_applyAspectRatio` uses the **average** scale factor if somehow multiple constrained axes are present (shouldn't happen with a single hull curve, but defensive).

