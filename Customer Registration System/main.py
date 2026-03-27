# Customer registration system
import random
from datetime import datetime

system = []

# --- functions ---

def add_customers():
    while True:
        first_name = input("Enter first name: ").strip()
        if first_name == "":
            print("No first name provided! Returning to menu.\n")
            return

        last_name = input("Enter last name: ").strip()
        if last_name == "":
            print("No last name provided! Returning to menu.\n")
            return

        while True:
            birth_date = input("Enter birth date dd.mm.yyyy: ").strip()
            if birth_date == "":
                print("No date provided! Returning to menu.\n")
                return
            try:
                datetime.strptime(birth_date, "%d.%m.%Y")
                break
            except ValueError:
                print("Invalid date format! Try again.\n")

        # Generate unique index
        index = random.randint(1000, 9999)
        while any(k["Index"] == index for k in system):
            index = random.randint(1000, 9999)

        customer = {"FirstName": first_name, "LastName": last_name, "BirthDate": birth_date, "Index": index}
        system.append(customer)

        print("\nCustomer added:")
        print("----------------------")
        print(f"ID: {customer['Index']}")
        print(f"First name: {customer['FirstName']}")
        print(f"Last name: {customer['LastName']}")
        print(f"Birth date: {customer['BirthDate']}")
        print("----------------------")
        
        continue_choice = input("Do you want to add another person? (y/n): ").lower()
        if continue_choice != "y":
            break


def edit_customer():
    try:
        index = int(input("Enter customer index: ").strip())
    except ValueError:
        print("Invalid index! Returning to menu.\n")
        return

    for customer in system:
        if customer["Index"] == index:
            print("Customer found:", customer)

            new_first_name = input("Enter new first name (Enter = no change): ").strip()
            if new_first_name != "":
                customer["FirstName"] = new_first_name

            new_last_name = input("Enter new last name (Enter = no change): ").strip()
            if new_last_name != "":
                customer["LastName"] = new_last_name

            new_birth_date = input("Enter new birth date (Enter = no change): ").strip()
            if new_birth_date != "":
                try:
                    datetime.strptime(new_birth_date, "%d.%m.%Y")
                    customer["BirthDate"] = new_birth_date
                except ValueError:
                    print("Invalid date format! Date not changed.\n")

            print("Updated!")
            return

    print("Customer not found.\n")


def delete_customer():
    try:
        index = int(input("Enter customer index: ").strip())
    except ValueError:
        print("Invalid index! Returning to menu.\n")
        return

    for customer in system:
        if customer["Index"] == index:
            system.remove(customer)
            print("Customer deleted.")
            return

    print("Customer not found.\n")


def show_customers():
    if len(system) == 0:
        print("No customers in the system.\n")
    else:
        for customer in system:
            print("----------------------")
            print(f"ID: {customer['Index']}")
            print(f"First name: {customer['FirstName']}")
            print(f"Last name: {customer['LastName']}")
            print(f"Birth date: {customer['BirthDate']}")
            print("----------------------")


def search_customers():
    data = input("Enter customer data: ").strip()
    if data == "":
        print("No data provided! Returning to menu.\n")
        return

    found = False

    for customer in system:
        if customer["FirstName"].lower() == data.lower():
            print("----------------------")
            print(f"ID: {customer['Index']}")
            print(f"First name: {customer['FirstName']}")
            print(f"Last name: {customer['LastName']}")
            print(f"Birth date: {customer['BirthDate']}")
            print("----------------------")
            found = True
        
        if customer["LastName"].lower() == data.lower():
            print("----------------------")
            print(f"ID: {customer['Index']}")
            print(f"First name: {customer['FirstName']}")
            print(f"Last name: {customer['LastName']}")
            print(f"Birth date: {customer['BirthDate']}")
            print("----------------------")
            found = True
        
        if customer["BirthDate"] == data:
            print("----------------------")
            print(f"ID: {customer['Index']}")
            print(f"First name: {customer['FirstName']}")
            print(f"Last name: {customer['LastName']}")
            print(f"Birth date: {customer['BirthDate']}")
            print("----------------------")
            found = True
        
        if str(customer["Index"]) == data:
            print("----------------------")
            print(f"ID: {customer['Index']}")
            print(f"First name: {customer['FirstName']}")
            print(f"Last name: {customer['LastName']}")
            print(f"Birth date: {customer['BirthDate']}")
            print("----------------------")
            found = True

    if not found:
        print("Customer not found.\n")


def save_to_file():
    with open("customers.txt", "w") as file:
        for customer in system:
            file.write(str(customer) + "\n")
    print("Saved to file.")


# --- menu ---

while True:
    print("What do you want to do?\n")
    print("1 - Add customer")
    print("2 - Edit customer")
    print("3 - Delete customer")
    print("4 - Show customers")
    print("5 - Search customer")
    print("6 - Save to file")
    print("0 - Exit")

    selected_action = input("\nChoose option: ").strip()

    if selected_action == "1":
        add_customers()
    elif selected_action == "2":
        edit_customer()
    elif selected_action == "3":
        delete_customer()
    elif selected_action == "4":
        show_customers()
    elif selected_action == "5":
        search_customers()
    elif selected_action == "6":
        save_to_file()
    elif selected_action == "0":
        break
    else:
        print("Unknown action.\n")

print("End of program")
