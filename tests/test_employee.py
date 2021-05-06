import unittest

from employee import Employee

class EmployeeTestCase(unittest.TestCase):

    def setUp(self):
        self.employee_1 = Employee(name="Mike", employee_id="12345",
                        department="Engineering", job_title="Developer")

        self.employee_2 = Employee(name="Yanga", employee_id="54321",
                                   department="Engineering", job_title="Developer")
        return super().setUp()

    def test_can_create_new_employee(self):
        mike = self.employee_1

        self.assertEqual(mike.name, "Mike")
        self.assertEqual(mike.employee_id, "12345")
        self.assertEqual(mike.department, "Engineering")
        self.assertEqual(mike.job_title, "Developer")
        self.assertEqual(mike.__str__(
        ), f"\nEmployee Name: {mike.name}\nID Number: {mike.employee_id}\nDepartment: {mike.department}\nJob Title: {mike.job_title}")
        self.assertEqual(len(Employee.employees), 2)
    
    def test_can_store_employees(self):
        #
        pass


if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()
