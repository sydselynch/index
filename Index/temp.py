''' For creating a demo address book and test the app'''

from AddressBook import AddressBook
'''
addressb = AddressBook("oct5")

addressb.add("Jim", "Li", "1080 Patterson Tower", "Eugene", "OR", "96542", "5419549644", "jinjiel@uoregon.edu")
addressb.add("Roger", "Luo", "2125Franklin", "Eugene", "OR", "97721", "5419549777", "rogerl@uregon.edu")
addressb.add("Adams", "Smith", "", "Eugene", "OR", "97351", "5419549644", "adamss@uoregon.edu")
addressb.add("Noah", "Johnson", "1081 Patterson Tower", "Eugene", "OR", "97242", "5419549644", "noahj@uoregon.edu")
addressb.add("Charlotte", "Jones", "1083 Patterson Tower", "Eugene", "OR", "97421", "5419549644", "charj@uoregon.edu")
addressb.add("Harper", "Davis", "1084 Patterson Tower", "Eugene", "OR", "97423", "5419549644", "harperd@uoregon.edu")

addressb.print_book()

print("sort by zipcode")

addressb.sort_by_zc()

print("sort by last name")
addressb.sort_by_ln()

addressb.close()



addressb = AddressBook("cis422")
addressb.update("Jim", "Li", "state", "OR")
addressb.print_book()
'''