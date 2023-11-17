import random
import warnings
import base64
import io
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
import shutil
from PIL import Image, ImageTk
# from PyQt5.QtWidgets import QApplication, QMainWindow


#  ___  ___       __   ________  ________
# |\  \|\  \     |\  \|\   __  \|\_____  \
# \ \  \ \  \    \ \  \ \  \|\  \|____|\  \
#  \ \  \ \  \  __\ \  \ \  \\\  \    \ \__\
#   \ \  \ \  \|\__\_\  \ \  \\\  \    \|__|
#    \ \__\ \____________\ \_______\       ___
#     \|__|\|____________|\|_______|      |\__\
#         (t)                             \|__|

# added this to suppress the warning about the image not being the expected size, this is not a problem so dont make my terminal all messy
warnings.filterwarnings('ignore', message='Image was not the expected size')

version = 'v0.3.7rc'
options_ver = 'v1.0.0'
os_name = os.name

icon_data = b'''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'''

img_data = b'''iVBORw0KGgoAAAANSUhEUgAAAQAAAAFACAYAAABTKqIKAAAC8XpUWHRSYXcgcHJvZmlsZSB0eXBlIGV4aWYAAHja7Zdd0usmDIbvWUWXYP0hsRwMZqY76PL7gu30S07OTNPeBsaICC
            yEHoEn6fjrz5H+QCEvmtQ8csl5Q9GihSs6sZ2lrpY2Xe1d6Gqf9EnvLkMKpJwDka+3bj09mdmoomc/DEW7BvbngaKn5HgxdC0k0yNGp1+GymVI+Bygy0A9t7XlEv5zC/txyn5vNM4nzUZ
            82X4Yef2tjuh1g1KYDyHZ0Irw6YDMR5JUdAQtSWDiVFYx1IrevVUE5F2cHqXAozFd1beTnqi09tC+pZheaSlfU+QlyPkh3+oT2XsqK/Q/VtZ4pMmTfpfFGh69RH8+Y/QYa8/YRdWMUOdr
            U/dWVg/zdiwxl44E1/LmeAwmfNWCGsjqBmp9a9uO2qgQA9cgpU6VBh1LNmpwUflI7OgwN5alDHEu3ECPRGelwS5FugQotoVdhR++0Fq2bC2t1QIrd8JUJhgjvPJxTZ++MMbMA6LtCj7SA
            n4xz2DDjUlutpg2T/G4gmorwHd9LZOrgKDNKM8jUhDY/TSxG/1zE8gCPfEa5HlcyPtlACHC0gZnSEAA1EiMMm3O7EQIZABQhessyjsIkBl3OMkqksEGJwlL4xWnNZWNoU7Q4zIDCZMsDj
            ZFKmCpGvLHNZBDFUdPzSybW1ixmiVrtpyz53kpVhfX5ObZ3cOL15DQsMjhEVGiFi6CS9NKLl6ilFIr1qywXPF2xYRad95l193SnnffYy97bUifps1abt6ilVY7d+m4P3ru3qOXXg86kEq
            HHnbkw484ylEHUm1IGjps5OEjRhn1QY2uY/taP6BGFzVepOZEf1CD1v02QfM6sckMwDgpgbhPBEhonsy2IFWe5CazreD6E2M4aZNZp0kMBPUgtkE3u8Qn0Unuf3FLrk/c+L+SSxPdh+R+
            5faOWp+foXUQr1M4g7oJTh/Gj6gcdX7sfpHpdwOfyq+hr6Gvoa+hr6GvoX8pBz5b8//H30mkSjALEF4WAAABhWlDQ1BJQ0MgcHJvZmlsZQAAeJx9kT1Iw1AUhU9TpaIVQTuIOGSoThZEi
            zhKFYtgobQVWnUweekfNGlIUlwcBdeCgz+LVQcXZ10dXAVB8AfE1cVJ0UVKvC8ptIjxwuN9nHfP4b37AKFRYarZNQmommWk4jExm1sVA6/wYxA+RNEnMVNPpBcz8Kyve+qkuovwLO++P6
            tfyZsM8InEc0w3LOIN4plNS+e8TxxiJUkhPieeMOiCxI9cl11+41x0WOCZISOTmicOEYvFDpY7mJUMlThKHFZUjfKFrMsK5y3OaqXGWvfkLwzmtZU012mNIo4lJJCECBk1lFGBhQjtGik
            mUnQe8/CPOP4kuWRylcHIsYAqVEiOH/wPfs/WLExPuUnBGND9YtsfY0BgF2jWbfv72LabJ4D/GbjS2v5qA5j9JL3e1sJHwMA2cHHd1uQ94HIHGH7SJUNyJD8toVAA3s/om3LA0C3Qu+bO
            rXWO0wcgQ7NavgEODoHxImWve7y7p3Nu//a05vcDZjZyok8K6uEAAA5VaVRYdFhNTDpjb20uYWRvYmUueG1wAAAAAAA8P3hwYWNrZXQgYmVnaW49Iu+7vyIgaWQ9Ilc1TTBNcENlaGlIe
            nJlU3pOVGN6a2M5ZCI/Pgo8eDp4bXBtZXRhIHhtbG5zOng9ImFkb2JlOm5zOm1ldGEvIiB4OnhtcHRrPSJYTVAgQ29yZSA0LjQuMC1FeGl2MiI+CiA8cmRmOlJERiB4bWxuczpyZGY9Im
            h0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPgogIDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiCiAgICB4bWxuczp4bXBNTT0iaHR0cDovL25zLmF
            kb2JlLmNvbS94YXAvMS4wL21tLyIKICAgIHhtbG5zOnN0RXZ0PSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VFdmVudCMiCiAgICB4bWxuczpkYz0iaHR0
            cDovL3B1cmwub3JnL2RjL2VsZW1lbnRzLzEuMS8iCiAgICB4bWxuczpHSU1QPSJodHRwOi8vd3d3LmdpbXAub3JnL3htcC8iCiAgICB4bWxuczp0aWZmPSJodHRwOi8vbnMuYWRvYmUuY
            29tL3RpZmYvMS4wLyIKICAgIHhtbG5zOnhtcD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLyIKICAgeG1wTU06RG9jdW1lbnRJRD0iZ2ltcDpkb2NpZDpnaW1wOjc0NzQ3MjA3LT
            IzYzktNGJiYi1hMTU0LTBhMjRiNmJmMzYyYiIKICAgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDo5NTgyNzFhOS01ODYwLTRjYTktYTk0YS0yYTcwNTdiYmM2MTIiCiAgIHhtcE1NOk9
            yaWdpbmFsRG9jdW1lbnRJRD0ieG1wLmRpZDpiMDc3NWUxMy01MDk3LTQ1YzQtOGQwNy03MGY3ZDgwYzc3ZmQiCiAgIGRjOkZvcm1hdD0iaW1hZ2UvcG5nIgogICBHSU1QOkFQST0iMi4w
            IgogICBHSU1QOlBsYXRmb3JtPSJXaW5kb3dzIgogICBHSU1QOlRpbWVTdGFtcD0iMTY3OTEwNDUyNTQ5NjcyMSIKICAgR0lNUDpWZXJzaW9uPSIyLjEwLjMyIgogICB0aWZmOk9yaWVud
            GF0aW9uPSIxIgogICB4bXA6Q3JlYXRvclRvb2w9IkdJTVAgMi4xMCIKICAgeG1wOk1ldGFkYXRhRGF0ZT0iMjAyMzowMzoxOFQwMjo1NToyNSswMTowMCIKICAgeG1wOk1vZGlmeURhdG
            U9IjIwMjM6MDM6MThUMDI6NTU6MjUrMDE6MDAiPgogICA8eG1wTU06SGlzdG9yeT4KICAgIDxyZGY6U2VxPgogICAgIDxyZGY6bGkKICAgICAgc3RFdnQ6YWN0aW9uPSJzYXZlZCIKICA
            gICAgc3RFdnQ6Y2hhbmdlZD0iLyIKICAgICAgc3RFdnQ6aW5zdGFuY2VJRD0ieG1wLmlpZDpmODdmOGVhZi02OTZhLTRjM2MtYWJjZi0wY2MxYTEzYTcyMTQiCiAgICAgIHN0RXZ0OnNv
            ZnR3YXJlQWdlbnQ9IkdpbXAgMi4xMCAoV2luZG93cykiCiAgICAgIHN0RXZ0OndoZW49IjIwMjMtMDMtMThUMDE6NTI6MjciLz4KICAgICA8cmRmOmxpCiAgICAgIHN0RXZ0OmFjdGlvb
            j0ic2F2ZWQiCiAgICAgIHN0RXZ0OmNoYW5nZWQ9Ii8iCiAgICAgIHN0RXZ0Omluc3RhbmNlSUQ9InhtcC5paWQ6NTM2MmU3ZTctMGYyOS00NmQ1LTg3OWQtMWRlMjcwMzI2Y2E5IgogIC
            AgICBzdEV2dDpzb2Z0d2FyZUFnZW50PSJHaW1wIDIuMTAgKFdpbmRvd3MpIgogICAgICBzdEV2dDp3aGVuPSIyMDIzLTAzLTE4VDAyOjU1OjI1Ii8+CiAgICA8L3JkZjpTZXE+CiAgIDw
            veG1wTU06SGlzdG9yeT4KICA8L3JkZjpEZXNjcmlwdGlvbj4KIDwvcmRmOlJERj4KPC94OnhtcG1ldGE+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
            ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgI
            CAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
            AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA
            gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
            ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgI
            CAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
            AgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA
            gICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
            ICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgI
            CAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
            AgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA
            gICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAK
            ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgI
            CAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgIC
            AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICA
            gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAg
            ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgI
            CAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
            AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAKPD94cGF
            ja2V0IGVuZD0idyI/PnJges4AAAAGYktHRAD/AP8A/6C9p5MAAAAJcEhZcwAACxMAAAsTAQCanBgAAAAHdElNRQfnAxIBNxmPiwadAAAKrklEQVR42u3da6xlZ0GA4ffMtZ2xnWmnA0ix
            hdbYixLTArGtVQqmIMQKltBWW1uKGogx0ZhGqUQxirExYhSraWOUCGL6B1QiVWu8IGDinbEwNGo1XKyUNvYyzExnembGH3uNNjAdO3DO3muf/TzJCgmU7u9861vvXmudfdYuAAAAAAAAA
            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'''


