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


# TODO optimization
# TODO graph showing % of online and offline
# TODO think of TODOS


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
                statusLabel.config(text="Website ist online")
        else:
            if options['options']['language'] == 'en':
                statusLabel.config(text="Website is offline")
            elif options['options']['language'] == 'de':
                statusLabel.config(text="Website ist offline")
    else:
        if options['options']['language'] == 'en':
            statusLabel.config(text="Please enter http or https")
        elif options['options']['language'] == 'de':
            statusLabel.config(text="Bitte geben Sie http oder https ein")


# check website Thread
def checkWebsiteThread():
    threading.Thread(target=checkWebsite).start()


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


# save history Thread
def historyThread():
    threading.Thread(target=history).start()


# load history Thread
def loadHistoryThread():
    threading.Thread(target=loadHistory).start()


# clear all history
def clearAllHistory():
    with open(".\\iwoSource\\fullHistory.json", "w") as f:
        json.dump({"history": {}}, f, indent=4)
    with open(".\\iwoSource\\History.json", "w") as f:
        json.dump([], f, indent=4)
    with open('.\\iwoSource\\options.json', 'r') as f:
        options = json.load(f)
    if options['options']['language'] == 'en':
        statusLabel.config(text="All history cleared")
    elif options['options']['language'] == 'de':
        statusLabel.config(text="Alle Verlauf gelöscht")


# get status for logs
def status():
    url = urlEntry.get().lower()
    if isWebsiteOnline(url):
        return 'online'
    else:
        return 'offline'


# save history with date and time
def historyWithDateAndTime():
    if os.path.exists('.\\iwoSource\\fullHistory.json'):
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
    else:
        with open(".\\iwoSource\\fullHistory.json", "w") as f:
            json.dump({"history": {}}, f, indent=4)
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
        checkButton.config(text="Check", command=lambda: checkWebsiteThread)
        clearButton.config(text="Clear", command=lambda: urlEntry.delete(
            0, tk.END) or httpOrHttpsEntry.delete(0, tk.END) or statusLabel.config(text="Cleared"))
        saveLogsButton.config(
            text="Save Logs", command=lambda: thread(historyWithDateAndTime))
        fileMenu.entryconfig(0, label="Open In Browser")
        fileMenu.entryconfig(1, label="Save History", command=historyThread)
        fileMenu.entryconfig(2, label="Load History",
                             command=loadHistoryThread)
        fileMenu.entryconfig(3, label="View Logs", command=seeLogs)
        fileMenu.entryconfig(4, label="Clear All History",
                             command=clearAllHistory)
        fileMenu.entryconfig(6, label="Options", command=optionsWindow)
        fileMenu.entryconfig(8, label="Exit", command=exit)
        helpMenu.entryconfig(0, label="About", command=about)
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
        checkButton.config(text="Testen", command=lambda: checkWebsiteThread)
        clearButton.config(text="Löschen", command=lambda: urlEntry.delete(
            0, tk.END) or httpOrHttpsEntry.delete(0, tk.END) or statusLabel.config(text="Gelöscht"))
        saveLogsButton.config(text="In Logs speichern",
                              command=lambda: thread(historyWithDateAndTime))
        fileMenu.entryconfig(0, label="In Browser öffnen")
        fileMenu.entryconfig(1, label="Verlauf speichern",
                             command=historyThread)
        fileMenu.entryconfig(2, label="Verlauf laden",
                             command=loadHistoryThread)
        fileMenu.entryconfig(3, label="Logs ansehen", command=seeLogs)
        fileMenu.entryconfig(
            4, label="Alle Verläufe löschen", command=clearAllHistory)
        fileMenu.entryconfig(6, label="Schließen")
        helpMenu.entryconfig(0, label="Über uns", command=about)


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
    # save options
    def saveOptions():
        options = {
            "options": {
                "language": lang2,
                "saveHistoryOnCheck": saveHistoryOnCheck.get()
            }
        }
        with open(".\\iwoSource\\options.json", "w") as f:
            json.dump(options, f, indent=4)
        # optionsWindow.destroy()

    def resetOptions():
        options = {
            "options": {
                "language": lang2,
                "saveHistoryOnCheck": 0
            }
        }
        with open(".\\iwoSource\\options.json", "w") as f:
            json.dump(options, f, indent=4)
        saveHistoryOnCheck.set(0)
        # optionsWindow.destroy()

    # get the value of the check mark box
    saveHistoryOnCheck = tk.IntVar()  # 0 = off, 1 = on

    # get the options from the options.json file
    with open(".\\iwoSource\\options.json", "r") as f:
        data = json.load(f)
        saveHistoryOnCheck.set(data["options"]["saveHistoryOnCheck"])

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

    # add save button to save the options
    saveButton = tk.Button(optionsWindow, text="Save", command=saveOptions)
    saveButton.place(x=10, y=170)

    # add reset button to reset the options
    resetButton = tk.Button(optionsWindow, text="Reset", command=resetOptions)
    resetButton.place(x=60, y=170)

    with open('.\\iwoSource\\options.json', 'r') as f:
        options2 = json.load(f)
    if options2['options']['language'] == 'en':
        optionsWindow.title("Options")
        checkMarkBox1.config(text="Save history on every check")
        saveButton.config(text="Save")
        resetButton.config(text="Reset")
    elif options2['options']['language'] == 'de':
        optionsWindow.title("Optionen")
        checkMarkBox1.config(text="Verlauf bei jedem Check speichern")
        saveButton.config(text="Speichern")
        resetButton.config(text="Zurücksetzen")


