import io
from unittest import TestCase
from unittest.mock import patch
import game


class TestBattleFoe(TestCase):
    @patch('random.choices', side_effect=[[True], [False], [False]])
    @patch('random.randint', side_effect=[35])
    def test_battle_foe_character_exp_increase_when_killed_foe(self, mock_randint, mock_choices):
        character = {'name': 'tester', 'level': 1, 'exp': 100, 'x-coor': 0, 'y-coor': 0,
                     'class': game.CLASS_A_STARTING_POINT.copy()}
        foe = {'name': 'Part-time Thief', 'foe_HP': 25, 'foe_damage': 50, 'foe_exp': 50}
        expected = 150
        game.battle_foe(character, foe)
        actual = character['exp']
        self.assertEqual(expected, actual)

    @patch('random.choices', side_effect=[[True], [False], [False]])
    @patch('random.randint', side_effect=[35])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_battle_foe_print_message_when_foe_is_killed(self, mock_stdout, mock_randint, mock_choices):
        character = {'name': 'tester', 'level': 1, 'exp': 100, 'x-coor': 0, 'y-coor': 0,
                     'class': game.CLASS_A_STARTING_POINT.copy()}
        foe = {'name': 'Part-time Thief', 'foe_HP': 25, 'foe_damage': 50, 'foe_exp': 50}
        expected = "You successfully struck your enemy!!\n"\
                   "You have destroyed your enemy with Lightning Jabs! You've collected 50exp!\n"
        game.battle_foe(character, foe)
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('random.choices', side_effect=[[True], [False], [False], [True]])
    @patch('random.randint', side_effect=[35, 25])
    def test_battle_foe_character_HP_decrease_being_attacked_while_fleeing(self, mock_randint, mock_choices):
        character = {'name': 'tester', 'level': 1, 'exp': 100, 'x-coor': 0, 'y-coor': 0,
                     'class': game.CLASS_A_STARTING_POINT.copy()}
        character['class']['HP'] = 50
        foe = {'name': 'Part-time Thief', 'foe_HP': 25, 'foe_damage': 50, 'foe_exp': 50}
        expected = 25
        game.battle_foe(character, foe)
        actual = character['class']['HP']
        self.assertEqual(expected, actual)

    @patch('random.choices', side_effect=[[False], [False], [False], [False]])
    def test_battle_foe_character_HP_unchanged_when_escape_successfully(self, mock_choices):
        character = {'name': 'tester', 'level': 1, 'exp': 100, 'x-coor': 0, 'y-coor': 0,
                     'class': game.CLASS_A_STARTING_POINT.copy()}
        character['class']['HP'] = 50
        foe = {'name': 'Part-time Thief', 'foe_HP': 25, 'foe_damage': 50, 'foe_exp': 50}
        expected = 50
        game.battle_foe(character, foe)
        actual = character['class']['HP']
        self.assertEqual(expected, actual)

    @patch('random.choices', side_effect=[[False], [False], [False], [True]])
    @patch('random.randint', side_effect=[25])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_battle_foe_print_message_when_character_attacked_on_flee(self, mock_stdout, mock_randint, mock_choices):
        character = {'name': 'tester', 'level': 1, 'exp': 100, 'x-coor': 0, 'y-coor': 0,
                     'class': game.CLASS_A_STARTING_POINT.copy()}
        foe = {'name': 'Part-time Thief', 'foe_HP': 200, 'foe_damage': 50, 'foe_exp': 50}
        character['class']['HP'] = 50
        expected = "You missed!\n" \
                   "Your HP is too low. Escape attempt..\n"\
                   "Ouch! You were attacked while fleeing! Your HP is now 25\n"
        game.battle_foe(character, foe)
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('random.choices', side_effect=[[False], [False], [True], [False]])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_battle_foe_print_message_when_foe_flee(self, mock_stdout, mock_choices):
        character = {'name': 'tester', 'level': 1, 'exp': 100, 'x-coor': 0, 'y-coor': 0,
                     'class': game.CLASS_A_STARTING_POINT.copy()}
        foe = {'name': 'Part-time Thief', 'foe_HP': 200, 'foe_damage': 50, 'foe_exp': 50}
        expected = "You missed!\n" \
                   "Your opponent has fled the scene!\n"
        game.battle_foe(character, foe)
        self.assertEqual(expected, mock_stdout.getvalue())
