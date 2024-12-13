# simulation3.py
import random

from techburg_simulation.model.objects.gatherer_bot3 import GathererBot
from techburg_simulation.model.objects.repair_bot3 import RepairBot
from techburg_simulation.model.space.grid3 import Grid


class Simulation:
    def __init__(self):
        # Initialize simulation parameters
        self.bots = []  # List to hold all bots
        self.grid = None
        self.techburg_grid_size = 0
        self.bot_id_counter = 1

    def run_simulation(self, grid_size):
        # Perform the simulation logic using the grid_size
        self.techburg_grid_size = int(grid_size)
        self.grid = Grid(self.techburg_grid_size)  # Use the Grid class
        self.initialize_simulation_environment(grid_size)
        self.initialize_bot_population(grid_size)
        return self.techburg_grid_size

    def get_cell(self, row, col):
        # Return the cell object at the specified row and column
        return self.grid[row][col]

    def initialize_simulation_environment(self, grid_size):
        pass

    def initialize_bot_population(self, grid_size):
        bot_coordinates = [
            (GathererBot, 25, 25),  # GathererBot at (25, 25)
            (RepairBot, 5, 5),      # RepairBot at (5, 5)
            (RepairBot, 15, 15),  # RepairBot at (5, 5)
        ]
        for bot_class, x, y in bot_coordinates:
            self.create_bot(bot_class, x, y)

    def create_bot(self, bot_class, x, y):
        bot_id = self.bot_id_counter  # Assign the current counter value as the bot ID
        bot = bot_class(self, self.grid, x, y, bot_id)  # Create a new bot of the specified class with the ID
        self.bots.append(bot)  # Add the bot to the list of bots
        self.bot_id_counter += 1  # Increment the counter for the next bot

    def update(self):
        for bot in self.bots:
            bot.move()  # Call the move method of each bot
