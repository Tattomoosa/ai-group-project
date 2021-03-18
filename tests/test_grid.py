import unittest
from tetris_ai import Grid


class TestGrid(unittest.TestCase):

    def test_wipe_complete_lines_flat(self):
        # Twelve complete lines
        cols = [0x0fff] * 10
        grid = Grid(cols)
        self.assertEqual(grid.complete_lines(), 12)
        grid.wipe_complete_lines()

        # All lines should be wiped
        self.assertEqual(grid.complete_lines(), 0)

    def test_wipe_1_complete_line_on_bottom(self):
        # Twelve complete lines
        cols = [0x0001] * 10
        cols[2] = 0x000f
        grid = Grid(cols)
        self.assertEqual(grid.complete_lines(), 1)
        grid.wipe_complete_lines()

        # The complete line should be wiped
        self.assertEqual(grid.complete_lines(), 0)

        # board should now match this collision_grid
        collision_grid_cols = [0] * 10
        collision_grid_cols[2] = 0x0007
        collision_grid = Grid(collision_grid_cols)
        self.assertTrue(grid == collision_grid)

    def test_wipe_2_complete_lines(self):
        # 2 complete lines
        cols = [0x0003] * 10
        # some cells sticking up above
        cols[2] = 0x000f
        grid = Grid(cols)
        self.assertEqual(grid.complete_lines(), 2)
        grid.wipe_complete_lines()

        # All lines should be wiped
        self.assertEqual(grid.complete_lines(), 0)

        # board should now match this collision_grid
        collision_grid_cols = [0] * 10
        collision_grid_cols[2] = 0x0003
        collision_grid = Grid(collision_grid_cols)
        self.assertTrue(grid == collision_grid)
