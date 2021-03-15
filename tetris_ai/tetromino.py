# official piece names according to https://tetris.fandom.com/wiki/Tetromino
# imagine grid:
# 0  1  2  3
# 4  5  6  7
# 8  9  10 11
# 12 13 14 15
#
tetromino_layouts = {
    "I": [[1, 5, 9, 13], [4, 5, 6, 7]],
    "J": [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
    "L": [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
    "O": [[1, 2, 5, 6]],
    "S": [[6, 7, 9, 10], [1, 5, 6, 10], ],
    "T": [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9], ],
    "Z": [[4, 5, 9, 10], [2, 6, 5, 9], ]
}


class Tetromino:
    def __init__(self, tetromino_shape: str):
        try:
            self._layout = tetromino_layouts[tetromino_shape].copy()
            self.shape = tetromino_shape
            self.rotation = 0
        except:
            raise KeyError(
                f"Tetromino type '{tetromino_shape}' not found." +
                f"Valid values are: {Tetromino.shape_keys()}")

    @classmethod
    def shape_keys(Self):
        return list(tetromino_layouts.keys())

    def rotate(self, steps: int = 1):
        '''1 rotates clockwise, -1 rotates counterclockwise'''
        self.rotation = (self.rotation + steps) % len(self._layout)

    @property
    def layout(self):
        return self._layout[self.rotation]

    def print_block(self):
        print()
        for y in range(4):
            for x in range(4):
                if ((y*4)+x) in self.layout:
                    print("█", end="")
                else:
                    print(" ", end="")
            print()
        print()
