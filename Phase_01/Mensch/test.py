import unittest
import board
import logic

class TestChain(unittest.TestCase):
    def setUp(self):
        board.create_board()

    def test_piece_in(self):
        pass

    def test_game(self):
        player = board.get_player()

        board.display_current_player()

        roll = board.roll()

        board.display_current_roll()

        options = logic.options(player, roll)

        board.query_player(options)

        board.next_player()