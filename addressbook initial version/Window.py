from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from AddressBook import *
from Contact import Contact
from StartScreen import *
import os

openBooks = []

class Window:
    def __init__(self, bookName):
        '''
        Main user interface of an opened address book. Initializes Tkinter instance.
        args:
        bookName - The name of an address book. Expected to be a .db file, but one will be created if
                   it doesn't already exist
        returns: none
        '''
        self.root = Tk()
        self.bookName = bookName
        self.addressBook = AddressBook(self.bookName)
        self.tree = None
        self.prompt = None
        self.contactHeader = ["ID", "First Name", "Last Name", "Address", "City", "State", "Zip", "Phone Number", "Email"]

        self.root.title(str(self.bookName))
        self.root.minsize(width=900, height=350)
        self.root.maxsize(width=900, height=350)
        self.initializeUI()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing) # Event when closing the window
        self.root.mainloop()

    def initializeUI(self):
        '''
        Initializes all Tkinter widgets of the main screen of an address book
        args: None
        returns: None
        '''
        # Dropdown menu items
        menu = Menu(self.root)
        fileMenu = Menu(menu, tearoff=0)
        fileMenu.add_command(label="New", comman=self.newFilePrompt)
        fileMenu.add_command(label="Open", command=self.openFile)
        fileMenu.add_command(label="Save")
        fileMenu.add_command(label="Save As", command=self.saveFile)

        fileMenu.add_separator()
        fileMenu.add_command(label="Close", command=self.on_closing)
        menu.add_cascade(label="File", menu=fileMenu)

        editMenu = Menu(menu, tearoff=0)
        menu.add_cascade(label="Edit", menu=editMenu)

        # Treeview, main widget
        self.tree = ttk.Treeview(self.root, columns=self.contactHeader, show="headings")

        for column in self.contactHeader:
            self.tree.heading(column, text=str(column), command=lambda c=column: self.sortBy(c))
            self.tree.column(column, width=90)

        # Implemented by Jim

        for row in self.addressBook.GetAllContacts():
            self.tree.insert('', 'end', values=(row))


        vertScroll = ttk.Scrollbar(self.root, orient="vertical", command=self.tree.yview)
        horScroll = ttk.Scrollbar(self.root, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vertScroll.set, xscrollcommand=horScroll.set)
        self.tree.grid(column=0, row=0, columnspan=5, sticky="nsew", pady=(15,0), padx=(35,0))
        vertScroll.grid(column=5, row=0, columnspan=5, sticky="ns", pady=(15,0))
        horScroll.grid(column=0, row=1, columnspan=5, sticky="ew", padx=(35,0))

        # Button widgets
        newButton = Button(self.root, text="New Contact", width=20, command = self.newPrompt)
        newButton.grid(column=0, row=2, pady=25)
        editButton = Button(self.root, text="Edit", width=20, command = self.editPrompt)
        editButton.grid(column=1, row=2, pady=25)
        deleteButton = Button(self.root, text="Delete", width=20 , command = self.DeleteContact)
        deleteButton.grid(column=2, row=2, pady=25)
        searchButton = Button(self.root, text="Search", width=20, command=self.searchPrompt)
        searchButton.grid(column=3, row=2, pady=25)
        defaultButton = Button(self.root, text="Default", width=5, command=self.defaultView)
        defaultButton.grid(column=4, row=2, pady=25)

        self.root.config(menu=menu)

    def newPrompt(self):
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

        contact = Contact(self.FirstNameEntry.get(), self.LastNameEntry.get(), self.AddressEntry.get(),
                          self.CityEntry.get(), self.StateEntry.get(), self.ZipEntry.get(), self.PhoneEntry.get(),
                          self.EmailEntry.get())
        self.addressBook.AddContact(contact)
        self.prompt.destroy()
        self.initializeUI()

    def DeleteContact(self):
        curItem = self.tree.focus()
        if curItem != '':   # validate one entry has been selected
            contact = Contact(self.tree.item(curItem)['values'][0], self.tree.item(curItem)['values'][1],
                              self.tree.item(curItem)['values'][2], self.tree.item(curItem)['values'][3],
                              self.tree.item(curItem)['values'][4], self.tree.item(curItem)['values'][5],
                              self.tree.item(curItem)['values'][6], self.tree.item(curItem)['values'][7])
            self.addressBook.DeleteContact(contact)
            self.initializeUI()

    def editPrompt(self):
        curItem = self.tree.focus()
        if curItem != '':  # validate one entry has been selected
            self.prompt = Toplevel(self.root)

            self.NameLabel = Label(self.prompt, text = "Full Name: ")
            self.NameLabel.grid(row=0, column=0, pady=5, padx=5)
            self.FirstLabel = Label(self.prompt, text = self.tree.item(curItem)['values'][0])
            self.FirstLabel.grid(row=0, column=1, pady=5, padx=5)
            self.LastLabel = Label(self.prompt, text = self.tree.item(curItem)['values'][1])
            self.LastLabel.grid(row=0, column=2, pady=5, padx=5)

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
            self.FirstNameEntry.insert(0, self.tree.item(curItem)['values'][0])
            self.FirstNameEntry.grid(row=1, column=1, padx=5, pady=5)
            self.LastNameEntry = Entry(self.prompt, bd=5)
            self.LastNameEntry.insert(0, self.tree.item(curItem)['values'][1])
            self.LastNameEntry.grid(row=2, column=1, padx=5, pady=5)
            self.AddressEntry = Entry(self.prompt, bd=5)
            self.AddressEntry.insert(0, self.tree.item(curItem)['values'][2])
            self.AddressEntry.grid(row=3, column=1, padx=5, pady=5)
            self.CityEntry = Entry(self.prompt, bd=5)
            self.CityEntry.insert(0, self.tree.item(curItem)['values'][3])
            self.CityEntry.grid(row=4, column=1, padx=5, pady=5)
            self.StateEntry = Entry(self.prompt, bd=5)
            self.StateEntry.insert(0, self.tree.item(curItem)['values'][4])
            self.StateEntry.grid(row=5, column=1, padx=5, pady=5)
            self.ZipEntry = Entry(self.prompt, bd=5)
            self.ZipEntry.insert(0, self.tree.item(curItem)['values'][5])
            self.ZipEntry.grid(row=6, column=1, padx=5, pady=5)
            self.PhoneEntry = Entry(self.prompt, bd=5)
            self.PhoneEntry.insert(0, self.tree.item(curItem)['values'][6])
            self.PhoneEntry.grid(row=7, column=1, padx=5, pady=5)
            self.EmailEntry = Entry(self.prompt, bd=5)
            self.EmailEntry.insert(0, self.tree.item(curItem)['values'][7])
            self.EmailEntry.grid(row=8, column=1, padx=5, pady=5)

            createButton = Button(self.prompt, text="Confirm", command=self.EditContact)
            createButton.grid(row=1, column=2, padx=3, pady=3)

    def EditContact(self):

        contact = Contact(self.FirstNameEntry.get(), self.LastNameEntry.get(), self.AddressEntry.get(),
                          self.CityEntry.get(), self.StateEntry.get(), self.ZipEntry.get(), self.PhoneEntry.get(),
                          self.EmailEntry.get())
        self.addressBook.UpdateContact(contact, self.FirstLabel["text"], self.LastLabel["text"])
        self.prompt.destroy()
        self.initializeUI()

    def searchPrompt(self):
        self.prompt = Toplevel(self.root)
        self.variable = StringVar(self.prompt)
        self.variable.set("First Name")
        self.options = OptionMenu(self.prompt, self.variable, *self.contactHeader)
        self.options.grid(row=0, column=0, padx=5, pady=5)
        self.searchEntry = Entry(self.prompt, bd=5)
        self.searchEntry.grid(row=0, column=1, padx=5, pady=5)
        searchButton = Button(self.prompt, width=10, text="Search", command=self.search)
        searchButton.grid(row=0, column=2, padx=5, pady=5)

    def search(self):
        print(self.searchEntry.get())
        print(self.variable.get())
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

    def defaultView(self):
        self.tree.delete(*self.tree.get_children())
        for row in self.addressBook.GetAllContacts():
            self.tree.insert('', 'end', values=(row))

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
        if (self.fileName not in openBooks):
            openBooks.append(self.fileName)
            Window(self.fileName)
        else:
            #display error
            pass

    def openFile(self):
        self.root.filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("DB files","*.db"),("all files","*.*")))
        self.root.filename = self.root.filename.split(".")[0]
        if self.root.filename != "":
            openBooks.append(self.root.filename)
            Window(self.root.filename)

    def saveFile(self):
        self.root.filename = filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("DB files","*.db"),("all files","*.*")))

    def sortBy(self, column):
        if column == "Last Name":
            self.tree.delete(*self.tree.get_children())
            for row in self.addressBook.GetAllContacts_ByLastName():
                self.tree.insert('', 'end', values=(row))
        elif column == "Zip":
            self.tree.delete(*self.tree.get_children())
            for row in self.addressBook.GetAllContacts_ByZipcode():
                self.tree.insert('', 'end', values=(row))

    def on_closing(self):
        openBooks.remove(self.bookName)
        self.addressBook.close()
        self.root.destroy()
