from tkinter import *
from tkinter import ttk
from AddressBook import AddressBook
import os

class Window:
    def __init__(self, bookName):
        self.root = Tk()
        self.bookName = bookName
        self.addressBook = AddressBook(self.bookName)
        print("affrim")
        self.tree = None
        self.contactHeader = ["First Name", "Last Name", "Address", "City", "State", "Zip", "Phone Number", "Email"]

        self.root.title(str(self.bookName))
        self.root.geometry("800x350")
        self.initializeUI()
        self.root.mainloop()

    def initializeUI(self):
        menu = Menu(self.root)
        fileMenu = Menu(menu, tearoff=0)
        fileMenu.add_command(label="New",)

        fileMenu.add_separator()
        fileMenu.add_command(label="Quit", command=self.root.quit)
        menu.add_cascade(label="File", menu=fileMenu)

        editMenu = Menu(menu, tearoff=0)
        menu.add_cascade(label="Edit", menu=editMenu)

        # Treeview
        self.tree = ttk.Treeview(self.root, columns=self.contactHeader, show="headings")

        for column in self.contactHeader:
            self.tree.heading(column, text=str(column))
            self.tree.column(column, width=90)

        # Implemented by Jim

        for row in self.addressBook.GetAllContacts():
            self.tree.insert('', 'end', values=(row))


        vertScroll = ttk.Scrollbar(orient="vertical", command=self.tree.yview)
        horScroll = ttk.Scrollbar(orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vertScroll.set, xscrollcommand=horScroll.set)
        self.tree.grid(column=0, row=0, columnspan=3, sticky="nsew", pady=(15,0), padx=(35,0))
        vertScroll.grid(column=3, row=0, columnspan=3, sticky="ns", pady=(15,0))
        horScroll.grid(column=0, row=1, columnspan=3, sticky="ew", padx=(35,0))

        #buttons
        newButton = Button(self.root, text="New Contact", width=20, command = self.newPrompt)
        newButton.grid(column=0, row=2, pady=25)
        editButton = Button(self.root, text="Edit", width=20)
        editButton.grid(column=1, row=2, pady=25)
        deleteButton = Button(self.root, text="Delete", width=20)
        deleteButton.grid(column=2, row=2, pady=25)

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


        createButton = Button(self.prompt, text="Confirm")
        createButton.grid(row=0, column=2, padx=3, pady=3)