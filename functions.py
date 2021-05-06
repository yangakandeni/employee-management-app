import re

from task_1 import Employee

"""" THIS FILE CONTAINS HELPER FUNCTIONS """

def display_menu():
    """ display program menu"""

    menu = f"\nPROGRAM MENU:\n1) Look up an employee\n2) Add a new employee\n3) Change an existing employee’s details\n4) Delete an employee\n5) Quit the program"

    return menu

def get_selected_option():
    """ prompt user to choose valid menu option """
    valid_options = [1, 2, 3, 4, 5]

    response = input("\nChoose between 1 to 4 OR press 5 to quit: ")
    try:
        # convert response to int
        response = int(response)

    except ValueError:
        # print(f'\nYour options are => {valid_options}')
        pass

    # continue to prompt user for a valid option
    while(response not in valid_options):
        print(f"\n'{response}' is not a valid option\nPlease try again..")
        response = input("\nChoose between 1 to 4 OR press 5 to quit: ")

        try:
            # convert response to int
            response = int(response)
        except ValueError:
            # print(f'\nYour options are => {valid_options}')
            pass

    return response

def search_employees(employee_id=None):
    employee = Employee.get_employee(employee_id)
    return employee

def create_new_employees():
    while(True):
        response = input("\nWould you like to create a new employee?\n(Yes/No): ")

        if not re.match(r'(yes|y)', response, re.IGNORECASE):
            print(f"\nYou entered: '{response}'\nprogram exited....\n")
            return Employee.employees

        # get user inputs
        name = input("\nEnter employee name: ")
        employee_id = input("\nEnter employee_id: ")
        department = input("\nEnter employee department: ")
        job_tile = input("\nEnter employee position: ")

        # create employee object
        Employee(name=name, employee_id=employee_id, department=department, job_title=job_tile)

    return Employee.employees

def display_employees():
    """" display created employees """

    employees = None
    response = input("\nWould you like to see all your employees?\n(Yes/No): ")

    # check if user wants to view employees
    if not re.match(r'(yes|y)', response, re.IGNORECASE):
        print(f"\nYou entered: '{response}'\nprogram exited....\n")
        employees = Employee.employees
        return employees

    # check if there's employees created
    if Employee.employees:
        print(f"\nHere are your employees: ")
        employees = Employee.display_details()
        return employees
    
    print(f"\nYou don't have any employees yet: \n")
    return employees

def exit_program():
    """" exit program"""
    exit()
