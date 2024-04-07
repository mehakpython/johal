"""
Employee Management System Module

This module provides various functionalities for managing employee data, 
including adding, deleting, updating, and generating reports.
"""
import src.menu as menu

def main():
    """
    Main function to start the Employee Management System.
    
    This function calls the main_menu() function to display the main menu
    of the Employee Managemen  t System to the user.
    """
    menu.main_menu()

if __name__ == "__main__":
    main()
    """
    Employee Operations Module

    This module provides functions for adding, deleting, and updating employee information.
    """


    def add_employee():
        def add_employee(employees):
            name = input("Enter employee name: ")
            age = input("Enter employee age: ")
            position = input("Enter employee position: ")

            new_employee = {
                'name': name,
                'age': age,
                'position': position
            }

            employees.append(new_employee)
            print("Employee added successfully.")

        employees_list = []

        add_employee(employees_list)

        print("Updated List of Employees:")
        print(employees_list)

        """
        Add Employee Function

        This function prompts the user to input details for a new employee and adds the employee
        to the system.

        """


    def delete_employee():
        def delete_employee(employees):
            name = input("Enter the name of the employee you want to delete: ")
            found = False

            for employee in employees:
                if employee['name'] == name:
                    employees.remove(employee)
                    found = True
                    print("Employee '{}' deleted successfully.".format(name))
                    break

            if not found:
                print("Employee '{}' not found.".format(name))

        employees_list = [
            {'name': 'Adams', 'age': 30, 'position': 'Manager'},
            {'name': 'Nick', 'age': 25, 'position': 'Developer'},
            {'name': 'Smith', 'age': 35, 'position': 'Designer'}
        ]

        delete_employee(employees_list)

        print("Updated List of Employees:")
        print(employees_list)

        """
        Delete Employee Function

        This function prompts the user to input the ID of the employee to be deleted and
        removes the employee from the system.

        """


    def update_employee():
        def update_employee(employees):
            name = input("Enter the name of the employee you want to update: ")
            found = False

            for employee in employees:
                if employee['name'] == name:
                    print("Employee found. Enter the new details:")
                    new_name = input("Enter new name (leave blank to keep the same): ")
                    new_age = input("Enter new age (leave blank to keep the same): ")
                    new_position = input("Enter new position (leave blank to keep the same): ")

                    if new_name:
                        employee['name'] = new_name
                    if new_age:
                        employee['age'] = new_age
                    if new_position:
                        employee['position'] = new_position

                    found = True
                    print("Employee '{}' updated successfully.".format(name))
                    break

            if not found:
                print("Employee '{}' not found.".format(name))

        employees_list = [
            {'name': 'John', 'age': 30, 'position': 'Manager'},
            {'name': 'Alice', 'age': 25, 'position': 'Developer'},
            {'name': 'Bob', 'age': 35, 'position': 'Designer'}
        ]

        update_employee(employees_list)

        print("Updated List of Employees:")
        print(employees_list)
        """
        Update Employee Function

        This function prompts the user to input the ID of the employee to be updated and
        allows the user to modify the employee's information such as name, department, or salary.

        """

