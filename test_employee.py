import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('setUpClass')

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass")

    def setUp(self) -> None:
        print("setUp")
        self.emp_1 = Employee('Dodullo', 'Khayrulloev', 50000)
        self.emp_2 = Employee('Umar', 'Umarov', 60000)

    def tearDown(self) -> None:
        print("tearDown\n")
        pass

    def test_email(self):
        print("test_email")
        self.assertEqual(self.emp_1.email, "Dodullo.Khayrulloev@mail.com")
        self.assertEqual(self.emp_2.email, "Umar.Umarov@mail.com")

        self.emp_1.first = 'Sam'
        self.emp_2.first = 'Armstrong'

        self.assertEqual(self.emp_1.email, "Sam.Khayrulloev@mail.com")
        self.assertEqual(self.emp_2.email, "Armstrong.Umarov@mail.com")

    def test_fullname(self):
        print("test_fullname")
        self.assertEqual(self.emp_1.fullname, "Dodullo Khayrulloev")
        self.assertEqual(self.emp_2.fullname, "Umar Umarov")

        self.emp_1.first = 'Sam'
        self.emp_2.first = 'Armstrong'

        self.assertEqual(self.emp_1.fullname, "Sam Khayrulloev")
        self.assertEqual(self.emp_2.fullname, "Armstrong Umarov")

    def test_apply_raise(self):
        print("test_apply_raise")
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):
        print("test_monthly_schedule")
        with patch('employee.requests.get') as mocked_get:
            # True case
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Khayrulloev/May')
            self.assertEqual(schedule, 'Success')

            # False case
            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Umarov/June')
            self.assertEqual(schedule, 'Bad request.')


if __name__ == '__main__':
    unittest.main()