def about():
    with open('.\\iwoSource\\options.json', 'r') as f:
        options2 = json.load(f)
    if options2['options']['language'] == 'en':
        messagebox.showinfo("About", "A simple program to check if a website is online or not.\n\nFeatures:\n1. Save and load history (only one item can be saved at a time)\n2. Open in browser\n3. CLI and GUI\n"
                            "4. Multiple languages\n5. Multithreading\n")
    elif options2['options']['language'] == 'de':
        messagebox.showinfo("Über uns", "Ein einfaches Programm um zu überprüfen ob eine Webseite online ist oder nicht.\n\nFunktionen:\n1. Verlauf speichern und laden (nur ein Eintrag kann gespeichert werden)\n2. In Browser öffnen\n3. CLI und GUI\n"
                            "4. Mehrere Sprachen\n5. Multithreading\n")


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
        imageLabel.grid(row=0, column=2, rowspan=4, padx=30, pady=5)

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
            root, text="Check", command=checkWebsiteThread)
        checkButton.grid(row=2, column=0, padx=5, pady=5)

        # Status Label
        statusLabel = ttk.Label(root, text="Waiting...")
        statusLabel.grid(row=2, column=1, columnspan=1, padx=0, pady=5)

        # Clear Button
        clearButton = ttk.Button(root, text="Clear", command=lambda: urlEntry.delete(
            0, tk.END) or httpOrHttpsEntry.delete(0, tk.END) or statusLabel.config(text="Cleared"))
        clearButton.grid(row=3, column=0, padx=5, pady=5)

        # save to logs button
        saveLogsButton = ttk.Button(
            root, text="Save to logs", command=lambda: thread(historyWithDateAndTime))
        saveLogsButton.grid(row=3, column=1, padx=5, pady=5)

        # Menu
        menu = tk.Menu(root, tearoff=False)
        root.config(menu=menu)

        # File Menu
        fileMenu = tk.Menu(menu, tearoff=False)
        menu.add_cascade(label="File", menu=fileMenu)
        fileMenu.add_command(label="Open In Browser", command=lambda: webbrowser.open(
            f"{httpOrHttpsEntry.get()}://{urlEntry.get()}"))
        fileMenu.add_command(label='Save History', command=historyThread)
        fileMenu.add_command(label='Load History', command=loadHistoryThread)
        fileMenu.add_command(label="See logs", command=seeLogs)
        fileMenu.add_command(label="Clear logs", command=clearAllHistory)
        fileMenu.add_separator()
        fileMenu.add_command(label='Options', command=optionsWindow)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=root.destroy)

        # Help Menu
        helpMenu = tk.Menu(menu, tearoff=False)
        menu.add_cascade(label="Help", menu=helpMenu)
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
