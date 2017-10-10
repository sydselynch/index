from AddressBook import AddressBook
from tkinter import *
import StartScreen
import Window
import os

class AddressBookEntries(object):
    @staticmethod
    def OpenAddressBook(name):
         '''
         Establishes a connection to an address book
         Loads all of the entries of contacts into a new addressbook object and returns it

         Param:
             AddressBook Name

         Returns:
             AddressBook Object: If it successfully establishes a connection AddressBook
             Bool -> False: If the AddressBook doesn't exists
         '''
         return

    @staticmethod
    def CloseAddressBook(name):
         '''
         Closes the connection to an address book

         Returns:
             Bool -> True: If it successfully closes the AddressBook
             Bool -> False: If the AddressBook doesn't exist
         '''
         return

    @staticmethod
    def GetAllAddressBookEntries():
        '''
        Closes the connection to an address book

        Returns:
            BookList -> List of AddressBook Entries
        '''
        booklist = []
        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        for f in files:
            if f.endswith(".db"):
                address = AddressBook(f[0:-3])
                booklist.append(address)
        return booklist