class CheckInput:
    def __init__(self, method, url):
        self.method = method
        self.url = url

    def is_valid_method(self):
        return self.method == "http" or self.method == "https"

    def is_valid_url(self):
        return "." in self.url


critDirs = ['./source']
critFiles = [
    f'./source/options-{options_ver}.json', './source/pasteHistory.json']

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
        if files == f'./source/options-{options_ver}.json':
            if os.path.exists(f'./source/options.json'):
                messagebox.showinfo(
                    'Options', 'Outdated options file found\n\nA new one will be created.')
                os.remove(f'./source/options.json')
            else:
                messagebox.showinfo(
                    'Options', 'Options file not found\n\nA new one will be created.')
            with open(files, "w") as f:
                json.dump(
                    {"options": {"saveHistoryOnCheck": 1, "checkForUpdatesOnStartup": 0, "clearLogsWithClearButton": 0, "reloadGUIwith": 0, "devPopUp": 0, "darkMode": "False", "temporaryMode": 0}, "fullHistory": {}}, f, indent=4)
        elif files == './source/pasteHistory.json':
            with open('./source/pasteHistory.json', "w") as f:
                json.dump([], f, indent=4)


options_file = f'./source/options-{options_ver}.json'
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


def checkIfOld():
    # This checks if the old iwoSource folder is there, if yes then it will move the contents to the new source folder
    if os.path.exists("./iwoSource"):
        if os.path.exists("./source"):
            try:
                for file in os.listdir("./iwoSource"):
                    shutil.move(f"./iwoSource/{file}", "./source")
                shutil.rmtree("./iwoSource")
            except:
                if messagebox.askyesno(
                        'Error', f'Error: Could not move "{file}" from old folder to new folder.\n\nPlease check your permissions, and try again or hit yes to delete the file in question.'):
                    os.remove(f"./iwoSource/{file}")
                    shutil.rmtree("./iwoSource")
                else:
                    pass
        else:
            os.rename("./iwoSource", "./source")


