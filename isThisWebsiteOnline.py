import os
import subprocess
from subprocess import DEVNULL, STDOUT
from tkinter import messagebox
import webbrowser
import httpx
import json
import threading
import datetime
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style


#  ___  ___       __   ________  ________
# |\  \|\  \     |\  \|\   __  \|\_____  \
# \ \  \ \  \    \ \  \ \  \|\  \|____|\  \
#  \ \  \ \  \  __\ \  \ \  \\\  \    \ \__\
#   \ \  \ \  \|\__\_\  \ \  \\\  \    \|__|
#    \ \__\ \____________\ \_______\       ___
#     \|__|\|____________|\|_______|      |\__\
#         (t)                             \|__|


version = 'v0.3.6'
os_name = os.name

# check if critical files and folders exist
critDirs = ['./iwoSource']
critFiles = ['./iwoSource/options.json', './iwoSource/History.json']


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
        # nt
        if files == './iwoSource/options.json':
            with open(files, "w") as f:
                json.dump(
                    {"options": {"saveHistoryOnCheck": 1, "checkForUpdatesOnStartup": 0, "clearLogsWithClearButton": 0, "reloadGUIwith": 0, "devPopUp": 0}, "fullHistory": {}}, f, indent=4)
        elif files == './iwoSource/History.json':
            with open("./iwoSource/History.json", "w") as f:
                json.dump([], f, indent=4)


options_file = './iwoSource/options.json'
last_modified_time = 0
global_options = {}


def load_options():
    global last_modified_time
    global global_options
    current_modified_time = os.path.getmtime(options_file)
    if current_modified_time != last_modified_time:
        with open(options_file, 'r') as f:
            options = json.load(f)
        global_options = options['options']
        last_modified_time = current_modified_time
    return global_options


def checkUpdate():
    try:
        r = httpx.get(
            'https://api.github.com/repos/jinx420/isThisWebsiteOnline/releases/latest')
        if r.status_code == 200:
            latestVersion = r.json()['tag_name']
            if latestVersion != f'{version}':
                if latestVersion > f'{version}':
                    if messagebox.askyesno('Update', 'There is a new update available. Do you want to download it?'):
                        # webbrowser.open(f'https://api.github.com/repos/jinx420/isThisWebsiteOnline/zipball/refs/tags/{latestVersion}')
                        webbrowser.open(
                            'https://github.com/jinx420/isThisWebsiteOnline/releases')
                elif latestVersion == f'{version}':
                    messagebox.showinfo(
                        'Update', 'You are using the latest version')
                elif latestVersion < f'{version}':
                    if messagebox.askyesno(
                            'Update', 'You are using an unstable Developer version. Do you want to download the latest stable version?'):
                        webbrowser.open(
                            'https://github.com/jinx420/isThisWebsiteOnline/releases')

            else:
                messagebox.showinfo(
                    'Update', 'You are using the latest version')
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
    options = load_options()
    if options['saveHistoryOnCheck'] == 1:
        historyWithDateAndTime()
    httpOrHttps = httpOrHttpsEntry.get().lower()
    url = urlEntry.get().lower()
    if httpOrHttps == "http" or httpOrHttps == 'https':
        if isWebsiteOnline(url):
            statusLabel.config(text="Website is online")
        else:
            statusLabel.config(text="Website is offline")
    else:
        statusLabel.config(text="Please enter http or https")


# save history
def history():
    history = []
    history.append(urlEntry.get())
    history.append(httpOrHttpsEntry.get())
    with open("./iwoSource/history.json", "w") as f:
        json.dump(history, f)
    statusLabel.config(text="History saved")


# load history
def loadHistory():
    with open("./iwoSource/history.json", "r") as f:
        history = json.load(f)
    urlEntry.delete(0, tk.END)
    httpOrHttpsEntry.delete(0, tk.END)
    urlEntry.insert(0, history[0])
    httpOrHttpsEntry.insert(0, history[1])
    statusLabel.config(text="History loaded")


