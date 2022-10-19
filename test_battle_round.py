import io
from unittest import TestCase
from unittest.mock import patch
import game


class TestBattleRound(TestCase):
    @patch('random.choices', side_effect=[[True], [False]])
    @patch('random.randint', side_effect=[35])
    def test_battle_round_character_causes_damage(self, mock_randint, mock_choices):
        character = {'name': 'tester', 'level': 2, 'exp': 100, 'x-coor': 0, 'y-coor': 0,
                     'class': game.CLASS_A_STARTING_POINT.copy()}
        foe = {'name': 'Part-time Thief', 'foe_HP': 200, 'foe_damage': 50, 'foe_exp': 50}
        expected = 165
        game.battle_round(character, foe)
        actual = foe['foe_HP']
        self.assertEqual(expected, actual)

    @patch('random.choices', side_effect=[[False], [True]])
    @patch('random.randint', side_effect=[25])
    def test_battle_round_foe_causes_damage(self, mock_randint, mock_choices):
        character = {'name': 'tester', 'level': 2, 'exp': 100, 'x-coor': 0, 'y-coor': 0,
                     'class': game.CLASS_A_STARTING_POINT.copy()}
        foe = {'name': 'Part-time Thief', 'foe_HP': 200, 'foe_damage': 50, 'foe_exp': 50}
        expected = 475
        game.battle_round(character, foe)
        actual = character['class']['HP']
        self.assertEqual(expected, actual)

    @patch('random.choices', side_effect=[[True], [True]])
    @patch('random.randint', side_effect=[35, 25])
    def test_battle_round_both_character_and_foe_cause_damage(self, mock_randint, mock_choices):
        character = {'name': 'tester', 'level': 2, 'exp': 100, 'x-coor': 0, 'y-coor': 0,
                     'class': game.CLASS_A_STARTING_POINT.copy()}
        foe = {'name': 'Part-time Thief', 'foe_HP': 200, 'foe_damage': 50, 'foe_exp': 50}
        expected = (475, 165)
        game.battle_round(character, foe)
        actual = (character['class']['HP'], foe['foe_HP'])
        self.assertEqual(expected, actual)

    @patch('random.choices', side_effect=[[True], [True]])
    @patch('random.randint', side_effect=[35, 25])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_battle_round_print_message_when_both_cause_damage(self, mock_stdout, mock_randint, mock_choices):
        character = {'name': 'tester', 'level': 2, 'exp': 100, 'x-coor': 0, 'y-coor': 0,
                     'class': game.CLASS_A_STARTING_POINT.copy()}
        foe = {'name': 'Part-time Thief', 'foe_HP': 200, 'foe_damage': 50, 'foe_exp': 50}
        expected = "You successfully struck your enemy!!\n"\
                   "Ouch! Your enemy fired back! Your hit point is now 475\n"
        game.battle_round(character, foe)
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('random.choices', side_effect=[[True], [False]])
    @patch('random.randint', side_effect=[35])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_battle_round_print_message_when_character_causes_damage(self, mock_stdout, mock_randint, mock_choices):
        character = {'name': 'tester', 'level': 2, 'exp': 100, 'x-coor': 0, 'y-coor': 0,
                     'class': game.CLASS_A_STARTING_POINT.copy()}
        foe = {'name': 'Part-time Thief', 'foe_HP': 200, 'foe_damage': 50, 'foe_exp': 50}
        expected = "You successfully struck your enemy!!\n"
        game.battle_round(character, foe)
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('random.choices', side_effect=[[False], [True]])
    @patch('random.randint', side_effect=[35])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_battle_round_print_message_when_foe_causes_damage(self, mock_stdout, mock_randint, mock_choices):
        character = {'name': 'tester', 'level': 2, 'exp': 100, 'x-coor': 0, 'y-coor': 0,
                     'class': game.CLASS_A_STARTING_POINT.copy()}
        foe = {'name': 'Part-time Thief', 'foe_HP': 200, 'foe_damage': 50, 'foe_exp': 50}
        expected = "You missed!\n"\
                   "Ouch! Your enemy fired back! Your hit point is now 465\n"
        game.battle_round(character, foe)
        self.assertEqual(expected, mock_stdout.getvalue())