def checkUpdate():
    try:
        r = httpx.get(
            'https://api.github.com/repos/jinx420/isThisWebsiteOnline/releases/latest')
        if r.status_code == 200:
            latestVersion = r.json()['tag_name']
            if latestVersion != f'{version}':
                if latestVersion > f'{version}':
                    if messagebox.askyesno('Update', 'There is a new update available. Do you want to download it?'):
                        # This is for downloading the zip file directly, but ideally I want people to read the release notes first
                        # webbrowser.open(f'https://api.github.com/repos/jinx420/isThisWebsiteOnline/zipball/refs/tags/{latestVersion}')
                        webbrowser.open(
                            'https://github.com/jinx420/isThisWebsiteOnline/releases')
                elif latestVersion == f'{version}':
                    messagebox.showinfo(
                        'Update', 'You are using the latest version')
                elif latestVersion < f'{version}':
                    if messagebox.askyesno(
                            'Update', "You are using an unstable Developer version, designated by the 'rc' at the end of the version number.\n\nDo you want to download the latest stable version?"):
                        webbrowser.open(
                            'https://github.com/jinx420/isThisWebsiteOnline/releases')

            else:
                messagebox.showinfo(
                    'Update', 'You are using the latest version')
        else:
            pass
    except ValueError:
        messagebox.showerror(
            'Error', 'Error: Could not check for updates.\n\nPlease check your internet connection and try again.')


def thread(func):
    threading.Thread(target=func).start()


def isWebsiteOnline(url, method):
    try:
        httpx.get(f'{method}: //{url}', timeout=5)
        return True
    except httpx.TimeoutException:
        return False
    except:
        return False


def checkWebsite():
    check = CheckInput(httpOrHttpsEntry.get().lower(), urlEntry.get().lower())

    if check.is_valid_method():
        pass
    else:
        messagebox.showerror(
            "Error", "Please enter a valid method.")
        return

    if check.is_valid_url():
        pass
    else:
        messagebox.showerror("Error", "Please enter a valid url.")
        return

    options = load_options()
    if options['saveHistoryOnCheck'] == 1:
        historyWithDateAndTime()

    method = httpOrHttpsEntry.get().lower()
    url = urlEntry.get().lower()

    if isWebsiteOnline(url, method):
        statusLabel.config(text="Website is online")
    else:
        statusLabel.config(
            text="Website is offline\nor took too long to respond")


