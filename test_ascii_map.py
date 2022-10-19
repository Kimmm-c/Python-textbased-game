import io
from unittest import TestCase
from unittest.mock import patch
from game import ascii_map


class TestAsciiMap(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_ascii_map_one(self, mock_stdout):
        character = {'name': 'tester', 'level': 1, 'exp': 100, 'x-coor': 2, 'y-coor': 0}
        board = {(row, column): "Testing Room" for row in range(5) for column in range(5)}
        expected = "[ ] [ ] [x] [ ] [ ] \n"\
                   "[ ] [ ] [ ] [ ] [ ] \n"\
                   "[ ] [ ] [ ] [ ] [ ] \n"\
                   "[ ] [ ] [ ] [ ] [ ] \n"\
                   "[ ] [ ] [ ] [ ] [ ] \n"
        ascii_map(board, character)
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_ascii_map_two(self, mock_stdout):
        character = {'name': 'tester', 'level': 1, 'exp': 100, 'x-coor': 5, 'y-coor': 5}
        board = {(row, column): "Testing Room" for row in range(10) for column in range(10)}
        expected = "[ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] \n" \
                   "[ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] \n" \
                   "[ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] \n" \
                   "[ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] \n" \
                   "[ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] \n" \
                   "[ ] [ ] [ ] [ ] [ ] [x] [ ] [ ] [ ] [ ] \n" \
                   "[ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] \n" \
                   "[ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] \n" \
                   "[ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] \n" \
                   "[ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] \n"
        ascii_map(board, character)
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_ascii_map_three(self, mock_stdout):
        character = {'name': 'tester', 'level': 1, 'exp': 100, 'x-coor': 2, 'y-coor': 2}
        board = {(row, column): "Testing Room" for row in range(3) for column in range(3)}
        expected = "[ ] [ ] [ ] \n" \
                   "[ ] [ ] [ ] \n" \
                   "[ ] [ ] [x] \n"
        ascii_map(board, character)
        self.assertEqual(expected, mock_stdout.getvalue())
