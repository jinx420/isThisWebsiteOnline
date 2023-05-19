@echo off
pyinstaller -F -w --icon=iwoSource\favicon.ico -n isThisWebsiteOnline convertme.py
python .\\move.py