def history():
    history = []
    history.append(urlEntry.get())
    history.append(httpOrHttpsEntry.get())
    with open("./source/pasteHistory.json", "w") as f:
        json.dump(history, f)
    statusLabel.config(text="History saved")


def loadHistory():
    with open("./source/pasteHistory.json", "r") as f:
        history = json.load(f)
    urlEntry.delete(0, tk.END)
    httpOrHttpsEntry.delete(0, tk.END)
    urlEntry.insert(0, history[0])
    httpOrHttpsEntry.insert(0, history[1])
    statusLabel.config(text="History loaded")


def clearAllHistory():
    options = load_options()
    saveHistoryOnCheck = options["saveHistoryOnCheck"]
    checkUpdateCM = options["checkForUpdatesOnStartup"]
    clearCM = options["clearLogsWithClearButton"]
    reloadCM = options["reloadGUIwith"]
    devPopUp = options["devPopUp"]
    darkMode = options["darkMode"]
    temporaryMode = options["temporaryMode"]

    with open(f"./source/options-{options_ver}.json", "w") as f:
        json.dump({"options": {"saveHistoryOnCheck": saveHistoryOnCheck, "checkForUpdatesOnStartup": checkUpdateCM, "clearLogsWithClearButton": clearCM,
                  "reloadGUIwith": reloadCM, "devPopUp": devPopUp, "darkMode": darkMode, "temporaryMode": temporaryMode}, "fullHistory": {}}, f, indent=4)

    with open("./source/pasteHistory.json", "w") as f:
        json.dump([], f, indent=4)

    if options['clearLogsWithClearButton'] == 0:
        statusLabel.config(text="All logs deleted")
    elif options['clearLogsWithClearButton'] == 1:
        statusLabel.config(text="Cleared everything")


def status():
    url = urlEntry.get().lower()
    method = httpOrHttpsEntry.get().lower()
    if isWebsiteOnline(url, method):
        return 'online'
    else:
        return 'offline'


def historyWithDateAndTime():
    json_file = f'./source/options-{options_ver}.json'
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


def viewLogs():
    root = tk.Toplevel()
    root.title("Press right click on a row to copy the url and method")
    root.geometry("670x350")
    icon = base64.b64decode(icon_data)
    icon = Image.open(io.BytesIO(icon))
    icon = ImageTk.PhotoImage(icon)
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
    with open(f"./source/options-{options_ver}.json", "r") as f:
        data = json.load(f)
        for i in data["fullHistory"]:
            tree.insert("", tk.END, text="", values=(
                i, data["fullHistory"][i]["url"], data["fullHistory"][i]["httpOrHttps"], data["fullHistory"][i]["status"], data["fullHistory"][i]["dateAndTime"]))
    tree.pack()


