from typing import List
from tetris_ai import Tetromino, TetrisGame, TetrisMove
import random


def pick_option(options: List[TetrisMove]):
    best_option = random.choice(options)
    for option in options:
        # Let's get some stats about this move's results
        # This would be some very useful info for an AI trying to decide how
        # good of a position this is!
        aggregate_height = option.result.aggregate_height()
        max_height = option.result.max_height()
        holes = option.result.holes()
        lines_cleared = option.lines_cleared
        print('OPTION: ',
              aggregate_height,
              max_height,
              holes,
              lines_cleared)

        # weight the above and figure out best option
        # if False:
        if aggregate_height < best_option.result.aggregate_height():
            best_option = option

    return best_option


def run_game_example():

    # Create new game grid and get a list of shapes
    game = TetrisGame()

    while not game.lost:
        # Clear the terminal
        print(chr(27) + "[2J")

        # Get possible moves with piece
        options = game.get_move_options()

        # No possible moves - game lost
        if not options:
            break

        # AI STEP - analyze result here
        move = pick_option(options)

        # updates game state for next step
        game.execute_move(move)

        # Let's print the new game grid and its stats
        print(game.grid)
        print("Aggregate height: " + str(game.grid.aggregate_height()))
        print("Max height: " + str(game.grid.max_height()))
        print("Holes: " + str(game.grid.holes()))
        print("Complete lines: " + str(game.grid.complete_lines()))
        print("Next piece:")
        game.current_piece.print_block()

        # Pause to let the user hit enter
        input("Press enter to continue...")


run_game_example()
