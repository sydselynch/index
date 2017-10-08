from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
from AddressBook import AddressBook

#root will be passed in as master

#root = Tk()
#gui = Window(root)
#root.mainloop()


#populate list with .db files
books = ["book1", "book2", "book3", "book4", "book5", "book6", "book7", "book8", "book9", "book10", "book11"]
contactHeader = ["First Name", "Last Name", "Address", "City", "State", "Zip", "Phone Number", "Email"]
class Start(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.root = root
        root.title("Address Book")
        root.minsize(width=450, height=250)
        root.maxsize(width=450, height=250)


        # self.newButton = Button(root, text="New")
        # self.newButton.pack()
        #
        # self.openButton = Button(root, text="Open")
        # self.openButton.pack()
        #
        # self.deleteButton = Button(root, text="Delete")
        # self.deleteButton.pack()

        self.initializeUI()

    def initializeUI(self):

        #Initialize buttons
        #TODO add functions to buttons
        newButton = Button(self.root, text="New", width=20)
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
        scrollbar.grid(column=2, row=1, rowspan=3, sticky=NS)
        for i in books:
            addressBookList.insert(END, i)

        addressBookList.grid(row=1, column=1, rowspan=3)

class Window:
    def __init__(self, root, bookName):
        self.root = root
        self.bookName = bookName
        self.tree = None
        #maybe make title name of address book opened
        root.title("Address Book")
        self.root.geometry("800x600")
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
            self.tree.column(column, width=tkFont.Font().measure(column.title()))
        vertScroll = ttk.Scrollbar(orient="vertical", command=self.tree.yview)
        horScroll = ttk.Scrollbar(orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vertScroll.set, xscrollcommand=horScroll.set)
        self.tree.grid(column=0, row=0, sticky="nsew")
        vertScroll.grid(column=1, row=0, sticky="ns")
        horScroll.grid(column=0, row=1, sticky="ew")







        self.root.config(menu=menu)





    #def contactWindow(self):
