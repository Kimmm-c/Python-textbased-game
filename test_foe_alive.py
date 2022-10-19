from unittest import TestCase
from game import foe_alive
from game import LV1_FOE


class TestFoeAlive(TestCase):
    def test_foe_alive_one(self):
        foe = LV1_FOE.copy()
        expected = True
        actual = foe_alive(foe)
        self.assertEqual(expected, actual)

    def test_foe_alive_two(self):
        foe = LV1_FOE.copy()
        foe['foe_HP'] = 0
        expected = False
        actual = foe_alive(foe)
        self.assertEqual(expected, actual)

    def test_foe_alive_three(self):
        foe = LV1_FOE.copy()
        foe['foe_HP'] = -3
        expected = False
        actual = foe_alive(foe)
        self.assertEqual(expected, actual)