def optionsWindow():
    def saveOptions():
        with open(f'./source/options-{options_ver}.json', 'r') as f:
            devVar = json.load(f)

        devPopUpVar = devVar['options']['devPopUp']

        options = {
            "options": {
                "saveHistoryOnCheck": saveHistoryOnCheck.get(),
                "checkForUpdatesOnStartup": checkUpdateCM.get(),
                "clearLogsWithClearButton": clearCM.get(),
                "reloadGUIwith": reloadGUIwith.get(),
                "devPopUp": devPopUpVar,
                "darkMode": str(switch_value),
                "temporaryMode": temporaryMode.get()
            },
            "fullHistory": {}
        }
        with open(f"./source/options-{options_ver}.json", "w") as f:
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
                "devPopUp": 0,
                "darkMode": "False",
                "temporaryMode": 0
            },
            "fullHistory": {}
        }

        with open(f"./source/options-{options_ver}.json", "w") as f:
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
        temporaryMode.set(options["temporaryMode"])

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
                "devPopUp": 0,
                "darkMode": str(switch_value),
                "temporaryMode": temporaryMode.get()
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
                    "devPopUp": 1,
                    "darkMode": str(switch_value),
                    "temporaryMode": temporaryMode.get()
                },
                "fullHistory": {}
            }
            with open(f"./source/options-{options_ver}.json", "w") as f:
                json.dump(options, f, indent=4)
        elif data['devPopUp'] == 1:
            pass

    # get the value of the check mark box
    saveHistoryOnCheck = tk.IntVar()  # 0 = off, 1 = on
    checkUpdateCM = tk.IntVar()  # 0 = off, 1 = on
    clearCM = tk.IntVar()  # 0 = off, 1 = on
    reloadGUIwith = tk.IntVar()  # 0 = reload with .exe, 1 = reload with .py
    temporaryMode = tk.IntVar()  # 0 = off, 1 = on

    # get the options from the options.json file
    data = load_options()
    saveHistoryOnCheck.set(data["saveHistoryOnCheck"])
    checkUpdateCM.set(data["checkForUpdatesOnStartup"])
    clearCM.set(data["clearLogsWithClearButton"])
    reloadGUIwith.set(data["reloadGUIwith"])
    temporaryMode.set(data["temporaryMode"])

    # options window
    optionsWindow = tk.Toplevel()
    optionsWindow.title("Options")
    optionsWindow.geometry("400x200")
    icon = base64.b64decode(icon_data)
    icon = Image.open(io.BytesIO(icon))
    icon = ImageTk.PhotoImage(icon)
    optionsWindow.resizable(False, False)

    checkMarkBox1 = tk.Checkbutton(optionsWindow, text="Save history on every check",
                                   variable=saveHistoryOnCheck, onvalue=1, offvalue=0, command=saveHistoryOnCheck)
    checkMarkBox1.place(x=10, y=10)

    checkUpdateCMBox = tk.Checkbutton(optionsWindow, text="Check for updates on startup",
                                      variable=checkUpdateCM, onvalue=1, offvalue=0, command=checkUpdateCM)
    checkUpdateCMBox.place(x=10, y=40)

    clearCMBox = tk.Checkbutton(
        optionsWindow, text="Clear the logs with the clear button", variable=clearCM, onvalue=1, offvalue=0)
    clearCMBox.place(x=10, y=70)

    reloadGUIBox = tk.Checkbutton(optionsWindow, text="Reload GUI with .exe or .py",
                                  variable=reloadGUIwith, onvalue=1, offvalue=0, command=lambda: devPopUp())
    reloadGUIBox.place(x=10, y=100)
    reloadExplanation = tk.Label(optionsWindow, text='(no checkmark = .exe | checkmark = .py)',
                                 padx=0, pady=0)
    reloadExplanation.place(x=30, y=120)

    temporaryModeBox = tk.Checkbutton(optionsWindow, text="Don't save Files",
                                      variable=temporaryMode, onvalue=1, offvalue=0)
    temporaryModeBox.place(x=10, y=140)

    saveButton = tk.Button(optionsWindow, text="Save", command=saveOptions)
    saveButton.place(x=10, y=170)

    resetButton = tk.Button(optionsWindow, text="Reset", command=resetOptions)
    resetButton.place(x=80, y=170)

    importButton = tk.Button(
        optionsWindow, text="Import", command=importOptions)
    importButton.place(x=150, y=170)

    exportButton = tk.Button(
        optionsWindow, text="Export", command=exportOptions, fg="black")
    exportButton.place(x=220, y=170)

    savedText = tk.Label(optionsWindow, text="", padx=0, pady=0)
    savedText.place(x=300, y=172)

    optionsWindow.protocol("WM_DELETE_WINDOW", lambda: exit_options())

    def exit_options():
        saveOptions()
        optionsWindow.destroy()
        root.deiconify()


def graph():
    with open(f"./source/options-{options_ver}.json", "r") as f:
        data = json.load(f)
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
        icon = base64.b64decode(icon_data)
        icon = Image.open(io.BytesIO(icon))
        icon = ImageTk.PhotoImage(icon)
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
    icon = base64.b64decode(icon_data)
    icon = Image.open(io.BytesIO(icon))
    icon = ImageTk.PhotoImage(icon)
    aboutWindow.resizable(False, False)

    aboutText = tk.Label(aboutWindow, text="A simple program to check if a website is online or not.\n"
                         "\n   A list of all the features can be found in the README.md, and on the github page."
                         "\n\nIf you have any suggestions or find any bugs,\nplease report them via the issues tab on the github page.",
                         padx=0, pady=0)
    aboutText.place(x=0, y=0)

    githubButton = tk.Button(aboutWindow, text="Github Issues", command=lambda: webbrowser.open(
        "https://github.com/jinx420/isThisWebsiteOnline/issues"))
    githubButton.place(x=230, y=125)

    githubButton = tk.Button(aboutWindow, text="Github Page", command=lambda: webbrowser.open(
        "https://github.com/jinx420/isThisWebsiteOnline"))
    githubButton.place(x=150, y=125)

    # idk why this is still here, but it is
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


