import os
from tkinter import messagebox
import webbrowser
import httpx
import json
import sys
import threading
import datetime
import tkinter as tk
from tkinter import ttk


# highest priority:
# TODO optimization

# high priority:


# medium priority:


# lower priority:
# TODO graph showing % of online and offline
# TODO make the clear button also clear the logs

# lowest priority:
# TODO add more options (like: file path for logs, folder etc.)
# TODO add link to documentation in the help tab (to github wiki)
# TODO change changeLanguage()
# TODO add more languages (unlikely because its too much work)
# TODO maybe add a status text to display "settings saved" in the settings tab


version = 'v0.2.7'

# check if critical files and folders exist
critDirs = ['.\\iwoSource']
critFiles = ['.\\iwoSource\\options.json',
             '.\\iwoSource\\fullHistory.json', '.\\iwoSource\\History.json']

for dirs in critDirs:
    if os.path.exists(dirs):
        # print(f'{dirs} Directory exists')
        pass
    else:
        os.mkdir(dirs)

for files in critFiles:
    if os.path.exists(files):
        # print(f'{files} File exists')
        pass
    else:
        if files == '.\\iwoSource\\options.json':
            with open(files, "w") as f:
                json.dump(
                    {"options": {"language": "en", "saveHistoryOnCheck": 1, "checkForUpdatesOnStartup": 0, "clearLogsWithClearButton": 0}}, f, indent=4)
        elif files == '.\\iwoSource\\fullHistory.json':
            with open(".\\iwoSource\\fullHistory.json", "w") as f:
                json.dump({"history": {}}, f, indent=4)
        elif files == '.\\iwoSource\\History.json':
            with open(".\\iwoSource\\History.json", "w") as f:
                json.dump([], f, indent=4)


def checkUpdate():
    with open('.\\iwoSource\\options.json', 'r') as f:
        options = json.load(f)
    try:
        r = httpx.get(
            'https://api.github.com/repos/jinx420/isThisWebsiteOnline/releases/latest')
        if r.status_code == 200:
            latestVersion = r.json()['tag_name']
            if latestVersion != f'{version}':
                if latestVersion > f'{version}':
                    if options['options']['language'] == 'en':
                        if messagebox.askyesno('Update', 'There is a new update available. Do you want to download it?'):
                            # webbrowser.open(f'https://api.github.com/repos/jinx420/isThisWebsiteOnline/zipball/refs/tags/{latestVersion}')
                            webbrowser.open(
                                'https://github.com/jinx420/isThisWebsiteOnline/releases')
                        else:
                            pass
                    elif options['options']['language'] == 'de':
                        if messagebox.askyesno('Update', 'Es ist ein Update verfügbar. Möchten Sie es herunterladen?'):
                            # webbrowser.open(f'https://api.github.com/repos/jinx420/isThisWebsiteOnline/zipball/refs/tags/{latestVersion}')
                            webbrowser.open(
                                'https://github.com/jinx420/isThisWebsiteOnline/releases')
                        else:
                            pass
                elif latestVersion < f'{version}':
                    if options['options']['language'] == 'en':
                        messagebox.showinfo(
                            'Update', 'You are using the latest version')
                    elif options['options']['language'] == 'de':
                        messagebox.showinfo(
                            'Update', 'Sie verwenden die neueste Version')

            else:
                if options['options']['language'] == 'en':
                    messagebox.showinfo(
                        'Update', 'You are using the latest version')
                elif options['options']['language'] == 'de':
                    messagebox.showinfo(
                        'Update', 'Sie verwenden die neueste Version')
        else:
            pass
    except ValueError:
        print('Error: Could not check for updates')


def thread(func):
    threading.Thread(target=func).start()


# check if website is online
def isWebsiteOnline(url):
    if httpOrHttpsEntry.get().lower() == "http":
        try:
            httpx.get(f'http://{url}')
            return True
        except:
            return False
    elif httpOrHttpsEntry.get().lower() == "https":
        try:
            httpx.get(f'https://{url}')
            return True
        except:
            return False


