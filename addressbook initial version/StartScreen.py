from tkinter import *
from tkinter import ttk, messagebox
from AddressBook import AddressBook
from AddressBookEntries import AddressBookEntries
from Window import *

windowList = []

class Start():
    def __init__(self, root):
        '''
        Main user interface of start screen when application is opened
        Sets the attribute bookList by calling the method GetAllAddressBookEntries() from the AddressBookEntries class
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
        self.root.title("In[]Dex")
        self.root.minsize(width=650, height=270)
        self.root.maxsize(width=650, height=270)

        self.InitializeUI()

    def InitializeUI(self):
        '''
        Initializes all Tkinter widgets necessary for start screen ands displays
        all of the Addressbooks in the User Interface using the attribute bookList

        args: None
        returns: None
        '''

        # Use a different image if the sys platform is a Mac
        if sys.platform == 'darwin':
            image = PhotoImage(file="LogoMac.gif")
            #self.root.iconbitmap('icon.icns')
        else:
            image = PhotoImage(file="Logo.gif")
            self.root.iconbitmap('icon.ico')
        label = Label(self.root, image=image, height=100, width=210)
        label.image = image
        label.grid(row=0, column=0,sticky="NW")
        #icon = PhotoImage(file="icon.ico")
        #self.root.tk.call('wm','iconphoto',self.root._w,icon)

        # Dropdown menu items
        menu = Menu(self.root)
        self.root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New", command= self.NewFilePrompt)
        filemenu.add_command(label="Open...", command=self.OpenFileinMenu)
        filemenu.add_command(label="Import", command=self.ImportPrompt)
        filemenu.add_command(label="Export", command=self.ExportPrompt)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.QuitAllWindows)

        #Initialize buttons
        newButton = Button(self.root, text="New", width=20, command=self.NewFilePrompt)
        newButton.grid(row=1, column=0, padx=25, pady=(10,0))
        openButton = Button(self.root, text="Open", width=20, command=self.OpenFile)
        openButton.grid(row=2, column=0, padx=25, pady=(10,0))
        deleteButton = Button(self.root, text="Delete", width=20, command=self.DeletePrompt)
        deleteButton.grid(row=3, column=0, padx=25, pady=(10,0))
        quitButton = Button(self.root, text="Quit", width=20, command=self.QuitAllWindows)
        quitButton.grid(row=4, column=0, padx=25, pady=(10,10))

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

    def UpdateBookList(self):
        self.addressBookList.delete(0, END)
        for book in self.bookList:
            self.addressBookList.insert(END, book)

    def NewFilePrompt(self):
        '''
        Create a new window prompt that displays when user presses the new button,
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
        on given address book name, displays an error by calling InvalidNamePrompt()
        if the name is empty or the book already exists
        '''
        books = []
        self.fileName = self.entry.get()
        if self.fileName != "":
            for book in self.bookList:
                books.append(book.name)
            if self.fileName not in books:
                newBook = AddressBook(self.fileName)
                self.bookList.append(newBook)
                self.prompt.destroy()
            else:
                self.InvalidNamePrompt()
        else:
            self.InvalidNamePrompt()
        self.InitializeUI()

    def InvalidNamePrompt(self):
        '''
        Prompt that displays error when user
        provides invalid address book name
        '''
        self.prompt.destroy()
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

    def OpenFileinMenu(self):
        '''
        Opens an address book from an existing address book,
        must be of type .db
        '''
        self.root.filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("DB files","*.db"),("all files","*.*")))
        self.root.filename = self.root.filename.split(".")[0]
        self.root.filename = self.root.filename.split("/")[-1]
        if self.root.filename != "" and self.root.filename not in openBooks:
            openBooks.append(self.root.filename)
            Window(self.root.filename, self)

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
            try:
                self.openWindows[address.name].root.destroy()
            except:
                pass
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

    def ImportPrompt(self):
        '''
        Import a outside txt file into a dababase address book
        '''

        self.root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                        filetypes=(("DB files", "*.db"), ("TXT files", "*.txt"),
                                                                   ("all files", "*.*")))

        fileNameSplit = self.root.filename.strip().split("/")
        files = fileNameSplit[-1].strip().split(".");

        if (files[1] == "txt"):
            file = open(self.root.filename, "r")
            if fileNameSplit != "":
                try:
                    fmt = file.readline()
                    txtfmt = "id\tfirst_name\tlast_name\taddress\tcity\tstate\tzip_code\tphone_number\temail\n"
                    if fmt != txtfmt:
                        raise EXCEPTION
                    else:
                        name = files[0]
                        addressbook = AddressBook(name)
                        self.bookList.append(addressbook)
                        for line in file:
                            line = line.strip() + "\t" * 8  # in case some entries are empty
                            line = line.split("\t")
                            id = line[0]
                            firstname = line[1]
                            lastname = line[2]
                            address = line[3]
                            city = line[4]
                            state = line[5]
                            zip_code = line[6]
                            phone = line[7]
                            email = line[8]
                            contact = Contact(firstname, lastname, address, city, state, zip_code, phone, email)
                            addressbook.AddContact(contact)
                        addressbook.close()
                        self.InitializeUI()
                except:
                    self.InvalidImportPrompt()
        elif(files[1] == "db"):
            pass

    def ExportPrompt(self):
        '''
        Export selected address book to other directory as a txt file

        '''

        fileIndex = self.addressBookList.curselection()
        if len(fileIndex) != 0 :
            addressbook = AddressBook(self.bookList[fileIndex[0]].name)
            self.filename = filedialog.asksaveasfilename(initialdir="/", title="Select file",
                                                         filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
            f = open("%s.txt" % self.filename, "w")
            f.write("id\tfirst_name\tlast_name\taddress\tcity\tstate\tzip_code\tphone_number\temail\n")
            for row in addressbook.GetAllContacts():
                f.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n"%(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]))
            f.close()
            self.prompt = Toplevel(self.root)
            self.prompt.title(string="Warning")
            self.prompt.minsize(width=200, height=75)
            self.prompt.maxsize(width=200, height=75)
            textLabel = Label(self.prompt, text="Export has been successful!")
            congratButton = Button(self.prompt, text="      OK      ", command=self.prompt.destroy)
            textLabel.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
            congratButton.grid(row=1, column=0, padx=(30, 5), pady=5)



    def InvalidImportPrompt(self):
        '''
        Prompt that displays error when user
        provides invalid address book name
        '''
        self.prompt = Toplevel(self.root)
        self.prompt.minsize(width=800, height=100)
        self.prompt.maxsize(width=1000, height=100)
        errorLabel = Label(self.prompt, text="This is not a standard .txt file. The standard txt file should be like:\n"
                                             "id    first_name  last_name   address city    state   zip_code    phone_number    email")
        button = Button(self.prompt, text="     OK     ", command=self.prompt.destroy)
        errorLabel.pack()
        button.pack()


    def OnClosing(self):
        self.root.destroy()
