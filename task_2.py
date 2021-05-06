import re
from task_1 import Employee
from functions import create_new_employees, display_employees

def program():
    """ create and display employee instances """
    create_new_employees()

    display_employees()
    
if __name__ == "__main__":
    
    # create default employees
    Employee(name="Susanna Myer", employee_id="47899", department="Accounting", job_title="Vice President")
    Employee(name="Mark Joseph", employee_id="39119", department="Info Tech", job_title="Programmer")
    Employee(name="Joyce Roberts", employee_id="81774", department="Manufacturing", job_title="Engineer")
    
    # create employess
    program()


