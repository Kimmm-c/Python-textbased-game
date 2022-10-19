from unittest import TestCase
import game


class TestHeal(TestCase):
    def test_heal_when_currentHP_is_less_than_maxHP(self):
        character = {'name': 'tester', 'level': 1, 'exp': 100, 'x-coor': 0, 'y-coor': 0,
                     'class': game.CLASS_A_STARTING_POINT.copy()}
        character['class']['HP'] = 425
        expected = 475
        game.heal(character)
        actual = character['class']['HP']
        self.assertEqual(expected, actual)

    def test_heal_when_currentHP_is_equal_to_maxHP(self):
        character = {'name': 'tester', 'level': 1, 'exp': 100, 'x-coor': 0, 'y-coor': 0,
                     'class': game.CLASS_A_STARTING_POINT.copy()}
        expected = 500
        game.heal(character)
        actual = character['class']['HP']
        self.assertEqual(expected, actual)

    def test_heal_when_after_heal_HP_is_larger_than_maxHP(self):
        character = {'name': 'tester', 'level': 1, 'exp': 100, 'x-coor': 0, 'y-coor': 0,
                     'class': game.CLASS_A_STARTING_POINT.copy()}
        character['class']['HP'] = 475
        expected = 500
        game.heal(character)
        actual = character['class']['HP']
        self.assertEqual(expected, actual)
