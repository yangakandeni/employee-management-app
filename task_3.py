import re
import os
from task_1 import Employee
from functions import display_menu, exit_program, get_selected_option, search_employees, create_new_employees, display_employees


def program():
    print(display_menu())

    selection = get_selected_option()
    # exit program if selection is 5
    if selection == 5:
        exit_program()
    
    # do employee lookup
    if selection == 1:
        employee_id = input("f\n\nPlease enter employee id: ")
        employee = search_employees(employee_id)

        # print search results
        print(employee)
    
    # add new employee
    if selection == 2:
        create_new_employees()
        display_employees()
    
    # update existing employee
    if selection == 3:
        pass
    


    # # do an employee lookup
    # if answer == 1:
    #     employee_id = input("\n1) Look up an employee\n\nEnter employee id: ")

    #     # retrieve an Employee
    #     Employee.get_employee(employee_id)

if __name__ == "__main__":
    program()
