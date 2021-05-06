import unittest

from task_1 import Employee

class EmployeeTestCase(unittest.TestCase):

    def setUp(self):
        self.employee_1 = Employee(name="Mike", employee_id="12345", department="Engineering", job_title="Developer")

        self.employee_2 = Employee(name="Yanga", employee_id="54321", department="Engineering", job_title="Developer")
        return super().setUp()

    def test_can_create_new_employee(self):
        mike = self.employee_1

        self.assertEqual(mike.name, "Mike")
        self.assertEqual(mike.employee_id, "12345")
        self.assertEqual(mike.department, "Engineering")
        self.assertEqual(mike.job_title, "Developer")
        self.assertEqual(mike.__str__(
        ), f"\nEmployee Name: {mike.name}\nID Number: {mike.employee_id}\nDepartment: {mike.department}\nJob Title: {mike.job_title}")
        self.assertEqual(len(Employee.employees), 3)
    
    def test_can_retrieve_employee(self):
        
        employee = Employee.get_employee("12345")
        self.assertEqual(employee.get('employee_id'), "12345")

    def test_cannot_retrieve_employee_with_invalid_id(self):
        employee = Employee.get_employee()
        self.assertEqual(employee, f"\nSorry, we could not find an employee with that id\n")
    
    def test_can_add_new_employee(self):
        new_employee = Employee(name="Kendrick", employee_id="88888", department="Music", job_title="Rapper")

        Employee.add_new_employee(new_employee)

        self.assertEqual(len(Employee.employees), 3)
    
    def test_can_update_employee(self):
        updated_employee = Employee.update_details(employee_number="12345", name="Michael", department="Arts", job_title="Artist")

        self.assertEqual(updated_employee.get('name'), "Michael")
        self.assertEqual(updated_employee.get('department'), "Arts")
        self.assertEqual(updated_employee.get('job_title'), "Artist")
    
    def test_can_delete_employee(self):
        deleted_employee = Employee.delete_employee(employee_number="88888")

        self.assertEqual(deleted_employee.get('name'), "Kendrick")


if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()