# clear all history
def clearAllHistory():
    options = load_options()
    saveHistoryOnCheck = options["saveHistoryOnCheck"]
    checkUpdateCM = options["checkForUpdatesOnStartup"]
    clearCM = options["clearLogsWithClearButton"]

    with open("./iwoSource/options.json", "w") as f:
        json.dump({"options": {"saveHistoryOnCheck": saveHistoryOnCheck,
                               "checkForUpdatesOnStartup": checkUpdateCM, "clearLogsWithClearButton": clearCM}, "fullHistory": {}}, f, indent=4)

    with open("./iwoSource/History.json", "w") as f:
        json.dump([], f, indent=4)

    if options['clearLogsWithClearButton'] == 0:
        statusLabel.config(text="All logs deleted")
    elif options['clearLogsWithClearButton'] == 1:
        statusLabel.config(text="Cleared everything")


# get status for logs
def status():
    url = urlEntry.get().lower()
    if isWebsiteOnline(url):
        return 'online'
    else:
        return 'offline'


# save history with date and time
def historyWithDateAndTime():
    json_file = './iwoSource/options.json'
    with open(json_file, 'r+') as jfile:
        j = json.load(jfile)
        data = j
    i = len(data['fullHistory'])
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
            j['fullHistory'][k] = v
        jfile.seek(0)
        json.dump(j, jfile, indent=4)


# view Logs
def viewLogs():
    root = tk.Toplevel()
    root.title("Press right click on a row to copy the url and method")
    root.geometry("670x350")
    root.iconbitmap("./iwoSource/favicon.ico")
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
    with open("./iwoSource/options.json", "r") as f:
        data = json.load(f)
        for i in data["fullHistory"]:
            tree.insert("", tk.END, text="", values=(
                i, data["fullHistory"][i]["url"], data["fullHistory"][i]["httpOrHttps"], data["fullHistory"][i]["status"], data["fullHistory"][i]["dateAndTime"]))
    tree.pack()


