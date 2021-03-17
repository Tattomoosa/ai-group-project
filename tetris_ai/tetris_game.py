from .grid import Grid
from .tetromino import Tetromino
from random import shuffle


class TetrisGame:

    def __init__(self):
        self.grid = Grid()
        self.lost = False
        # will be filled next time get_next_tetromino is called
        self.tetromino_bag = []
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
        return grid

    # returns (x, rotation)[]
    def get_possible_moves(self, piece: Tetromino) -> [(int, int)]:
        moves = []
        half_grid_width = int(Grid.WIDTH / 2)
        for x in range(-half_grid_width, half_grid_width + 1):
            # for each unique rotation of the piece
            for rotation in range(piece.number_of_unique_rotations):
                moves.append((x, rotation))
        return moves

    def get_possible_outcomes(self, piece: Tetromino) -> [((Tetromino, int), Grid)]:
        moves = self.get_possible_moves(piece)

        def map_fn(move):
            x = move[0]
            rotated_piece = piece.copy()
            rotated_piece.rotation = move[1]
            print('piece rotation: ', rotated_piece.rotation)
            return self.get_move_outcome(piece, x)
        return list(map(map_fn, moves))

    def get_next_tetromino(self) -> Tetromino:
        ''' gets a random tetris piece - according to tetris rules '''
        if not self.tetromino_bag:
            self.tetromino_bag = Tetromino.get_all()
            shuffle(self.tetromino_bag)
        self.current_piece = self.tetromino_bag.pop()
        return self.current_piece

    def execute_move(self, piece: Tetromino, x: int):
        self.grid = self.get_move_outcome(piece, x)
        self.turns_elapsed += 1
