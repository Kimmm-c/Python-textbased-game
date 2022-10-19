import io
import unittest
from unittest import TestCase
from unittest.mock import patch
from game import class_assignment
from game import CLASS_B_STARTING_POINT, CLASS_A_STARTING_POINT


class TestClassAssignment(TestCase):
    @patch('builtins.input', side_effect=['1'])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_class_assignment_print_classes(self, mock_stdout, mock_input):
        expected = "1 MMA Fighter\n"\
                   "2 Olympic Archer\n"\
                   "3 Unemployed Magician\n"\
                   "4 Elite Fencer\n"
        class_assignment()
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['2'])
    def test_class_assignment_user_input(self, mock_input):
        actual = class_assignment()
        expected = CLASS_B_STARTING_POINT.copy()
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['1'])
    def test_class_assignment_user_input_two(self, mock_input):
        actual = class_assignment()
        expected = CLASS_A_STARTING_POINT.copy()
        self.assertEqual(actual, expected)