# check website
def checkWebsite():
    with open('.\\iwoSource\\options.json', 'r') as f:
        options = json.load(f)
    if options['options']['saveHistoryOnCheck'] == 1:
        historyWithDateAndTime()
    httpOrHttps = httpOrHttpsEntry.get().lower()
    url = urlEntry.get().lower()
    if httpOrHttps == "http" or httpOrHttps == 'https':
        if isWebsiteOnline(url):
            if options['options']['language'] == 'en':
                statusLabel.config(text="Website is online")
            elif options['options']['language'] == 'de':
                statusLabel.config(text="Webseite ist online")
        else:
            if options['options']['language'] == 'en':
                statusLabel.config(text="Website is offline")
            elif options['options']['language'] == 'de':
                statusLabel.config(text="Webseite ist offline")
    else:
        if options['options']['language'] == 'en':
            statusLabel.config(text="Please enter http or https")
        elif options['options']['language'] == 'de':
            statusLabel.config(text="Bitte geben Sie http oder https ein")


# save history
def history():
    history = []
    history.append(urlEntry.get())
    history.append(httpOrHttpsEntry.get())
    with open(".\\iwoSource\\history.json", "w") as f:
        json.dump(history, f)
    with open('.\\iwoSource\\options.json', 'r') as f:
        options = json.load(f)
    if options['options']['language'] == 'en':
        statusLabel.config(text="History saved")
    elif options['options']['language'] == 'de':
        statusLabel.config(text="Verlauf gespeichert")


# load history
def loadHistory():
    with open(".\\iwoSource\\history.json", "r") as f:
        history = json.load(f)
    urlEntry.delete(0, tk.END)
    urlEntry.insert(0, history[0])
    httpOrHttpsEntry.delete(0, tk.END)
    httpOrHttpsEntry.insert(0, history[1])
    with open('.\\iwoSource\\options.json', 'r') as f:
        options = json.load(f)
    if options['options']['language'] == 'en':
        statusLabel.config(text="History loaded")
    elif options['options']['language'] == 'de':
        statusLabel.config(text="Verlauf geladen")


# clear all history
def clearAllHistory():
    with open(".\\iwoSource\\fullHistory.json", "w") as f:
        json.dump({"history": {}}, f, indent=4)
    with open(".\\iwoSource\\History.json", "w") as f:
        json.dump([], f, indent=4)
    with open('.\\iwoSource\\options.json', 'r') as f:
        options = json.load(f)
    if options['options']['language'] == 'en':
        if options['options']['clearLogsWithClearButton'] == 0:
            statusLabel.config(text="All logs deleted")
        elif options['options']['clearLogsWithClearButton'] == 1:
            statusLabel.config(text="Cleared everything")
    elif options['options']['language'] == 'de':
        if options['options']['clearLogsWithClearButton'] == 0:
            statusLabel.config(text="Alle Logs gelöscht")
        elif options['options']['clearLogsWithClearButton'] == 1:
            statusLabel.config(text="Alles geleert")


# get status for logs
def status():
    url = urlEntry.get().lower()
    if isWebsiteOnline(url):
        return 'online'
    else:
        return 'offline'


# save history with date and time
def historyWithDateAndTime():
    json_file = '.\\iwoSource\\fullHistory.json'
    with open(json_file, 'r+') as jfile:
        j = json.load(jfile)
        data = j
    i = len(data['history'])
    i += 1
    json_data = {
        f"{i}": {
            "url": urlEntry.get(),
            "httpOrHttps": httpOrHttpsEntry.get(),
            "status": status(),
            "dateAndTime": datetime.datetime.now().strftime("%H:%M:%S %d/%m")
        }
    }
    with open(json_file, 'r+') as jfile:
        j = json.load(jfile)
        for k, v in json_data.items():
            j['history'][k] = v
        jfile.seek(0)
        json.dump(j, jfile, indent=4)


