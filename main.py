from operations import *

def menu():
    while True:
        print("===================================")
        print("  EMPLOYEE MANAGEMENT SYSTEM")
        print("===================================")
        print("1. Load Data from File")
        print("2. Add Employee")
        print("3. View Employees")
        print("4. Search Employee")
        print("5. Update Employee")
        print("6. Delete Employee")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            load_data()
        elif choice == "2":
            add_employee()
        elif choice == "3":
            view_employees()
        elif choice == "4":
            search_employee()
        elif choice == "5":
            update_employee()
        elif choice == "6":
            delete_employee()
        elif choice == "7":
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice!\n")

menu()