from Contact import Contact
import unittest

class TestContact(unittest.TestCase):
    
    def testNewContactAllFields(self):
        contact = Contact('FirstName', 'LastName', 'Address', 'City', 'State', 'Zipcode', 'PhoneNumber', 'Email')

        self.assertEqual(contact.FirstName, 'FirstName')
        self.assertEqual(contact.LastName, 'LastName')
        self.assertEqual(contact.Address, 'Address')
        self.assertEqual(contact.City, 'City')
        self.assertEqual(contact.State, 'State')
        self.assertEqual(contact.Zipcode, 'Zipcode')
        self.assertEqual(contact.PhoneNumber, 'PhoneNumber')
        self.assertEqual(contact.Email, 'Email')

unittest.main()
