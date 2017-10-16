import Contact

import Contact
import sqlite3
import os


class AddressBook(object):

    def __init__(self, name):
        '''
        self.name = AddressBook Name
        self.conn = Connection to Database
        self.c = Database Executable
        '''

        self.name = name
        self.CreateDatabase()

    def CreateDatabase(self):

        '''
        Creates a database if it doesn't exist

        Returns:
            Bool -> True: If it successfully created the new database for the AddressBook
            Bool -> False: If database already exists
        '''

        '''files = [f for f in os.listdir('.') if os.path.isfile(f)]
        if ("%s.db" % self.name) in files:   # Determine if it exists
            self.conn = sqlite3.connect('%s.db' % self.name)
            self.c = self.conn.cursor()
            self.c.execute(
                ''''''CREATE TABLE IF NOT EXISTS AddressBook (first_name TEXT, last_name TEXT, address TEXT, city TEXT,
                   state TEXT, zip_code INT, phone_number INT, email TEXT)'''''')
            self.conn.commit()
            return True
        else:
            return False'''

        self.conn = sqlite3.connect('%s.db' % self.name)
        self.c = self.conn.cursor()
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS AddressBook (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, first_name TEXT, last_name TEXT, address TEXT, city TEXT,
               state TEXT, zip_code INT, phone_number INT, email TEXT)''')
        self.conn.commit()

    def AddContact(self, Contact):
        '''
        Adds contact to a database

        Param:
            Contact

        Returns:
            Bool -> True: If it successfully added a new contact in the AddressBook
            Bool -> False: If it wasn't able to successfully add the contact to the AddressBook
        '''
        try:
            sql = ''' INSERT INTO AddressBook (first_name, last_name, address, city, state, zip_code, phone_number, email )
                              VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''
            self.c.execute(sql, (Contact.GetFirstName(), Contact.GetLastName(), Contact.GetAddress(), Contact.GetCity(),
                                 Contact.GetState(), Contact.GetZipcode(), Contact.GetPhoneNumber(),
                                 Contact.GetEmail()))
            self.conn.commit()
            return True
        except:
            return False


    def DeleteContact(self, contact):
        '''
        Deletes contact from a database

        Param:
            Contact

        Returns:
            Bool -> True: If it successfully deleted a contact in the AddressBook
            Bool -> False: If it wasn't able to delete the contact from the AddressBook (ie. doesn't exist)
        '''
        try:
            sql = ''' DELETE FROM AddressBook WHERE first_name = (?) AND last_name = (?) '''
            self.c.execute(sql, (contact.FirstName, contact.LastName))
            self.conn.commit()
            return True
        except:
            return False

    def DeleteAddressBook(self):

        '''
        Deletes AddressBook from database

        Returns:
            Bool -> True: If it successfully deleted AddressBook
            Bool -> False: If it wasn't able to delete the AddressBook (ie. doesn't exist)
        '''
        self.conn.close()
        os.remove("%s.db" % self.name)
        return True

    def UpdateContact(self, contact, firstname, lastname):
        '''
        Updates contact from AddressBook

        Param:
            Contact

        Returns:
            Bool -> True: If it successfully updated a contact in the AddressBook
            Bool -> False: If it wasn't able to updaye the contact from the AddressBook (ie. doesn't exist)
        '''

        self.c.execute("UPDATE AddressBook SET first_name = (?) WHERE first_name = (?) AND last_name = (?)",
                       (contact.GetFirstName(), firstname, lastname))
        self.c.execute("UPDATE AddressBook SET last_name = (?) WHERE first_name = (?) AND last_name = (?)",
                       (contact.GetLastName(), contact.GetFirstName(), lastname))
        self.c.execute("UPDATE AddressBook SET address = (?) WHERE first_name = (?) AND last_name = (?)",
                       (contact.GetAddress(), contact.GetFirstName(), contact.GetLastName()))
        self.c.execute("UPDATE AddressBook SET city = (?) WHERE first_name = (?) AND last_name = (?)",
                       (contact.GetCity(), contact.GetFirstName(), contact.GetLastName()))
        self.c.execute("UPDATE AddressBook SET state = (?) WHERE first_name = (?) AND last_name = (?)",
                       (contact.GetState(), contact.GetFirstName(), contact.GetLastName()))
        self.c.execute("UPDATE AddressBook SET zip_code = (?) WHERE first_name = (?) AND last_name = (?)",
                       (contact.GetZipcode(), contact.GetFirstName(), contact.GetLastName()))
        self.c.execute("UPDATE AddressBook SET phone_number = (?) WHERE first_name = (?) AND last_name = (?)",
                       (contact.GetPhoneNumber(), contact.GetFirstName(), contact.GetLastName()))
        self.c.execute("UPDATE AddressBook SET email = (?) WHERE first_name = (?) AND last_name = (?)",
                       (contact.GetEmail(), contact.GetFirstName(), contact.GetLastName()))
        self.conn.commit()
        return

    def GetAllContacts(self):

        '''
        Displays all of the contacts from AddressBook
        (gets all of the contacts from the database and populates a list of objects from the class Contacts)

        Returns:
            list of contacts
        '''
        self.c.execute('SELECT * FROM AddressBook')
        return self.c.fetchall()

    def GetAllContacts_ByZipcode(self):
        '''
        Displays all of the contacts from AddressBook sorted by zipcode
        (gets all of the contacts from the database and populates a list of objects from the class Contacts)

        Returns:
            sorted list of contacts
        '''
        self.c.execute('SELECT * FROM AddressBook ORDER BY zip_code ASC')
        return self.c.fetchall()

    def GetAllContacts_ByLastName(self):
        '''
        Displays all of the contacts from AddressBook sorted by last name
        (gets all of the contacts from the database and populates a list of objects from the class Contacts)

        Returns:
            sorted list of contacts
        '''
        self.c.execute('SELECT * FROM AddressBook ORDER BY last_name')
        return self.c.fetchall()

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

    def searchLN(self, ln):
        self.c.execute('SELECT * FROM AddressBook WHERE last_name LIKE ?', ("%"+ln+"%",))
        return self.c.fetchall()

    def print_book(self):
        self.c.execute('SELECT * FROM AddressBook')
        for row in self.c.fetchall():
            print(row)

    def print_name(self):
        print(self.name)
