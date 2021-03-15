import unittest
from tetris_ai import Tetromino

tetrominos = [
    Tetromino("I"),
    Tetromino("J"),
    Tetromino("L"),
    Tetromino("O"),
    Tetromino("S"),
    Tetromino("T"),
    Tetromino("Z"),
]


class TestTetromino(unittest.TestCase):
    def test_print(self):
        for tetromino in tetrominos:
            print(f"Printing '{tetromino.shape}'")
            tetromino.print_block()
