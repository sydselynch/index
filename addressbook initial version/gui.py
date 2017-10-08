from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
from AddressBook import AddressBook
import os
#root will be passed in as master

#root = Tk()
#gui = Window(root)
#root.mainloop()


#populate list with .db files
books = ["book1", "book2", "book3", "book4", "book5", "book6", "book7", "book8", "book9", "book10", "book11"]
contactHeader = ["First Name", "Last Name", "Address", "City", "State", "Zip", "Phone Number", "Email"]

def update_booklist():
    booklist = []
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in files:
        if f.endswith(".db"):
            booklist.append(f[0:-3])
    return booklist


class Start(Frame):
    def __init__(self, root):
        #Frame.__init__(self, root)
        self.bookList = update_booklist()
        self.root = root
        root.title("Address Book")
        root.minsize(width=450, height=250)
        root.maxsize(width=450, height=250)

        self.initializeUI()

    def initializeUI(self):

        #Initialize buttons
        #TODO add functions to buttons
        newButton = Button(self.root, text="New", width=20, command=self.openMainWindow)
        newButton.grid(row=0, column=0, padx=25, pady=(30,10))
        openButton = Button(self.root, text="Open", width=20)
        openButton.grid(row=1, column=0, padx=25, pady=10)
        deleteButton = Button(self.root, text="Delete", width=20)
        deleteButton.grid(row=2, column=0, padx=25, pady=10)


        #List of files

        addressBookListLabel = Label(self.root, text="Address Books")
        addressBookListLabel.grid(row=0, column=1, padx=45)
        scrollbar = Scrollbar(self.root, orient=VERTICAL)
        addressBookList = Listbox(self.root, yscrollcommand=scrollbar.set, selectmode=SINGLE)
        scrollbar.config(command=addressBookList.yview)
        scrollbar.grid(column=2, row=1, rowspan=3, sticky="ns")
        for i in self.bookList:
            addressBookList.insert(END, i)

        addressBookList.grid(row=1, column=1, rowspan=2, sticky="ns")

    def newFile(self):
        return
    def openFile(self):
        return
    def removeFile(self):
        return


    def openMainWindow(self):
        mainScreen = Window("test")
        self.root.destroy()


class Window:
    def __init__(self, bookName):
        self.root = Tk()
        self.bookName = bookName
        self.tree = None

        self.root.title(str(self.bookName))
        self.root.geometry("800x350")
        self.initializeUI()

    def initializeUI(self):
        menu = Menu(self.root)
        fileMenu = Menu(menu, tearoff=0)
        fileMenu.add_command(label="New",)

        fileMenu.add_separator()
        fileMenu.add_command(label="Quit", command=self.root.quit)
        menu.add_cascade(label="File", menu=fileMenu)


        editMenu = Menu(menu, tearoff=0)
        menu.add_cascade(label="Edit", menu=editMenu)

        # tree view
        self.tree = ttk.Treeview(self.root, columns=contactHeader, show="headings")

        for column in contactHeader:
            self.tree.heading(column, text=str(column))
            self.tree.column(column, width=90)
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





    #def contactWindow(self):
