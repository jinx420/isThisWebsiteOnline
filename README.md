# Website Status Checker

![Interface](https://raw.githubusercontent.com/jinx420/isThisWebsiteOnline/master/misc/v0.3.6.png)

*Note: The picture above will be updated every major version or every major UI overhaul.*

- [Features](#features)
  - [Planned Features and Enhancements](#planned-features)
  - [Unsure Features](#unsure-features)
  - [Scrapped Features](#scrapped-features)
- [How to Compile It Yourself](#how-to-compile-it-yourself)
  - [With the Batch File](#with-the-batch-file)
  - [Without the Batch File](#without-the-batch-file)
- [Known Issues](#known-issues)
- [Notice for Developers](#notice-for-developers)

This is a simple Python project designed to check the availability of websites. It provides both a command-line interface (CLI) and a graphical user interface (GUI), making it easy to use for different preferences. This project is currently a work in progress (WIP), and there is no estimated completion date at the moment. The project offers the following features:

## Features

- [x] CLI and GUI: Choose between the command-line interface or the graphical user interface to check the status of a website. 

    *Note: The CLI is available at `isThisWebsiteOnlineCLI.py` and `isThisWebsiteOnlineCLI.exe`.*

- [x] Open in Browser: Quickly open the website in your default web browser directly from the program.
- [x] Save and Load History: Keep a record of website status checks by saving and loading the history.
- [x] Multithreading: Utilize multithreading to improve performance.
- [x] Automatic Updates: Stay up to date with the latest version of the program through automatic updates.
- [x] Online-Offline Ratio Graph: Visualize the online and offline ratio of websites with a graphical representation.
- [x] Easily import and export your options to use them on another system or after a version upgrade.
- [x] Support for the GNU/Linux Operating System.

### Planned Features and Enhancements

*Note: The order of contents does not represent the order in which they will be implemented. Active development on a feature is marked by (**WIP**).*

- [ ] More Options
- [ ] Major UI overhaul
- [ ] Favorites
- [ ] Minor UI change (**WIP** *Note: This is about 50% done.*)

### Unsure Features

*Note: The order represents the likelihood of them being implemented.*

- [ ] Batch checking
- [ ] Extensions
- [ ] HTTP Request sender (Don't know the use for this yet, but it seems cool)
- [ ] Dark Mode (Kind of a pain to do)
- [ ] Documentation

### Scrapped Features

*Note: Features listed here are gone for good, some will also have an explanation why I decided to remove them (see `Explanation:`). There is a very slim chance they will get implemented again after some time. Farewell, my friends.* 😢

- Multiple Languages (*Explanation: This is a pain in the ass to maintain/verify translation, it also adds like **300** lines, many of which repeat themselves due to how this code is structured and due to limitations of the way I chose to implement it. The multiple languages were kinda alright at the beginning, but as soon as the code kept getting bigger, so did the translations. For every line of code, I had to add like 3 lines for translation. This made the code very bloated, inefficient, and it also introduced lots of bugs.*)

## How to Compile It Yourself

### With the Batch File

*Note: Make sure you have the `iwoSource` folder along with the required `.ico` and `.png` files in the same directory. These files are necessary for displaying the program's icon and main window image.*

1. Download the following files: `compile.bat`, `isThisWebsiteOnline.py`, `move.py`, and `requirements.txt`. If you haven't already, install Python.
2. Open the terminal or command prompt.
3. Install the required dependencies by running the command: `pip3 install -r requirements.txt`.
4. Execute the batch file by entering the command: `.\compile.bat`.
5. The compilation process will be completed, and you're ready to use the program.

### Without the Batch File

*Note: Make sure you have the `iwoSource` folder along with the required `.ico` and `.png` files in the same directory. These files are necessary for displaying the program's icon and main window image.*

1. Download the following files: `isThisWebsiteOnline.py` and `requirements.txt`. If you haven't already, install Python.
2. Open the terminal or command prompt.
3. Install the required dependencies by running the command: `pip3 install -r requirements.txt`.
4. Compile the program by entering the following command: `pyinstaller -F -w --icon=iwoSource\favicon.ico -n isThisWebsiteOnline isThisWebsiteOnline.py`.

## Known Issues

1. **Language-dependent Message Box Buttons:** When opening the about window, the "Yes/No" buttons may appear in the language set by the operating system. This issue is inherent to how message boxes are handled by the OS and cannot be fixed without compromising the functionality of the message box.

2. **False Positive Antivirus Detection:** Some antivirus software may flag the `.exe` file generated by the program as malicious. This is a known issue with PyInstaller due to its potential for compiling Python malware. However, this issue should be resolved for most antivirus products since a custom PyInstaller bootloader was compiled. You can verify the file's safety by uploading it to VirusTotal. Windows Defender should no longer flag the file, but if it does, ensure you are using an up-to-date version. The fixed `.exe` file will be available in version v0.2.6 or newer.

3. **Failed to Execute Script: Unhandled Exception - Bitmap Not Defined:** If you encounter an error stating "Failed to execute script 'convertme' due to an unhandled exception: bitmap ".\iwoSource\favicon.ico" not defined" or "bitmap ".\iwoSource\favicon.png" not defined," it means the `iwoSource` folder and its contents are missing. Please download the `iwoSource` folder and ensure it is present in the correct location. (***This is no longer an issue.***)

4. **Empty History After Updating to v0.2.8 or Newer:** After updating to version v0.2.8 or newer, the history may appear empty. This is because the program now saves the full history in the `options.json` file instead of the previous `fullHistory.json` file. You can safely delete the old `fullHistory.json` file as it is no longer used.

5. **Unable to Open Options Menu:** If you are unable to open the options menu, it is likely due to having an outdated `options.json` file. The program checks for enabled options when opening the menu, and if a new option does not exist in the old `options.json`, the program cannot proceed. Deleting the old `options.json` file fixes the issue, but the easiest way to fix this is to use the new button to regenerate your `options.json`. Please note that it will reset all your options. Currently, there is only a small number of options, so this is not a significant concern.

6. **Settings Not Saved in v0.2.9:** In version v0.2.9 (and possibly older versions), a bug prevented settings from being saved due to an update in the status text. This issue has been resolved in version v0.3.0 or newer.

7. **My Settings wont get carried over to never Versions:** Every time you upgrade to a newer version of this program, you can either export your settings and put them in the `iwoSource` folder, or you just use the newer `.exe` or `.py` and copy that to the old directory where you had it installed.

## Notice for Developers

⚠️ **Important Notice:** Starting from version v0.3.2, the branch `develop` has been renamed to `old-develop` and is no longer actively maintained. To streamline our development process and focus efforts on the `master` branch, which contains the latest stable version, we have made this change.

If you have been actively working on the `develop` branch, I recommend switching to the `master` branch and creating a new branch based on it for your ongoing development work. Please ensure that any bug fixes or new features are implemented on the `master` branch going forward.

I appreciate your understanding and cooperation in this transition. If you have any questions or need further assistance, please don't hesitate to reach out to me. Thank you for your continued support and dedication to this project!

---

- Older commits and or tags might be tagged as unverified. This is due to a switch of GPG keys.

- Starting from v0.3.5, the `convertme.py` file has been removed, and the CLI has been moved to `isThisWebsiteOnlineCLI.py` and `isThisWebsiteOnlineCLI.exe`.
