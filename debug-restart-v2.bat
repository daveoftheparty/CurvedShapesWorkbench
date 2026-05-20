@echo off

taskkill /T /F /IM freecad.exe 2>nul
taskkill /T /F /IM code.exe 2>nul
rmdir /s /q "C:\Users\DSPEER\AppData\Roaming\FreeCAD\v1-1\Mod\CurvedShapes\__pycache__" 2>nul

echo Checking port 5678...
netstat -ano | findstr 5678

echo Launching FreeCAD...
start "" cmd /c "C:\Program Files\FreeCAD 1.1\bin\freecad.exe"

echo Launching VS Code...
start "" cmd /c "C:\Program Files\Microsoft VS Code\Code.exe"

echo Done. Ready for next command.