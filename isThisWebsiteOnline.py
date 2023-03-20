from tkinter import messagebox
import webbrowser
import httpx
import json
import sys
import threading
import datetime
import tkinter as tk
from tkinter import ttk


# TODO options menu with option to save to logs on every check
# TODO optimization
# TODO graph showing % of online and offline
# TODO think of TODOS


def thread(func):
    threading.Thread(target=func).start()


# check if website is online using http
def isWebsiteOnlineHTTP(url):
    try:
        httpx.get(f'http://{url}')
        return True
    except:
        return False


# check if website is online using https
def isWebsiteOnlineHTTPS(url):
    try:
        httpx.get(f'https://{url}')
        return True
    except:
        return False


# check website EN
def checkWebsiteEN():
    httpOrHttps = httpOrHttpsEntry.get()
    httpOrHttpsL = httpOrHttps.lower()
    url = urlEntry.get()
    urlL = url.lower()
    if httpOrHttpsL == "http":
        if isWebsiteOnlineHTTP(urlL):
            statusLabel.config(text="Website is online")
        else:
            statusLabel.config(text="Website is offline")
    elif httpOrHttpsL == "https":
        if isWebsiteOnlineHTTPS(urlL):
            statusLabel.config(text="Website is online")
        else:
            statusLabel.config(text="Website is offline")
    else:
        statusLabel.config(text="Please enter http or https")


# check website DE
def checkWebsiteDE():
    httpOrHttps = httpOrHttpsEntry.get()
    httpOrHttpsL = httpOrHttps.lower()
    url = urlEntry.get()
    urlL = url.lower()
    if httpOrHttpsL == "http":
        if isWebsiteOnlineHTTP(urlL):
            statusLabel.config(text="Webseite ist online")
        else:
            statusLabel.config(text="Webseite ist offline")
    elif httpOrHttpsL == "https":
        if isWebsiteOnlineHTTPS(urlL):
            statusLabel.config(text="Website ist online")
        else:
            statusLabel.config(text="Website ist offline")
    else:
        statusLabel.config(text="http oder https eingeben")


# check website ThreadEN
def checkWebsiteThreadEN():
    threading.Thread(target=checkWebsiteEN).start()


# check website ThreadDE
def checkWebsiteThreadDE():
    threading.Thread(target=checkWebsiteDE).start()


# save history
def history():
    history = []
    history.append(urlEntry.get())
    history.append(httpOrHttpsEntry.get())
    with open(".\\iwoSource\\history.json", "w") as f:
        json.dump(history, f)


# load history
def loadHistory():
    with open(".\\iwoSource\\history.json", "r") as f:
        history = json.load(f)
    urlEntry.delete(0, tk.END)
    urlEntry.insert(0, history[0])
    httpOrHttpsEntry.delete(0, tk.END)
    httpOrHttpsEntry.insert(0, history[1])


# save history Thread
def historyThreadEN():
    statusLabel.config(text="History saved")
    threading.Thread(target=history).start()


def historyThreadDE():
    statusLabel.config(text="Verlauf gespeichert")
    threading.Thread(target=history).start()


# load history Thread
def loadHistoryThreadEN():
    statusLabel.config(text="History loaded")
    threading.Thread(target=loadHistory).start()


def loadHistoryThreadDE():
    statusLabel.config(text="Verlauf geladen")
    threading.Thread(target=loadHistory).start()


# clear all history EN
def clearAllHistoryEN():
    with open(".\\iwoSource\\fullHistory.json", "w") as f:
        json.dump({"history": {}}, f, indent=4)
    with open(".\\iwoSource\\History.json", "w") as f:
        json.dump([], f, indent=4)
    statusLabel.config(text="All history cleared")


def clearAllHistoryDE():
    with open(".\\iwoSource\\fullHistory.json", "w") as f:
        json.dump({"history": {}}, f, indent=4)
    with open(".\\iwoSource\\History.json", "w") as f:
        json.dump([], f, indent=4)
    statusLabel.config(text="Alle Verläufe gelöscht")


# get status for logs
def status():
    httpOrHttps = httpOrHttpsEntry.get()
    httpOrHttpsL = httpOrHttps.lower()
    url = urlEntry.get()
    urlL = url.lower()
    if httpOrHttpsL == "http":
        if isWebsiteOnlineHTTP(urlL):
            return 'online'
        else:
            return 'offline'
    elif httpOrHttpsL == "https":
        if isWebsiteOnlineHTTPS(urlL):
            return 'online'
        else:
            return 'offline'


# save history with date and time EN
def historyWithDateAndTimeEN():
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
    statusLabel.config(text="All history saved")
    with open(json_file, 'r+') as jfile:
        j = json.load(jfile)
        for k, v in json_data.items():
            j['history'][k] = v
        jfile.seek(0)
        json.dump(j, jfile, indent=4)


def historyWithDateAndTimeDE():
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
    statusLabel.config(text="Alle Verläufe gespeichert")
    with open(json_file, 'r+') as jfile:
        j = json.load(jfile)
        for k, v in json_data.items():
            j['history'][k] = v
        jfile.seek(0)
        json.dump(j, jfile, indent=4)


