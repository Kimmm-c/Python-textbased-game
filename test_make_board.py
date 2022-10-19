from unittest import TestCase
from unittest.mock import patch
from game import make_board


class TestMakeBoard(TestCase):
    def test_make_board_room(self):
        row = 10
        column = 10
        expected = row*column
        actual = len(make_board(row, column))
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[0, 0, 0, 0, 17, 0, 0, 18, 0])
    def test_make_board_first(self, mock_randint):
        expect = {(0, 0): "\033[0;35mOutdoor Pool\033[0m. Suddenly a gust of wind sends shivers down your spine.\n",
                  (0, 1): "\033[0;35mOutdoor Pool\033[0m. Suddenly a gust of wind sends shivers down your spine.\n",
                  (0, 2): "\033[0;35mOutdoor Pool\033[0m. Suddenly a gust of wind sends shivers down your spine.\n",
                  (1, 0): "\033[0;35mOutdoor Pool\033[0m. Suddenly a gust of wind sends shivers down your spine.\n",
                  (1, 1): "\033[0;35mSauna\033[0m. The charcoal was long put out. This room is nothing but "
                          "darkness0.\n",
                  (1, 2): "\033[0;35mOutdoor Pool\033[0m. Suddenly a gust of wind sends shivers down your spine.\n",
                  (2, 0): "\033[0;35mOutdoor Pool\033[0m. Suddenly a gust of wind sends shivers down your spine.\n",
                  (2, 1): "\033[0;35mWorship Room\033[0m. You have never seen that many reliquaries in your life!\n",
                  (2, 2): "\033[0;35mOutdoor Pool\033[0m. Suddenly a gust of wind sends shivers down your spine.\n"}
        actual = make_board(3, 3)
        self.assertEqual(expect, actual)

    @patch('random.randint', side_effect=[2, 0, 5, 1])
    def test_make_board_second(self, mock_randint):
        expect = {(0, 0): "\033[0;35mBoxing Room\033[0m. The heavy bags are all worn out! Someone must have used them "
                          "frequently..\n",
                  (0, 1): "\033[0;35mOutdoor Pool\033[0m. Suddenly a gust of wind sends shivers down your spine.\n",
                  (1, 0): "\033[0;35mMelisa's Bedroom\033[0m. There is a picture frame facing down on the night stand. "
                          "You walk over\n"
                          "and pick it up. It's a picture of Melisa with her family. You feel really sorry for her.\n",
                  (1, 1): "\033[0;35mArcade Room\033[0m. The room is huge but all the machines are broken. You can see "
                          "the wires\n"
                          "hanging down from the ceiling.\n"}
        actual = make_board(2, 2)
        self.assertEqual(expect, actual)
