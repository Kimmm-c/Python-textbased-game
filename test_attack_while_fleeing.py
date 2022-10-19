import io
from unittest import TestCase
from unittest.mock import patch
import game


class TestAttackWhileFleeing(TestCase):
    @patch('random.choices', side_effect=[[True]])
    @patch('random.randint', side_effect=[50])
    def test_attack_while_fleeing_character_HP_test1(self, mock_randint, mock_choices):
        character = {'name': 'tester', 'level': 2, 'exp': 100, 'x-coor': 0, 'y-coor': 0,
                     'class': game.CLASS_A_STARTING_POINT.copy()}
        foe = {'name': 'Part-time Thief', 'foe_HP': 200, 'foe_damage': 50, 'foe_exp': 50}
        expected = 450
        game.attack_while_fleeing(character, foe)
        actual = character['class']['HP']
        self.assertEqual(expected, actual)

    @patch('random.choices', side_effect=[[False]])
    def test_attack_while_fleeing_character_HP_test2(self, mock_choices):
        character = {'name': 'tester', 'level': 2, 'exp': 100, 'x-coor': 0, 'y-coor': 0,
                     'class': game.CLASS_A_STARTING_POINT.copy()}
        foe = {'name': 'Part-time Thief', 'foe_HP': 200, 'foe_damage': 50, 'foe_exp': 50}
        expected = 500
        game.attack_while_fleeing(character, foe)
        actual = character['class']['HP']
        self.assertEqual(expected, actual)

    @patch('random.choices', side_effect=[[True]])
    @patch('random.randint', side_effect=[75])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_attack_while_fleeing_print_message1(self, mock_stdout, mock_randint, mock_choices):
        character = {'name': 'tester', 'level': 2, 'exp': 100, 'x-coor': 0, 'y-coor': 0,
                     'class': game.CLASS_A_STARTING_POINT.copy()}
        foe = {'name': 'Part-time Thief', 'foe_HP': 200, 'foe_damage': 50, 'foe_exp': 50}
        expected = "Ouch! You were attacked while fleeing! Your HP is now 425\n"
        game.attack_while_fleeing(character, foe)
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('random.choices', side_effect=[[False]])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_attack_while_fleeing_print_message2(self, mock_stdout, mock_choices):
        character = {'name': 'tester', 'level': 2, 'exp': 100, 'x-coor': 0, 'y-coor': 0,
                     'class': game.CLASS_A_STARTING_POINT.copy()}
        foe = {'name': 'Part-time Thief', 'foe_HP': 200, 'foe_damage': 50, 'foe_exp': 50}
        expected = "Successfully escaped!\n"
        game.attack_while_fleeing(character, foe)
        self.assertEqual(expected, mock_stdout.getvalue())