def prediction():
    # predict what the outcome will be and display it in a messagebox
    # this is a very simple prediction, and is not always correct
    # i would like to use PyTorch to make a better prediction but that would make the .exe like at least a gigabyte.
    # i might make a seperate version that uses PyTorch, but for now this will do.
    url = urlEntry.get()
    httpOrHttps = httpOrHttpsEntry.get()

    check = CheckInput(httpOrHttps, url)

    if check.is_valid_method():
        pass
    else:
        messagebox.showerror("Error", "Please enter a valid method.")
        return

    if check.is_valid_url():
        pass
    else:
        messagebox.showerror("Error", "Please enter a valid url.")
        return

    online = 0
    offline = 0
    with open(f"./source/options-{options_ver}.json", "r") as f:
        data = json.load(f)
    for i in data["fullHistory"]:
        if data["fullHistory"][i]["url"] == url and data["fullHistory"][i]["httpOrHttps"] == httpOrHttps:
            if data["fullHistory"][i]["status"] == "online":
                online += 1
            elif data["fullHistory"][i]["status"] == "offline":
                offline += 1

    # if it has been online more, it will predict that it will be online, add a 0.5% random chance of it being offline
    if online > offline:
        prediction = "online"
        randomNum = random.randint(0, 200)
        if randomNum == 0:
            prediction = "offline"

    # if it has been offline more, it will predict that it will be offline, add a 0.5% random chance of it being online
    elif offline > online:
        prediction = "offline"
        randomNum = random.randint(0, 200)
        if randomNum == 0:
            prediction = "online"

    # if it has been online and offline the same amount of times, it will be a random outcome
    elif online == offline:
        prediction = random.choice(["online", "offline"])

    # display prediction
    messagebox.showinfo(
        "Prediction", f"The prediction for {httpOrHttps}: //{url} is: \n\n {httpOrHttps}: //{url} should be {prediction}.")
    # print(f"Prediction: {prediction}")


