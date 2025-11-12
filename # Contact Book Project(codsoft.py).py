# Contact Book Project

contacts = {}   # Dictionary to store contact details

# Function to add a new contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
    print("Contact added successfully!\n")

# Function to view all contacts
def view_contacts():
    if not contacts:
        print("No contacts found.\n")
    else:
        print("\n--- Contact List ---")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['Phone']}")
        print()

# Function to search contact by name or phone
def search_contact():
    search = input("Enter name or phone number to search: ")
    found = False
    for name, info in contacts.items():
        if name.lower() == search.lower() or info['Phone'] == search:
            print("\nContact Found:")
            print(f"Name: {name}")
            print(f"Phone: {info['Phone']}")
            print(f"Email: {info['Email']}")
            print(f"Address: {info['Address']}\n")
            found = True
            break
    if not found:
        print("Contact not found.\n")

# Function to update contact details
def update_contact():
    name = input("Enter the name of contact to update: ")
    if name in contacts:
        print("Enter new details (leave blank to keep current):")
        phone = input(f"New phone number ({contacts[name]['Phone']}): ") or contacts[name]['Phone']
        email = input(f"New email ({contacts[name]['Email']}): ") or contacts[name]['Email']
        address = input(f"New address ({contacts[name]['Address']}): ") or contacts[name]['Address']
        contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
        print("Contact updated successfully!\n")
    else:
        print("Contact not found.\n")

# Function to delete a contact
def delete_contact():
    name = input("Enter the name of contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!\n")
    else:
        print("Contact not found.\n")

# Main program loop
while True:
    print("------ Contact Book Menu ------")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Thank you for using Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.\n")
