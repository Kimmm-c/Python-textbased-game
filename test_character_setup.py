from unittest import TestCase
from unittest.mock import patch
from game import character_setup


class TestCharacterSetup(TestCase):
    @patch('builtins.input', side_effect=['kimmm', "1"])
    def test_character_setup_one(self, mock_input):
        expected = {'name': 'kimmm', 'level': 1, 'exp': 100, 'x-coor': 0, 'y-coor': 0,
                    'class': {'class_name': 'MMA Fighter',
                              'level_name': ('Featherweight', 'Lightweight', 'Heavyweight'),
                              'skill': ('Lightning Jabs', 'Destructive Roundhouse', 'Deontay Punches'), 'HP': 500,
                              'max_HP': 500, 'damage': 120, 'stamina': 100, 'accuracy': 80}}
        actual = character_setup()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['amieee', '2'])
    def test_character_setup_two(self, mock_input):
        expected = {'name': 'amieee', 'level': 1, 'exp': 100, 'x-coor': 0, 'y-coor': 0,
                    'class': {'class_name': 'Olympic Archer', 'level_name': ('Kindergarten', 'High school', 'Master'),
                              'skill': ('Flying Flip-flop', 'Shooting Butter Knives', 'Poisonous Arrows'), 'HP': 500,
                              'max_HP': 500, 'damage': 80, 'stamina': 100, 'accuracy': 120}}
        actual = character_setup()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['kc', '3'])
    def test_character_setup_three(self, mock_input):
        expected = {'name': 'kc', 'level': 1, 'exp': 100, 'x-coor': 0, 'y-coor': 0,
                    'class': {'class_name': 'Unemployed Magician', 'level_name': ('Mage', 'Wizard', 'Sakura CardCaptor'),
                              'skill': ('Spiky Roses', 'Bunny Spirit Summon', 'Cursed Playing Cards'), 'HP': 600,
                              'max_HP': 600, 'damage': 100, 'stamina': 80, 'accuracy': 100}}
        actual = character_setup()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['kccc', '4'])
    def test_character_setup_four(self, mock_input):
        expected = {'name': 'kccc', 'level': 1, 'exp': 100, 'x-coor': 0, 'y-coor': 0,
                    'class': {'class_name': 'Elite Fencer',
                              'level_name': ('Rookie', 'Local Fencer', 'International Fencer'),
                              'skill': ('Clothes Hanger Strike', 'Ranging Sweeper', 'Sabre Slash'), 'HP': 400,
                              'max_HP': 400, 'damage': 100, 'stamina': 120, 'accuracy': 100}}
        actual = character_setup()
        self.assertEqual(expected, actual)
