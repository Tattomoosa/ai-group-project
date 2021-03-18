import unittest
from tetris_ai import Tetromino, Grid
from tetris_ai.tetris_game import TetrisGame, TetrisMove


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
        self.assertEqual(game.grid, Grid())
        grid_start = game.grid
        game.execute_move(Tetromino("I"), 2)
        # TODO assert grid correctly reflects move above
        self.assertNotEqual(grid_start, game.grid)
        self.assertEqual(game.turns_elapsed, 1)

    def test_move_outcome_equals_move_executed(self):
        game = TetrisGame()
        # starts with empty board
        self.assertEqual(game.grid, Grid())
        after_drop_grid = game.get_move_outcome(Tetromino("I"), 2)

        # state of board should be == to after_drop_grid_check
        after_drop_grid_check_cols = [0] * 10
        after_drop_grid_check_cols[6] = 0xf
        after_drop_grid_check = Grid(after_drop_grid_check_cols)
        self.assertEqual(after_drop_grid, after_drop_grid_check)

        # execute move for real
        game.execute_move(Tetromino("I"), 2)
        self.assertEqual(game.grid, after_drop_grid_check)

    def test_possible_outcomes(self):
        game = TetrisGame()
        move_options = game.get_move_options(Tetromino("I"))

        for option in move_options:
            game = TetrisGame()
            game.execute_move(option.tetromino, option.x)
            self.assertEqual(game.grid, option.result)
