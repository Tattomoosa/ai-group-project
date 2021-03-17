from collections import deque


def count_bits_set(num: int):

    # counts the number of bits set in the given integer
    count = 0

    while num:
        num &= num - 1
        count += 1

    return count


class Grid:

    HEIGHT = 24
    WIDTH = 10

    def __init__(self, cols=[0] * WIDTH):

        # Creates a new Grid from the given columns
        # Defaults to empty grid

        assert len(cols) == Grid.WIDTH

        # Copies columns from cols, or uses cols directly if it's a deque
        self._cols = cols if isinstance(cols, deque) else deque(cols)

    def translate(self, x: int, y: int):

        # Translates this grid
        #    x: horizontal shift, positive for right shift and negative for left
        #    y: vertical shift downward (must be non-negative)
        # Returns a new, transformed grid for a successful transform, or None
        # if the transform would move blocks out of bounds

        assert y >= 0
        assert y <= Grid.HEIGHT
        assert x >= -Grid.WIDTH
        assert x <= Grid.WIDTH

        # Copy columns as we'll be creating a new grid if translate succeeds
        new_cols = deque(self._cols)

        # Horizontal shift

        # If x is negative, we're shifting left
        if x < 0:
            col_count = -x
            rotate_direction = -1
            edge_index = 0

        # If x is positive, we're shifting right
        else:
            col_count = x
            rotate_direction = 1
            edge_index = -1

        # Check that col_count columns on the edge are empty and rotate grid
        for _ in range(col_count):
            if new_cols[edge_index] == 0:
                new_cols.rotate(rotate_direction)
            else:
                # If column wasn't empty, piece is going out of bounds
                return None

        # Vertical shift

        if y > 0:
            for _ in range(Grid.WIDTH):

                old_col = new_cols[0]
                new_col = old_col >> y

                # Check to be sure we haven't moved non-zero bits out of bounds
                if (new_col << y) == old_col:
                    new_cols[0] = new_col
                else:
                    return None

                new_cols.rotate(1)

        # Translate was successful, update this grid
        return Grid(new_cols)

    def collision(selfA, selfB):

        # Returns true if there is a collision between two grids

        for colA, colB in zip(selfA._cols, selfB._cols):
            if (colA & colB) != 0:
                return True

        return False

    def absorb(self, other):

        # Combines another grid's blocks into this one
        # (for example, a transformed tetromino)

        assert not self.collision(other)

        for _ in range(Grid.WIDTH):
            self._cols[0] |= other._cols[0]
            self._cols.rotate(1)
            other._cols.rotate(1)

    def copy(self):
        # Creates a copy of this grid
        return Grid(deque(self._cols))

    @staticmethod
    def cell_to_string(col: int, y: int):
        return "  " if ((col >> (Grid.HEIGHT - y - 1)) & 1) == 0 else "██"

    def row_to_string(self, y: int):
        return "|" + "".join(Grid.cell_to_string(col, y) for col in self._cols) + "|"

    def to_string(self):
        return "\n".join(self.row_to_string(y) for y in range(Grid.HEIGHT))

    def __str__(self):
        return self.to_string()

    def __eq__(self, other):
        ''' returns true if 2 Grids are equal '''
        if not isinstance(other, type(self)):
            return False
        for i in range(len(self._cols)):
            if self._cols[i] != other._cols[i]:
                return False
        return True

    def __ne__(self, other):
        return not self == other

    def aggregate_height(self):
        return sum(col.bit_length() for col in self._cols)

    def max_height(self):
        return max(col.bit_length() for col in self._cols)

    @staticmethod
    def holes_in_column(col: int) -> int:

        # gets the number of bits under the 'surface'
        relevent_bits = col.bit_length() - 1

        if relevent_bits < 1:
            return 0

        # flip bits so holes are 1's and blocks are 0's
        # mask so only relevent_bits are kept
        col = ~col & ((1 << relevent_bits) - 1)

        return count_bits_set(col)

    def holes(self) -> int:
        # Returns the number of holes in this grid, that is, empty cells with
        # at least one block above them
        return sum(Grid.holes_in_column(col) for col in self._cols)

    def complete_line_mask(self):

        # mask all bits
        mask = -1

        # AND with the existing blocks in each column
        for col in self._cols:
            mask &= col

        # only rows with all bits set will still have a bit set
        return mask

    def complete_lines(self) -> int:
        # Returns the number of complete lines on this grid
        return count_bits_set(self.complete_line_mask())

    def wipe_masked_lines(self, mask: int):

        count = 0

        while (line := mask.bit_length() - 1) >= 0:

            mask &= ~(1 << line)
            mask_before = ~(-1 << line)
            mask_after = -1 << (line + 1)

            for _ in range(Grid.WIDTH):
                col = self._cols[0]
                self._cols[0] = (col & mask_before) | (col & mask_after) >> 1
                self._cols.rotate(1)

            count += 1

        return count

    def wipe_complete_lines(self):
        # Wipes all complete lines on this grid
        self.wipe_masked_lines(self.complete_lines())


def layout_to_grid(layout):

    cols = deque([0] * Grid.WIDTH)

    for x in range(4):

        col = 8 if ((x) in layout) else 0
        col |= 4 if ((x + 4) in layout) else 0
        col |= 2 if ((x + 8) in layout) else 0
        col |= 1 if ((x + 12) in layout) else 0
        col <<= Grid.HEIGHT - 4

        cols[0] = col
        cols.rotate(-1)

    cols.rotate((4 - Grid.WIDTH) // 2)

    return Grid(cols)
