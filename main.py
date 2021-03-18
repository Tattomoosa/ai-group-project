from typing import List
from tetris_ai import Tetromino, TetrisGame, TetrisMove
import random
import time

# settings
PRESS_ENTER_TO_ADVANCE = False
SLEEP_TIME = 0.1


def clear_terminal():
    # Clear the terminal
    print(chr(27) + "[2J")


def pick_option(options: List[TetrisMove]):
    # The weights for our heuristics
    weights = {
        "aggregate_height": -1,
        "max_height": -1,
        "holes": -1,
        "lines_cleared": 1,
        "score": 1,
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
        score = option.score
        # print(f'OPTION {index}: ',
        #      aggregate_height,
        #      max_height,
        #      holes,
        #      lines_cleared)

        # TODO do something better
        # Higher the score means better option
        test_eval = calc_pick(option, weights)
        if test_eval > best_option_eval:
            # if False:
            best_option = option
            best_option_eval = test_eval

    # print(f'PICKED OPTION {best_index}:')
    # print(best_option)
    # sleep_or_wait("Press enter to drop...")
    return best_option


# Evaluate how good an option is based on the weight, higher score is better
def calc_pick(option, weights):
    return (option.result.aggregate_height() * weights["aggregate_height"]
            + option.result.max_height() * weights["max_height"]
            + option.result.holes() * weights["holes"]
            + option.lines_cleared * weights["lines_cleared"]
            + option.score * weights["score"])


def run_game_example():

    # Create new game grid and get a list of shapes
    game = TetrisGame()

    while not game.lost:
        clear_terminal()

        # Get possible moves with piece
        options = game.get_move_options()

        # No possible moves - game lost
        if not options:
            break

        # AI STEP - analyze result here
        move = pick_option(options)
        game.print_stats()
        print(move)
        time.sleep(SLEEP_TIME)

        # updates game state for next step
        game.execute_move(move)

        clear_terminal()
        # Let's print the new game grid and its stats
        game.print_stats()
        print(game.grid)

        # Pause to let the user hit enter
        if PRESS_ENTER_TO_ADVANCE:
            input("Press Enter to continue...")
        else:
            time.sleep(SLEEP_TIME)


run_game_example()
