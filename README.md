# Website Status Checker

![Website Status Checker](https://github.com/jinx420/isThisWebsiteOnline/blob/master/iwoSource/favicon.png?raw=true)

This is a simple Python project designed to check the availability of websites. It provides both a command-line interface (CLI) and a graphical user interface (GUI), making it easy to use for different preferences. The project offers the following features:

## Features

1. CLI and GUI: Choose between the command-line interface or the graphical user interface to check the status of a website.
2. Open in Browser: Quickly open the website in your default web browser directly from the program.
3. Save and Load History: Keep a record of website status checks by saving and loading the history.
4. Multithreading: Utilize multithreading to improve performance and check multiple websites simultaneously.
5. Multiple Languages: Enjoy the flexibility of multiple language support to cater to a global user base.
6. Automatic Updates: Stay up to date with the latest version of the program through automatic updates.
7. Automatic Dependency Install: Simplify the installation process by automatically installing necessary dependencies.
8. Online-Offline Ratio Graph: Visualize the online and offline ratio of websites with a graphical representation.

## Planned Features

1. Option to Disable Automatic Dependency Installation: In an upcoming update, an option to disable automatic dependency installation will be added to allow advanced users more control over the installation process.

## How to Compile It Yourself

### With the Batch File

*Note: Make sure you have the `iwoSource` folder along with the required `.ico` and `.png` files in the same directory. These files are necessary for displaying the program's icon and main window image.*

1. Download the following files: `compile.bat`, `convertme.py`, `move.py`, and `requirements.txt`. If you haven't already, install Python.
2. Open the terminal or command prompt.
3. Install the required dependencies by running the command: `pip3 install -r requirements.txt`.
4. Execute the batch file by entering the command: `.\compile.bat`.
5. The compilation process will be completed, and you're ready to use the program.

### Without the Batch File

*Note: Make sure you have the `iwoSource` folder along with the required `.ico` and `.png` files in the same directory. These files are necessary for displaying the program's icon and main window image.*

1. Download the following files: `convertme.py` and `requirements.txt`. If you haven't already, install Python.
2. Open the terminal or command prompt.
3. Install the required dependencies by running the command: `pip3 install -r requirements.txt`.
4. Compile the program by entering the following command: `pyinstaller -F -w --icon=iwoSource\favicon.ico -n isThisWebsiteOnline convertme.py`.

## Known Issues

1. **Language-dependent Message Box Buttons:** When opening the about window, the "Yes/No" buttons may appear in the language set by the operating system. This issue is inherent to how message boxes are handled by the OS and cannot be fixed without compromising the functionality of the message box.

2. **False Positive Antivirus Detection:** Some antivirus software may flag the `.exe` file generated by the program as malicious. This is a known issue with PyInstaller due to its potential for compiling Python malware. However, this issue should be resolved for most antivirus products since a custom PyInstaller bootloader was compiled. You can verify the file's safety by uploading it to VirusTotal. Windows Defender should no longer flag the file, but if it does, ensure you are using an up-to-date version. The fixed `.exe` file will be available in version v0.2.6 or newer.

3. **Failed to Execute Script: Unhandled Exception - Bitmap Not Defined:** If you encounter an error stating "Failed to execute script 'convertme' due to an unhandled exception: bitmap ".\iwoSource\favicon.ico" not defined" or "bitmap ".\iwoSource\favicon.png" not defined," it means the `iwoSource` folder and its contents are missing. Please download the `iwoSource` folder and ensure it is present in the correct location.

4. **Empty History After Updating to v0.2.8 or Newer:** After updating to version v0.2.8 or newer, the history may appear empty. This is because the program now saves the full history in the `options.json` file instead of the previous `fullHistory.json` file. You can safely delete the old `fullHistory.json` file as it is no longer used.

5. **Unable to Open Options Menu:** If you are unable to open the options menu, it is likely due to having an outdated `options.json` file. The program checks for enabled options when opening the menu, and if a new option does not exist in the old `options.json`, the program cannot proceed. Deleting the old `options.json` file is the easiest fix for this issue, but please note that it will reset all your options. Currently, there are only three options, so this is not a significant concern.

6. **Settings Not Saved in v0.2.9:** In version v0.2.9 (and possibly older versions), a bug prevented settings from being saved due to an update in the status text. This issue has been resolved in version v0.3.0 or newer.

## Notice for Developers

⚠️ **Important Notice:** Starting from version v0.3.2, the branch `develop` has been renamed to `old-develop` and is no longer actively maintained. To streamline our development process and focus efforts on the `master` branch, which contains the latest stable version, we have made this change.

If you have been actively working on the `develop` branch, we recommend switching to the `master` branch and creating a new branch based on it for your ongoing development work. Please ensure that any bug fixes or new features are implemented on the `master` branch going forward.

We appreciate your understanding and cooperation in this transition. If you have any questions or need further assistance, please don't hesitate to reach out to our team. Thank you for your continued support and dedication to this project!
