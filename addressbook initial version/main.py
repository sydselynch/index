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

if __name__ == "__main__":
    main()


