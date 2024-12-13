# Survivor Bots:
# - Movement and Energy:
#   Each move depletes bot energy by 5%.
#   If energy drops to 5% or below, bots consume parts immediately to restore energy.
#   Energy is restored at recharge stations; bots can also rest to regenerate at a rate of 1% per simulation step without consuming parts.
# - Carrying and Collecting:
#   Bots can carry only one part at a time.
#   Prioritize larger parts when selecting.

# survivor_bot.py
import random  # Importing the random module to enable random selection of movement


class SurvivorBot:
    def __init__(self, grid, row, col):
        self.energy_value = 100  # Start with full energy (100%)
        self.carrying_part_status = None  # Initially not carrying any part
        self.grid = grid  # Store a reference to the Grid instance
        self.__location = [row, col]  # Store the bots location as a private attribute
        self.grid.set_cell(row, col, 'survivor_bot')  # Set the initial location in the grid

    def _move(self, bot_type):
        free_locations = []  # List to store potential new locations for the bot
        row, col = self.__location  # Get the current location of the bot
        # Define possible movement directions as (row_change, col_change)
        directions = [(-1, -1), (-1, 0), (-1, +1), (0, -1), (0, 0), (0, +1), (+1, -1), (+1, 0), (+1, +1)]
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            # Check if the new position is within the bounds of the grid
            if 0 <= new_row < self.grid.grid_size and 0 <= new_col < self.grid.grid_size:
                cell = self.grid.get_cell(new_row, new_col)
                # Check if the cell is unoccupied or has a green background
                if cell.content == "empty":
                    free_locations.append([new_row, new_col])  # Add the valid new location to the list

        if free_locations:  # Check if there are any free locations to move to
            free = random.choice(free_locations)  # Randomly select one of the free locations
            previous = self.__location  # Store the current location before moving
            # Move the bot to the new location in the grid
            self.grid.set_cell(free[0], free[1], bot_type)
            # Instead of clearing the old cell, just set its content to empty and keep its background
            self.grid.set_cell(previous[0], previous[1], 'empty')  # Clear the bots old location in the grid
            self.__location = free  # Update the bots location to the new position

            # Each move depletes bot energy by 5%.
            self.energy_value -= 5
            print("energy reduce by 5, energy is now at:", [self.energy_value])
            return self.energy_value

    def _charge(self, energy):
        #   Energy is restored at recharge stations; bots can also rest to regenerate at a rate of 1% per simulation step without consuming parts.
        pass

    def _rest(self):
        # Energy is restored at recharge stations; bots can also rest to regenerate at a rate of 1% per simulation step without consuming parts.
        pass

    def _carry(self):
        #   Bots can carry only one part at a time.
        #   Prioritize larger parts when selecting.
        pass

    def _eat(self):
        # If energy drops to 5% or below, bots consume parts immediately to restore energy.
        pass

    def _memory(self):
        pass

    def _super_boost(self):
        #  Bots can enhance speed, vision, or energy based on spare parts consumed:
        # #   Speed: Default movement occurs every other simulation step; a speed enhancement of 51–100% allows movement every step, with a maximum enhancement of 100%.
        # #   Vision: Detects parts in adjacent cells; with 51–100% enhancement, bots detect two cells away, and up to three cells away with 101–150% enhancement. Maximum detection enhancement is 150%.
        pass

    def act(self):
        self._move('survivor_bot')  # Public method to allow the bot to act (move)
