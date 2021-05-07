from task_1 import Employee


class ContractEmployee(Employee):
    contract_workers = {}

    def __init__(self, name, employee_id, department, job_title, contract_end_date, contract_salary, abn):
        super().__init__(name, employee_id, department, job_title)
        self.contract_end_date = contract_end_date
        self.contract_salary = contract_salary
        self.abn = abn
        self.staff = {
            'name': self.name,
            'employee_id': self.employee_id,
            'department': self.department,
            'job_title': self.job_title,
            'contract_end_date': self.contract_end_date,
            'contract_salary': self.contract_salary,
            'abn': self.abn
        }

        # assign employee details to contract_workers dict
        ContractEmployee.contract_workers.setdefault(self.employee_id, self.staff)

    def get_contract_type(self):
        if self.contract_end_date == 1:
            return "Day Contract"
        elif self.contract_end_date == 2:
            return "Night Contract"

    # override Employeee display_details() method
    @classmethod
    def display_details(cls):

        print(cls.contract_workers)

        return cls.contract_workers

    # override __str__ method
    def __str__(self):
        return f"\nEmployee Name: {self.name}\nID Number: {self.employee_id}\nDepartment: {self.department}\nJob Title: {self.job_title}\nContract: {self.get_contract_type()}\nPay Rate: {self.contract_salary}"
