import io
from unittest import TestCase
from unittest.mock import patch
from game import animate_message


class TestAnimateMessage(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_animate_message_one(self, mock_stdout):
        message = "Game start"
        list_of_lettes = ["\033[1;31m" + letter.upper() + "\033[0m " for letter in message]
        expected = "".join(list_of_lettes)
        animate_message(message)
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_animate_message_two(self, mock_stdout):
        message = "welcometoforgotisland"
        list_of_lettes = ["\033[1;31m" + letter.upper() + "\033[0m " for letter in message]
        expected = "".join(list_of_lettes)
        animate_message(message)
        self.assertEqual(expected, mock_stdout.getvalue())
