# official piece names according to https://tetris.fandom.com/wiki/Tetromino

# this configuration is based on https://levelup.gitconnected.com/writing-tetris-in-python-2a16bddb5318
# 1s indicate filled, 0s indicate empty indexes in this grid:
# 0  1  2  3
# 4  5  6  7
# 8  9  10 11
# 12 13 14 15
# each index in the array represents

tetromino_layouts = {
    "I": [[1, 5, 9, 13], [4, 5, 6, 7]],
    "J": [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
    "L": [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
    "O": [[1, 2, 5, 6]],
    "S": [[6, 7, 9, 10], [1, 5, 6, 10]],
    "T": [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
    "Z": [[4, 5, 9, 10], [2, 5, 6, 9]]
}


class Tetromino:
    def __init__(self, tetromino_shape_key: str):
        try:
            self._layout = tetromino_layouts[tetromino_shape_key.upper()]
            self.shape_key = tetromino_shape_key
            self.rotation = 0
        except:
            raise KeyError(
                f"Tetromino type '{tetromino_shape_key}' not found. " +
                f"Valid values are: {Tetromino.valid_layout_keys()}")

    def rotate(self, steps: int = 1):
        '''default 1 rotates counterclockwise, -1 rotates clockwise'''
        self.rotation = (self.rotation + steps) % len(self._layout)

    @staticmethod
    def valid_layout_keys():
        ''' I, J, L, O, S, T, Z '''
        return list(tetromino_layouts.keys())

    @property
    def layout(self):
        '''returns the correct layout with respect to rotation'''
        return self._layout[self.rotation].copy()

    def as_shape(self):
        '''returns the current shape in a 4x4 grid of flags'''
        layout = self.layout
        shape = []
        for y in range(4):
            row = []
            shape.append(row)
            for x in range(4):
                if ((y*4)+x) in layout:
                    row.append(1)
                else:
                    row.append(0)
        return shape

    def print_block(self):
        shape = self.as_shape()
        print()
        for row in shape:
            for cell in row:
                print("█" if cell else ".", end="")
            print()
        print()
