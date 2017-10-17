from AddressBookEntries import *
import unittest

class TestAddressBookEntries(unittest.TestCase):

    def testOpenAddressBookFailure(self):
        result = AddressBookEntries.OpenAddressBook('TESTNONEXISTENTDATABASE')

        self.assertFalse(result)

    def testOpenAddressBookSuccess(self):
        address = AddressBook('TESTREALDATABASE')
        result = AddressBookEntries.OpenAddressBook(address.name)

        self.assertNotEqual(type(result), None)

        # delete address book
        address.DeleteAddressBook()

    def testGetAllAddressBookEntries(self):
        address = AddressBook('TESTREALDATABASE')
        result = AddressBookEntries.GetAllAddressBookEntries()

        self.assertGreater(len(result), 0)

        # delete address book
        address.DeleteAddressBook()

    def testCloseAddressBookSuccess(self):
        address = AddressBook('TESTREALDATABASE')
        result = AddressBookEntries.CloseAddressBook(address.name)

        self.assertTrue(result)

        # delete address book
        address.DeleteAddressBook()

unittest.main()
