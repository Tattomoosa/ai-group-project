from .grid import Grid
from .tetromino import Tetromino
from random import shuffle


class TetrisMove:
    def __init__(self, tetromino: Tetromino, x: int, outcome: Grid, lines_cleared: int):
        self.tetromino = tetromino
        self.x = x
        self.result = outcome
        self.lines_cleared = lines_cleared

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False
        return self.tetromino == other.tetromino and \
            self.x == other.x and \
            self.result == other.result

    def __ne__(self, other):
        return not self == other


class TetrisGame:

    def __init__(self):
        self.grid = Grid()
        self.lost = False
        # will be filled next time get_next_tetromino is called
        self._tetromino_bag = []
        self._get_next_tetromino()
        self.turns_elapsed = 0

    def get_move_outcome(self, tetromino: Tetromino, x: int) -> [Grid, None]:
        tet_grid = tetromino.grid
        tet_grid = tet_grid.translate(x, 0)
        # translate already checks collisions, if None comes back then
        # the tetromino is out of bounds
        if tet_grid is None:
            return None

        # if starting position is invalid, move is invalid
        if self.grid.collision(tet_grid):
            return None

        # drop piece
        while tet_grid_down := tet_grid.translate(0, 1):
            if self.grid.collision(tet_grid_down):
                break
            tet_grid = tet_grid_down

        grid = self.grid.copy()
        grid.absorb(tet_grid)
        lines_cleared = grid.complete_lines()
        grid.wipe_complete_lines()
        return TetrisMove(tetromino, x, grid, lines_cleared)

    # returns (x, rotation)[]
    def _get_possible_moves(self, piece: Tetromino) -> [(int, int)]:
        moves = []
        half_grid_width = int(Grid.WIDTH / 2)
        for x in range(-half_grid_width, half_grid_width + 1):
            # for each unique rotation of the piece
            for rotation in range(piece.number_of_unique_rotations):
                moves.append((x, rotation))
        return moves

    def get_move_options(self, piece: Tetromino) -> TetrisMove:
        moves = self._get_possible_moves(piece)

        def map_moves_to_outcomes(move):
            x = move[0]
            rotated_piece = piece.copy()
            rotated_piece.rotation = move[1]
            return self.get_move_outcome(rotated_piece, x)

        outcomes = map(map_moves_to_outcomes, moves)
        outcomes = filter(lambda x: x != None, outcomes)
        return list(outcomes)

    def _get_next_tetromino(self) -> Tetromino:
        ''' gets a random tetris piece - according to tetris rules '''
        if not self._tetromino_bag:
            self._tetromino_bag = Tetromino.get_all()
            shuffle(self._tetromino_bag)
        self.current_piece = self._tetromino_bag.pop()
        return self.current_piece

    def execute_move(self, move: TetrisMove):
        self.grid = move.result
        self.current_piece = self._get_next_tetromino()
        self.turns_elapsed += 1
