from unittest import TestCase
from game import encounter_boss


class TestEncounterBoss(TestCase):
    def test_encounter_boss_one(self):
        character = {'name': 'tester', 'level': 1, 'exp': 100, 'x-coor': 0, 'y-coor': 5}
        expected = False
        actual = encounter_boss(character)
        self.assertEqual(expected, actual)

    def test_encounter_boss_two(self):
        character = {'name': 'tester', 'level': 1, 'exp': 100, 'x-coor': 5, 'y-coor': 5}
        expected = False
        actual = encounter_boss(character)
        self.assertEqual(expected, actual)

    def test_encounter_boss_three(self):
        character = {'name': 'tester', 'level': 1, 'exp': 100, 'x-coor': 7, 'y-coor': 7}
        expected = True
        actual = encounter_boss(character)
        self.assertEqual(expected, actual)