# change language
def changeLanguage(lang):
    global lang2
    if lang == "en":
        with open('.\\iwoSource\\options.json', 'r+') as f:
            data = json.load(f)
            data["options"]['language'] = "en"
            f.seek(0)
            json.dump(data, f, indent=4)

        lang2 = lang
        httpOrHttpsLabel.config(text="Is the website using http or https? : ")
        urlLabel.config(text="Enter the url: ")
        statusLabel.config(text="Waiting...")
        checkButton.config(text="Check", command=lambda: thread(checkWebsite))
        clearButton.config(text="Clear", command=clear)
        viewLogsButton.config(
            text="View Logs", command=seeLogs)

        # file menu
        fileMenu.entryconfig(0, label="History")
        fileMenu.entryconfig(1, label="Misc")
        fileMenu.entryconfig(3, label="Options", command=optionsWindow)
        fileMenu.entryconfig(5, label="Exit", command=root.destroy)

        # History sub menu
        historysubMenu.entryconfig(0, label="Save History")
        historysubMenu.entryconfig(1, label="Load History",
                                   command=lambda: thread(loadHistory))
        historysubMenu.entryconfig(2, label="View Logs", command=seeLogs)
        historysubMenu.entryconfig(3, label="Clear All History",
                                   command=clearAllHistory)

        # misc sub menu
        miscSubMenu.entryconfig(0, label="Open in Browser")

        # help menu
        helpMenu.entryconfig(0, label="Check for update", command=checkUpdate)
        helpMenu.entryconfig(1, label="About", command=about)

    elif lang == "de":
        with open('.\\iwoSource\\options.json', 'r+') as f:
            data = json.load(f)
            data["options"]['language'] = "de"
            f.seek(0)
            json.dump(data, f, indent=4)
        lang2 = lang
        httpOrHttpsLabel.config(text="Nutzt die Webseite http oder https? :")
        urlLabel.config(text="Url der Webseite: ")
        statusLabel.config(text="Warten...")
        checkButton.config(text="Testen", command=lambda: thread(checkWebsite))
        clearButton.config(text="Leeren", command=clear)
        viewLogsButton.config(text="Logs ansehen",
                              command=seeLogs)

        # file menu
        fileMenu.entryconfig(0, label="Verlauf")
        fileMenu.entryconfig(1, label="Verschiedenes")
        fileMenu.entryconfig(3, label="Optionen", command=optionsWindow)
        fileMenu.entryconfig(5, label="Schließen", command=root.destroy)

        # sub menu
        historysubMenu.entryconfig(0, label="Verlauf speichern")
        historysubMenu.entryconfig(1, label="Verlauf laden",
                                   command=lambda: thread(loadHistory))
        historysubMenu.entryconfig(2, label="Logs ansehen", command=seeLogs)
        historysubMenu.entryconfig(3, label="Alle Verläufe löschen",
                                   command=clearAllHistory)

        # misc sub menu
        miscSubMenu.entryconfig(0, label="Im Browser öffnen")

        # help menu
        helpMenu.entryconfig(
            0, label="Nach Updates suchen", command=checkUpdate)
        helpMenu.entryconfig(1, label="Über", command=about)


