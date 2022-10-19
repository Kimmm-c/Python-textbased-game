import io
from unittest import TestCase
from unittest.mock import patch
import game


class TestBattleBoss(TestCase):
    @patch('random.choices', side_effect=[[False], [True], [True]])
    @patch('random.randint', side_effect=[35, 25])
    def test_battle_boss_character_HP_decrease_being_attack_while_fleeing(self, mock_randint, mock_choices):
        character = {'name': 'tester', 'level': 1, 'exp': 100, 'x-coor': 0, 'y-coor': 0,
                     'class': game.CLASS_A_STARTING_POINT.copy()}
        character['class']['HP'] = 75
        boss = game.BOSS.copy()
        expected = 15
        game.battle_boss(character, boss)
        actual = character['class']['HP']
        self.assertEqual(expected, actual)

    @patch('random.choices', side_effect=[[False], [False], [False]])
    def test_battle_boss_character_HP_unchanged_when_escape_successfully(self, mock_choices):
        character = {'name': 'tester2', 'level': 1, 'exp': 100, 'x-coor': 0, 'y-coor': 0,
                     'class': game.CLASS_A_STARTING_POINT.copy()}
        character['class']['HP'] = 50
        boss = game.BOSS.copy()
        expected = 50
        game.battle_boss(character, boss)
        actual = character['class']['HP']
        self.assertEqual(expected, actual)

    @patch('random.choices', side_effect=[[True], [False]])
    @patch('random.randint', side_effect=[100])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_battle_boss_print_message_when_boss_is_killed(self, mock_stdout, mock_randint, mock_choices):
        character = {'name': 'tester3', 'level': 1, 'exp': 100, 'x-coor': 0, 'y-coor': 0,
                     'class': game.CLASS_A_STARTING_POINT.copy()}
        boss = game.BOSS.copy()
        boss['foe_HP'] = 75
        expected = "You successfully struck your enemy!!\n"\
                   "Unbelievable!! PSYCHO is down!!!\n"
        game.battle_boss(character, boss)
        self.assertEqual(expected, mock_stdout.getvalue())