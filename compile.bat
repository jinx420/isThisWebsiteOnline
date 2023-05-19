@echo off
pyinstaller -F -w --icon=iwoSource\favicon.ico -n isThisWebsiteOnline isThisWebsiteOnline.py
python .\\move.py
