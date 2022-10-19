from unittest import TestCase
from unittest.mock import patch
import game


class TestGetDirection(TestCase):
    @patch('builtins.input', side_effect=['1'])
    def test_get_direction_North(self, mock_input):
        character = {'name': 'tester', 'level': 1, 'exp': 100, 'x-coor': 0, 'y-coor': 0,
                     'class': {'HP': 450, 'max_HP': 500}}
        board = {(row, column): "Testing Room" for row in range(3) for column in range(3)}
        expected = "NORTH"
        actual = game.get_direction(board, character)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['2'])
    def test_get_direction_East(self, mock_input):
        character = {'name': 'tester', 'level': 1, 'exp': 100, 'x-coor': 0, 'y-coor': 0,
                     'class': {'HP': 300, 'max_HP': 500}}
        board = {(row, column): "Testing Room" for row in range(3) for column in range(3)}
        expected = "EAST"
        actual = game.get_direction(board, character)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['3'])
    def test_get_direction_South(self, mock_input):
        character = {'name': 'tester', 'level': 1, 'exp': 100, 'x-coor': 0, 'y-coor': 0,
                     'class': {'HP': 350, 'max_HP': 500}}
        board = {(row, column): "Testing Room" for row in range(3) for column in range(3)}
        expected = "SOUTH"
        actual = game.get_direction(board, character)
        self.assertEqual(expected, actual)
