# Repair Bots and Gatherer Bots.
# #   Collaboration among bots allows creation of new bots at stations:
# #   20% chance of creating a gatherer bot (costs 30% energy from each bot).
# #   5% chance of creating a repair bot (costs 50% energy from each bot).
# gatherer_bot.py
import random
from techburg_simulation.src.bots.survivor_bot import SurvivorBot


class GathererBot(SurvivorBot):
    def __init__(self, grid, row, col):
        super().__init__(grid, row, col)
        self.grid = grid  # Store a reference to the Grid instance
        self.__location = [row, col]  # Store the bot's location as a private attribute
        self.grid.set_cell(row, col, 'gatherer_bot')  # Set the initial location in the grid

    def __move(self):
        free_locations = []  # List to store potential new locations for the bot
        row, col = self.__location  # Get the current location of the bot

        # Define possible movement directions as (row_change, col_change)
        directions = [(-1, -1), (-1, 0), (-1, +1), (0, -1), (0, 0), (0, +1), (+1, -1), (+1, 0), (+1, +1)]
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            # Check if the new position is within the bounds of the grid and is unoccupied
            if 0 <= new_row < self.grid.grid_size and 0 <= new_col < self.grid.grid_size:
                cell = self.grid.get_cell(new_row, new_col)
                if cell.emoji == "":  # Assuming emoji is None if the cell is unoccupied
                    free_locations.append([new_row, new_col])  # Add the valid new location to the list

        if free_locations:  # Check if there are any free locations to move to
            free = random.choice(free_locations)  # Randomly select one of the free locations
            previous = self.__location  # Store the current location before moving
            self.grid.set_cell(free[0], free[1], 'gatherer_bot')  # Move the bot to the new location in the grid
            self.grid.set_cell(previous[0], previous[1], None)  # Clear the bot's old location in the grid
            self.__location = free  # Update the bot's location to the new position

    def act(self):
        self.__move()  # Public method to allow the bot to act (move)
