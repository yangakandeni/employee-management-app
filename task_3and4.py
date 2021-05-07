import re
import os
from task_1 import Employee
from functions import display_menu, exit_program, get_selected_option, search_employees, create_new_employees, display_employees, update_employee, delete_employee, get_employee_id, load_employees, save_employees


def program():
    print(display_menu(options=[
            "Look up an employee",
            "Add a new employee",
            "Change an existing employee’s details", 
            "Delete an employee", 
            "Quit the program"
        ]
    ))

    selection = get_selected_option(valid_options=[1,2,3,4,5])
    
    # do employee lookup
    if selection == 1:
        employee_id = get_employee_id()
        employee = search_employees(employee_id)

        # print search results
        print(f"\nEMPLOYEE FOUND: \n\n{employee}\n")
    
    # add new employee
    if selection == 2:
        create_new_employees()
        display_employees()
    
    # update existing employee
    if selection == 3:
        employee_id = get_employee_id()
        update_employee(employee_id)

    # delete existing employee
    if selection == 4:
        employee_id = get_employee_id()
        delete_employee(employee_id)
    
    # exit program if selection is 5
    if selection == 5:
        exit_program()


if __name__ == "__main__":
    # create default employees
    # Employee(name="Susanna Myer", employee_id="47899", department="Accounting", job_title="Vice President")
    # Employee(name="Mark Joseph", employee_id="39119", department="Info Tech", job_title="Programmer")
    # Employee(name="Joyce Roberts", employee_id="81774", department="Manufacturing", job_title="Engineer")
    # save_employees(Employee.employees)
    
    employees = load_employees('employees.pickle')
    print(f"\nCURRENT EMPLOYEES:\n{employees}\n")
    program()
