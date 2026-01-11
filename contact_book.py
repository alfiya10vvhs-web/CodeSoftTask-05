# Contact Book Application

contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
        return

    print("\nContact List:")
    for name, info in contacts.items():
        print(f"Name: {name}, Phone: {info['phone']}")

def search_contact():
    search = input("Enter name or phone number to search: ")

    found = False
    for name, info in contacts.items():
        if search.lower() in name.lower() or search == info["phone"]:
            print("\nContact Found:")
            print(f"Name: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print(f"Address: {info['address']}")
            found = True

    if not found:
        print("Contact not found.")

def update_contact():
    name = input("Enter name of contact to update: ")

    if name in contacts:
        print("Leave blank to keep existing value.")

        phone = input("New phone number: ")
        email = input("New email: ")
        address = input("New address: ")

        if phone:
            contacts[name]["phone"] = phone
        if email:
            contacts[name]["email"] = email
        if address:
            contacts[name]["address"] = address

        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name of contact to delete: ")

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

while True:
    print("\n---- CONTACT BOOK MENU ----")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
