"""
File Operations Module

This module provides functions for reading from and writing to the text file
that stores employee data.
"""
def read_employees():
     employees_file = open("employees.txt", "r")
    employees_data = employees_file.read()
    lines = employees_data.splitlines()
    employee_list = []
    for line in lines:
        fields = line.split(",")
        employee_data = {
            "id": int(fields[0]),
            "firstname": fields[1],
            "secondname":fields[2],
            "birth":fields[3],
            "startingdate":fields[4],
            "position":fields[5],
            "salary": float(fields[6]),
        }
        employee_list.append(employee_data)
        employees_file.close()
        return employee_list


    """
    Read Employees Function

    This function reads employee data from the text file and returns it.

    Returns:
        list: A list containing employee data read from the text file.
    """


def write_employees():
     employees_file = open("employees.txt", "w")

    for employee in employees_data:
        line = f"{employee['id']},{employee['firstname']},{employee['secondname']},{employee['birth']},{employee['startingdate']},{employee['positon']},{employee['salary']}\n"
        employees_file.write(line)

    employees_file.close()
    """
    Write Employees Function

    This function writes employee data to the text file.

    Parameters:
        employees_data (list): A list containing employee data to be written to the text file.
    """
