from unittest import TestCase
from unittest.mock import patch
from game import user_choice_to_fight


class TestUserChoiceToFight(TestCase):
    @patch('builtins.input', side_effect=['y'])
    def test_user_choice_to_fight_yes(self, mock_input):
        expected = True
        actual = user_choice_to_fight()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['n'])
    def test_user_choice_to_fight_no(self, mock_input):
        expected = False
        actual = user_choice_to_fight()
        self.assertEqual(expected, actual)
