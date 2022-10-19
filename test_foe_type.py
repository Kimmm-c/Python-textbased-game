from unittest import TestCase
import game


class TestFoeType(TestCase):
    def test_foe_type_character_lv1(self):
        character = {'name': 'tester', 'level': 1, 'exp': 100, 'x-coor': 0, 'y-coor': 0}
        expected = game.LV1_FOE.copy()
        actual = game.foe_type(character)
        self.assertEqual(expected, actual)

    def test_foe_type_character_lv2(self):
        character = {'name': 'tester', 'level': 2, 'exp': 100, 'x-coor': 0, 'y-coor': 0}
        expected = game.LV2_FOE.copy()
        actual = game.foe_type(character)
        self.assertEqual(expected, actual)

    def test_foe_type_character_lv3(self):
        character = {'name': 'tester', 'level': 3, 'exp': 100, 'x-coor': 0, 'y-coor': 0}
        expected = game.LV3_FOE.copy()
        actual = game.foe_type(character)
        self.assertEqual(expected, actual)