# see logs
def seeLogs():
    with open('.\\iwoSource\\options.json', 'r') as f:
        options = json.load(f)
    if options['options']['language'] == 'en':
        root = tk.Toplevel()
        root.title("Press right click on a row to copy the url and method")
        root.geometry("670x350")
        root.iconbitmap(".\\iwoSource\\favicon.ico")
        root.resizable(False, False)
        tree = ttk.Treeview(root)
        tree.pack(fill=tk.BOTH, expand=True)

        def popup(event):
            try:
                item = tree.identify_row(event.y)
                tree.selection_set(item)
                url = tree.item(item, "values")[1]
                httpOrHttps = tree.item(item, "values")[2]
                urlEntry.delete(0, tk.END)
                httpOrHttpsEntry.delete(0, tk.END)
                urlEntry.insert(0, url)
                httpOrHttpsEntry.insert(0, httpOrHttps)
            except IndexError:
                pass

        tree.bind("<Button-3>", popup)
        tree["columns"] = ("one", "two", "three", "four", "five")
        tree.column("#0", width=0, stretch=tk.NO)
        tree.column("one", anchor=tk.W, width=100)
        tree.column("two", anchor=tk.W, width=100)
        tree.column("three", anchor=tk.W, width=100)
        tree.column("four", anchor=tk.W, width=100)
        tree.column("five", anchor=tk.W, width=100)
        tree.heading("#0", text="", anchor=tk.W)
        tree.heading("one", text="Index", anchor=tk.W)
        tree.heading("two", text="Url", anchor=tk.W)
        tree.heading("three", text="http/https", anchor=tk.W)
        tree.heading("four", text="Status", anchor=tk.W)
        tree.heading("five", text="Date and Time", anchor=tk.W)
        with open(".\\iwoSource\\fullHistory.json", "r") as f:
            data = json.load(f)
            for i in data["history"]:
                tree.insert("", tk.END, text="", values=(
                    i, data["history"][i]["url"], data["history"][i]["httpOrHttps"], data["history"][i]["status"], data["history"][i]["dateAndTime"]))
        tree.pack()
    elif options['options']['language'] == 'de':
        root = tk.Toplevel()
        root.title(
            "Rechtsklick auf eine Zeile um die Url und Methode zu kopieren")
        root.geometry("670x350")
        root.iconbitmap(".\\iwoSource\\favicon.ico")
        root.resizable(False, False)
        tree = ttk.Treeview(root)
        tree.pack(fill=tk.BOTH, expand=True)

        def popup(event):
            try:
                item = tree.identify_row(event.y)
                tree.selection_set(item)
                url = tree.item(item, "values")[1]
                httpOrHttps = tree.item(item, "values")[2]
                urlEntry.delete(0, tk.END)
                httpOrHttpsEntry.delete(0, tk.END)
                urlEntry.insert(0, url)
                httpOrHttpsEntry.insert(0, httpOrHttps)
            except IndexError:
                pass

        tree.bind("<Button-3>", popup)
        tree["columns"] = ("one", "two", "three", "four", "five")
        tree.column("#0", width=0, stretch=tk.NO)
        tree.column("one", anchor=tk.W, width=100)
        tree.column("two", anchor=tk.W, width=100)
        tree.column("three", anchor=tk.W, width=100)
        tree.column("four", anchor=tk.W, width=100)
        tree.column("five", anchor=tk.W, width=100)
        tree.heading("#0", text="", anchor=tk.W)
        tree.heading("one", text="Index", anchor=tk.W)
        tree.heading("two", text="Url", anchor=tk.W)
        tree.heading("three", text="http/https", anchor=tk.W)
        tree.heading("four", text="Status", anchor=tk.W)
        tree.heading("five", text="Datum und Uhrzeit", anchor=tk.W)
        with open(".\\iwoSource\\fullHistory.json", "r") as f:
            data = json.load(f)
            for i in data["history"]:
                tree.insert("", tk.END, text="", values=(
                    i, data["history"][i]["url"], data["history"][i]["httpOrHttps"], data["history"][i]["status"], data["history"][i]["dateAndTime"]))


def optionsWindow():
    cwd = os.getcwd()
    # save options

    def saveOptions():
        options = {
            "options": {
                "language": lang2,
                "saveHistoryOnCheck": saveHistoryOnCheck.get(),
                "checkForUpdatesOnStartup": checkUpdateCM.get(),
                "clearLogsWithClearButton": clearCM.get()
            }
        }
        with open(".\\iwoSource\\options.json", "w") as f:
            json.dump(options, f, indent=4)
        # optionsWindow.destroy()

    def resetOptions():
        options = {
            "options": {
                "language": lang2,
                "saveHistoryOnCheck": 1,
                "checkForUpdatesOnStartup": 0,
                "clearLogsWithClearButton": 0
            }
        }
        with open(".\\iwoSource\\options.json", "w") as f:
            json.dump(options, f, indent=4)
        saveHistoryOnCheck.set(1)
        checkUpdateCM.set(0)
        clearCM.set(0)
        # optionsWindow.destroy()

    # get the value of the check mark box
    saveHistoryOnCheck = tk.IntVar()  # 0 = off, 1 = on
    checkUpdateCM = tk.IntVar()  # 0 = off, 1 = on
    clearCM = tk.IntVar()  # 0 = off, 1 = on

    # get the options from the options.json file
    with open(".\\iwoSource\\options.json", "r") as f:
        data = json.load(f)
        saveHistoryOnCheck.set(data["options"]["saveHistoryOnCheck"])
        checkUpdateCM.set(data["options"]["checkForUpdatesOnStartup"])
        clearCM.set(data["options"]["clearLogsWithClearButton"])

    # options window
    optionsWindow = tk.Toplevel()
    optionsWindow.title("Options")
    optionsWindow.geometry("300x200")
    optionsWindow.iconbitmap(".\\iwoSource\\favicon.ico")
    optionsWindow.resizable(False, False)

    # check mark boxes to enable or disable the options
    checkMarkBox1 = tk.Checkbutton(optionsWindow, text="Save history on every check",
                                   variable=saveHistoryOnCheck, onvalue=1, offvalue=0, command=saveHistoryOnCheck)
    checkMarkBox1.place(x=10, y=10)

    # add a check update on startup check mark box
    checkUpdateCMBox = tk.Checkbutton(optionsWindow, text="Check for updates on startup",
                                      variable=checkUpdateCM, onvalue=1, offvalue=0, command=checkUpdateCM)
    checkUpdateCMBox.place(x=10, y=40)

    # clear button to also clear the logs
    clearCMBox = tk.Checkbutton(
        optionsWindow, text="Clear the logs with the clear button", variable=clearCM, onvalue=1, offvalue=0)
    clearCMBox.place(x=10, y=70)

    # add save button to save the options
    saveButton = tk.Button(optionsWindow, text="Save", command=saveOptions)
    saveButton.place(x=10, y=170)

    # add reset button to reset the options
    resetButton = tk.Button(optionsWindow, text="Reset", command=resetOptions)
    resetButton.place(x=80, y=170)

    if data['options']['language'] == 'en':
        optionsWindow.title("Options")
        checkMarkBox1.config(text="Save history on every check")
        checkUpdateCMBox.config(text="Check for updates on startup")
        clearCMBox.config(text="Clear the logs with the clear button")
        saveButton.config(text="Save")
        resetButton.config(text="Reset")
    elif data['options']['language'] == 'de':
        optionsWindow.title("Optionen")
        checkMarkBox1.config(text="Verlauf bei jedem Check speichern")
        checkUpdateCMBox.config(text="Auf Updates beim Start prüfen")
        clearCMBox.config(text="Logs beim leeren löschen")
        saveButton.config(text="Speichern")
        resetButton.config(text="Zurücksetzen")


