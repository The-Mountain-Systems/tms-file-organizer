#!/bin/python3
# Program has been made by The Mountain Systems 2026 Copyright
import shutil,exifread,subprocess
from pathlib import Path
from modules import IntroScreen

def organize_img():
    home = Path.home()
    img_extensions = {".jpg", ".jpeg", ".png", ".gif", ".heic"}

    print("\033[33m[*] Fetching all files in progress...\033[0m")
    images = []
    for item in home.rglob("*"):
        if item.is_file() and item.suffix.lower() in img_extensions:
            images.append(item)
    # Look into metadata -> Date&Time
    print("\033[33m[*] Extracting metadata from Pictures\033[0m")
    if images:
        for img in images:
            with open(img,'rb') as f:
                tags = exifread.process_file(f)
            date_time = tags.get("EXIF DateTimeOriginal")
            if date_time:
                date = str(date_time)[:11]
                print("\033[32m[v] Extracted Date succesfully from Pictures \033[0m")
                # Check if folder for specific date exists
                if Path(f"{home}/Pictures/{date}").is_dir():
                    # Copy img/vid to pictures folder
                    print(f"\033[33m[v] Copying {img} to Pictures\033[0m")
                    shutil.copy(img,f"~/Pictures/{date}")
                    print(f"\033[32m[v] Copied {img} succesfully from Pictures\033[0m")
                else:
                    # Creating the folder
                    print(f"\033[36m[*] Folder {date} doesn't exist... Creating folder...\033[0m")
                    Path(f"~/Pictures/{date}").mkdir()
                    # Copy img/vid to pictures folder
                    print(f"\033[33m[v] Copying {img} to Pictures\033[0m")
                    shutil.copy(img,f"~/Pictures/{date}")
                    print(f"\033[32m[v] Copied {img} succesfully from Pictures\033[0m")
    else:
         print(f"\033[32m[v] There were no images to organize... Going back to main menu\033[0m")
    
            

def organize_docs():
    pass

def organize_dsktp():
    pass

def organize_downloads():
    pass
def main():
    # Intro Screen
    intro = IntroScreen('Linux','1.0')
    choice = ""
    while choice != "Q":
        intro.show_banner()                    
        choice = input("Enter your choice: ")  
        result = intro.options(choice)

        if result == '1':
            organize_img()
        elif result == '2':
            pass
        elif result == '3':
            pass
        elif result == '4':
            pass
        elif result == '5':
            pass