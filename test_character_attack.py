from unittest import TestCase
from unittest.mock import patch
from game import character_attack


class TestCharacterAttack(TestCase):
    @patch('random.choices', side_effect=[[True]])
    def test_character_attack_True(self, mock_choices):
        character = {'name': 'tester', 'level': 2, 'exp': 100, 'x-coor': 0, 'y-coor': 0,
                     'class': {'class_name': 'MMA Fighter'}}
        expected = True
        actual = character_attack(character)
        self.assertEqual(expected, actual)

    @patch('random.choices', side_effect=[[False]])
    def test_character_attack_False(self, mock_choices):
        character = {'name': 'tester', 'level': 2, 'exp': 100, 'x-coor': 0, 'y-coor': 0,
                     'class': {'class_name': 'Olympic Archer'}}
        expected = False
        actual = character_attack(character)
        self.assertEqual(expected, actual)
