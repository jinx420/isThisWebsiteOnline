@echo off
title Compiler v0.1.0
echo +++++++++++++++++++
echo + Compiler v0.1.0 +
echo +   By: jinx420   +
echo +  Compiling...   +
echo +++++++++++++++++++
echo.
echo If you encounter any errors, please report them at https://github.com/jinx420/isThisWebsiteOnline/issues 
echo or contact me on Discord: majoad
echo.
TIMEOUT /T 5 /NOBREAK

pyinstaller -F -w --icon=source\favicon.ico -n isThisWebsiteOnline isThisWebsiteOnline.py
python .\\move.py

echo.
echo Compiling finished! Press any key to exit...
pause > nul
