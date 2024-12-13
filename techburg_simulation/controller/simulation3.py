# simulation3.py
import random

from techburg_simulation.model.objects.gatherer_bot3 import GathererBot
from techburg_simulation.model.space.grid3 import Grid


class Simulation:
    def __init__(self):
        # Initialize simulation parameters
        self.repair_bot = None
        self.gatherer_bot = None
        self.survivor_bot = None
        self.recharge_station1 = None
        self.recharge_station2 = None
        self.recharge_station3 = None
        self.grid = None
        self.techburg_grid_size = 0

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
        # random.randint(0, grid_size - 1)
        x_gatherer1 = 1
        y_gatherer1 = 1
        self.gatherer_bot = GathererBot(self, self.grid, x_gatherer1, y_gatherer1)

    def update(self):
        if self.gatherer_bot:
            self.gatherer_bot.move()  # Call the move method of the GathererBot
