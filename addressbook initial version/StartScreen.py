from tkinter import *
from tkinter import ttk
from AddressBook import AddressBook
from AddressBookEntries import AddressBookEntries
from Window import *

class Start():
    def __init__(self, root):
        '''
        Main user interface of start screen when application is opened
        args: root - Tkinter instance
        returns: None
        '''
        self.bookList = AddressBookEntries.GetAllAddressBookEntries()
        self.root = root
        self.addressBookList = None
        self.file = None
        self.prompt = None
        self.entry = None
        root.title("Address Book")
        root.minsize(width=550, height=250)
        root.maxsize(width=550, height=250)

        self.initializeUI()

    def initializeUI(self):
        '''
        Initializes all Tkinter widgets necessary for start screen
        args: None
        returns: None
        '''
        #Initialize buttons
        newButton = Button(self.root, text="New", width=20, command=self.newFilePrompt)
        newButton.grid(row=0, column=0, padx=25, pady=(30,10))
        openButton = Button(self.root, text="Open", width=20, command=self.openFile)
        openButton.grid(row=1, column=0, padx=25, pady=10)
        deleteButton = Button(self.root, text="Delete", width=20, command=self.deletePrompt)
        deleteButton.grid(row=2, column=0, padx=25, pady=10)
        quitButton = Button(self.root, text="Quit", width=20, command=self.root.destroy)
        quitButton.grid(row=3, column=0)

        #List of files
        addressBookListLabel = Label(self.root, text="Address Books")
        addressBookListLabel.grid(row=0, column=1, padx=10, pady=10)
        scrollbar = Scrollbar(self.root, orient=VERTICAL)
        self.addressBookList = Listbox(self.root, yscrollcommand=scrollbar.set, selectmode=SINGLE, width=35)
        scrollbar.config(command=self.addressBookList.yview)
        scrollbar.grid(column=2, row=1, rowspan=3, sticky="NS")
        for i in self.bookList:
            self.addressBookList.insert(END, i.name)

        self.addressBookList.grid(row=1, column=1, rowspan=3, sticky="NS")
        self.addressBookList.columnconfigure(1, weight=1)


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
        if self.fileName not in self.bookList and self.fileName != "":
            self.bookList.append(AddressBook(self.fileName))
            self.prompt.destroy()
        else:
            #display error
            self.invalidNamePrompt()
        self.initializeUI()

    def invalidNamePrompt(self):
        self.prompt = Toplevel(self.root)
        self.prompt.minsize(width=225, height=75)
        self.prompt.maxsize(width=225, height=75)
        errorLabel = Label(self.prompt, text="Please enter a valid filename")
        button = Button(self.prompt, text="OK", command=self.prompt.destroy)
        errorLabel.pack()
        button.pack()

    def openFile(self):
        fileIndex = self.addressBookList.curselection()
        if len(fileIndex) != 0 and self.bookList[fileIndex[0]].name not in openBooks:
            openBooks.append(self.bookList[fileIndex[0]].name)
            mainScreen = Window(self.bookList[fileIndex[0]].name)

    def deleteFile(self):
        self.prompt.destroy()
        if len(self.selection) != 0:
            address = self.bookList[self.selection[0]]
            address.DeleteAddressBook()
            self.bookList = AddressBookEntries.GetAllAddressBookEntries()
        self.initializeUI()
        self.selection = None

    def deletePrompt(self):
        self.selection = self.addressBookList.curselection()
        if (len(self.selection) > 0):
            self.prompt = Toplevel(self.root)
            self.prompt.title(string="Warning")
            self.prompt.minsize(width=225, height=75)
            self.prompt.maxsize(width=225, height=75)
            errorLabel = Label(self.prompt, text="Are you sure?")
            yesButton = Button(self.prompt, text= "      OK      ", command= self.deleteFile)
            noButton = Button(self.prompt, text="      Cancel      ", command= self.prompt.destroy)
            errorLabel.grid(row=0, column=0, columnspan=2, padx=65, pady=5)
            yesButton.grid(row=1, column=0, padx=(30,5), pady=5)
            noButton.grid(row=1, column=1, padx=(5,30), pady=5)
            self.initializeUI()
