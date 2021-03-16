import unittest
from tetris_ai import Tetromino


class TestTetromino(unittest.TestCase):

    # tests whether layouts change as expected based on rotation
    def test_i_spin(self):
        block = Tetromino("I")
        self.assertEqual(block.layout, [1, 5, 9, 13])
        block.rotate()
        self.assertEqual(block.layout, [4, 5, 6, 7])
        block.rotate()
        self.assertEqual(block.layout, [1, 5, 9, 13])
        block.rotate()
        self.assertEqual(block.layout, [4, 5, 6, 7])
        block.rotate()
        self.assertEqual(block.layout, [1, 5, 9, 13])
        block.rotate(-1)
        self.assertEqual(block.layout, [4, 5, 6, 7])
        block.rotate(-1)
        self.assertEqual(block.layout, [1, 5, 9, 13])
        block.rotate(-1)
        self.assertEqual(block.layout, [4, 5, 6, 7])
        block.rotate(-1)
        self.assertEqual(block.layout, [1, 5, 9, 13])

    def test_j_spin(self):
        block = Tetromino("J")
        self.assertEqual(block.layout, [1, 2, 5, 9])
        block.rotate()
        self.assertEqual(block.layout, [0, 4, 5, 6])
        block.rotate()
        self.assertEqual(block.layout, [1, 5, 9, 8])
        block.rotate()
        self.assertEqual(block.layout, [4, 5, 6, 10])
        block.rotate()
        self.assertEqual(block.layout, [1, 2, 5, 9])
        block.rotate(-1)
        self.assertEqual(block.layout, [4, 5, 6, 10])
        block.rotate(-1)
        self.assertEqual(block.layout, [1, 5, 9, 8])
        block.rotate(-1)
        self.assertEqual(block.layout, [0, 4, 5, 6])
        block.rotate(-1)
        self.assertEqual(block.layout, [1, 2, 5, 9])

    def test_l_spin(self):
        block = Tetromino("L")
        self.assertEqual(block.layout, [1, 2, 6, 10])
        block.rotate()
        self.assertEqual(block.layout, [5, 6, 7, 9])
        block.rotate()
        self.assertEqual(block.layout, [2, 6, 10, 11])
        block.rotate()
        self.assertEqual(block.layout, [3, 5, 6, 7])
        block.rotate()
        self.assertEqual(block.layout, [1, 2, 6, 10])
        block.rotate(-1)
        self.assertEqual(block.layout, [3, 5, 6, 7])
        block.rotate(-1)
        self.assertEqual(block.layout, [2, 6, 10, 11])
        block.rotate(-1)
        self.assertEqual(block.layout, [5, 6, 7, 9])
        block.rotate(-1)
        self.assertEqual(block.layout, [1, 2, 6, 10])

    def test_o_spin(self):
        block = Tetromino("O")
        self.assertEqual(block.layout, [1, 2, 5, 6])
        block.rotate()
        self.assertEqual(block.layout, [1, 2, 5, 6])
        block.rotate()
        self.assertEqual(block.layout, [1, 2, 5, 6])
        block.rotate()
        self.assertEqual(block.layout, [1, 2, 5, 6])
        block.rotate()
        self.assertEqual(block.layout, [1, 2, 5, 6])
        block.rotate(-1)
        self.assertEqual(block.layout, [1, 2, 5, 6])
        block.rotate(-1)
        self.assertEqual(block.layout, [1, 2, 5, 6])
        block.rotate(-1)
        self.assertEqual(block.layout, [1, 2, 5, 6])
        block.rotate(-1)
        self.assertEqual(block.layout, [1, 2, 5, 6])

    def test_s_spin(self):
        block = Tetromino("S")
        self.assertEqual(block.layout, [6, 7, 9, 10])
        block.rotate()
        self.assertEqual(block.layout, [1, 5, 6, 10])
        block.rotate()
        self.assertEqual(block.layout, [6, 7, 9, 10])
        block.rotate()
        self.assertEqual(block.layout, [1, 5, 6, 10])
        block.rotate()
        self.assertEqual(block.layout, [6, 7, 9, 10])
        block.rotate(-1)
        self.assertEqual(block.layout, [1, 5, 6, 10])
        block.rotate(-1)
        self.assertEqual(block.layout, [6, 7, 9, 10])
        block.rotate(-1)
        self.assertEqual(block.layout, [1, 5, 6, 10])
        block.rotate(-1)
        self.assertEqual(block.layout, [6, 7, 9, 10])

    def test_t_spin(self):
        block = Tetromino("T")
        self.assertEqual(block.layout, [1, 4, 5, 6])
        block.rotate()
        self.assertEqual(block.layout, [1, 4, 5, 9])
        block.rotate()
        self.assertEqual(block.layout, [4, 5, 6, 9])
        block.rotate()
        self.assertEqual(block.layout, [1, 5, 6, 9])
        block.rotate()
        self.assertEqual(block.layout, [1, 4, 5, 6])
        block.rotate(-1)
        self.assertEqual(block.layout, [1, 5, 6, 9])
        block.rotate(-1)
        self.assertEqual(block.layout, [4, 5, 6, 9])
        block.rotate(-1)
        self.assertEqual(block.layout, [1, 4, 5, 9])
        block.rotate(-1)
        self.assertEqual(block.layout, [1, 4, 5, 6])

    def test_z_spin(self):
        block = Tetromino("Z")
        self.assertEqual(block.layout, [4, 5, 9, 10])
        block.rotate()
        self.assertEqual(block.layout, [2, 5, 6, 9])
        block.rotate()
        self.assertEqual(block.layout, [4, 5, 9, 10])
        block.rotate()
        self.assertEqual(block.layout, [2, 5, 6, 9])
        block.rotate()
        self.assertEqual(block.layout, [4, 5, 9, 10])
        block.rotate(-1)
        self.assertEqual(block.layout, [2, 5, 6, 9])
        block.rotate(-1)
        self.assertEqual(block.layout, [4, 5, 9, 10])
        block.rotate(-1)
        self.assertEqual(block.layout, [2, 5, 6, 9])
        block.rotate(-1)

    # tests whether layouts get converted to correct 2D shape layout
    def test_i_as_shape(self):
        block = Tetromino("I")
        self.assertEqual(block.as_shape(), [
            [0, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 0, 0],
        ])
        block.rotate()
        self.assertEqual(block.as_shape(), [
            [0, 0, 0, 0],
            [1, 1, 1, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ])

    def test_j_as_shape(self):

        block = Tetromino("J")
        self.assertEqual(block.as_shape(), [
            [0, 1, 1, 0],
            [0, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 0],
        ])
        block.rotate()
        self.assertEqual(block.as_shape(), [
            [1, 0, 0, 0],
            [1, 1, 1, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ])
        block.rotate()
        self.assertEqual(block.as_shape(), [
            [0, 1, 0, 0],
            [0, 1, 0, 0],
            [1, 1, 0, 0],
            [0, 0, 0, 0],
        ])
        block.rotate()
        self.assertEqual(block.as_shape(), [
            [0, 0, 0, 0],
            [1, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 0],
        ])

    def test_l_as_shape(self):
        block = Tetromino("L")
        self.assertEqual(block.as_shape(), [
            [0, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 0]
        ])
        block.rotate()
        self.assertEqual(block.as_shape(), [
            [0, 0, 0, 0],
            [0, 1, 1, 1],
            [0, 1, 0, 0],
            [0, 0, 0, 0]
        ])
        block.rotate()
        self.assertEqual(block.as_shape(), [
            [0, 0, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 1, 1],
            [0, 0, 0, 0]
        ])
        block.rotate()
        self.assertEqual(block.as_shape(), [
            [0, 0, 0, 1],
            [0, 1, 1, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ])

    def test_o_as_shape(self):
        block = Tetromino("O")
        self.assertEqual(block.as_shape(), [
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ])
        block.rotate()
        self.assertEqual(block.as_shape(), [
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ])

    def test_s_as_shape(self):
        block = Tetromino("S")
        self.assertEqual(block.as_shape(), [
            [0, 0, 0, 0],
            [0, 0, 1, 1],
            [0, 1, 1, 0],
            [0, 0, 0, 0]
        ])
        block.rotate()
        self.assertEqual(block.as_shape(), [
            [0, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 0]
        ])

    def test_t_as_shape(self):
        block = Tetromino("T")
        self.assertEqual(block.as_shape(), [
            [0, 1, 0, 0],
            [1, 1, 1, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ])
        block.rotate()
        self.assertEqual(block.as_shape(), [
            [0, 1, 0, 0],
            [1, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 0]
        ])
        block.rotate()
        self.assertEqual(block.as_shape(), [
            [0, 0, 0, 0],
            [1, 1, 1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 0]
        ])

    def test_z_as_shape(self):
        block = Tetromino("Z")
        self.assertEqual(block.as_shape(), [
            [0, 0, 0, 0],
            [1, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0]
        ])
        block.rotate()
        self.assertEqual(block.as_shape(), [
            [0, 0, 1, 0],
            [0, 1, 1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 0]
        ])
