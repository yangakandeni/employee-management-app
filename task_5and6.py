from task_1 import Employee

class ShiftEmployee(Employee):
    shift_workers = {}

    def __init__(self, name, employee_id, department, job_title, shift_number, pay_rate):
        super().__init__(name, employee_id, department, job_title)
        self.shift_number = shift_number
        self.pay_rate = pay_rate
        self.staff = {
            'name': self.name,
            'employee_id': self.employee_id,
            'department': self.department,
            'job_title': self.job_title,
            'shfft_number': self.shift_number,
            'pay_rate': self.pay_rate
        }

        # assign employee details to shift_workers dict
        ShiftEmployee.shift_workers.setdefault(self.employee_id, self.staff)
    
    def get_shift_type(self):
        if self.shift_number == 1:
            return "Day Shift"
        elif self.shift_number == 2:
            return "Night Shift"

    # override Employeee display_details() method
    @classmethod
    def display_details(cls):

        # get parent employees dict
        # details = super().employees

        # # add shift number and payrate
        # details.update(cls.shift_workers)

        print(cls.shift_workers)
        # for count, employee in enumerate(cls.shift_workers, 1):
        #     print(f"\nEmployee {count}: {cls.shift_workers.get(employee)}\n")

        return cls.shift_workers

    # override __str__ method
    def __str__(self):
        return f"\nEmployee Name: {self.name}\nID Number: {self.employee_id}\nDepartment: {self.department}\nJob Title: {self.job_title}\nShift: {self.get_shift_type()}\nPay Rate: {self.pay_rate}"
        
    
    

    
    
    
    
    