# save history with date and time Thread
def historyWithDateAndTimeThreadEN():
    threading.Thread(target=historyWithDateAndTimeEN).start()


def historyWithDateAndTimeThreadDE():
    threading.Thread(target=historyWithDateAndTimeDE).start()


# change language
def changeLanguage(lang):
    if lang == "en":
        httpOrHttpsLabel.config(text="Is the website using http or https? : ")
        urlLabel.config(text="Enter the url: ")
        statusLabel.config(text="Waiting...")
        checkButton.config(text="Check", command=checkWebsiteThreadEN)
        clearButton.config(text="Clear", command=lambda: urlEntry.delete(
            0, tk.END) or httpOrHttpsEntry.delete(0, tk.END) or statusLabel.config(text="Cleared"))
        saveLogsButton.config(
            text="Save Logs", command=historyWithDateAndTimeThreadEN)
        fileMenu.entryconfig(0, label="Open In Browser")
        fileMenu.entryconfig(1, label="Save History", command=historyThreadEN)
        fileMenu.entryconfig(2, label="Load History",
                             command=loadHistoryThreadEN)
        fileMenu.entryconfig(3, label="View Logs", command=seeLogsEN)
        fileMenu.entryconfig(4, label="Clear All History",
                             command=clearAllHistoryEN)
        fileMenu.entryconfig(6, label="Exit")
        helpMenu.entryconfig(0, label="About", command=aboutEN)
    elif lang == "de":
        httpOrHttpsLabel.config(text="Nutzt die Webseite http oder https? :")
        urlLabel.config(text="Url der Webseite: ")
        statusLabel.config(text="Warten...")
        checkButton.config(text="Testen", command=checkWebsiteThreadDE)
        clearButton.config(text="Löschen", command=lambda: urlEntry.delete(
            0, tk.END) or httpOrHttpsEntry.delete(0, tk.END) or statusLabel.config(text="Gelöscht"))
        saveLogsButton.config(text="In Logs speichern",
                              command=historyWithDateAndTimeThreadDE)
        fileMenu.entryconfig(0, label="In Browser öffnen")
        fileMenu.entryconfig(1, label="Verlauf speichern",
                             command=historyThreadDE)
        fileMenu.entryconfig(2, label="Verlauf laden",
                             command=loadHistoryThreadDE)
        fileMenu.entryconfig(3, label="Logs ansehen", command=seeLogsDE)
        fileMenu.entryconfig(
            4, label="Alle Verläufe löschen", command=clearAllHistoryDE)
        fileMenu.entryconfig(6, label="Schließen")
        helpMenu.entryconfig(0, label="Über uns", command=aboutDE)


# see logs EN
def seeLogsEN():
    root = tk.Tk()
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


# see logs EN
def seeLogsDE():
    root = tk.Tk()
    root.title("Rechtsklick auf eine Zeile um die Url und Methode zu kopieren")
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
    tree.pack()


def aboutEN():
    messagebox.showinfo("About", "A simple program to check if a website is online or not.\n\nFeatures:\n1. Save and load history (only one item can be saved at a time)\n2. Open in browser\n3. CLI and GUI\n"
                        "4. Multiple languages\n5. Multithreading\n")


def aboutDE():
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
        if sys.argv[3] == "http":
            if isWebsiteOnlineHTTP(sys.argv[2]):
                print("Website is online")
            else:
                print("Website is offline")
        elif sys.argv[3] == "https":
            if isWebsiteOnlineHTTPS(sys.argv[2]):
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

        changeLanguage('en')

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
            root, text="Check", command=checkWebsiteThreadEN)
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
            root, text="Save to logs", command=historyWithDateAndTimeThreadEN)
        saveLogsButton.grid(row=3, column=1, padx=5, pady=5)

        # Menu
        menu = tk.Menu(root, tearoff=False)
        root.config(menu=menu)

        # File Menu
        fileMenu = tk.Menu(menu, tearoff=False)
        menu.add_cascade(label="File", menu=fileMenu)
        fileMenu.add_command(label="Open In Browser", command=lambda: webbrowser.open(
            f"{httpOrHttpsEntry.get()}://{urlEntry.get()}"))
        fileMenu.add_command(label='Save History', command=historyThreadEN)
        fileMenu.add_command(label='Load History', command=loadHistoryThreadEN)
        fileMenu.add_command(label="See logs", command=seeLogsEN)
        fileMenu.add_command(label="Clear logs", command=clearAllHistoryEN)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=root.destroy)

        # Help Menu
        helpMenu = tk.Menu(menu, tearoff=False)
        menu.add_cascade(label="Help", menu=helpMenu)
        helpMenu.add_command(label="About", command=aboutEN)

        # Language Menu
        languageMenu = tk.Menu(menu, tearoff=False)
        menu.add_cascade(label="Language", menu=languageMenu)
        languageMenu.add_command(
            label="English", command=lambda: changeLanguage("en"))
        languageMenu.add_command(
            label="Deutsch", command=lambda: changeLanguage("de"))

        # MinSize and MaxSize
        root.update()
        root.minsize(root.winfo_width(), root.winfo_height())
        root.maxsize(root.winfo_width(), root.winfo_height())
        root.update()

        # Topmost
        root.attributes("-topmost", True)
        root.attributes("-topmost", False)

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
