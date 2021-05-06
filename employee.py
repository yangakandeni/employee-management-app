class Employee:
    # stores all the created employees
    employees = dict()

    def __init__(self, name, employee_id, department, job_title):
        self.name = name
        self.department = department
        self.employee_id = employee_id
        self.job_title = job_title

        # saves an employee instance to the employees dict
        Employee.employees.setdefault(self.employee_id, {
            'Name': self.name,
            'ID': self.employee_id,
            'Department': self.department,
            'Position': self.job_title
        })

    def __str__(self):
        return f"\nEmployee Name: {self.name}\nID Number: {self.employee_id}\nDepartment: {self.department}\nJob Title: {self.job_title}"