def optionsWindow():
    def saveOptions():
        with open('./iwoSource/options.json', 'r') as f:
            devVar = json.load(f)

        devPopUpVar = devVar['options']['devPopUp']

        options = {
            "options": {
                "saveHistoryOnCheck": saveHistoryOnCheck.get(),
                "checkForUpdatesOnStartup": checkUpdateCM.get(),
                "clearLogsWithClearButton": clearCM.get(),
                "reloadGUIwith": reloadGUIwith.get(),
                "devPopUp": devPopUpVar
            },
            "fullHistory": {}
        }
        with open("./iwoSource/options.json", "w") as f:
            json.dump(options, f, indent=4)

        savedText.config(text="Options saved")
        # optionsWindow.destroy()

    def resetOptions():
        optionsReset = {
            "options": {
                "saveHistoryOnCheck": 1,
                "checkForUpdatesOnStartup": 0,
                "clearLogsWithClearButton": 0,
                "reloadGUIwith": 0,
                "devPopUp": 0
            },
            "fullHistory": {}
        }

        with open("./iwoSource/options.json", "w") as f:
            json.dump(optionsReset, f, indent=4)
        saveHistoryOnCheck.set(1)
        checkUpdateCM.set(0)
        clearCM.set(0)
        reloadGUIwith.set(0)

        savedText.config(text="Options reset")
        # optionsWindow.destroy()

    def importOptions():
        optionsFile = tk.filedialog.askopenfilename(
            initialdir=os.getcwd(), title="Select options.json file", filetypes=(("JSON files", "*.json"), ("All files", "*.*")))

        with open(optionsFile, "r") as f:
            options = json.load(f)

        saveHistoryOnCheck.set(options["saveHistoryOnCheck"])
        checkUpdateCM.set(options["checkForUpdatesOnStartup"])
        clearCM.set(options["clearLogsWithClearButton"])
        reloadGUIwith.set(options["reloadGUIwith"])

        savedText.config(text="Options imported")

        saveOptions()

    def exportOptions():
        optionsFile = tk.filedialog.asksaveasfilename(
            initialdir=os.getcwd(), title="Select options.json file", filetypes=(("JSON files", "*.json"), ("All files", "*.*")))

        options = {
            "options": {
                "saveHistoryOnCheck": saveHistoryOnCheck.get(),
                "checkForUpdatesOnStartup": checkUpdateCM.get(),
                "clearLogsWithClearButton": clearCM.get(),
                "reloadGUIwith": reloadGUIwith.get(),
                "devPopUp": 0
            },
            "fullHistory": {}
        }

        with open(optionsFile, "w") as f:
            json.dump(options, f, indent=4)

        savedText.config(text="Options exported")

    def devPopUp():
        data = load_options()
        if data['devPopUp'] == 0:
            messagebox.showinfo(
                "Dev", "This feature is meant for developers. If you are not a developer, please do not use this feature."
                "\nUsing this feature can cause the program to break, use with caution.")
            options = {
                "options": {
                    "saveHistoryOnCheck": saveHistoryOnCheck.get(),
                    "checkForUpdatesOnStartup": checkUpdateCM.get(),
                    "clearLogsWithClearButton": clearCM.get(),
                    "reloadGUIwith": reloadGUIwith.get(),
                    "devPopUp": 1
                },
                "fullHistory": {}
            }
            with open("./iwoSource/options.json", "w") as f:
                json.dump(options, f, indent=4)
        elif data['devPopUp'] == 1:
            pass

    # get the value of the check mark box
    saveHistoryOnCheck = tk.IntVar()  # 0 = off, 1 = on
    checkUpdateCM = tk.IntVar()  # 0 = off, 1 = on
    clearCM = tk.IntVar()  # 0 = off, 1 = on
    reloadGUIwith = tk.IntVar()  # 0 = reload with .exe, 1 = reload with .py

    # get the options from the options.json file
    data = load_options()
    saveHistoryOnCheck.set(data["saveHistoryOnCheck"])
    checkUpdateCM.set(data["checkForUpdatesOnStartup"])
    clearCM.set(data["clearLogsWithClearButton"])
    reloadGUIwith.set(data["reloadGUIwith"])

    # options window
    optionsWindow = tk.Toplevel()
    optionsWindow.title("Options")
    optionsWindow.geometry("400x200")
    optionsWindow.iconbitmap("./iwoSource/favicon.ico")
    optionsWindow.resizable(False, False)

    # check mark boxes to enable or disable the options
    checkMarkBox1 = tk.Checkbutton(optionsWindow, text="Save history on every check",
                                   variable=saveHistoryOnCheck, onvalue=1, offvalue=0, command=saveHistoryOnCheck)
    checkMarkBox1.place(x=10, y=10)

    # check mark box to check for updates on startup
    checkUpdateCMBox = tk.Checkbutton(optionsWindow, text="Check for updates on startup",
                                      variable=checkUpdateCM, onvalue=1, offvalue=0, command=checkUpdateCM)
    checkUpdateCMBox.place(x=10, y=40)

    # clear button to also clear the logs
    clearCMBox = tk.Checkbutton(
        optionsWindow, text="Clear the logs with the clear button", variable=clearCM, onvalue=1, offvalue=0)
    clearCMBox.place(x=10, y=70)

    # reload gui with .py or .exe
    reloadGUIBox = tk.Checkbutton(optionsWindow, text="Reload GUI with .exe or .py",
                                  variable=reloadGUIwith, onvalue=1, offvalue=0, command=lambda: devPopUp())
    reloadGUIBox.place(x=10, y=100)
    reloadExplanation = tk.Label(optionsWindow, text='(no checkmark = .exe | checkmark = .py)',
                                 padx=0, pady=0)
    reloadExplanation.place(x=30, y=120)

    # save button
    saveButton = tk.Button(optionsWindow, text="Save", command=saveOptions)
    saveButton.place(x=10, y=170)

    # reset button
    resetButton = tk.Button(optionsWindow, text="Reset", command=resetOptions)
    resetButton.place(x=80, y=170)

    # import button
    importButton = tk.Button(
        optionsWindow, text="Import", command=importOptions)
    importButton.place(x=150, y=170)

    # export button
    exportButton = tk.Button(
        optionsWindow, text="Export", command=exportOptions)
    exportButton.place(x=220, y=170)

    # saved text
    savedText = tk.Label(optionsWindow, text="", padx=0, pady=0)
    savedText.place(x=300, y=172)


