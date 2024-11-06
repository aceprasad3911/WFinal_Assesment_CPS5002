# Repair Bots and Gatherer Bots.
# #   Collaboration among bots allows creation of new bots at stations:
# #   20% chance of creating a gatherer bot (costs 30% energy from each bot).
# #   5% chance of creating a repair bot (costs 50% energy from each bot).

# repair_bot.py

import random
from techburg_simulation.src.bots.survivor_bot import SurvivorBot


class RepairBot(SurvivorBot):
    def __init__(self, grid, row, col):
        super().__init__(grid, row, col)  # Initialize the parent class
        self.grid.set_cell(row, col, 'repair_bot')  # Set the initial location in the grid

    # You can override the __move method if you want different movement logic
    def __move(self):
        free_locations = []  # List to store potential new locations for the bot
        row, col = self._SurvivorBot__location  # Access the private attribute from the parent class

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
            previous = self._SurvivorBot__location  # Store the current location before moving
            self.grid.set_cell(free[0], free[1], 'repair_bot')  # Move the bot to the new location in the grid
            self.grid.set_cell(previous[0], previous[1], None)  # Clear the bot's old location in the grid
            self._SurvivorBot__location = free  # Update the bot's location to the new position

    def act(self):
        self.__move()  # Public method to allow the bot to act (move)
        self.repair()  # Call the repair method after moving

    def repair(self):
        # Logic for repairing nearby malfunctioning drones or other bots
        row, col = self._SurvivorBot__location
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                if dr == 0 and dc == 0:
                    continue  # Skip the current cell
                neighbor_row, neighbor_col = row + dr, col + dc
                if 0 <= neighbor_row < self.grid.grid_size and 0 <= neighbor_col < self.grid.grid_size:
                    neighbor_cell = self.grid.get_cell(neighbor_row, neighbor_col)
                    if neighbor_cell.content == "malfunctioning_drone":
                        neighbor_cell.set_content("repaired_drone")  # Change the content to indicate repair
                        self.grid.update_display()  # Update the display to reflect the change
                        print(f"RepairBot repaired a drone at ({neighbor_row}, {neighbor_col})")