def about():
    with open('.\\iwoSource\\options.json', 'r') as f:
        options2 = json.load(f)
    if options2['options']['language'] == 'en':
        messagebox.showinfo("About", "A simple program to check if a website is online or not.\n\nFeatures:\n1. Save and load history (only one item can be saved at a time)\n2. Open in browser\n3. CLI and GUI\n"
                            "4. Multiple languages\n5. Multithreading\n6. Table to show the history and status of past checks\n")
    elif options2['options']['language'] == 'de':
        messagebox.showinfo("Über uns", "Ein einfaches Programm um zu überprüfen ob eine Webseite online ist oder nicht.\n\nFunktionen:\n1. Verlauf speichern und laden (nur ein Eintrag kann gespeichert werden)\n2. In Browser öffnen\n3. CLI und GUI\n"
                            "4. Mehrere Sprachen\n5. Multithreading\n6. Tabelle um den Verlauf und den Status von vergangenen Checks anzuzeigen\n")


def clear():
    with open('.\\iwoSource\\options.json', 'r') as f:
        options = json.load(f)

    if options['options']['clearLogsWithClearButton'] == 0:
        urlEntry.delete(0, tk.END)
        httpOrHttpsEntry.delete(0, tk.END)
        if options['options']['language'] == 'en':
            statusLabel.config(text="Cleared")
        elif options['options']['language'] == 'de':
            statusLabel.config(text="Gelöscht")

    elif options['options']['clearLogsWithClearButton'] == 1:
        urlEntry.delete(0, tk.END)
        httpOrHttpsEntry.delete(0, tk.END)
        clearAllHistory()


