from unittest import TestCase
import game


class TestCharacterAlive(TestCase):
    def test_character_alive_True(self):
        character = {'name': 'tester', 'level': 1, 'exp': 100, 'x-coor': 7, 'y-coor': 7,
                     'class': game.CLASS_A_STARTING_POINT.copy()}
        expected = True
        actual = game.character_alive(character)
        self.assertEqual(expected, actual)

    def test_character_alive_False(self):
        character = {'name': 'tester', 'level': 1, 'exp': 100, 'x-coor': 7, 'y-coor': 7,
                     'class': game.CLASS_A_STARTING_POINT.copy()}
        character['class']['HP'] = 0
        expected = False
        actual = game.character_alive(character)
        self.assertEqual(expected, actual)

    def test_character_alive_HP_negative(self):
        character = {'name': 'tester', 'level': 1, 'exp': 100, 'x-coor': 7, 'y-coor': 7,
                     'class': game.CLASS_A_STARTING_POINT.copy()}
        character['class']['HP'] = -5
        expected = False
        actual = game.character_alive(character)
        self.assertEqual(expected, actual)
