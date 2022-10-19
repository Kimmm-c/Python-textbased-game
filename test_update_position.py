import io
from unittest import TestCase
from unittest.mock import patch

from game import update_position


class TestUpdatePosition(TestCase):
    def test_update_position_character_East(self):
        character = {'name': 'tester', 'level': 1, 'exp': 100, 'x-coor': 0, 'y-coor': 0}
        board = {(row, column): "Testing Room" for row in range(3) for column in range(3)}
        direction = "EAST"
        expected = {'name': 'tester', 'level': 1, 'exp': 100, 'x-coor': 1, 'y-coor': 0}
        update_position(board, character, direction)
        self.assertEqual(expected, character)

    def test_update_position_character_South(self):
        character = {'name': 'tester', 'level': 1, 'exp': 100, 'x-coor': 1, 'y-coor': 1}
        board = {(row, column): "Testing Room" for row in range(3) for column in range(3)}
        direction = "SOUTH"
        expected = {'name': 'tester', 'level': 1, 'exp': 100, 'x-coor': 1, 'y-coor': 2}
        update_position(board, character, direction)
        self.assertEqual(expected, character)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_update_position_print_location_description(self, mock_stout):
        character = {'name': 'tester', 'level': 1, 'exp': 100, 'x-coor': 1, 'y-coor': 1}
        board = {(row, column): "Testing Room" for row in range(3) for column in range(3)}
        direction = "SOUTH"
        expected = "\nYou've entered the Testing Room\n"
        update_position(board, character, direction)
        self.assertEqual(expected, mock_stout.getvalue())

