#!/bin/python3
import shutil
from modules import IntroScreen

def main():
    # Intro Screen
    intro = IntroScreen('Linux','1.0')
    intro.show_banner()                    

    choice = input("Enter your choice: ")  
    result = intro.options(choice)

    print(result) 
    