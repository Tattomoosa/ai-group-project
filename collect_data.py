from statistics import mean, pstdev
from typing import List
from tetris_ai import TetrisGame, TetrisMove
import matplotlib.pyplot as plt
import random

# -------- STEPS FOR RUNNING TESTS -------- #

# 1) Edit "WEIGHTS"
# 2) Change plt.title in plot_data(), so that test number is correct
# 3) Run with command: python collect_data.py
# 4) Save the plot for our data, and record the printed information

# ----------------------------------------- #


# settings
WEIGHTS = {
    "aggregate_height": -1,
    "max_height": -1,
    "holes": -1,
    "lines_cleared": 1,
    "score": 1,
}


def pick_option(options: List[TetrisMove], weights):
    best_option = random.choice(options)
    best_option_eval = calc_pick(best_option, weights)
    for option in options:
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
            + option.lines_cleared * weights["lines_cleared"]
            + option.score * weights["score"])


# Plots one score for every 10 trials, ex. the point at 10 is the average of trials 0-9
def plot_data(scores, iterations):
    x_points = list(range(10, iterations + 1, 10))
    y_points = []

    # Average every 10 data points so graph is not as wild
    i = 0
    while i < iterations:
        y_points.append(mean(scores[i:i+10]))
        i += 10

    plt.plot(x_points, y_points)

    # Change the title to the test number
    plt.title("Test X")
    plt.xlabel("Trial Number")
    plt.ylabel("Score")
    plt.show()


def run_test(iterations=100):
    scores = []
    lines_cleared = []
    for i in range(iterations):
        # Create new game grid and get a list of shapes
        game = TetrisGame()

        while not game.lost:
            # Get possible moves with piece
            options = game.get_move_options()

            # No possible moves - game lost
            if not options:
                break

            # AI STEP - analyze result here
            move = pick_option(options, WEIGHTS)

            # updates game state for next step
            game.execute_move(move)

        scores.append(game.score)
        lines_cleared.append(game.lines_cleared)

    # Print some data after the tests
    print("Average Score: " + str(mean(scores)))
    print("High Score: " + str(max(scores)))
    print("Standard Deviation of Scores: " + str(pstdev(scores)))
    print("Average Lines Cleared per Game: " + str(mean(lines_cleared)))
    print("Most Lines Cleared in a Game: " + str(max(lines_cleared)))
    print("Standard Deviation of Lines: " + str(pstdev(lines_cleared)))

    # Plot the scores
    plot_data(scores, iterations)


run_test()
