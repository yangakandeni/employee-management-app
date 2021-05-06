class Employee:
    # stores employees
    employees = {}

    def __init__(self, name, employee_id, department, job_title):
        self.name = name
        self.department = department
        self.employee_id = employee_id
        self.job_title = job_title
        # create staff dict to store employee details
        self.staff = {
            'Name': self.name,
            'ID': self.employee_id,
            'Department': self.department,
            'Position': self.job_title
        }

        # assign employee details to staff dict
        Employee.employees.setdefault(self.employee_id, self.staff)

    @classmethod
    def get_employee(cls, employee_number):

        try:
            return cls.employees.get(employee_number)
        except Exception:
            print(f"\nSorry, we could not find an employee with that id\n")

    @classmethod
    def display_employees(cls):
        return cls.employees

    def __str__(self):
        return f"\nEmployee Name: {self.name}\nID Number: {self.employee_id}\nDepartment: {self.department}\nJob Title: {self.job_title}"
