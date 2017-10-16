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
        self.orderby = Store the order for sorting
        '''

        self.name = name
        self.CreateDatabase()

        self.orderbyfirstname = 0
        self.orderbylastname = 0
        self.orderbyaddress = 0
        self.orderbycity = 0
        self.orderbystate = 0
        self.orderbyphone = 0
        self.orderbyzipcode = 0
        self.orderbyemail = 0

    def CreateDatabase(self):

        '''
        Creates a database if it doesn't exist

        Returns:
            Bool -> True: If it successfully created the new database for the AddressBook
            Bool -> False: If database already exists
        '''


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

    def UpdateContact(self, contact, ID):
        '''
        Updates contact from AddressBook

        Param:
            Contact

        Returns:
            Bool -> True: If it successfully updated a contact in the AddressBook
            Bool -> False: If it wasn't able to updaye the contact from the AddressBook (ie. doesn't exist)
        '''

        self.c.execute("UPDATE AddressBook SET first_name = (?) WHERE id = (?)",
                       (contact.GetFirstName(), ID))
        self.c.execute("UPDATE AddressBook SET last_name = (?) WHERE id = (?)",
                       (contact.GetLastName(), ID))
        self.c.execute("UPDATE AddressBook SET address = (?) WHERE id = (?)",
                       (contact.GetAddress(), ID))
        self.c.execute("UPDATE AddressBook SET city = (?) WHERE id = (?)",
                       (contact.GetCity(), ID))
        self.c.execute("UPDATE AddressBook SET state = (?) WHERE id = (?)",
                       (contact.GetState(), ID))
        self.c.execute("UPDATE AddressBook SET zip_code = (?) WHERE id = (?)",
                       (contact.GetZipcode(), ID))
        self.c.execute("UPDATE AddressBook SET phone_number = (?) WHERE id = (?)",
                       (contact.GetPhoneNumber(), ID))
        self.c.execute("UPDATE AddressBook SET email = (?) WHERE id = (?)",
                       (contact.GetEmail(), ID))
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
        if self.orderbyzipcode == 0:
            self.c.execute('SELECT * FROM AddressBook ORDER BY zip_code ASC')
            self.orderbyzipcode = 1
        else:
            self.c.execute('SELECT * FROM AddressBook ORDER BY zip_code DESC')
            self.orderbyzipcode = 0
        return self.c.fetchall()

    def GetAllContacts_ByLastName(self):
        '''
        Displays all of the contacts from AddressBook sorted by last name
        (gets all of the contacts from the database and populates a list of objects from the class Contacts)

        Returns:
            sorted list of contacts
        '''
        if self.orderbylastname == 0:
            self.c.execute('SELECT * FROM AddressBook ORDER BY last_name ASC')
            self.orderbylastname = 1
        else:
            self.c.execute('SELECT * FROM AddressBook ORDER BY last_name DESC')
            self.orderbylastname = 0

        return self.c.fetchall()

    def sortByFN(self):
        if self.orderbyfirstname == 0:
            self.c.execute('SELECT * FROM AddressBook ORDER BY first_name ASC')
            self.orderbyfirstname = 1
        else:
            self.c.execute('SELECT * FROM AddressBook ORDER BY first_name DESC')
            self.orderbyfirstname = 0

        return self.c.fetchall()

    def sortByAddress(self):
        if self.orderbyaddress == 0:
            self.c.execute('SELECT * FROM AddressBook ORDER BY address ASC')
            self.orderbyaddress = 1
        else:
            self.c.execute('SELECT * FROM AddressBook ORDER BY address DESC')
            self.orderbyaddress = 0
        return self.c.fetchall()

    def sortByCity(self):
        if self.orderbycity == 0:
            self.c.execute('SELECT * FROM AddressBook ORDER BY city ASC')
            self.orderbycity = 1
        else:
            self.c.execute('SELECT * FROM AddressBook ORDER BY city DESC')
            self.orderbycity = 0
        return self.c.fetchall()

    def sortByState(self):
        if self.orderbystate == 0:
            self.c.execute('SELECT * FROM AddressBook ORDER BY state ASC')
            self.orderbystate = 1
        else:
            self.c.execute('SELECT * FROM AddressBook ORDER BY state DESC')
            self.orderbystate = 0

        return self.c.fetchall()

    def sortByPhone(self):
        if self.orderbyphone == 0:
            self.c.execute('SELECT * FROM AddressBook ORDER BY phone_number ASC')
            self.orderbyphone = 1
        else:
            self.c.execute('SELECT * FROM AddressBook ORDER BY phone_number DESC')
            self.orderbyphone = 0
        return self.c.fetchall()

    def sortByEmail(self):
        if self.orderbyemail == 0:
            self.c.execute('SELECT * FROM AddressBook ORDER BY email ASC')
            self.orderbyemail = 1
        else:
            self.c.execute('SELECT * FROM AddressBook ORDER BY email DESC')
            self.orderbyemail = 0
        return self.c.fetchall()

    def open(self):
        self.conn = sqlite3.connect("%s.db" % self.n)
        self.c = self.conn.cursor()

    def close(self):
        self.c.close()
        self.conn.close()

    def searchLN(self, ln):
        self.c.execute('SELECT * FROM AddressBook WHERE last_name LIKE ?', ("%"+ln+"%",))
        return self.c.fetchall()

    def searchFN(self, fn):
        self.c.execute('SELECT * FROM AddressBook WHERE first_name LIKE ?', ("%"+fn+"%",))
        return self.c.fetchall()

    def searchAddress(self, address):
        self.c.execute('SELECT * FROM AddressBook WHERE address LIKE ?', ("%"+address+"%",))
        return self.c.fetchall()

    def searchCity(self, city):
        self.c.execute('SELECT * FROM AddressBook WHERE city LIKE ?', ("%"+city+"%",))
        return self.c.fetchall()

    def searchState(self, state):
        self.c.execute('SELECT * FROM AddressBook WHERE state LIKE ?', ("%"+state+"%",))
        return self.c.fetchall()

    def searchZip(self, zip):
        self.c.execute('SELECT * FROM AddressBook WHERE zip_code LIKE ?', ("%"+zip+"%",))
        return self.c.fetchall()

    def searchPhone(self, phone):
        self.c.execute('SELECT * FROM AddressBook WHERE phone_number LIKE ?', ("%"+phone+"%",))
        return self.c.fetchall()

    def searchEmail(self, email):
        self.c.execute('SELECT * FROM AddressBook WHERE email LIKE ?', ("%"+email+"%",))
        return self.c.fetchall()

    def print_book(self):
        self.c.execute('SELECT * FROM AddressBook')
        for row in self.c.fetchall():
            print(row)

    def print_name(self):
        print(self.name)
