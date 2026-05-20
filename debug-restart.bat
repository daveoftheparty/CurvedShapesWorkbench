

taskkill /T /F /IM freecad.exe
taskkill /T /F /IM code.exe
rmdir /s /q "C:\Users\DSPEER\AppData\Roaming\FreeCAD\v1-1\Mod\CurvedShapes\__pycache__"

netstat -ano | findstr 5678

REM start "" "C:/Program Files/FreeCAD 1.1/bin/freecad.exe"
REM start "" "C:\Program Files\Microsoft VS Code\Code.exe"