def graph():
    data = load_options()
    online = 0
    offline = 0
    for i in data["fullHistory"]:
        if data["fullHistory"][i]["status"] == "online":
            online += 1
        elif data["fullHistory"][i]["status"] == "offline":
            offline += 1
    if online == 0 and offline == 0:
        messagebox.showerror(
            "Error", "You need to check a website first to make a graph.")
    else:
        graphWindow = tk.Toplevel()
        graphWindow.title("Graph")
        graphWindow.geometry("500x500")
        graphWindow.iconbitmap("./iwoSource/favicon.ico")
        graphWindow.resizable(False, False)

        colors = ["#32cd32", "#dc143c"]
        fig = Figure(figsize=(5, 5), dpi=100)
        fig.add_subplot(111).pie([online, offline], labels=[
            "Online", "Offline"], autopct='%1.1f%%', shadow=True, startangle=90, colors=colors)
        fig.set_facecolor("#808080")
        fig.set_edgecolor("#808080")
        canvas = FigureCanvasTkAgg(fig, master=graphWindow)
        canvas.draw()
        canvas.get_tk_widget().pack()


def about():
    aboutWindow = tk.Toplevel()
    aboutWindow.title("About")
    aboutWindow.geometry("450x150")
    aboutWindow.iconbitmap("./iwoSource/favicon.ico")
    aboutWindow.resizable(False, False)

    aboutText = tk.Label(aboutWindow, text="A simple program to check if a website is online or not.\n"
                         "\nIf you have any suggestions or find any bugs, please report them on the github page.\nhttps://github.com/jinx420/isThisWebsiteOnline/issues\n"
                         "\nA list of all the features can be found in the README.md, and on the github page.\nhttps://github.com/jinx420/isThisWebsiteOnline/",
                         padx=0, pady=0)
    aboutText.place(x=0, y=0)

    githubButton = tk.Button(aboutWindow, text="Github Issues", command=lambda: webbrowser.open(
        "https://github.com/jinx420/isThisWebsiteOnline/issues"))
    githubButton.place(x=5, y=125)

    githubButton = tk.Button(aboutWindow, text="Github Page", command=lambda: webbrowser.open(
        "https://github.com/jinx420/isThisWebsiteOnline"))
    githubButton.place(x=100, y=125)

    # messagebox.showinfo("About", f"A simple program to check if a website is online or not."
    #                     "\n\nIf you have any suggestions or find any bugs, please report them on the github page.\nhttps://github.com/jinx420/isThisWebsiteOnline/issues"
    #                     "\n\nA list of all teh features can be found in the README.md, and on the github page.\nhttps://github.com/jinx420/isThisWebsiteOnline/")


def clear():
    options = load_options()

    if options['clearLogsWithClearButton'] == 0:
        urlEntry.delete(0, tk.END)
        httpOrHttpsEntry.delete(0, tk.END)
        statusLabel.config(text="Cleared")

    elif options['clearLogsWithClearButton'] == 1:
        urlEntry.delete(0, tk.END)
        httpOrHttpsEntry.delete(0, tk.END)
        clearAllHistory()


