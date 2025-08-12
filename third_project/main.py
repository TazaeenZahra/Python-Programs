# contact book CLI APP

# contact_file = open("Contact Book.txt","r")
import contact_methods

print("-----Welcome to Contact Book App-----\n")

while True:
    choice=(input("Enter your choice:\n1.Add a contact\n2.Search a contact\n3.Delete a contact\n4.View all contact\n5.Save Contacts\nTo exit, press e\n"))
    if choice.lower() == "e":
        break
    else:
        choice =int(choice)
        match choice:
            case 1:
                contact_methods.Addcontact()
            case 2:
                contact_methods.searchContact()
            case 3:
                contact_methods.deleteContact()
            case 4:
                contact_methods.viewAllContacts()
            case 5:
                contact_methods.save_contact()
            case _:
                print("invalid choice. please try again\n")
