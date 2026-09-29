phonebook = {}

while True:
    print("\n--- PHONEBOOK ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display Contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add contact
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")

        phonebook[name] = {
            "phone": phone,
            "email": email
        }
        print("Contact added successfully.")

    # Search contact
    elif choice == "2":
        name = input("Enter name to search: ")

        if name in phonebook:
            print("Phone:", phonebook[name]["phone"])
            print("Email:", phonebook[name]["email"])
        else:
            print("Contact not found.")

    # Update contact
    elif choice == "3":
        name = input("Enter name to update: ")

        if name in phonebook:
            phonebook[name]["phone"] = input("Enter new phone: ")
            phonebook[name]["email"] = input("Enter new email: ")
            print("Contact updated.")
        else:
            print("Contact not found.")

    # Delete contact
    elif choice == "4":
        name = input("Enter name to delete: ")

        if name in phonebook:
            del phonebook[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")

    # Display contacts
    elif choice == "5":
        print("\nNames:", phonebook.keys())
        print("Contact Details:", phonebook.values())

        print("\nAll Contacts:")
        for name, details in phonebook.items():
            print(name, ":", details)

        # List comprehension for names
        names = [name for name in phonebook.keys()]
        print("Names using list comprehension:", names)

    # Exit
    elif choice == "6":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")