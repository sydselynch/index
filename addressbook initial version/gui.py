from tkinter import *
from tkinter import ttk
from AddressBook import AddressBook

#root will be passed in as master

#root = Tk()
#gui = Window(root)
#root.mainloop()

books = ["book1", "book2"]

class Start(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.root = root
        root.title("Address Book")

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
        #self.pack(fill=BOTH, expand=1)

        #List of files
        Label(self, text="Address Books").grid(row=0)
        addressBookList = Listbox(self)
        for i in books:
            addressBookList.insert(END, i)

        addressBookList.grid(row=1, rowspan=5)

class Window:
    def __init__(self, root):
        self.master = master
        master.title("Address Book")



    #def contactWindow(self):
