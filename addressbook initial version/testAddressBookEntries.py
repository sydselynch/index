from AddressBookEntries import *
import unittest

class TestAddressBookEntries(unittest.TestCase):

    def testOpenAddressBookFailure(self):
        result = AddressBookEntries.OpenAddressBook('hello')

        self.assertFalse(result)

unittest.main()
