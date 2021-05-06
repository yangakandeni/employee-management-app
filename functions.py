from task_1 import Employee

"""" THIS FILE CONTAINS HELPER (TASK 3) FUNCTIONS """

def display_menu():
    """ display program menu"""

    menu = f"\nPROGRAM MENU:\n1) Look up an employee\n2) Add a new employee\n3) Change an existing employee’s details\n4) Delete an employee\n5) Quit the program"

    return menu

def get_selected_option():
    """ prompt user to choose valid menu option """
    valid_options = [1, 2, 3, 4, 5]

    answer = input("\nChoose between 1 to 4 OR press 5 to quit: ")
    try:
        # convert answer to int
        answer = int(answer)

    except ValueError:
        # print(f'\nYour options are => {valid_options}')
        pass

    # continue to prompt user for a valid option
    while(answer not in valid_options):
        print(f"\n'{answer}' is not a valid option\nPlease try again..")
        answer = input("\nChoose between 1 to 4 OR press 5 to quit: ")

        try:
            # convert answer to int
            answer = int(answer)
        except ValueError:
            # print(f'\nYour options are => {valid_options}')
            pass

    return answer

def search_employees(employee_id=None):
    # try:
    #     employee = Employee.get_employee(employee_id)
    #     return employee
    # except AttributeError:
    #     print("oops")
    pass
    


def exit_program():
    exit()
