import unittest
from tetris_ai import TetrisGame, Tetromino


class TestTetrisGame(unittest.TestCase):

    def test_random_tetrominoes(self):
        all_tetromino_keys = ["I", "J", "L", "O", "S", "T", "Z"]
        game = TetrisGame()
        tetrominos = []
        at_least_one_different_from_default = False
        for _ in range(500):
            # get a whole bag
            for _ in range(7):
                tetrominos.append(game.get_next_tetromino())

            tetrominos_keys = list(
                map(lambda x: x.shape_key, tetrominos))
            # can be different from the default (weak test of randomness but eh)
            if tetrominos_keys != all_tetromino_keys:
                at_least_one_different_from_default = True
            # has one of every piece
            tetrominos_keys.sort()
            self.assertListEqual(
                tetrominos_keys,
                all_tetromino_keys
            )
            tetrominos = []
        self.assertTrue(at_least_one_different_from_default)

    def test_turn_increment(self):
        game = TetrisGame()
        self.assertEqual(game.turns_elapsed, 0)
        # TODO assert grid is empty
        grid_start = game.grid
        game.execute_move(Tetromino("I"), 2)
        # TODO assert grid correctly reflects move above
        self.assertNotEqual(grid_start, game.grid)
        self.assertEqual(game.turns_elapsed, 1)
