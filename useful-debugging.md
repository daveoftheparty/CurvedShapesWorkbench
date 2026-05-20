## general process
open freecad and open vs code to this folder
if you don't know that this is the right folder, run (fill me in)
now, in FC:
-  open your file you're testing with
-  go to Macros->Macros on the menu and choose your macro and say edit
-  click run to run the macro
-  

switch to vs code
click run-start debugging

fc should print in the report view that the debugger is running

now you can debug



## commands run to help between debug runs (these are also in debug-restart.bat, though i couldn't get it to successfully reopen freecad and vs code)

rmdir /s /q "C:\Users\DSPEER\AppData\Roaming\FreeCAD\v1-1\Mod\CurvedShapes\__pycache__"

taskkill /T /F /IM freecad.exe
taskkill /T /F /IM code.exe

netstat -ano | findstr 5678