# main
if __name__ == "__main__":
    # removed due to it causing problems if you use the python file instead of the exe and try to reload the gui
    # this also caused a slow startup time and overall slower performance
    # i figured that it would still be a good idea to keep this code here in case i want to add it back in the future
    # or if someone else wants to improve it and add it back in :D

    # if os.path.exists('.\\isThisWebsiteOnline.py') and os_name == 'nt':
    #     with open(os.devnull, "w") as devnull:
    #         subprocess.call(
    #             ["pip3", "install", "-r", ".\\requirements.txt"], stdout=DEVNULL, stderr=STDOUT)
    # elif os.path.exists('./isThisWebsiteOnline.py') and os_name == 'posix':
    #     with open(os.devnull, "w") as devnull:
    #         subprocess.call(
    #             ["pip3", "install", "-r", "./requirements.txt"], stdout=DEVNULL, stderr=STDOUT)

    options = load_options()

    # root
    root = tk.Tk()
    root.title(
        "IsThisWebsiteOnline?                                                                                  Made with 💜 by jinx")
    root.geometry("670x350")
    root.iconbitmap("./iwoSource/favicon.ico")
    root.resizable(False, False)
    root.config(background="#26777f")

    # reload gui
    def reloadGUI():
        options = load_options()
        root.destroy()
        if options['reloadGUIwith'] == 1:
            subprocess.call(
                ["python3", "isThisWebsiteOnline.py", "gui"])
        elif options['reloadGUIwith'] == 0:
            subprocess.call([".\isThisWebsiteOnline.exe"])

    # regenerate options.json
    def regenerateOptions():
        with open("./iwoSource/options.json", "w") as f:
            json.dump(
                {"options": {"saveHistoryOnCheck": 1, "checkForUpdatesOnStartup": 0, "clearLogsWithClearButton": 0, "reloadGUIwith": 0, "devPopUp": 0}, "fullHistory": {}}, f, indent=4)

        statusLabel.config(text="options.json regenerated!")

    # reload gui button
    reloadGUIButton = ttk.Button(
        root, text="Reload GUI", command=reloadGUI)
    reloadGUIButton.place(x=10, y=300)

    # regenerate options.json button
    regenerateOptionsButton = ttk.Button(
        root, text="Regenerate options.json", command=regenerateOptions)
    regenerateOptionsButton.place(x=120, y=300)

    # image
    image = tk.PhotoImage(file="./iwoSource/favicon.png")
    imageLabel = ttk.Label(root, image=image)
    imageLabel.place(x=390, y=0)
    imageLabel.config(background="#FFFFFF")

    # http or https label
    httpOrHttpsLabel = ttk.Label(
        root, text="Is the website using http or https? : ")
    httpOrHttpsLabel.place(x=10, y=23)
    httpOrHttpsLabel.config(background="#FFFFFF")

    # http or https entry
    httpOrHttpsEntry = ttk.Entry(root)
    httpOrHttpsEntry.config(background="#FFFFFF")
    httpOrHttpsEntry.place(x=220, y=20)

    # url label
    urlLabel = ttk.Label(root, text="Enter the url: ")
    urlLabel.place(x=10, y=53)
    urlLabel.config(background="#FFFFFF")

    # url entry
    urlEntry = ttk.Entry(root)
    urlEntry.place(x=220, y=50)

    # Check Button
    checkButton = ttk.Button(
        root, text="Check", command=lambda: thread(checkWebsite))
    checkButton.place(x=10, y=100)

    # Status Label
    statusLabel = ttk.Label(root, text="Waiting...")
    statusLabel.place(x=235, y=102)
    statusLabel.config(background="#FFFFFF")

    # Clear Button
    clearButton = ttk.Button(root, text="Clear", command=clear)
    clearButton.place(x=120, y=100)

    # save to logs button
    viewLogsButton = ttk.Button(
        root, text="View logs", command=viewLogs)
    viewLogsButton.place(x=10, y=150)

    # graph button
    graphButton = ttk.Button(
        root, text="Graph", command=lambda: thread(graph))
    graphButton.place(x=120, y=150)

    # version
    versionLabel = tk.Label(root, text=f"Version: {version}")
    versionLabel.place(x=580, y=311)
    versionLabel.config(background="#FFFFFF")

    # Menu
    menu = tk.Menu(root, tearoff=False)
    root.config(menu=menu)

    style = Style(theme='pulse')

    # File Menu
    file_menu = tk.Menu(menu, tearoff=False)
    menu.add_cascade(label="File", menu=file_menu)
    menu.config(background="#FFFFFF")
    file_menu.config(background="#FFFFFF")

    # history sub menu
    history_submenu = tk.Menu(file_menu, tearoff=False)
    file_menu.add_cascade(label="History", menu=history_submenu)
    history_submenu.add_command(label='Save History',
                                command=lambda: thread(history))
    history_submenu.add_command(label='Load History',
                                command=lambda: thread(loadHistory))
    history_submenu.add_command(label="View logs", command=viewLogs)
    history_submenu.add_command(
        label="Clear logs", command=clearAllHistory)

    # misc sub menu
    misc_submenu = tk.Menu(file_menu, tearoff=False)
    file_menu.add_cascade(label="Misc", menu=misc_submenu)
    misc_submenu.add_command(label="Open In Browser", command=lambda: webbrowser.open(
        f"{httpOrHttpsEntry.get()}://{urlEntry.get()}"))

    file_menu.add_separator()
    file_menu.add_command(label='Options', command=optionsWindow)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.destroy)

    # Help Menu
    help_menu = tk.Menu(menu, tearoff=False)
    menu.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label='Check for update', command=checkUpdate)
    help_menu.add_command(label="About", command=about)
    help_menu.config(background="#FFFFFF")

    # MinSize and MaxSize
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    root.maxsize(root.winfo_width(), root.winfo_height())
    root.update()

    # Topmost
    root.attributes("-topmost", True)
    root.attributes("-topmost", False)

    if options['checkForUpdatesOnStartup'] == True:
        checkUpdate()

    # Mainloop
    root.mainloop()
