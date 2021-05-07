from task_5and6 import ShiftEmployee

from functions import create_new_employees, display_employees

def program():
    # create shift workers
    create_new_employees(employee_type="shift_worker", attributes=['name', 'employee_id', 'department', 'job_title', 'shift_number', 'pay_rate'])

    # display shift workers
    display_employees(employee_type="shift_worker")


if __name__ == "__main__":
    program()
