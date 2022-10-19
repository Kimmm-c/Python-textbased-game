from unittest import TestCase
from game import boss_alive
from game import BOSS


class TestBossAlive(TestCase):
    def test_boss_alive_one(self):
        boss = BOSS.copy()
        expected = True
        actual = boss_alive(boss)
        self.assertEqual(expected, actual)

    def test_boss_alive_two(self):
        boss = BOSS.copy()
        boss['foe_HP'] = 0
        expected = False
        actual = boss_alive(boss)
        self.assertEqual(expected, actual)

    def test_boss_alive_three(self):
        boss = BOSS.copy()
        boss['foe_HP'] = -100
        expected = False
        actual = boss_alive(boss)
        self.assertEqual(expected, actual)
