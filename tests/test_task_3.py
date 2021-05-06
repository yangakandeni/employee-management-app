
import unittest

from functions import display_menu, get_selected_option, exit_program, search_employees, display_employees
from task_1 import Employee

class TASK3TestCase(unittest.TestCase):

    def setUp(self):

        Employee(name="Mike", employee_id="12345", department="Engineering", job_title="Developer")
        return super().setUp()

    def test_can_display_menu(self):
        menu = display_menu(options=[
                    "Look up an employee",
                    "Add a new employee",
                    "Change an existing employee’s details", 
                    "Delete an employee", 
                    "Quit the program"
                ]
            )

        self.assertEqual(menu, f"\nPROGRAM MENU:\n1) Look up an employee\n2) Add a new employee\n3) Change an existing employee’s details\n4) Delete an employee\n5) Quit the program")

        
    def test_can_choose_option(self):
        valid_options = [1, 2, 3, 4, 5]
        answer = get_selected_option(valid_options=[1, 2, 3, 4, 5])

        self.assertTrue(answer in valid_options)
    
        with self.assertRaises(SystemExit):
            exit_program()
    
    def test_can_search_employees(self):
        employee = search_employees("12345")
        self.assertEqual(employee.get('name'), 'Mike')

    
