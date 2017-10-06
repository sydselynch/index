
import sqlite3


class AddressBook(object):

    def __init__(self,n):
        '''
        self.name = AddressBook Name
        self.conn = Connection to Database
        self.c = Database Executable
        '''

        self.name = n
        self.conn = sqlite3.connect('%s.db' % n)
        self.c = self.conn.cursor()
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS AddressBook (first_name TEXT, last_name TEXT, address TEXT, city TEXT,
               state TEXT, zip_code INT, phone_number INT, email TEXT)''')
        self.conn.commit()

    def CreateDatabase(self):
        '''
        Creates a database if it doesn't exist

        Returns:
            Bool -> True: If it successfully created the new database for the AddressBook
            Bool -> False: If database already exists
        '''
        return

    def AddContact(self, contact):
        '''
        Adds contact to a database

        Param:
            Contact

        Returns:
            Bool -> True: If it successfully added a new contact in the AddressBook
            Bool -> False: If it wasn't able to successfully add the contact to the AddressBook
        '''
        return

    def DeleteContact(self, contact):
        '''
        Deletes contact from a database

        Param:
            Contact

        Returns:
            Bool -> True: If it successfully deleted a contact in the AddressBook
            Bool -> False: If it wasn't able to delete the contact from the AddressBook (ie. doesn't exist)
        '''
        return

    def DeleteAddressBook(self):
        '''
        Deletes addressbook from database

        Returns:
            Bool -> True: If it successfully deleted AddressBook
            Bool -> False: If it wasn't able to delete the AddressBook (ie. doesn't exist)
        '''
        return

    def UpdateContact(self, contact):
        '''
        Updates contact from AddressBook

        Param:
            Contact

        Returns:
            Bool -> True: If it successfully updated a contact in the AddressBook
            Bool -> False: If it wasn't able to updaye the contact from the AddressBook (ie. doesn't exist)
        '''
        return

    def GetAllContacts(self):
        '''
        Displays all of the contacts from AddressBook
        (gets all of the contacts from the database and populates a list of objects from the class Contacts)

        Returns:
            list of contacts
        '''
        return

    def GetAllContacts_ByZipcode(self):
        '''
        Displays all of the contacts from AddressBook sorted by zipcode
        (gets all of the contacts from the database and populates a list of objects from the class Contacts)

        Returns:
            sorted list of contacts
        '''

    def GetAllContacts_ByLastName(self):
        '''
        Displays all of the contacts from AddressBook sorted by last name
        (gets all of the contacts from the database and populates a list of objects from the class Contacts)

        Returns:
            sorted list of contacts
        '''
        return

    def open(self):
        self.conn = sqlite3.connect("%s.db" % self.n)
        self.c = self.conn.cursor()

    def close(self):
        self.c.close()
        self.conn.close()

    def add(self, fn, ln, ad, ci, sta, zip, pho, emai):
        sql = ''' INSERT INTO AddressBook (first_name, last_name, address, city, state, zip_code, phone_number, email )
                  VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''
        self.c.execute(sql,(fn, ln, ad, ci, sta, zip, pho, emai))
        self.conn.commit()

    def delete_entry(self, fn, ln):
        self.c.execute('DELETE FROM AddressBook WHERE first_name = (?) AND last_name = (?)', (fn, ln))
        self.conn.commit()

    def delete(self):
        self.c.execute('DROP TABLE AddressBook')
        self.conn.commit()

    def update(self, fn, ln, entry, value):
        self.c.execute("UPDATE AddressBook SET %s = (?) WHERE first_name = (?) AND last_name = (?)" % entry, (value, fn, ln))
        self.conn.commit()

    def sort_by_ln(self):
        self.c.execute('SELECT * FROM AddressBook ORDER BY last_name')
        for row in self.c.fetchall():
            print(row)

    def sort_by_zc(self):
        self.c.execute('SELECT * FROM AddressBook ORDER BY zip_code ASC')
        for row in self.c.fetchall():
            print(row)

    def print_book(self):
        self.c.execute('SELECT * FROM AddressBook')
        for row in self.c.fetchall():
            print(row)

    def print_name(self):
        print(self.name)







