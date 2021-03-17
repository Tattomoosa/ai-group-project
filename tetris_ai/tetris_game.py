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

    def get_move_outcome(self, piece: Tetromino, x: int) -> Grid:
        # TODO
        return Grid()

    # returns (x, rotation)
    def get_possible_moves(self, piece: Tetromino) -> [(int, int)]:
        moves = []
        # -1 is minimum place a piece could potentially go I think?
        for x in range(-1, self.grid.width):
            # for each unique rotation of the piece
            for rotation in range(piece.number_of_unique_rotations):
                moves.append((x, rotation))
        return moves

    def get_possible_outcomes(self) -> [((Tetromino, int), Grid)]:
        moves = self.get_possible_moves(self.current_piece)

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


def run():
    game = TetrisGame()
    turn_count = 0
    while not game.lost:
        turn_count += 1
        if turn_count > 5000:
            game.lost = True
