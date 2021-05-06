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
            'name': self.name,
            'employee_id': self.employee_id,
            'department': self.department,
            'job_title': self.job_title
        }

        # assign employee details to staff dict
        Employee.employees.setdefault(self.employee_id, self.staff)

    @classmethod
    def get_employee(cls, employee_number=None):
        """
        params: cls: Employee class
        params: employee_number: employee id to lookup
        """

        try:
            employee = cls.employees.get(employee_number, None)

            # raise lookup error if employee is None
            if not employee: raise LookupError
            else: return employee
        except LookupError:
            return f"\nSorry, we could not find an employee with that id\n"
    
    @classmethod
    def add_new_employee(cls, new_employee):
        """
        Add new employee to the employees dict
        """

        # add new employee to employees dict
        Employee.employees.setdefault(new_employee.employee_id, new_employee)

        return cls.get_employee(new_employee.employee_id)

    @classmethod
    def update_details(cls, employee_number, name=None, department=None, job_title=None):
        """
        Lookup employee with provided employee_number
        Update employee info with provided details
        """

        # lookup employee to modify
        try:
            current_employee = Employee.get_employee(employee_number)

            # new details
            new_details = {}
            if name: new_details.setdefault('name', name)
            if department: new_details.setdefault('department', department)
            if job_title: new_details.setdefault('job_title', job_title)

            # update employee details
            current_employee.update(new_details)

            return current_employee
        except AttributeError:
            return f"\nSorry, we could not find an employee with that id\n"

    @classmethod 
    def delete_employee(cls, employee_number):
        try:
            deleted_employee = Employee.employees.pop(employee_number)

            if deleted_employee is None: raise KeyError()
            else: return deleted_employee

        except KeyError:
            print(f"\nSorry, we could not find an employee with that id\n")
            return 
    
    @classmethod
    def display_details(cls):
        for count, employee in enumerate(cls.employees, 1):
            print(f"\nEmployee {count}: {cls.employees.get(employee)}\n")

        return cls.employees
    def __str__(self):
        return f"\nEmployee Name: {self.name}\nID Number: {self.employee_id}\nDepartment: {self.department}\nJob Title: {self.job_title}"
