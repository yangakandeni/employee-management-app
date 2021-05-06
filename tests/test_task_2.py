from functions import create_new_employees, display_employees
from unittest import TestCase
from task_1 import Employee

class AddNewEmployeesTestCase(TestCase):

    def setUp(self):
        Employee(name="Mike", employee_id="12345", department="Engineering", job_title="Developer")
        return super().setUp()

    def test_can_create_new_employees(self):
        employees = create_new_employees()
        self.assertEqual(employees, Employee.employees)

    def test_can_display_employees(self):
        employees = display_employees()

        self.assertEqual(employees, Employee.employees)

