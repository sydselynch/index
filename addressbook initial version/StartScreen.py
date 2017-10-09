from tkinter import *
from tkinter import ttk
from Window import Window
from AddressBook import AddressBook
import os

def update_booklist():
    booklist = []
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in files:
        if f.endswith(".db"):
            booklist.append(f[0:-3])
    return booklist

class Start():
    def __init__(self, root):
        self.bookList = update_booklist()
        self.root = root
        self.addressBookList = None
        self.file = None
        self.prompt = None
        self.entry = None
        root.title("Address Book")
        root.minsize(width=450, height=250)
        root.maxsize(width=450, height=250)

        self.initializeUI()

    def initializeUI(self):

        #Initialize buttons
        newButton = Button(self.root, text="New", width=20, command=self.newFilePrompt)
        newButton.grid(row=0, column=0, padx=25, pady=(30,10))
        openButton = Button(self.root, text="Open", width=20, command=self.openFile)
        openButton.grid(row=1, column=0, padx=25, pady=10)
        deleteButton = Button(self.root, text="Delete", width=20, command=self.deleteFile)
        deleteButton.grid(row=2, column=0, padx=25, pady=10)

        #List of files
        addressBookListLabel = Label(self.root, text="Address Books")
        addressBookListLabel.grid(row=0, column=1, padx=10, pady=10)
        scrollbar = Scrollbar(self.root, orient=VERTICAL)
        self.addressBookList = Listbox(self.root, yscrollcommand=scrollbar.set, selectmode=SINGLE, width=35)
        scrollbar.config(command=self.addressBookList.yview)
        scrollbar.grid(column=2, row=1, rowspan=2, sticky="NS")
        for i in self.bookList:
            self.addressBookList.insert(END, i)

        self.addressBookList.grid(row=1, column=1, rowspan=2, sticky="NS")

    def newFilePrompt(self):
        self.prompt = Toplevel(self.root)
        fileNameLabel = Label(self.prompt, text="Address Book Name")
        fileNameLabel.grid(row=0, column=0, pady=5, padx=5)
        self.entry = Entry(self.prompt, bd=5)
        self.entry.grid(row=0, column=1, padx=5, pady=5)
        createButton = Button(self.prompt, text="Create", command=self.newFile)
        createButton.grid(row=0, column=2, padx=3, pady=3)

    def newFile(self):
        self.fileName = self.entry.get()
        self.prompt.destroy()
        print(self.fileName)
        if (self.fileName not in self.bookList):
            self.bookList.append(self.fileName)
            AddressBook(self.fileName)
        else:
            #display error
            pass
        self.initializeUI()

    def openFile(self):
        fileIndex = self.addressBookList.curselection()
        print(fileIndex)
        if len(fileIndex) != 0:
            self.root.destroy()
            mainScreen = Window(self.bookList[fileIndex[0]])

    def deleteFile(self):
        fileIndex = self.addressBookList.curselection()
        if len(fileIndex) != 0:
            os.remove("%s.db" % self.bookList[fileIndex[0]])
            self.bookList = update_booklist()
            self.initializeUI()
