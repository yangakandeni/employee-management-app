
import unittest

from functions import display_menu, get_selected_option, exit_program, search_employees, display_employees, load_employees, save_employees
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

    def test_can_pickle_employees_to_file(self):
        employees = Employee.employees
        response = save_employees(employees)

        self.assertDictEqual(response, employees)

    def test_can_load_employees_from_pickle(self):
        pickled_data = save_employees(Employee.employees, filename='test')
        employees = load_employees(filepath='test.pickle')

        self.assertDictEqual(employees, pickled_data)
    
    def test_cannot_load_with_invalid_filepath(self):
        employees = load_employees(filepath='')
        self.assertDictEqual(employees, dict())
    
    def test_can_append_picked_file(self):
        pickled_data = save_employees(Employee.employees, filename='test')
        employees = load_employees(filepath='test.pickle')

