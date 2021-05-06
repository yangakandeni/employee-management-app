import re
from employee import Employee

def program():
    """ create employee instances """

    while(True):
        create_new_employee = input("\nWould you like to create a new employee?\n(Yes/No): ")

        if not re.match(r'(yes|y)', create_new_employee, re.IGNORECASE):
            # print(f"\nYou entered: '{create_new_employee}'\nprogram exited....\n")
            break
        
        # get user inputs
        name = input("\nEnter employee name: ")
        employee_id = input("\nEnter employee_id: ")
        department = input("\nEnter employee department: ")
        job_tile = input("\nEnter employee position: ")

        # create employee object
        Employee(name=name, employee_id=employee_id, department=department, job_title=job_tile)
    
    # display details of all created employees
    display_details()
    
def display_details():
    """" ask if user wants to see employee details """

    answer = input("\nWould you like to see all your employees?\n(Yes/No): ")

    # check if user wants to view employees
    if not re.match(r'(yes|y)', answer, re.IGNORECASE):
        print(f"\nYou entered: '{answer}'\n\nprogram exited....\n")
        exit()
    
    # check if there's employees created
    if Employee.employees:
        print(f"\nHere are your employees: ")
        Employee.display_details()
        exit()
    
    print(f"\nYou don't have any employees yet: \n")
    
    
if __name__ == "__main__":
    
    # create default employees
    Employee(name="Susanna Myer", employee_id="47899", department="Accounting", job_title="Vice President")
    Employee(name="Mark Joseph", employee_id="39119", department="Info Tech", job_title="Programmer")
    Employee(name="Joyce Roberts", employee_id="81774", department="Manufacturing", job_title="Engineer")
    
    # create employess
    program()


