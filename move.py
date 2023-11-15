import sys
import os
import shutil

cwd = os.getcwd()

if os.path.exists(f"{cwd}\\dist\\isThisWebsiteOnline.exe"):
    if os.path.exists(f"{cwd}\\isThisWebsiteOnline.exe"):
        os.remove(f"{cwd}\\isThisWebsiteOnline.exe")
        print("Deleted old .\\isThisWebsiteOnline.exe")
    else:
        print("No .\\isThisWebsiteOnline.exe found")
    shutil.move(f"{cwd}\\dist\\isThisWebsiteOnline.exe",
                f"{cwd}\\isThisWebsiteOnline.exe")
    os.remove(f"{cwd}\\isThisWebsiteOnline.spec")
    try:
        shutil.rmtree(f"{cwd}\\dist")
        shutil.rmtree(f"{cwd}\\build")
    except ValueError:
        print(f"Error while deleting files {ValueError}")
        sys.exit(0)
else:
    print("No .\\dist\\isThisWebsiteOnline.exe found")
    shutil.rmtree(f"{cwd}\\dist")
    shutil.rmtree(f"{cwd}\\build")
    os.remove(f"{cwd}\\isThisWebsiteOnline.spec")
    sys.exit(0)
