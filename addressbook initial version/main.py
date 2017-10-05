from AddressBook import AddressBook
import os

#  Store the name of the address books currently using
currentbook = ''

# Save the existing address book
booklist = []

# Control the process 1-> Main manu 2-> entering an address book
process = 1;

def update_booklist():
    booklist = []
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in files:
        if f.endswith(".db"):
            booklist.append(f[0:-3])
    return booklist

while True:
    if process == 1:                     # Welcome menu
        control = input('''
Welcome to AddressBook!

Press 1 to add a new address book;
Press 2 to present all existing address books;
Press 3 to open an address book;
Press 4 to delete an address book;
Press 5 to quit the app. 

''')
        if control == "1":  # Add
            name = input(" Enter a name for a new address book: ")
            currentbook = name
            booklist.append(name)
            book = AddressBook(name)
            process = 2
        elif control == "2": # Present
            booklist = update_booklist()
            for i in booklist:
                print(i)
        elif control == "3": # Open
            name = input(" Enter the name of the address book: ")
            currentbook = name
            book = AddressBook(name)
            process = 2
        elif control == "4": # Delete
            booklist = update_booklist()
            name = input(" Enter the name of the address book: ")
            if name in booklist:
                os.remove("%s.db" % name)
                print(" Delete successfully")
                process = 1
            else:
                print(" Sorry, there is no such an address book")
        elif control == "5": # Quit
            break
    elif process == 2:    # Opening a specific address book
        while True:
            control = input(''' 
You are currently in the address book %s:
            
Press 1 to print the address book;
Press 2 to sort the address book by last name;
Press 3 to sort the address book by zip code;
Press 4 to add a person into the address book;
Press 5 to update the info;
Press 6 to delete a person from the address book;
Press 7 to return

''' % currentbook)
            if control == "1": # Print the address book
                book.print_book()
            elif control == "2": # Sort the address book by last name
                book.sort_by_ln()
            elif control == "3": # Sort the address book by zip code
                book.sort_by_zc()
            elif control == "4": # Add a person into the address book
                print(''' Please enter the information in this order:
first name, last name, address, city, state, zip code, phone number, email

''')
                fn = input("First name: ")
                ln = input("Last name: ")
                ad = input("Address: ")
                ci = input("City: ")
                sta = input("State: ")
                zip = input("Zip code: ")
                pho = input("Phone number: ")
                emai = input("Email: ")
                book.add(fn, ln, ad, ci, sta, zip, pho, emai)
            elif control == "5": # Update the info
                print(''' Please enter the information in this order:
fisrt name, last name, the entry to be updated, the new value of the entry
                
''')
                fn = input("First name: ")
                ln = input("Last name: ")
                entry = input("Entry: ")
                value = input("Value: ")
                book.update(fn, ln, entry, value)
            elif control == "6": # Delete a person from the address book
                print(''' Please enter the information in this order:
first name, last name
                
''')
                fn = input("First name: ")
                ln = input("Last name: ")
                book.delete_entry(fn, ln)
            elif control == "7": # Return
                book.close()
                process = 1
                break
    continue


