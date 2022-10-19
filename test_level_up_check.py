from unittest import TestCase
import game


class TestLevelUpCheck(TestCase):
    def test_level_up_check_False(self):
        character = {'name': 'tester', 'level': 1, 'exp': 100, 'x-coor': 7, 'y-coor': 7,
                     'class': game.CLASS_A_STARTING_POINT.copy()}
        expected = False
        actual = game.level_up_check(character)
        self.assertEqual(expected, actual)

    def test_level_up_check_from_lv1_to_lv2(self):
        character = {'name': 'tester', 'level': 1, 'exp': 300, 'x-coor': 7, 'y-coor': 7,
                     'class': game.CLASS_A_STARTING_POINT.copy()}
        expected = True
        actual = game.level_up_check(character)
        self.assertEqual(expected, actual)


    def test_level_up_check_from_lv2_to_lv3(self):
        character = {'name': 'tester', 'level': 2, 'exp': 701, 'x-coor': 7, 'y-coor': 7,
                     'class': game.CLASS_A_STARTING_POINT.copy()}
        expected = True
        actual = game.level_up_check(character)
        self.assertEqual(expected, actual)

