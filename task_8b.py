from task_8a import ContractEmployee

from functions import create_new_employees, display_employees

def program():
    # create shift workers
    create_new_employees(employee_type="contract_worker", attributes=['name', 'employee_id', 'department', 'job_title', 'contract_end_date', 'contract_salary', 'abn'])

    # display shift workers
    display_employees(employee_type="contract_worker")

if __name__ == "__main__":
    program()
