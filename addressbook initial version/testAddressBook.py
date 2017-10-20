from AddressBook import *
import unittest

class TestAddressBook(unittest.TestCase):

    def testCreateAddressBook(self):
        address = AddressBook('test')

        self.assertTrue(os.path.isfile(("%s.db" % address.name)))

        # delete address book
        address.DeleteAddressBook()

    def testAddContactSuccess(self):
        address = AddressBook('test')
        contact = Contact.Contact('FirstName', 'LastName', 'Address', 'City', 'State', 'Zipcode', 'PhoneNumber', 'Email')
        result = address.AddContact(contact)

        self.assertTrue(result)

        # delete address book
        address.DeleteAddressBook()

    def testDeleteContactSuccess(self):
        address = AddressBook('test')
        contact = Contact.Contact('FirstName', 'LastName', 'Address', 'City', 'State', 'Zipcode', 'PhoneNumber', 'Email')
        result = address.DeleteContact(contact)

        self.assertTrue(result)

        # delete address book
        address.DeleteAddressBook()

    def testUpdateContactSuccess(self):
        address = AddressBook('test')
        contact = Contact.Contact('Hello', 'Hey2', 'AddressUpdated', 'City', 'State', 'Zipcode', 'PhoneNumber', 'Email')
        result = address.UpdateContact(contact, 'Hello', 'Hey')
        self.assertEqual(contact.FirstName, result.FirstName)
        self.assertEqual(contact.LastName, result.LastName)
        self.assertEqual(contact.Address, contact.Address)

        # delete address book
        address.DeleteAddressBook()

    def testDeleteAddressBook(self):
        address = AddressBook('test')
        result = address.DeleteAddressBook()

        self.assertTrue(result)
        self.assertFalse(os.path.isfile(("%s.db" % address.name)))


unittest.main()
