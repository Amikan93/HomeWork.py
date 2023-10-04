import json

class Employee:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

def save_to_file(employees, filename):
    with open(filename, 'w') as file:
        json.dump(employees, file, default=lambda x: x.__dict__)

def load_from_file(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            employees = [Employee(**employee) for employee in data]
        return employees
    except FileNotFoundError:
        return []

def display_all(employees):
    for employee in employees:
        print(f"{employee.first_name} {employee.last_name}, {employee.age} years old")

def add_employee(employees):
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    age = int(input("Enter age: "))
    employees.append(Employee(first_name, last_name, age))
    print("Employee added successfully!")

def edit_employee(employees, last_name):
    for employee in employees:
        if employee.last_name == last_name:
            employee.first_name = input("Enter new first name: ")
            employee.last_name = input("Enter new last name: ")
            employee.age = int(input("Enter new age: "))
            print("Employee information updated successfully!")
            return
    print(f"No employee found with last name {last_name}")

def delete_employee(employees, last_name):
    for employee in employees:
        if employee.last_name == last_name:
            employees.remove(employee)
            print("Employee deleted successfully!")
            return
    print(f"No employee found with last name {last_name}")

def search_by_last_name(employees, last_name):
    found_employees = [employee for employee in employees if employee.last_name == last_name]
    if found_employees:
        display_all(found_employees)
    else:
        print(f"No employee found with last name {last_name}")

def search_by_age(employees, age):
    found_employees = [employee for employee in employees if employee.age == age]
    if found_employees:
        display_all(found_employees)
    else:
        print(f"No employee found with age {age}")

def search_by_first_letter(employees, letter):
    found_employees = [employee for employee in employees if employee.last_name.startswith(letter)]
    if found_employees:
        display_all(found_employees)
    else:
        print(f"No employee found with last name starting with {letter}")

# Основной блок программы
filename = input("Enter filename for employee data: ")
employees = load_from_file(filename)

while True:
    print("\n1. Display all employees")
    print("2. Add employee")
    print("3. Edit employee")
    print("4. Delete employee")
    print("5. Search by last name")
    print("6. Search by age")
    print("7. Search by first letter of last name")
    print("8. Save and exit")
    
    choice = input("\nEnter your choice (1-8): ")

    if choice == '1':
        display_all(employees)
    elif choice == '2':
        add_employee(employees)
    elif choice == '3':
        last_name = input("Enter last name of employee to edit: ")
        edit_employee(employees, last_name)
    elif choice == '4':
        last_name = input("Enter last name of employee to delete: ")
        delete_employee(employees, last_name)
    elif choice == '5':
        last_name = input("Enter last name to search: ")
        search_by_last_name(employees, last_name)
    elif choice == '6':
        age = int(input("Enter age to search: "))
        search_by_age(employees, age)
    elif choice == '7':
        letter = input("Enter first letter of last name to search: ")
        search_by_first_letter(employees, letter)
    elif choice == '8':
        save_to_file(employees, filename)
        print("Data saved. Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 8.")
