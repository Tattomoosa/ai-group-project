from .grid import Grid
from .tetromino import Tetromino
from random import shuffle


class TetrisMove:
    def __init__(
        self,
        tetromino: Tetromino,
        x: int,
        before: Grid,
        result: Grid,
        lines_cleared: int
    ):
        self.tetromino = tetromino
        self.x = x
        self.before = before
        self.result = result
        self.lines_cleared = lines_cleared
        self.score = 0
        if lines_cleared == 1:
            self.score = 50
        elif lines_cleared == 2:
            self.score = 150
        elif lines_cleared == 3:
            self.score = 350
        elif lines_cleared == 4:
            self.score = 1000

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False
        return self.tetromino == other.tetromino and \
            self.x == other.x and \
            self.result == other.result

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        tet_grid = self.tetromino.grid.translate(self.x, 0)
        move_grid = self.before.copy()
        move_grid.absorb(tet_grid)
        return str(move_grid)


class TetrisGame:

    def __init__(self):
        self.grid = Grid()
        self.lost = False
        # will be filled next time get_next_tetromino is called
        self._tetromino_bag = []
        self._get_next_tetromino()
        self.turns_elapsed = 0
        self.lines_cleared = 0
        self.score = 0

    def _get_move_outcome(self, tetromino: Tetromino, x: int) -> [Grid, None]:
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
        return TetrisMove(tetromino, x, self.grid.copy(), grid, lines_cleared)

    # returns (x, rotation)[]
    def _get_possible_moves(self, piece: Tetromino) -> [(int, int)]:
        moves = []
        half_grid_width = int(Grid.WIDTH / 2)
        for x in range(-half_grid_width, half_grid_width + 1):
            # for each unique rotation of the piece
            for rotation in range(piece.number_of_unique_rotations):
                moves.append((x, rotation))
        return moves

    def get_move_options(self, piece: [Tetromino, None] = None) -> TetrisMove:
        if piece is None:
            piece = self.current_piece
        moves = self._get_possible_moves(piece)

        def map_moves_to_outcomes(move):
            x = move[0]
            rotated_piece = piece.copy()
            rotated_piece.rotation = move[1]
            return self._get_move_outcome(rotated_piece, x)

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
        self.lines_cleared += move.lines_cleared
        self.score += move.score

    def print_stats(self):
        print("Next piece:")
        self.current_piece.print_block()
        print(f"Score: {self.score}")
        print(f"Pieces dropped: {self.turns_elapsed}")
        print(f"Lines cleared: {self.lines_cleared}")
        print("Aggregate height: " + str(self.grid.aggregate_height()))
        print("Max height: " + str(self.grid.max_height()))
        print("Holes: " + str(self.grid.holes()))
