from AddressBook import AddressBook
from tkinter import *
import StartScreen
import Window
import os
import unittest
import sys

def main():
    '''
    Initializes the Start class, which displays the user interface.
    The user interface it is updated continuously in an infinite loop initiated by this method.
    '''
    root = Tk()
    startScreen = StartScreen.Start(root)
    root.mainloop()

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

if __name__ == "__main__":
    main()
