import io
from unittest import TestCase
from unittest.mock import patch
import game


class TestEvents(TestCase):
    @patch('builtins.input', side_effect=['n'])
    @patch('random.choices', side_effect=[[False], [True]])
    @patch('random.randint', side_effect=[50])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_events_print_message_when_character_encounters_boss(self, mock_stdout, mock_input, mock_randint,
                                                                 mock_choices):
        character = {'name': 'tester', 'level': 1, 'exp': 100, 'x-coor': 7, 'y-coor': 7,
                     'class': game.CLASS_A_STARTING_POINT.copy()}
        boss = game.BOSS.copy()
        expected = "You have encountered the boss!!\n"\
                   "Ouch! You were attacked while fleeing! Your HP is now 450\n"
        game.events(character, boss)
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['n'])
    @patch('random.choices', side_effect=[[True], [False]])
    @patch('random.randint', side_effect=[0])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_events_print_message_when_character_encounters_foe(self, mock_stdout, mock_input, mock_randint,
                                                                mock_choices):
        character = {'name': 'tester1', 'level': 1, 'exp': 100, 'x-coor': 0, 'y-coor': 0,
                     'class': game.CLASS_A_STARTING_POINT.copy()}
        boss = game.BOSS.copy()
        foe = game.LV1_FOE.copy()
        expected = "You are blocked by a Part-time Thief\n"\
                   "Successfully escaped!\n"
        game.events(character, boss)
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('random.choices', side_effect=[[False]])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_events_print_message_when_character_encounters_nothing(self, mock_stdout, mock_choices):
        character = {'name': 'tester2', 'level': 1, 'exp': 100, 'x-coor': 0, 'y-coor': 0,
                     'class': game.CLASS_A_STARTING_POINT.copy()}
        boss = game.BOSS.copy()
        expected = "There's nothing here. Keep moving!\n"
        game.events(character, boss)
        self.assertEqual(expected, mock_stdout.getvalue())

