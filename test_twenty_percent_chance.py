from unittest import TestCase
from unittest.mock import patch
from game import twenty_percent_chance


class TestTwentyPercentChance(TestCase):
    @patch('random.choices', side_effect=[[True]])
    def test_twenty_percent_chance_True(self, mock_choices):
        expected = True
        actual = twenty_percent_chance()
        self.assertEqual(expected, actual)

    @patch('random.choices', side_effect=[[False]])
    def test_twenty_percent_chance_False(self, mock_choices):
        expected = False
        actual = twenty_percent_chance()
        self.assertEqual(expected, actual)

