from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from AddressBook import *
from Contact import Contact
from StartScreen import *
import os

openBooks = []

class Window:
    def __init__(self, bookName, parent):
        '''
        Main user interface of an opened address book. Initializes Tkinter instance.
        args:
        bookName - The name of an address book. Expected to be a .db file, but one will be created if
                   it doesn't already exist
        returns: none
        '''
        self.root = Toplevel()
        self.parent = parent
        self.bookName = bookName
        self.addressBook = AddressBook(self.bookName)
        self.tree = None
        self.prompt = None
        self.contactHeader = ["ID", "First Name", "Last Name", "Address", "City", "State", "Zip", "Phone Number", "Email"]

        self.root.title(str(self.bookName))
        self.root.minsize(width=1000, height=350)
        self.root.maxsize(width=1000, height=350)
        self.InitializeUI()
        self.root.protocol("WM_DELETE_WINDOW", self.OnClosing) # Event when closing the window
        self.root.mainloop()

    def InitializeUI(self):
        '''
        Initializes all Tkinter widgets of the main screen of an address book
        args: None
        returns: None
        '''
        logo = PhotoImage(file="icon.gif")
        label = Label(self.root, image=logo, height=50, width=50)
        label.image = logo
        label.grid(row=2, column=5,sticky="NW")
        #icon = PhotoImage(file="icon.ico")
        #self.root.tk.call('wm','iconphoto',self.root._w,icon)
        self.root.iconbitmap('icon.ico')



        # Dropdown menu items
        menu = Menu(self.root)
        fileMenu = Menu(menu, tearoff=0)
        fileMenu.add_command(label="New", comman=self.NewFilePrompt)
        fileMenu.add_command(label="Open", command=self.OpenFile)
        fileMenu.add_command(label="Save")
        fileMenu.add_command(label="Save As", command=self.SaveFile)

        fileMenu.add_separator()
        fileMenu.add_command(label="Close", command=self.OnClosing)
        menu.add_cascade(label="File", menu=fileMenu)

        # Treeview, main widget
        self.tree = ttk.Treeview(self.root, columns=self.contactHeader, show="headings")

        for column in self.contactHeader:
            self.tree.heading(column, text=str(column), command=lambda c=column: self.SortBy(c))
            if column == 'ID':
                self.tree.column(column, width=5)
            else:
                self.tree.column(column, width=50)


        for row in self.addressBook.GetAllContacts():
            self.tree.insert('', 'end', values=(row))

        vertScroll = ttk.Scrollbar(self.root, orient="vertical", command=self.tree.yview)
        horScroll = ttk.Scrollbar(self.root, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vertScroll.set, xscrollcommand=horScroll.set)
        self.tree.grid(column=0, row=0, columnspan=5, sticky="nsew", pady=(15,0), padx=(35,0))
        vertScroll.grid(column=5, row=0, columnspan=5, sticky="ns", pady=(15,0), padx=(0,20))
        horScroll.grid(column=0, row=1, columnspan=5, sticky="ew", padx=(35,0))

        # Button widgets
        newButton = Button(self.root, text="New Contact", width=20, command = self.NewPrompt)
        newButton.grid(column=0, row=2, pady=25)
        editButton = Button(self.root, text="Edit", width=20, command = self.EditPrompt)
        editButton.grid(column=1, row=2, pady=25)
        deleteButton = Button(self.root, text="Delete", width=20, command = self.DeletePrompt)
        deleteButton.grid(column=2, row=2, pady=25)
        searchButton = Button(self.root, text="Search", width=20, command=self.SearchPrompt)
        searchButton.grid(column=3, row=2, pady=25)
        defaultButton = Button(self.root, text="Default", width=10, command=self.InitializeUI)
        defaultButton.grid(column=4, row=2, pady=25)

        self.root.config(menu=menu)
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)
        self.root.columnconfigure(3, weight=1)
        self.root.columnconfigure(4, weight=1)
        self.root.columnconfigure(5, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)

        # Add window to parent
        self.parent.AddWindow(self)

    def NewPrompt(self):
        '''
        Prompt that will display when creating a new contact,
        allows user to enter new contact information
        args: None
        returns: None
        '''
        self.prompt = Toplevel(self.root)

        FirstNameLabel = Label(self.prompt, text="First Name")
        FirstNameLabel.grid(row=0, column=0, pady=5, padx=5)
        LastNameLabel = Label(self.prompt, text="Last Name")
        LastNameLabel.grid(row=1, column=0, pady=5, padx=5)
        AddressLabel = Label(self.prompt, text="Address")
        AddressLabel.grid(row=2, column=0, pady=5, padx=5)
        CityLabel = Label(self.prompt, text="City")
        CityLabel.grid(row=3, column=0, pady=5, padx=5)
        StateLabel = Label(self.prompt, text="State")
        StateLabel.grid(row=4, column=0, pady=5, padx=5)
        ZipLabel = Label(self.prompt, text="Zip")
        ZipLabel.grid(row=5, column=0, pady=5, padx=5)
        PhoneLabel = Label(self.prompt, bd=5, text="Phone Number")
        PhoneLabel.grid(row=6, column=0, pady=5, padx=5)
        EmailLabel = Label(self.prompt, text="Email")
        EmailLabel.grid(row=7, column=0, pady=5, padx=5)

        self.FirstNameEntry = Entry(self.prompt, bd=5)
        self.FirstNameEntry.grid(row=0, column=1, padx=5, pady=5)
        self.LastNameEntry = Entry(self.prompt, bd=5)
        self.LastNameEntry.grid(row=1, column=1, padx=5, pady=5)
        self.AddressEntry = Entry(self.prompt, bd=5)
        self.AddressEntry.grid(row=2, column=1, padx=5, pady=5)
        self.CityEntry = Entry(self.prompt, bd=5)
        self.CityEntry.grid(row=3, column=1, padx=5, pady=5)
        self.StateEntry = Entry(self.prompt, bd=5)
        self.StateEntry.grid(row=4, column=1, padx=5, pady=5)
        self.ZipEntry = Entry(self.prompt, bd=5)
        self.ZipEntry.grid(row=5, column=1, padx=5, pady=5)
        self.PhoneEntry = Entry(self.prompt, bd=5)
        self.PhoneEntry.grid(row=6, column=1, padx=5, pady=5)
        self.EmailEntry = Entry(self.prompt, bd=5)
        self.EmailEntry.grid(row=7, column=1, padx=5, pady=5)

        createButton = Button(self.prompt, text="Confirm", command=self.AddContact)
        createButton.grid(row=0, column=2, padx=3, pady=3)

    def AddContact(self):
        '''
        Adds a contact to the open address book with information
        provided by the user and refreshes the interface
        args: None
        returns: None
        '''

        contact = Contact(self.FirstNameEntry.get(), self.LastNameEntry.get(), self.AddressEntry.get(),
                          self.CityEntry.get(), self.StateEntry.get(), self.ZipEntry.get(), self.PhoneEntry.get(),
                          self.EmailEntry.get())
        self.addressBook.AddContact(contact)
        self.prompt.destroy()
        self.InitializeUI()

    def DeletePrompt(self):
        '''
        Warning prompt that requires confirmation from the
        user before deleting an address book
        '''
        self.selection = self.tree.focus()
        if self.selection != "":
            self.prompt = Toplevel(self.root)
            self.prompt.title(string="Warning")
            self.prompt.minsize(width=225, height=75)
            self.prompt.maxsize(width=225, height=75)
            errorLabel = Label(self.prompt, text="Are you sure?")
            yesButton = Button(self.prompt, text= "      OK      ", command= self.DeleteContact)
            noButton = Button(self.prompt, text="      Cancel      ", command= self.prompt.destroy)
            errorLabel.grid(row=0, column=0, columnspan=2, padx=65, pady=5)
            yesButton.grid(row=1, column=0, padx=(30,5), pady=5)
            noButton.grid(row=1, column=1, padx=(5,30), pady=5)
            self.InitializeUI()

    def DeleteContact(self):
        '''
        Removes a contact from the address book and refreshes
        the interface
        '''
        self.prompt.destroy()
        curItem = self.selection
        if curItem != '':   # validate one entry has been selected

            self.addressBook.DeleteContact(self.tree.item(curItem)['values'][0])
            self.InitializeUI()

    def EditPrompt(self):
        '''
        Prompt that will display when user presses edit button,
        allows user to edit an existing contact
        '''
        curItem = self.tree.focus()
        if curItem != '':  # validate one entry has been selected
            self.prompt = Toplevel(self.root)
            self.ID = self.tree.item(curItem)['values'][0]

            FirstNameLabel = Label(self.prompt, text="First Name")
            FirstNameLabel.grid(row=1, column=0, pady=5, padx=5)
            LastNameLabel = Label(self.prompt, text="Last Name")
            LastNameLabel.grid(row=2, column=0, pady=5, padx=5)
            AddressLabel = Label(self.prompt, text="Address")
            AddressLabel.grid(row=3, column=0, pady=5, padx=5)
            CityLabel = Label(self.prompt, text="City")
            CityLabel.grid(row=4, column=0, pady=5, padx=5)
            StateLabel = Label(self.prompt, text="State")
            StateLabel.grid(row=5, column=0, pady=5, padx=5)
            ZipLabel = Label(self.prompt, text="Zip")
            ZipLabel.grid(row=6, column=0, pady=5, padx=5)
            PhoneLabel = Label(self.prompt, bd=5, text="Phone Number")
            PhoneLabel.grid(row=7, column=0, pady=5, padx=5)
            EmailLabel = Label(self.prompt, text="Email")
            EmailLabel.grid(row=8, column=0, pady=5, padx=5)

            self.FirstNameEntry = Entry(self.prompt, bd=5)
            self.FirstNameEntry.insert(0, self.tree.item(curItem)['values'][1])
            self.FirstNameEntry.grid(row=1, column=1, padx=5, pady=5)
            self.LastNameEntry = Entry(self.prompt, bd=5)
            self.LastNameEntry.insert(0, self.tree.item(curItem)['values'][2])
            self.LastNameEntry.grid(row=2, column=1, padx=5, pady=5)
            self.AddressEntry = Entry(self.prompt, bd=5)
            self.AddressEntry.insert(0, self.tree.item(curItem)['values'][3])
            self.AddressEntry.grid(row=3, column=1, padx=5, pady=5)
            self.CityEntry = Entry(self.prompt, bd=5)
            self.CityEntry.insert(0, self.tree.item(curItem)['values'][4])
            self.CityEntry.grid(row=4, column=1, padx=5, pady=5)
            self.StateEntry = Entry(self.prompt, bd=5)
            self.StateEntry.insert(0, self.tree.item(curItem)['values'][5])
            self.StateEntry.grid(row=5, column=1, padx=5, pady=5)
            self.ZipEntry = Entry(self.prompt, bd=5)
            self.ZipEntry.insert(0, self.tree.item(curItem)['values'][6])
            self.ZipEntry.grid(row=6, column=1, padx=5, pady=5)
            self.PhoneEntry = Entry(self.prompt, bd=5)
            self.PhoneEntry.insert(0, self.tree.item(curItem)['values'][7])
            self.PhoneEntry.grid(row=7, column=1, padx=5, pady=5)
            self.EmailEntry = Entry(self.prompt, bd=5)
            self.EmailEntry.insert(0, self.tree.item(curItem)['values'][8])
            self.EmailEntry.grid(row=8, column=1, padx=5, pady=5)

            createButton = Button(self.prompt, text="Confirm", command=self.EditContact)
            createButton.grid(row=1, column=2, padx=3, pady=3)

    def EditContact(self):
        '''
        Saves the information inputted by the user when editing
        a contact, refreshes the interface
        '''

        contact = Contact(self.FirstNameEntry.get(), self.LastNameEntry.get(), self.AddressEntry.get(),
                          self.CityEntry.get(), self.StateEntry.get(), self.ZipEntry.get(), self.PhoneEntry.get(),
                          self.EmailEntry.get())
        self.addressBook.UpdateContact(contact, self.ID)
        self.prompt.destroy()
        self.InitializeUI()

    def SearchPrompt(self):
        '''
        Prompt that displays when user presses the search button,
        allows user to search for any characters in the selected
        column
        '''
        self.prompt = Toplevel(self.root)
        self.variable = StringVar(self.prompt)
        self.variable.set("First Name")
        self.options = OptionMenu(self.prompt, self.variable, *self.contactHeader)
        self.options.grid(row=0, column=0, padx=5, pady=5)
        self.searchEntry = Entry(self.prompt, bd=5)
        self.searchEntry.grid(row=0, column=1, padx=5, pady=5)
        searchButton = Button(self.prompt, width=10, text="Search", command=self.Search)
        searchButton.grid(row=0, column=2, padx=5, pady=5)

    def Search(self):
        '''
        Searches the address book for the characters
        entered by the user in the given column
        '''
        if self.searchEntry.get() is not None:
            if self.variable.get() == "Last Name":
                self.tree.delete(*self.tree.get_children())
                for row in self.addressBook.searchLN(self.searchEntry.get()):
                    self.tree.insert('', 'end', values=(row))
            elif self.variable.get() == "First Name":
                self.tree.delete(*self.tree.get_children())
                for row in self.addressBook.searchFN(self.searchEntry.get()):
                    self.tree.insert('', 'end', values=(row))
            elif self.variable.get() == "Address":
                self.tree.delete(*self.tree.get_children())
                for row in self.addressBook.searchAddress(self.searchEntry.get()):
                    self.tree.insert('', 'end', values=(row))
            elif self.variable.get() == "City":
                self.tree.delete(*self.tree.get_children())
                for row in self.addressBook.searchCity(self.searchEntry.get()):
                    self.tree.insert('', 'end', values=(row))
            elif self.variable.get() == "State":
                self.tree.delete(*self.tree.get_children())
                for row in self.addressBook.searchState(self.searchEntry.get()):
                    self.tree.insert('', 'end', values=(row))
            elif self.variable.get() == "Zip":
                self.tree.delete(*self.tree.get_children())
                for row in self.addressBook.searchZip(self.searchEntry.get()):
                    self.tree.insert('', 'end', values=(row))
            elif self.variable.get() == "Phone Number":
                self.tree.delete(*self.tree.get_children())
                for row in self.addressBook.searchPhone(self.searchEntry.get()):
                    self.tree.insert('', 'end', values=(row))
            elif self.variable.get() == "Email":
                self.tree.delete(*self.tree.get_children())
                for row in self.addressBook.searchEmail(self.searchEntry.get()):
                    self.tree.insert('', 'end', values=(row))
            else:
                self.tree.delete(*self.tree.get_children())
                for row in self.addressBook.GetAllContacts():
                    self.tree.insert('', 'end', values=(row))

        self.prompt.destroy()

    def NewFilePrompt(self):
        '''
        Prompt that displays when creating a new address book
        from an existing address book, allows user to enter
        address book name
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
        Creates a new address book with the name
        provided by the user
        '''
        self.fileName = self.entry.get()
        self.prompt.destroy()
        if (self.fileName not in openBooks):
            openBooks.append(self.fileName)
            Window(self.fileName, self.parent)
        else:
            #display error
            pass

    def OpenFile(self):
        '''
        Opens an address book from an existing address book,
        must be of type .db
        '''
        self.root.filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("DB files","*.db"),("all files","*.*")))
        self.root.filename = self.root.filename.split(".")[0]
        if self.root.filename != "":
            openBooks.append(self.root.filename)
            Window(self.root.filename, self.parent)

    def SaveFile(self):
        #not done
        self.root.filename = filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("DB files","*.db"),("all files","*.*")))

    def SortBy(self, column):
        '''
        Retrieves a list of contacts sorted by values in
        the selected column
        args:
            column - The name of the column to sort by
        '''
        if column == "Last Name":
            self.tree.delete(*self.tree.get_children())
            for row in self.addressBook.GetAllContacts_ByLastName():
                self.tree.insert('', 'end', values=(row))
        elif column == "Zip":
            self.tree.delete(*self.tree.get_children())
            for row in self.addressBook.GetAllContacts_ByZipcode():
                self.tree.insert('', 'end', values=(row))
        elif column == "First Name":
            self.tree.delete(*self.tree.get_children())
            for row in self.addressBook.sortByFN():
                self.tree.insert('', 'end', values=(row))
        elif column == "Address":
            self.tree.delete(*self.tree.get_children())
            for row in self.addressBook.sortByAddress():
                self.tree.insert('', 'end', values=(row))
        elif column == "City":
            self.tree.delete(*self.tree.get_children())
            for row in self.addressBook.sortByCity():
                self.tree.insert('', 'end', values=(row))
        elif column == "State":
            self.tree.delete(*self.tree.get_children())
            for row in self.addressBook.sortByState():
                self.tree.insert('', 'end', values=(row))
        elif column == "Phone Number":
            self.tree.delete(*self.tree.get_children())
            for row in self.addressBook.sortByPhone():
                self.tree.insert('', 'end', values=(row))
        elif column == "Email":
            self.tree.delete(*self.tree.get_children())
            for row in self.addressBook.sortByEmail():
                self.tree.insert('', 'end', values=(row))

    def OnClosing(self):
        '''
        Called whenever self.root is destroyed, ensures
        that the address book is removed from the global
        list openBook
        '''
        openBooks.remove(self.bookName)
        self.addressBook.close()
        # remove window from parent
        self.parent.RemoveWindow(self)
        self.root.destroy()