# main
if __name__ == "__main__":
    # removed due to it causing problems if you use a venv for this project
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

    checkIfOld()
    options = load_options()

    root = tk.Tk()
    root.title(
        "IsThisWebsiteOnline?                                                                                  Made with 💜 by jinx")
    root.geometry("670x335")
    if os.name != "nt":
        root.geometry("710x340")

    root.resizable(False, False)
    icon = base64.b64decode(icon_data)
    img = ImageTk.PhotoImage(Image.open(io.BytesIO(icon)))
    root.iconphoto(True, img)

    def reloadGUI():
        options = load_options()
        root.destroy()
        if options['reloadGUIwith'] == 1 and os.name != "nt":
            subprocess.call(
                ["python3", "isThisWebsiteOnline.py", "gui"])
        elif options['reloadGUIwith'] == 1 and os.name == "nt":
            subprocess.call(
                ["python", "isThisWebsiteOnline.py", "gui"])
        elif options['reloadGUIwith'] == 0 and os.name == "nt":
            subprocess.call([".\isThisWebsiteOnline.exe"])
        elif options['reloadGUIwith'] == 0 and os.name != "nt":
            messagebox.showerror(
                "Error", "This feature is only available on Windows. Please use the .py file instead.")

    def regenerateOptions():
        with open(f"./source/options-{options_ver}.json", "w") as f:
            json.dump(
                {"options": {"saveHistoryOnCheck": 1, "checkForUpdatesOnStartup": 0, "clearLogsWithClearButton": 0, "reloadGUIwith": 0, "devPopUp": 0, "darkMode": "False", "temporaryMode": 1}, "fullHistory": {}}, f, indent=4)

        statusLabel.config(text="options.json regenerated!")

    reloadGUIButton = ttk.Button(
        root, text="Reload GUI", command=reloadGUI)
    reloadGUIButton.place(x=10, y=300)

    regenerateOptionsButton = ttk.Button(
        root, text="Regenerate options.json", command=regenerateOptions)
    regenerateOptionsButton.place(x=120, y=300)

    # image
    img_decoded = base64.b64decode(img_data)
    image = ImageTk.PhotoImage(Image.open(io.BytesIO(img_decoded)))
    imageLabel = ttk.Label(root, image=image)
    imageLabel.place(x=390, y=0)
    if os.name != "nt":
        imageLabel.place(x=440, y=0)

    httpOrHttpsLabel = ttk.Label(
        root, text="Is the website using http or https? : ")
    httpOrHttpsLabel.place(x=10, y=23)

    httpOrHttpsEntry = ttk.Entry(root)
    httpOrHttpsEntry.place(x=220, y=20)
    httpOrHttpsEntry.config(width=23)
    if os.name != "nt":
        httpOrHttpsEntry.config(width=19)

    urlLabel = ttk.Label(root, text="Enter the url: ")
    urlLabel.place(x=10, y=57)

    urlEntry = ttk.Entry(root)
    urlEntry.place(x=220, y=54)
    urlEntry.config(width=23)
    if os.name != "nt":
        urlEntry.config(width=19)

    checkButton = ttk.Button(
        root, text="Check", command=lambda: statusLabel.config(text='Checking...') or thread(checkWebsite))
    checkButton.place(x=10, y=100)

    statusLabel = ttk.Label(root, text="Waiting...")
    statusLabel.place(x=235, y=102)

    clearButton = ttk.Button(root, text="Clear", command=clear)
    clearButton.place(x=120, y=100)

    viewLogsButton = ttk.Button(
        root, text="View logs", command=viewLogs)
    viewLogsButton.place(x=10, y=150)

    graphButton = ttk.Button(
        root, text="Graph", command=lambda: thread(graph))
    graphButton.place(x=120, y=150)

    predictionButton = ttk.Button(
        root, text="Prediction", command=lambda: thread(prediction))
    predictionButton.place(x=10, y=200)

    # version
    versionLabel = tk.Label(root, text=f"Version: {version}")
    versionLabel.place(x=575, y=311)
    if os.name != "nt":
        versionLabel.place(x=586, y=311)

    # smol easteregg, dont cheat and look at the source code >:(
    # if you do, I will eat your cookies :D
    eastereggLabel = tk.Label(root, text=" ")
    eastereggLabel.place(x=50, y=5)

    eastereggLabel.bind(
        "<Button-1>", lambda e: eastereggLabel.config(text="You found me!") or easteregg2Label.place(x=95, y=57))

    easteregg2Label = tk.Label(root, text=" ")

    easteregg2Label.bind(
        "<Button-1>", lambda e: easteregg2Label.config(text="You found me again!") or easteregg3Label.place(x=400, y=3))

    easteregg3Label = tk.Label(root, text=" ")

    easteregg3Label.bind(
        "<Button-1>", lambda e: easteregg3Label.config(text="This is the last one, I promise!") or disappearEastereggsButton.place(x=74, y=100))

    easteregg4Label = tk.Label(root, text="Click me!")

    easteregg4Label.bind(
        "<Button-1>", lambda e: easteregg4Label.config(text="Or is it?") or b64_window())

    def disappearEastereggs():
        eastereggLabel.place_forget()
        easteregg2Label.place_forget()
        easteregg3Label.place_forget()
        disappearEastereggsButton.place_forget()

        easteregg4Label.place(x=119, y=129)

    def b64_window():
        window = tk.Toplevel(root)
        window.title("???")
        window.geometry("200x200")
        window.resizable(False, False)
        icon = base64.b64decode(icon_data)
        img = ImageTk.PhotoImage(Image.open(io.BytesIO(icon)))
        window.iconphoto(True, img)

        easteregg4Label.place_forget()

        text = tk.Text(window, width=200, height=150)
        text.pack()

        text.insert(
            tk.END, "d2hhdCBkb2VzIHRoaXMgbWVhbj8=\n\n\n\n Copy this text")

        text.config(state=tk.DISABLED)

        def on_closing():
            urlEntry.insert(tk.END, "Help I don't speak spanish")
            httpOrHttpsEntry.insert(tk.END, "Привет, мой друг!")
            root.title(
                "What is happening?                                                                                     Made with 💔 by jinx")

            style.theme_use('simplex')
            versionLabel.config(text='Version: v6.6.6')

            window.destroy()

        window.protocol("WM_DELETE_WINDOW", on_closing)

    disappearEastereggsButton = ttk.Button(
        root, text="???", command=disappearEastereggs)

    nerdEggLabel = tk.Label(root, text=" ")
    nerdEggLabel.place(x=105, y=330)

    nerdEggLabel.bind(
        "<Button-1>", lambda e: nerdEggLabel.place(x=310, y=150) or nerdEggLabel.config(text="🤓") or changeButName())

    # idk why I did this, pls send help
    def changeButName():
        checkButton.config(text="ChEcK")
        clearButton.config(text="ClEaR")
        viewLogsButton.config(text="ViEw LoGs")
        graphButton.config(text="GrApH")
        root.title(
            "WhAt Is HaPpEnInG?                                                                                 MaDe WiTh 🤓 By JiNx")
        versionLabel.config(text="VeRsIoN: v69.420")
        statusLabel.config(text="WaItInG...")
        urlLabel.config(text="UrL:")
        httpOrHttpsLabel.config(text="hTtPs:")

        regenerateOptionsButton.config(text="ReGeNeRaTe OpTiOnS")
        reloadGUIButton.config(text="ReLoAd GuI")
        predictionButton.config(text="PrEdIcTiOn")

        menu.entryconfigure("File", label="FiLe")
        menu.entryconfigure('Help', label='HeLp')
        file_menu.entryconfigure("Exit", label="ExIt")
        file_menu.entryconfigure('Options', label='OpTiOnS')
        file_menu.entryconfigure('Themes', label='ThEmEs')
        file_menu.entryconfigure('Misc', label='MiSc')
        file_menu.entryconfigure('History', label='HiStOrY')
        help_menu.entryconfigure('About', label='AbOuT')
        help_menu.entryconfigure(
            'Check for update', label='ChEcK fOr UpDaTe')

        # history_submenu.entryconfigure('Save history', label='SaVe hIsToRy')
        # history_submenu.entryconfigure('View history', label='ViEw HiStOrY')
        # history_submenu.entryconfigure('View Logs', label='ViEw LoGs')
        # history_submenu.entryconfigure('Clear Logs', label='ClEaR lOgS')

        themes_menu.entryconfigure('Darkly', label='DaRkLy')
        themes_menu.entryconfigure('Pulse', label='PuLsE')
        themes_menu.entryconfigure('Vapor', label='VaPoR')
        themes_menu.entryconfigure('Solar', label='SoLaR')
        themes_menu.entryconfigure('Simplex', label='SiMpLeX')

        # misc_submenu.entryconfigure('Open in browser', label='OpEn In BrOwSeR')

        def neverGonnaCloseYou():
            rickWindow()

        def rickWindow():
            window = tk.Toplevel(root)
            window.title("Never gonna close you")
            window.geometry("250x200")
            window.resizable(False, False)
            icon = base64.b64decode(icon_data)
            img = ImageTk.PhotoImage(Image.open(io.BytesIO(icon)))
            window.iconphoto(True, img)

            text = tk.Text(window, width=200, height=150)
            text.pack()

            text.insert(
                tk.END, "Never gonna let you down\n\nNever gonna run around and desert you\n\nNever gonna make you cry\n\nNever gonna say goodbye\n\nNever gonna tell a lie and hurt you")

            text.config(state=tk.DISABLED)

            def on_closing():
                neverGonnaCloseYou()

            window.protocol("WM_DELETE_WINDOW", on_closing)
            root.protocol("WM_DELETE_WINDOW", on_closeing2)
            file_menu.entryconfigure(
                "ExIt", label="ExIt", command=lambda: on_closeing2())

        def on_closeing2():
            root.destroy()
            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

        neverGonnaCloseYou()

    # Menu
    menu = tk.Menu(root, tearoff=False)
    root.config(menu=menu)

    style = Style(theme='darkly')

    def toggle():
        global switch_value
        if switch_value:
            switch.config(text='Light Mode')
            style.theme_use('darkly')
            switch_value = False
        else:
            switch.config(text='Dark Mode')
            style.theme_use('pulse')
            switch_value = True

    # dark mode and flashbang mode (aka light mode) button
    switch = ttk.Button(root, text="Light Mode", command=lambda: toggle())
    switch.place(x=230, y=150)

    if load_options()['darkMode'] == "True":
        switch_value = True
        style.theme_use('pulse')
        switch.config(text='Dark Mode')
    elif load_options()['darkMode'] == "False":
        switch_value = False
        style.theme_use('darkly')
        switch.config(text='Light Mode')

    # File Menu
    file_menu = tk.Menu(menu, tearoff=False)
    menu.add_cascade(label="File", menu=file_menu)
    menu.config(background="#222222", foreground="#FFFFFF")
    file_menu.config(background="#222222", foreground="#FFFFFF")

    # history sub menu
    history_submenu = tk.Menu(file_menu, tearoff=False)
    history_submenu.config(background="#222222", foreground="#FFFFFF")
    file_menu.add_cascade(label="History", menu=history_submenu)
    history_submenu.add_command(label='Save History',
                                command=lambda: thread(history))
    history_submenu.add_command(label='Load History',
                                command=lambda: thread(loadHistory))
    history_submenu.add_command(label="View logs", command=viewLogs)
    history_submenu.add_command(
        label="Clear logs", command=clearAllHistory)

    # themes sub menu
    themes_menu = tk.Menu(file_menu, tearoff=False)
    file_menu.add_cascade(label='Themes', menu=themes_menu)
    themes_menu.add_command(
        label='Darkly', command=lambda: style.theme_use('darkly'))
    themes_menu.add_command(
        label='Pulse', command=lambda: style.theme_use('pulse'))
    themes_menu.add_command(
        label='Vapor', command=lambda: style.theme_use('vapor'))
    themes_menu.add_command(
        label='Solar', command=lambda: style.theme_use('solar'))
    themes_menu.add_command(
        label='Simplex', command=lambda: style.theme_use('simplex'))

    # misc sub menu
    misc_submenu = tk.Menu(file_menu, tearoff=False)
    misc_submenu.config(background="#222222", foreground="#FFFFFF")
    file_menu.add_cascade(label="Misc", menu=misc_submenu)
    misc_submenu.add_command(label="Open In Browser", command=lambda: webbrowser.open(
        f"{httpOrHttpsEntry.get()}: //{urlEntry.get()}"))

    file_menu.add_separator()
    file_menu.add_command(label='Options', command=optionsWindow)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.destroy)

    # Help Menu
    help_menu = tk.Menu(menu, tearoff=False)
    menu.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label='Check for update', command=checkUpdate)
    help_menu.add_command(label="About", command=about)
    help_menu.config(background="#222222", foreground="#FFFFFF")

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

    def temp():
        shutil.rmtree("source")
        root.destroy()

    def on_closing():
        try:
            options = load_options()
            if options['temporaryMode'] == True:
                temp()
            else:
                root.destroy()
        except:
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    # Mainloop
    root.mainloop()
