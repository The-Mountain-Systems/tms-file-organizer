#!/bin/python3
# Program has been made by The Mountain Systems 2026 Copyright
import shutil,exifread
from pathlib import Path
from modules import IntroScreen

def organize_img():
    home = Path.home()
    img_extensions = {".jpg", ".jpeg", ".png", ".gif", ".heic"}

    images = []
    for item in home.rglob("*"):
        if item.is_file() and item.suffix.lower() in img_extensions:
            images.append(item)
    # Look into metadata -> Date&Time
    for img in images:
        with open(img,'rb') as f:
            tags = exifread.process_file(f)
        date_time = tags.get("EXIF DateTimeOrginial")
        if date_time:
            date = str(date_time)[:11]
        # Check if folder for specific date exists
        if Path(f"~/Pictures/{date}").is_dir():
            # Copy img/vid to pictures folder
            shutil.copy(img,f"~/Pictures/{date}")
        else:
            # Creating the folder
            Path(f"~/Pictures/{date}").mkdir()
            # Copy img/vid to pictures folder
            shutil.copy(img,f"~/Pictures/{date}")
            

def organize_docs():
    pass

def organize_dsktp():
    pass

def organize_downloads():
    pass
def main():
    # Intro Screen
    intro = IntroScreen('Linux','1.0')
    intro.show_banner()                    

    choice = input("Enter your choice: ")  
    result = intro.options(choice)
    