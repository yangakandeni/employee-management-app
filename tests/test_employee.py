import unittest

from employee import Employee

class EmployeeTestCase(unittest.TestCase):

    def test_can_create_new_employee(self):
        mike = Employee(name="Mike", id_number="12345", department="Engineering", job_title="Developer")

        self.assertEqual(mike.name, "Mike")
        self.assertEqual(mike.id_number, "12345")
        self.assertEqual(mike.department, "Engineering")
        self.assertEqual(mike.job_title, "Developer")


if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()
