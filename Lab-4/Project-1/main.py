import os

CONTACT_FILE = "contacts.txt"

def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()
    try:
        with open(CONTACT_FILE, "a") as f:
            f.write(f"{name},{phone}\n")
        print("Contact added successfully.")
    except Exception as e:
        print(f"Error adding contact: {e}")

def view_contacts():
    try:
        with open(CONTACT_FILE, "r") as f:
            contacts = f.readlines()
            if not contacts:
                print("No contacts found.")
                return
            print("\n--- Contact List ---")
            for contact in contacts:
                name, phone = contact.strip().split(",")
                print(f"Name: {name}, Phone: {phone}")
    except FileNotFoundError:
        print("No contact file found. Please add a contact first.")
    except Exception as e:
        print(f"Error reading contacts: {e}")

def search_contact():
    keyword = input("Enter name or phone to search: ").strip().lower()
    try:
        with open(CONTACT_FILE, "r") as f:
            found = False
            for contact in f:
                name, phone = contact.strip().split(",")
                if keyword in name.lower() or keyword in phone:
                    print(f"Name: {name}, Phone: {phone}")
                    found = True
            if not found:
                print("No matching contact found.")
    except FileNotFoundError:
        print("No contact file found.")
    except Exception as e:
        print(f"Error searching contact: {e}")

def delete_contact():
    keyword = input("Enter name or phone to delete: ").strip().lower()
    try:
        with open(CONTACT_FILE, "r") as f:
            contacts = f.readlines()

        updated_contacts = []
        deleted = False

        for contact in contacts:
            name, phone = contact.strip().split(",")
            if keyword in name.lower() or keyword in phone:
                deleted = True
                print(f"Deleted: {name} ({phone})")
            else:
                updated_contacts.append(contact)

        if deleted:
            with open(CONTACT_FILE, "w") as f:
                f.writelines(updated_contacts)
        else:
            print("No contact found to delete.")

    except FileNotFoundError:
        print("No contact file found.")
    except Exception as e:
        print(f"Error deleting contact: {e}")

def main():
    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter choice: ").strip()
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Exiting Contact Book...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
