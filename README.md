# This is a simple python project to check if a website is online or not
# Features:
1. CLI and Gui
2. Open in Browser
3. Save and Load history
4. Multithreading
5. Multiple Languages
6. Automatic Updates

# Planned features:
1. Graph showing the online offline ratio

## How to compile it yourself (with the batch file)
* Note: you need to have the Folder iwoSource and the .ico, .png file from it otherwise it wont work (you could choose a different icon for compiling but the program needs the .ico and .png for displaying the icon and the picture in the main window)
1. download the files (compile.bat, convertme.py, move.py and requirements.txt) and install python if you havent done that
2. open terminal / cmd 
3. pip install -r requirements.txt
4. .\compile.bat
5. then you are done

# How to compile it yourself (without the batch file)
* Note: you need to have the Folder iwoSource and the .ico, .png file from it otherwise it wont work (you could choose a different icon for compiling but the program needs the .ico and .png for displaying the icon and the picture in the main window)
1. download the files (convertme.py and requirements.txt) and install python if you havent done that
2. open terminal / cmd
3. pip install -r requirements.txt
4. pyinstaller -F -w --icon=iwoSource\favicon.ico -n isThisWebsiteOnline convertme.py