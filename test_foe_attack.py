from unittest import TestCase
from unittest.mock import patch
from game import foe_attack


class TestFoeAttack(TestCase):
    @patch('random.choices', side_effect=[[True]])
    def test_foe_attack_True(self, mock_choices):
        foe = {'name': 'Part-time Thief', 'foe_HP': 200, 'foe_damage': 50, 'foe_exp': 50}
        expected = True
        actual = foe_attack(foe)
        self.assertEqual(expected, actual)

    @patch('random.choices', side_effect=[[False]])
    def test_foe_attack_False(self, mock_choices):
        foe = {'name': 'Part-time Thief', 'foe_HP': 200, 'foe_damage': 50, 'foe_exp': 50}
        expected = False
        actual = foe_attack(foe)
        self.assertEqual(expected, actual)
