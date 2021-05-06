class Employee:
    def __init__(self, name, id_number, department, job_title):
        self.name = name
        self.department = department
        self.id_number = id_number
        self.job_title = job_title
        
    def __str__(self):
        return f"\nEmployee Name: {self.name}\nID Number: {self.id_number}\nDepartment: {self.department}\nJob Title: {self.job_title}"