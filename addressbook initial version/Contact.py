class Contact:
    def __init__(self, firstName, lastName, address, city, state, zipcode, phoneNumber, email):
        self.FirstName = firstName
        self.LastName = lastName
        self.Address = address
        self.City = city
        self.State = state
        self.Zipcode = zipcode
        self.PhoneNumber = phoneNumber
        self.Email = email

    def GetFirstName(self):
        return self.FirstName

    def GetLastName(self):
        return self.LastName

    def GetAddress(self):
        return self.Address

    def GetCity(self):
        return self.City

    def GetState(self):
        return self.State

    def GetZipcode(self):
        return self.Zipcode

    def GetPhoneNumber(self):
        return self.PhoneNumber

    def GetEmail(self):
        return self.Email

