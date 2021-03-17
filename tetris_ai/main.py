from tetromino import *
from grid import *
import random

def run_game_example():
    
    # Create new game grid and get a list of shapes
    game_grid = Grid()
    shapes = Tetromino.valid_layout_keys()
    
    while True:
    
        # Choose random tetromino
        shape = random.choice(shapes)
        tet = Tetromino(shape)
        tet_grid = tet.grid
        
        # Check to see if this piece can be placed on the board without a
        # collision.  (If not, it's game over)
        if game_grid.collision(tet_grid):
            print("Game over!")
            break
        
        # Rotate the tetromino randomly
        tet.rotate(random.randint(1, tet.rotation_steps))
        tet_grid = tet.grid
        
        # Check for a collision again, if there is one, revert back
        if game_grid.collision(tet_grid):
            tet = Tetromino(shape)
            tet_grid = tet.grid
        
        # Let's try moving the tetromino either right or left a random amount
        direction = random.choice([-1, 1])
        count = random.randint(0, 5)
        
        # Move the tetromino that direction step-by-step, checking for
        # collisions each step
        while count and (tet_grid_side := tet_grid.translate(direction, 0)):
            if game_grid.collision(tet_grid_side):
                break
            tet_grid = tet_grid_side
            count -= 1
        
        
        # Let's move the tetromino down until it can't go down anymore
        # We go either until the translation is invalid (meaning we tried to
        # move passed the floor) or until we collide with existing blocks
        while tet_grid_down := tet_grid.translate(0, 1):
            if(game_grid.collision(tet_grid_down)):
                break
            tet_grid = tet_grid_down
        
        # We've found a good random spot to plant our tetromino
        # Let's get some stats about this move
        game_grid_copy = game_grid.copy()
        game_grid_copy.absorb(tet_grid)
        
        aggregate_height = game_grid_copy.aggregate_height()
        max_height = game_grid_copy.max_height()
        holes = game_grid_copy.holes()
        complete_lines = game_grid_copy.complete_lines()
        
        # That would be some very useful info for an AI trying to decide how
        # good of a position this is!
        
        # Let's print the new game grid and its stats
        print(game_grid_copy)
        
        print("Aggregate height: " + str(aggregate_height))
        print("Max height: " + str(max_height))
        print("Holes: " + str(holes))
        print("Complete lines: " + str(complete_lines))
        
        # Pause to let the user hit enter
        input("Press enter to continue...")
        
        # Let's commit to that state
        game_grid = game_grid_copy
        
        # Time to do some post-move clean-up
        game_grid.wipe_complete_lines()
        

run_game_example()
