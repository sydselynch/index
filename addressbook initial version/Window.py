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

        # Implement by Jim

        for row in self.addressBook.GetAllContacts():
            self.tree.insert('', 'end', values=(row))


        vertScroll = ttk.Scrollbar(orient="vertical", command=self.tree.yview)
        horScroll = ttk.Scrollbar(orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vertScroll.set, xscrollcommand=horScroll.set)
        self.tree.grid(column=0, row=0, columnspan=3, sticky="nsew", pady=(15,0), padx=(35,0))
        vertScroll.grid(column=3, row=0, columnspan=3, sticky="ns", pady=(15,0))
        horScroll.grid(column=0, row=1, columnspan=3, sticky="ew", padx=(35,0))

        #buttons
        newButton = Button(self.root, text="New Contact", width=20)
        newButton.grid(column=0, row=2, pady=25)
        editButton = Button(self.root, text="Edit", width=20)
        editButton.grid(column=1, row=2, pady=25)
        deleteButton = Button(self.root, text="Delete", width=20)
        deleteButton.grid(column=2, row=2, pady=25)


        self.root.config(menu=menu)
