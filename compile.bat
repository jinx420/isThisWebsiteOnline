@echo off
pyinstaller -F -w --icon=iwoSource\favicon.ico -n isThisWebsiteOnline isThisWebsiteOnlineExE.py
python .\\iwoDev\\move.py