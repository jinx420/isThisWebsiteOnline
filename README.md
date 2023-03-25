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
- UPDATE: This should be fixed for most AV products since i compiled my own pyinstaller bootloader, if you want to see which AV products will flag this file feel free to upload it to virustotal, windows defender should no longer flag this file if it does maybe you are using an older version, the new .exe will be available for the version v.0.2.6 or newer.
- OLD: This is an issue with pyinstaller since it can be used to compile python malware and obfuscate it so that AVs cant detect it, and because the pyinstaller bootloader is the only shared part it gets flagged as malicious, i would have to encrypt or encode the code and currently there is no plan to do so.

The program wont run it gives me an error showing Failed to execute script 'convertme' due to unhandled exception: bitmap ".\iwoSource\favicon.ico" not defined
- Currently I havent found a fix for that yet :(, the only fix would be to download the iwoSource folder and its contents or use the old iwoSource folder from your previous install.

The program wont run it gives me an error showing Failed to execute script 'convertme' due to unhandled exception: bitmap ".\iwoSource\favicon.png" not defined
- As described above currently there is no fix for it, the only fix would be to download the iwoSource folder and its contents or the old iwoSource folder from your previous install.

My history is empty after updating from v0.2.7 to v0.2.8 or newer
- This is because in v0.2.8 I changed the way how the full history is saved, now the full history will be saved in the options.json file. (You can delete the old fullHistory.json file since it isnt used anymore and is jsut wasted space)

The program wont open the options menu
- This is most likely caused by having an old options.json file, because when opening the options it checks which options are enabled or not and if the new option doesnt exist in the old options.json then the program doesnt know what to do. I might work on a fix for this but right now the easiest fix is to just delete the old options.json (This will reset all you options, which isnt a big deal currently since there are only 3 options).