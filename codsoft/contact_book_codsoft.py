contacts = []

def display_menu():
    print("Contact Menu")
    print("1. Add contact")
    print("2. Search contact")
    print("3. Update contact")
    print("4. Delete contact")
    print("5. Display all the contacts")
    print("6. Exit")
def add_contact():
    name = input("Enter the contact's name: ")
    email = input("Enter their email: ")
    phone = input("Enter their phone number: ")
    contact = {"Name": name, "Email": email, "Phone": phone}
    contacts.append(contact)
    print("Contact added successfully!!")
def search_contact():

    search_term = input("Enter the name or email of the person you want to search: ")
    found_contacts = []
    for contact in contacts:
        if search_term.lower() in contact["Name"].lower() or search_term.lower() in contact["Email"].lower():
            found_contacts.append(contact)

    if found_contacts:
        print("Matching contacts found:")
        for contact in found_contacts:
            print("Name :", contact["Name"])
            print("Email :", contact["Email"])
            print("Phone :", contact["Phone"])
            print("~~~~~~~~~~~~~~~~~~~~~~~~")
    else:
        print(" Oops ~ No matching contacts found.")
def update_contact():

    name = input("Enter the name of the contact to update: ")
    found_contact = None
    for contact in contacts:
        if contact["Name"].lower() == name.lower():
            found_contact = contact

    if found_contact:
        print("Contact found. Enter the new details:")
        found_contact["Name"] = input("Enter new name: ")
        found_contact["Email"] = input("Enter new email: ")
        found_contact["Phone"] = input("Enter new phone number: ")
        print(" Done. Contact updated successfully!")
    else:
        print(" Oh no ! Contact not found.")
def delete_contact():

    name = input("Enter the name of the contact to delete: ")
    for contact in contacts:
        if contact["Name"].lower() == name.lower():
            contacts.remove(contact)
            print("Contact deleted successfully!")
            break
    else:
        print(" Oh no ! Contact not found.")
def display_all_contacts():

    if contacts:
        print("All Contacts:")

        for contact in contacts:
            print("------------------- ")
            print("Name:", contact["Name"])
            print("Email:", contact["Email"])
            print("Phone:", contact["Phone"])
            print("-------------------")
    else:
        print("No contacts found.")

while True:
    display_menu()


    choice = input(" Your choice please? ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        display_all_contacts()
    elif choice == "6":
        print("THANK YOU \n Bye!!")
        break
    else:
        print("Invalid choice.Kindly enter a valid option.")


