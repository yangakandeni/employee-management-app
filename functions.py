import re

from task_1 import Employee

"""" THIS FILE CONTAINS HELPER FUNCTIONS """


def create_new_employees():
    while(True):
        response = input("\nWould you like to add a new employee?\n(Yes/No): ")

        if not re.match(r'(yes|y)', response, re.IGNORECASE):
            # print(f"\nYou entered: '{response}'\nprogram exited....\n")
            return Employee.employees

        # get user inputs
        name = input("\nEnter employee name: ")
        employee_id = input("\nEnter employee_id: ")
        department = input("\nEnter employee department: ")
        job_tile = input("\nEnter employee position: ")

        # create employee object
        Employee(name=name, employee_id=employee_id,
                 department=department, job_title=job_tile)

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


def display_menu(option_1=None, option_2=None, option_3=None, option_4=None, option_5=None):
    """ display program menu"""

    menu = f"\nPROGRAM MENU:\n1) {option_1}\n2) {option_2}\n3) {option_3}\n4) {option_4}\n5) {option_5}"

    return menu

def get_selected_option(valid_options=[]):
    """ prompt user to choose valid menu option """

    response = input(f"\nChoose between {valid_options[0]} to {valid_options[-2]} OR press {valid_options[-1]} to quit: ")
    try:
        # convert response to int
        response = int(response)

    except ValueError:
        # print(f'\nYour options are => {valid_options}')
        pass

    # continue to prompt user for a valid option
    while(response not in valid_options):
        print(f"\n'{response}' is not a valid option\nPlease try again..")
        response = input(f"\nChoose between {valid_options[0]} to {valid_options[-2]} OR press {valid_options[-1]} to quit: ")

        try:
            # convert response to int
            response = int(response)
        except ValueError:
            # print(f'\nYour options are => {valid_options}')
            pass

    return response

def search_employees(employee_id=None):
    return Employee.get_employee(employee_id)

def exit_program():
    """" exit program"""
    print(f"\nprogram exited....\n")
    exit()


def get_employee_id():
    employee_id = input("f\n\nPlease enter employee id: ")
    return employee_id

def update_employee(employee_id=None):
    # define variables
    name = None
    department = None
    job_title = None

    employee = search_employees(employee_id)

    if type(employee) is not str:
        print(f"\nWould you like to update about '{employee.get('name')}'?{display_menu(option_1='Name', option_2='Department', option_3='Job Title', option_4='All')}")

        response = get_selected_option(valid_options=[1,2,3,4,5])

        if response == 5: exit_program()

        elif response == 1:
            name = input(f"\nChange '{employee.get('name')}' to : ")

        elif response == 2:
            department = input(f"\nChange '{employee.get('department')}' to : ")
            
        elif response == 3:
            job_title = input(f"\nChange '{employee.get('job_title')}' to : ")
        
        elif response == 4:
            name = input(f"\nChange '{employee.get('name')}' to : ")
            department = input(f"\nChange '{employee.get('department')}' to : ")
            job_title = input(f"\nChange '{employee.get('job_title')}' to : ")

        updated =  Employee.update_details(employee_id, name=name, department=department, job_title=job_title)

        print(f"\nUPDATED:\n\n{updated}\n")
        return updated
    else:
        print(employee)

def delete_employee(employee_id=None):
    return Employee.delete_employee(employee_id)
