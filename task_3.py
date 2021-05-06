import re
import os
from task_1 import Employee
from functions import display_menu, exit_program, get_selected_option, search_employees


def program():
    print(display_menu())

    # exit program if selection is 5
    if get_selected_option() == 5:
        exit_program()

    # # do an employee lookup
    # if answer == 1:
    #     employee_id = input("\n1) Look up an employee\n\nEnter employee id: ")

    #     # retrieve an Employee
    #     Employee.get_employee(employee_id)

if __name__ == "__main__":
    program()
