''' For creating a demo address book and test the app'''

from AddressBook import AddressBook

addressb = AddressBook("cis422")

addressb.add("Jim", "Li", "1080 Patterson Tower", "Eugene", "OR", "97403", "5419549644", "jinjiel@uoregon.edu")
addressb.add("Roger", "Luo", "2125Franklin", "Eugene", "OR", "97401", "5419549777", "rogerl@uregon.edu")

addressb.print_book()

print("sort by zipcode")

addressb.sort_by_zc()

print("sort by last name")
addressb.sort_by_ln()

addressb.close()