from tkinter import *
from tkinter import ttk
from AddressBook import AddressBook
from AddressBookEntries import AddressBookEntries
from Window import *

windowList = []

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
        self.openWindows = {}
        root.title("In[]Dex")
        root.minsize(width=650, height=270)
        root.maxsize(width=650, height=270)

        self.InitializeUI()

    def InitializeUI(self):
        '''
        Initializes all Tkinter widgets necessary for start screen
        args: None
        returns: None
        '''
        image = PhotoImage(file="Logo.gif")
        label = Label(self.root, image=image, height=100, width=210)
        label.image = image
        label.grid(row=0, column=0,sticky="NW")
        self.root.iconbitmap('icon.ico')
        #icon = PhotoImage(file="icon.ico")
        #self.root.tk.call('wm','iconphoto',self.root._w,icon)

        #Initialize buttons
        newButton = Button(self.root, text="New", width=20, command=self.NewFilePrompt)
        newButton.grid(row=1, column=0, padx=25, pady=(10,0))
        openButton = Button(self.root, text="Open", width=20, command=self.OpenFile)
        openButton.grid(row=2, column=0, padx=25, pady=(10,0))
        deleteButton = Button(self.root, text="Delete", width=20, command=self.DeletePrompt)
        deleteButton.grid(row=3, column=0, padx=25, pady=(10,0))
        quitButton = Button(self.root, text="Quit", width=20, command=self.QuitAllWindows)
        quitButton.grid(row=4, column=0, pady=(10,10))

        #List of files
        addressBookListLabel = Label(self.root, text="Available Address Books", font=('TkHeadingFont', 13))
        addressBookListLabel.grid(row=4, column=1)
        scrollbar = Scrollbar(self.root, orient=VERTICAL)
        self.addressBookList = Listbox(self.root, yscrollcommand=scrollbar.set, selectmode=SINGLE, width=55, height=10, font=('TkHeadingFont'))
        scrollbar.config(command=self.addressBookList.yview)
        scrollbar.grid(column=2, row=0, rowspan=4, sticky="NSE", pady=10, padx=(0,50))
        for i in self.bookList:
            self.addressBookList.insert(END, i.name)

        self.addressBookList.grid(row=0, column=1, rowspan=4, sticky="NSEW", pady=10, padx=(0,0))
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.root.rowconfigure(3, weight=1)
        self.root.rowconfigure(4, weight=1)


    def NewFilePrompt(self):
        '''
        Prompt that displays when user presses the new button,
        allows user to enter an address book name
        '''
        self.prompt = Toplevel(self.root)
        fileNameLabel = Label(self.prompt, text="Address Book Name")
        fileNameLabel.grid(row=0, column=0, pady=5, padx=5)
        self.entry = Entry(self.prompt, bd=5)
        self.entry.grid(row=0, column=1, padx=5, pady=5)
        createButton = Button(self.prompt, text="Create", command=self.NewFile)
        createButton.grid(row=0, column=2, padx=3, pady=3)

    def NewFile(self):
        '''
        Creates a new address book and .db file based
        on given address book name, displays an error
        if the name is empty or the book already exists
        '''
        self.fileName = self.entry.get()
        if self.fileName not in self.bookList and self.fileName != "":
            self.bookList.append(AddressBook(self.fileName))
            self.prompt.destroy()
        else:
            self.InvalidNamePrompt()
        self.InitializeUI()

    def InvalidNamePrompt(self):
        '''
        Prompt that displays error when user
        provides invalid address book name
        '''
        self.prompt = Toplevel(self.root)
        self.prompt.minsize(width=225, height=75)
        self.prompt.maxsize(width=225, height=75)
        errorLabel = Label(self.prompt, text="Please enter a valid filename")
        button = Button(self.prompt, text="     OK     ", command=self.prompt.destroy)
        errorLabel.pack()
        button.pack()

    def OpenFile(self):
        '''
        Opens the address book that the user has
        selected from the list of address books as
        long as it is not already open
        '''
        fileIndex = self.addressBookList.curselection()
        if len(fileIndex) != 0 and self.bookList[fileIndex[0]].name not in openBooks:
            openBooks.append(self.bookList[fileIndex[0]].name)
            Window(self.bookList[fileIndex[0]].name, self)

    def AddWindow(self, window):
        '''
        Adds a window to the windows attribute list if a new one is created
        '''
        self.openWindows[window.bookName] = window

    def RemoveWindow(self, window):
        '''
        Removes a window from the attribute list if the window is closed
        '''
        self.openWindows.pop(window.bookName, None)

    def QuitAllWindows(self):
        '''
        Quits all of the opened child windows and the root window
        '''
        if len(self.openWindows) != 0:
            for i in self.openWindows:
                self.openWindows[i].root.destroy()
        self.root.destroy()

    def DeleteFile(self):
        '''
        Deletes an existing address book from the list,
        will display a warning prior to deletion
        '''
        self.prompt.destroy()
        if len(self.selection) != 0:
            address = self.bookList[self.selection[0]]
            # close window if database is deleted
            self.openWindows[address.name].root.destroy()
            address.DeleteAddressBook()
            self.bookList = AddressBookEntries.GetAllAddressBookEntries()
        self.InitializeUI()
        self.selection = None

    def DeletePrompt(self):
        '''
        Warning prompt that requires confirmation from the
        user before deleting an address book
        '''
        self.selection = self.addressBookList.curselection()
        if (len(self.selection) > 0):
            self.prompt = Toplevel(self.root)
            self.prompt.title(string="Warning")
            self.prompt.minsize(width=225, height=75)
            self.prompt.maxsize(width=225, height=75)
            errorLabel = Label(self.prompt, text="Are you sure?")
            yesButton = Button(self.prompt, text= "      OK      ", command= self.DeleteFile)
            noButton = Button(self.prompt, text="      Cancel      ", command= self.prompt.destroy)
            errorLabel.grid(row=0, column=0, columnspan=2, padx=65, pady=5)
            yesButton.grid(row=1, column=0, padx=(30,5), pady=5)
            noButton.grid(row=1, column=1, padx=(5,30), pady=5)
            self.InitializeUI()

    def OnClosing(self):
        # print(windowList)
        # for window in windowList:
        #     window.root.destroy()
        self.root.destroy()
