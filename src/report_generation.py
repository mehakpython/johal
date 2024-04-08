"""
Report Generation Module

This module provides a function for generating reports based on employee data.
"""

def generate_reports():
    departments = set(employee["department"] for employee in employees_data)
    department_salaries = {}
    department_employees = {}

    for department in departments:
        department_salaries[department] = sum(employee["salary"] for employee in employees_data if employee["department"] == department)
        department_employees[department] = [
            employee for employee in employees_data if employee["department"] == department
        ]

    report_1 = list(departments)

    report_2 = [
        {"id": employee["id"], "full_name": f"{employee['first_name']} {employee['last_name']}", "department": employee["department"]}
        for employee in employees_data
    ]

    report_3 = [
        {
"department": department,
            "average_age": sum(employee["age"] for employee in employees_data if employee["department"] == department) / len(department_employees[department]),
            "average_salary": department_salaries[department] / len(department_employees[department]),
        }
        for department in departments
    ]

    report_4 = []
    for department in departments:
        for employee in department_employees[department]:
            report_4.append(
                {
                    "id": employee["id"],
                    "full_name": f"{employee['first_name']} {employee['last_name']}",
                    "date_of_birth": employee["date_of_birth"],
                    "salary": employee["salary"],
                    "total_salary_for_department": department_salaries[department],
                }
            )

    return {
        "report_1": report_1,
        "report_2": report_2,
        "report_3": report_3,
        "report_4": report_4,
    }
    
    """
    Generate Reports Function

    This function generates various reports based on employee data, such as:
    - List of departments
    - List of all employees with ID, full name, and department
    - List of all departments with the average age and salary of employees
    - List of employees in each department with ID, full name, date of birth, salary,
      and total salary for department's employees
    """
