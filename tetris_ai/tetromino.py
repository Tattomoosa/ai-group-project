# official piece names according to https://tetris.fandom.com/wiki/Tetromino

# this configuration is based on https://levelup.gitconnected.com/writing-tetris-in-python-2a16bddb5318
# numbers indicated filled indices in this grid:

# 0  1  2  3
# 4  5  6  7
# 8  9  10 11
# 12 13 14 15

# each index in the array represents

from .grid import layout_to_grid


tetromino_layouts = {
    "I": [[1, 5, 9, 13], [4, 5, 6, 7]],
    "J": [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
    "L": [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
    "O": [[1, 2, 5, 6]],
    "S": [[6, 7, 9, 10], [1, 5, 6, 10]],
    "T": [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
    "Z": [[4, 5, 9, 10], [2, 5, 6, 9]]
}


tetromino_grids = {
    shape: list(map(layout_to_grid, tetromino_layouts[shape]))
    for shape in tetromino_layouts.keys()
}


class Tetromino:
    def __init__(self, tetromino_shape_key: str, rotation: int = 0):
        try:
            self._layout = tetromino_layouts[tetromino_shape_key.upper()]
            self._grid = tetromino_grids[tetromino_shape_key.upper()]
            self.shape_key = tetromino_shape_key
            self._rotation = rotation
        except:
            raise KeyError(
                f"Tetromino type '{tetromino_shape_key}' not found. " +
                f"Valid values are: {Tetromino.valid_layout_keys()}")

    def rotate(self, steps: int = 1):
        '''default 1 rotates counterclockwise, -1 rotates clockwise'''
        self.rotation += steps

    @staticmethod
    def valid_layout_keys():
        ''' I, J, L, O, S, T, Z '''
        return list(tetromino_layouts.keys())

    @staticmethod
    def get_all():
        ''' Returns a fresh list of all tetrominos '''
        return list(map(lambda x: Tetromino(x), Tetromino.valid_layout_keys()))

    @property
    def layout(self):
        '''returns the correct layout with respect to rotation'''
        return self._layout[self.rotation].copy()

    @property
    def rotation(self):
        return self._rotation

    @rotation.setter
    def rotation(self, value):
        self._rotation = value % len(self._layout)

    @property
    def rotation_steps(self):
        '''returns the number of rotation steps this piece has'''
        return len(self._layout)

    @property
    def grid(self):
        '''returns the correct grid with respect to rotation'''
        return self._grid[self.rotation]

    @property
    def number_of_unique_rotations(self):
        '''
        returns the number of rotation shapes that are unique, e.g. "O" has 1,
        "J" has 4
        '''
        return len(self._layout)

    def as_shape(self):
        '''
        returns the current shape in a 4x4 grid of flags, e.g "I" shape:
        [
            0, 1, 0, 0,
            0, 1, 0, 0,
            0, 1, 0, 0,
            0, 1, 0, 0,
        ]
        '''
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
        ''' prints as a tetris block '''
        shape = self.as_shape()
        print()
        for row in shape:
            for cell in row:
                print("██" if cell else "  ", end="")
            print()
        print()

    def copy(self):
        copy = Tetromino(self.shape_key)
        copy.rotation = self.rotation
        return copy

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False
        return self.shape_key == other.shape_key and self.rotation == other.rotation

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return f"< Tetromino shape_key = '{self.shape_key}' rotation = {self.rotation} >"
