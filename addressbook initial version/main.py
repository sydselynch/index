from AddressBook import AddressBook
from tkinter import *
import StartScreen
import Window
import os

def main():
    root = Tk()
    startScreen = StartScreen.Start(root)
    root.mainloop()

if __name__ == "__main__":
    main()