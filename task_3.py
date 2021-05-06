import re
import os
from task_1 import Employee
from functions import display_menu, exit_program, get_selected_option, search_employees, create_new_employees, display_employees, update_employee, delete_employee, get_employee_id


def program():
    print(display_menu(
        option_1="Look up an employee", 
        option_2="Add a new employee", 
        option_3="Change an existing employee’s details", 
        option_4="Delete an employee", 
        option_5="Quit the program"
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
    Employee(name="Mike", employee_id="12345", department="Engineering", job_title="Developer")
    program()
