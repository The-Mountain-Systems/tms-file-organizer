#!/bin/python3
import shutil,exifread
from modules import IntroScreen

def organize_img():
    pass

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
    