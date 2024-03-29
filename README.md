# Website Status Checker

![Interface](https://raw.githubusercontent.com/jinx420/isThisWebsiteOnline/master/misc/v0.3.6.png)

*Note: The picture above will be updated every major / minor UI overhaul, depends on the change.*

- [Website Status Checker](#website-status-checker)
  - [Features](#features)
    - [Planned Features and Enhancements](#planned-features-and-enhancements)
    - [Unsure Features](#unsure-features)
    - [Scrapped Features](#scrapped-features)
  - [How to Compile It Yourself](#how-to-compile-it-yourself)
    - [With the Batch File](#with-the-batch-file)
    - [Without the Batch File](#without-the-batch-file)
  - [Known Issues](#known-issues)
  - [Notice for Developers](#notice-for-developers)
    - [General Notices](#general-notices)

This is a simple Python project designed to check the availability of websites. It provides both a command-line interface (CLI) and a graphical user interface (GUI), making it easy to use for different preferences. This project is currently a work in progress (WIP) but I don't have that much time to work on it, and there is no estimated completion date at the moment.

## Features

- [x] CLI and GUI: Choose between the command-line interface or the graphical user interface to check the status of a website. 

    *Note: The CLI is available at `isThisWebsiteOnlineCLI.py` and `isThisWebsiteOnlineCLI.exe`.*

- [x] Open in Browser: Quickly open the website in your default web browser directly from the program.
- [x] Save and Load History: Keep a record of website status checks by saving and loading the history.
- [x] Multi threading: Utilize multi threading to improve performance.
- [x] Automatic Updates: Stay up to date with the latest version of the program through automatic updates.
- [x] Online-Offline Ratio Graph: Visualize the online and offline ratio of websites with a graphical representation.
- [x] Easily import and export your options to use them on another system or after a version upgrade.
- [x] Support for the GNU/Linux Operating System.
- [x] Dark and Light Mode

### Planned Features and Enhancements

*Note: The sequence of contents listed does not reflect their implementation order. Features currently under active development are indicated with (**In Progress**). Major features and enhancements are highlighted in bold.*

- [x] ⚠️ Fix the issue of having an outdated `options.json`
- [ ] More Options (Things like: Save location etc.)
- [ ] **UI overhaul (Things like: Status overhaul and more.)**
- [x] Fix the issue of deleting existing `./source` folder in current working directory
- [x] Minor UI change
- [x] Remove need for `.png` and or `.ico` file.
- [x] Predictions
- [x] Add statusLabel update when hitting check button

### Unsure Features

*Note: The order represents the likelihood of them being implemented.*

- [ ] Favorites
- [ ] Batch checking
- [ ] Extensions
- [ ] Request sender (Don't know the use for this yet, but it seems cool. Basically just like this project 😅)
- [ ] Documentation

### Scrapped Features

*Note: Many features listed here are gone for good, but some might only be here temporarily (will be marked if that's the case). Some will also have an explanation why I decided to remove them (see `Explanation:`).*

- Multiple Languages (*`Explanation:` This is a pain in the ass to maintain/verify translation, it also adds like **300** lines of code, many of which repeat themselves due to how this code is structured and due to limitations of the way I chose to implement it. The multiple languages were kind of alright at the beginning, but as soon as the code kept getting bigger, so did the translations. For every line of code, I had to add like 3 lines for translation. This made the code very bloated, inefficient, and it also introduced lots of bugs. I might try to implement this in a different way some time in the future, but currently there are no plans for this.*)

## How to Compile It Yourself

### With the Batch File

*Note: Make sure you have the `source` folder along with the required `.ico` file in the same directory. This file is necessary for displaying the program's icon.*

1. Download the following files: `compile.bat`, `isThisWebsiteOnline.py`, `move.py`, and `requirements.txt`. If you haven't already, install Python.
2. Open the terminal or command prompt.
3. Install the required dependencies by running the command: `pip3 install -r requirements.txt`.
4. Execute the batch file by entering the command: `.\compile.bat`.
5. The compilation process will be completed, and you're ready to use the program.

### Without the Batch File

*Note: Make sure you have the `source` folder along with the required `.ico` file in the same directory. This file is necessary for displaying the program's icon.*

1. Download the following files: `isThisWebsiteOnline.py` and `requirements.txt`. If you haven't already, install Python.
2. Open the terminal or command prompt.
3. Install the required dependencies by running the command: `pip3 install -r requirements.txt`.
4. Compile the program by entering the following command: `pyinstaller -F -w --icon=source\favicon.ico -n isThisWebsiteOnline isThisWebsiteOnline.py`.

## Known Issues

*Note: Since `v0.3.6`, the `iwoSource` folder is now known as `source`.*

1. **Language-dependent Message Box Buttons:** When opening the about window, the "Yes/No" buttons may appear in the language set by the operating system. This issue is inherent to how message boxes are handled by the OS and cannot be fixed without compromising the functionality of the message box.

2. **False Positive Antivirus Detection:** Some antivirus software may flag the `.exe` file generated by the program as malicious. This is a known issue with PyInstaller due to its potential for compiling Python malware. However, this issue should be resolved for most antivirus products since a custom PyInstaller bootloader was compiled. You can verify the file's safety by uploading it to VirusTotal. Windows Defender should no longer flag the file, but if it does, ensure you are using an up-to-date version. The fixed `.exe` file will be available in version v0.2.6 or newer.

3. **Failed to Execute Script: Unhandled Exception - Bitmap Not Defined:** If you encounter an error stating "Failed to execute script 'convertme' due to an unhandled exception: bitmap ".\iwoSource\favicon.ico" not defined" or "bitmap ".\source\favicon.png" not defined," it means the `source` folder and its contents are missing. Please download the `source` folder and ensure it is present in the correct location. (***This is no longer an issue. Due to me removing the need for the `.ico` and `.png` file.***)

4. **Empty History After Updating to v0.2.8 or Newer:** After updating to version v0.2.8 or newer, the history may appear empty. This is because the program now saves the full history in the `options.json` file instead of the previous `fullHistory.json` file. You can safely delete the old `fullHistory.json` file as it is no longer used.

5. **Unable to Open Options Menu:** If you are unable to open the options menu, it is likely due to having an outdated `options.json` file. The program checks for enabled options when opening the menu, and if a new option does not exist in the old `options.json`, the program cannot proceed. Deleting the old `options.json` file fixes the issue, but the easiest way to fix this is to use the new button to regenerate your `options.json`. Please note that it will reset all your options. Currently, there is only a small number of options, so this is not a significant concern.

6. **Settings Not Saved in v0.2.9:** In version `v0.2.9` (*and possibly older versions*), a bug prevented settings from being saved due to an update in the status text. This issue has been resolved in `v0.3.0` or `above`.

7. **My Settings wont get carried over to never Versions:** Every time you upgrade to a newer version of this program, you can either export your settings and put them in the `source` folder, or you just use the newer `.exe` or `.py` and copy that to the old directory where you had it installed.

8. **The application's functionality is not fully operational, and I cannot update it via the automated update check:** If you have been provided with a Preview version prior to `v0.3.6`, you will essentially be stuck on that version until a new release is available, unless you manually update it. The reason for this limitation is the way the automated update check functions, which only verifies the version number within the code and the GitHub release page. To differentiate between preview versions and production-ready samples, I have started using the suffix `rc` (release candidate) at the end of the version number, such as `v0.3.7rc`.

	  *Note: This also applies if you utilize the application's source code directly, as I have removed the development branch. For further Information read more [here](#notice-for-developers).*

9. **On MacOS the Buttons in the Options Window don't get rendered correctly:** I have tried every fix I could think of, but this seems to be an issue with tkinter and the 'new' `Apple Silicone`, due to their switch from `AMD64` to `ARM`.

10. **My Settings will always get deleted after closing the program:**  You probably have enabled TemporaryMode, which will prevent any files from staying behind after closing it.

11. **I can't close the program when the options file gets deleted while it's open:** This was fixed in this commit [00d3f25](https://github.com/jinx420/isThisWebsiteOnline/commit/00d3f251cf7d036aeb97ea7b5df0824719aa94ea).

## Notice for Developers

⚠️ **Transition Notice:** ~~As of version v0.3.2, the `develop` branch has been renamed to `old-develop` and will no longer receive updates. We've streamlined our development process to concentrate our efforts on the `master` branch, which holds the most recent stable version.~~

~~If you've been working on the `develop` branch, we advise switching to the `master` branch and initiating a new branch from it for your ongoing development tasks. Please ensure future bug fixes or feature additions are implemented on the `master` branch.~~

~~We appreciate your understanding and cooperation during this transition. For any queries or further assistance, feel free to reach out. Thank you for your unwavering support and dedication to this project!~~

- **Update 17.11.23:** The `old-develop` branch has now been removed.

---
### General Notices

- Starting from v0.3.5, the `convertme.py` file has been removed, and the CLI is now located in `isThisWebsiteOnlineCLI.py` and `isThisWebsiteOnlineCLI.exe`.
