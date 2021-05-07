import unittest
from task_5and6 import ShiftEmployee

class ShiftEmployeeTestCase(unittest.TestCase):

    def setUp(self):
        self.employee = ShiftEmployee(employee_id="12345", name="Michael", department="Arts", job_title="Artist", shift_number=1, pay_rate=15.5)
        return super().setUp()
    
    def test_shift_employee_details(self):
        self.assertEqual(self.employee.name, "Michael")
        self.assertEqual(self.employee.employee_id, "12345")
        self.assertEqual(self.employee.department, "Arts")
        self.assertEqual(self.employee.job_title, "Artist")
        self.assertEqual(self.employee.shift_number, 1)
        self.assertEqual(self.employee.pay_rate, 15.5)
        self.assertDictEqual(ShiftEmployee.display_details(), ShiftEmployee.employees)
        self.assertEqual(self.employee.__str__(), f"\nEmployee Name: {self.employee.name}\nID Number: {self.employee.employee_id}\nDepartment: {self.employee.department}\nJob Title: {self.employee.job_title}\nShift: {self.employee.get_shift_type()}\nPay Rate: {self.employee.pay_rate}")
    
    def test_add_new_shift_worker(self):
        employee = ShiftEmployee(employee_id="5555", name="Mike", department="Science", job_title="Scientist", shift_number=1, pay_rate=15.5)

        ShiftEmployee.add_new_employee(employee)

        self.assertEqual(len(ShiftEmployee.employees), 2)
