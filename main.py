from typing import List
from tetris_ai import Tetromino, TetrisGame, TetrisMove
import random


def pick_option(options: List[TetrisMove]):
    # The weights for our heuristics
    weights = {
        "aggregate_height": -1,
        "max_height": -1,
        "holes": -1,
        "lines_cleared": 1
    }
    best_option = random.choice(options)
    best_option_eval = calc_pick(best_option, weights)
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

        # TODO do something better
        # Higher the score means better option
        test_eval = calc_pick(option, weights)
        if test_eval > best_option_eval:
            # if False:
            best_option = option
            best_option_eval = test_eval

    return best_option


# Evaluate how good an option is based on the weight, higher score is better
def calc_pick(option, weights):
    return (option.result.aggregate_height() * weights["aggregate_height"]
            + option.result.max_height() * weights["max_height"]
            + option.result.holes() * weights["holes"]
            + option.lines_cleared * weights["lines_cleared"])


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