# main
if __name__ == "__main__":
    # check if the user entered the correct arguments
    if len(sys.argv) < 4:
        print('usage: python isThisWebsiteOnline.py <cli or gui> <url> <http or https>')
        sys.exit(1)

    # cli
    if sys.argv[1] == "cli":
        if sys.argv[3] == "http" or sys.argv[3] == "https":
            if isWebsiteOnline(sys.argv[2]):
                print("Website is online")
            else:
                print("Website is offline")
        else:
            print(
                "usage: python isThisWebsiteOnline.py <cli or gui> <url> <http or https>")

    # gui
    elif sys.argv[1] == "gui":
        # root
        root = tk.Tk()
        root.title("IsThisWebsiteOnline?")
        root.geometry("670x350")
        root.iconbitmap(".\\iwoSource\\favicon.ico")
        root.resizable(False, False)

        # image
        image = tk.PhotoImage(file=".\\iwoSource\\favicon.png")
        imageLabel = ttk.Label(root, image=image)
        imageLabel.grid(row=0, column=2, rowspan=4, padx=30, pady=3)

        # http or https label
        httpOrHttpsLabel = ttk.Label(
            root, text="Is the website using http or https? : ")
        httpOrHttpsLabel.grid(row=0, column=0, padx=5, pady=5)

        # http or https entry
        httpOrHttpsEntry = ttk.Entry(root)
        httpOrHttpsEntry.insert(0, sys.argv[3])
        httpOrHttpsEntry.grid(row=0, column=1, padx=5, pady=5)

        # url label
        urlLabel = ttk.Label(root, text="Enter the url: ")
        urlLabel.grid(row=1, column=0, padx=5, pady=5)

        # url entry
        urlEntry = ttk.Entry(root)
        urlEntry.insert(0, sys.argv[2])
        urlEntry.grid(row=1, column=1, padx=5, pady=5)

        # Check Button
        checkButton = ttk.Button(
            root, text="Check", command=lambda: thread(checkWebsite))
        checkButton.grid(row=2, column=0, padx=5, pady=5)

        # Status Label
        statusLabel = ttk.Label(root, text="Waiting...")
        statusLabel.grid(row=2, column=1, columnspan=1, padx=0, pady=5)

        # Clear Button
        clearButton = ttk.Button(root, text="Clear", command=clear)
        clearButton.grid(row=3, column=0, padx=5, pady=5)

        # save to logs button
        viewLogsButton = ttk.Button(
            root, text="View logs", command=seeLogs)
        viewLogsButton.grid(row=3, column=1, padx=5, pady=5)

        # version
        versionLabel = tk.Label(root, text=f"Version: {version}")
        versionLabel.place(x=580, y=311)

        # Menu
        menu = tk.Menu(root, tearoff=False)
        root.config(menu=menu)

        # File Menu
        fileMenu = tk.Menu(menu, tearoff=False)
        menu.add_cascade(label="File", menu=fileMenu)

        # add History submenu
        historysubMenu = tk.Menu(fileMenu, tearoff=False)
        fileMenu.add_cascade(label="History", menu=historysubMenu)
        historysubMenu.add_command(label='Save History',
                                   command=lambda: thread(history))
        historysubMenu.add_command(label='Load History',
                                   command=lambda: thread(loadHistory))
        historysubMenu.add_command(label="See logs", command=seeLogs)
        historysubMenu.add_command(label="Clear logs", command=clearAllHistory)

        # add misc submenu
        miscSubMenu = tk.Menu(fileMenu, tearoff=False)
        fileMenu.add_cascade(label="Misc", menu=miscSubMenu)
        miscSubMenu.add_command(label="Open In Browser", command=lambda: webbrowser.open(
            f"{httpOrHttpsEntry.get()}://{urlEntry.get()}"))

        fileMenu.add_separator()
        fileMenu.add_command(label='Options', command=optionsWindow)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=root.destroy)

        # Help Menu
        helpMenu = tk.Menu(menu, tearoff=False)
        menu.add_cascade(label="Help", menu=helpMenu)
        helpMenu.add_command(label='Check for update', command=checkUpdate)
        helpMenu.add_command(label="About", command=about)

        # Language Menu
        languageMenu = tk.Menu(menu, tearoff=False)
        menu.add_cascade(label="Language", menu=languageMenu)
        languageMenu.add_command(
            label="English", command=lambda: changeLanguage('en'))
        languageMenu.add_command(
            label="Deutsch", command=lambda: changeLanguage('de'))

        # MinSize and MaxSize
        root.update()
        root.minsize(root.winfo_width(), root.winfo_height())
        root.maxsize(root.winfo_width(), root.winfo_height())
        root.update()

        # Topmost
        root.attributes("-topmost", True)
        root.attributes("-topmost", False)

        # change default language
        with open('.\\iwoSource\\options.json', 'r') as f:
            options = json.load(f)
            lang2 = options['options']['language']
        changeLanguage(lang2)

        if options['options']['checkForUpdatesOnStartup'] == True:
            checkUpdate()

        # Mainloop
        root.mainloop()

    # neither cli nor gui
    elif sys.argv[1] != "cli" and sys.argv[1] != "gui":
        print('usage: python isThisWebsiteOnline.py <cli or gui> <url> <http or https>')
        sys.exit(1)

    # invalid http or https
    elif sys.argv[3] != "http" and sys.argv[3] != "https":
        print('usage: python isThisWebsiteOnline.py <cli or gui> <url> <http or https>')
        sys.exit(1)

    sys.exit(0)
