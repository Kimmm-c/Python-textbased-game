import io
from unittest import TestCase
from unittest.mock import patch
import game


class TestLevelUp(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_level_up_print_message_lv1_to_lv2(self, mock_stdout):
        character = {'name': 'tester', 'level': 1, 'exp': 300, 'x-coor': 7, 'y-coor': 7,
                     'class': game.CLASS_A_STARTING_POINT.copy()}
        expected = "You've levelled up, tester! Here's your current stats: \n"\
                   "Level: 2\n"\
                   "Class name: Lightweight\n"\
                   "Skills: Destructive Roundhouse\n"\
                   "HP: 1100\n"\
                   "Damage: 195\n"\
                   "Stamina: 150\n"\
                   "Accuracy: 130\n"
        game.level_up(character)
        self.assertEqual(expected, mock_stdout.getvalue())

    def test_level_up_character_stats_update_lv1_to_lv2(self):
        character = {'name': 'tester', 'level': 1, 'exp': 300, 'x-coor': 7, 'y-coor': 7,
                     'class': game.CLASS_A_STARTING_POINT.copy()}
        expected = {'name': 'tester', 'level': 2, 'exp': 300, 'x-coor': 7, 'y-coor': 7,
                    'class': {'class_name': 'MMA Fighter',
                              'level_name': ('Featherweight', 'Lightweight', 'Heavyweight'),
                              'skill': ('Lightning Jabs', 'Destructive Roundhouse', 'Deontay Punches'),
                              'HP': 1100, 'max_HP': 1100, 'damage': 195, 'stamina': 150, 'accuracy': 130}}
        game.level_up(character)
        actual = character
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_level_up_print_message_lv2_to_lv3(self, mock_stdout):
        character = {'name': 'tester2', 'level': 2, 'exp': 705, 'x-coor': 7, 'y-coor': 7,
                     'class': {'class_name': 'MMA Fighter',
                               'level_name': ('Featherweight', 'Lightweight', 'Heavyweight'),
                               'skill': ('Lightning Jabs', 'Destructive Roundhouse', 'Deontay Punches'),
                               'HP': 1100, 'max_HP': 1100, 'damage': 195, 'stamina': 150, 'accuracy': 130}}
        expected = "You've levelled up, tester2! Here's your current stats: \n" \
                   "Level: 3\n" \
                   "Class name: Heavyweight\n" \
                   "Skills: Deontay Punches\n" \
                   "HP: 2000\n" \
                   "Damage: 270\n" \
                   "Stamina: 200\n" \
                   "Accuracy: 180\n"
        game.level_up(character)
        self.assertEqual(expected, mock_stdout.getvalue())

    def test_level_up_character_stats_update_lv2_to_lv3(self):
        character = {'name': 'tester2', 'level': 2, 'exp': 705, 'x-coor': 7, 'y-coor': 7,
                     'class': {'class_name': 'MMA Fighter',
                               'level_name': ('Featherweight', 'Lightweight', 'Heavyweight'),
                               'skill': ('Lightning Jabs', 'Destructive Roundhouse', 'Deontay Punches'),
                               'HP': 1100, 'max_HP': 1100, 'damage': 195, 'stamina': 150, 'accuracy': 130}}
        expected = {'name': 'tester2', 'level': 3, 'exp': 705, 'x-coor': 7, 'y-coor': 7,
                    'class': {'class_name': 'MMA Fighter',
                              'level_name': ('Featherweight', 'Lightweight', 'Heavyweight'),
                              'skill': ('Lightning Jabs', 'Destructive Roundhouse', 'Deontay Punches'),
                              'HP': 2000, 'max_HP': 2000, 'damage': 270, 'stamina': 200, 'accuracy': 180}}
        game.level_up(character)
        actual = character
        self.assertEqual(expected, actual)
