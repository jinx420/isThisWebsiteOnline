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

# Known issues:
When you open the about window it shows the yes / no button in the os language
- This is an issue with how message boxes are handled by the os (i cant fix this if i want to keep the message box)

My AV is flagging the .exe as malicous
- This is an issue with pyinstaller since it can be used to compile python malware and obfuscate it so that AVs cant detect it, and because the pyinstaller bootloader is the only shared part it gets flagged as malicious, i would have to encrypt or encode the code and currently there is no plan to do so