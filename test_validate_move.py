from unittest import TestCase
from game import validate_move


class TestValidateMove(TestCase):
    def test_validate_move_one(self):
        character = {'name': 'tester', 'level': 1, 'exp': 100, 'x-coor': 0, 'y-coor': 0}
        board = {(row, column): "Testing Room" for row in range(3) for column in range(3)}
        direction = "NORTH"
        expected = False
        actual = validate_move(board, character, direction)
        self.assertEqual(expected, actual)

    def test_validate_move_two(self):
        character = {'name': 'tester', 'level': 1, 'exp': 100, 'x-coor': 0, 'y-coor': 2}
        board = {(row, column): "Testing Room" for row in range(3) for column in range(3)}
        direction = "NORTH"
        expected = True
        actual = validate_move(board, character, direction)
        self.assertEqual(expected, actual)

    def test_validate_move_three(self):
        character = {'name': 'tester', 'level': 1, 'exp': 100, 'x-coor': 0, 'y-coor': 0}
        board = {(row, column): "Testing Room" for row in range(3) for column in range(3)}
        direction = "WEST"
        expected = False
        actual = validate_move(board, character, direction)
        self.assertEqual(expected, actual)

    def test_validate_move_four(self):
        character = {'name': 'tester', 'level': 1, 'exp': 100, 'x-coor': 0, 'y-coor': 0}
        board = {(row, column): "Testing Room" for row in range(3) for column in range(3)}
        direction = "EAST"
        expected = True
        actual = validate_move(board, character, direction)
        self.assertEqual(expected, actual)

    def test_validate_move_five(self):
        character = {'name': 'tester', 'level': 1, 'exp': 100, 'x-coor': 0, 'y-coor': 0}
        board = {(row, column): "Testing Room" for row in range(3) for column in range(3)}
        direction = "SOUTH"
        expected = True
        actual = validate_move(board, character, direction)
        self.assertEqual(expected, actual)
