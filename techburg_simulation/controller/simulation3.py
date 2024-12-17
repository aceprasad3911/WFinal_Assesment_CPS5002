# simulation3.py
import random

from techburg_simulation.model.objects.bots.gatherer_bot3 import GathererBot
from techburg_simulation.model.objects.bots.malfunction_bot3 import MalfunctionBot
from techburg_simulation.model.objects.bots.repair_bot3 import RepairBot
from techburg_simulation.model.objects.bots.scavenger_bot3 import ScavengerBot
from techburg_simulation.model.objects.recharge_station3 import RechargeStation
from techburg_simulation.model.objects.spare_part3 import SparePart
from techburg_simulation.model.space.grid3 import Grid


class Simulation:
    def __init__(self):
        # Initialize simulation parameters
        self.objects = []  # List to hold all objects
        self.bots = []  # List to hold all bots
        self.grid = None
        self.techburg_grid_size = 0
        self.bot_id_counter = 1
        self.object_id_counter = 1

    def run_simulation(self, grid_size):
        # Perform the simulation logic using the grid_size
        self.techburg_grid_size = int(grid_size)
        self.grid = Grid(self.techburg_grid_size)  # Use the Grid class
        self.initialize_simulation_environment(grid_size)
        self.initialize_bot_population(grid_size)
        return self.techburg_grid_size

    def initialize_simulation_environment(self, grid_size):
        object_coordinates = [
            (RechargeStation, 10, 10),  # Add recharge station at (10, 10)
            (RechargeStation, 20, 20),  # Add another recharge station at (20, 20)
        ]

        # Add 1000 spare parts at random locations
        for _ in range(100):
            x = random.randint(0, grid_size - 1)  # Assuming grid_size is the size of the grid
            y = random.randint(0, grid_size - 1)
            object_coordinates.append((SparePart, x, y))

            # Create all objects in the environment
            for object_class, x, y in object_coordinates:
                self.create_object(object_class, x, y)

    def initialize_bot_population(self, grid_size):
        bot_coordinates = [
            (GathererBot, 8, 8),  # GathererBot at (25, 25)
            (RepairBot, 12, 12),      # RepairBot at (5, 5)
            (RepairBot, 8, 12),  # RepairBot at (5, 5)
            (MalfunctionBot, 47, 30),
            (ScavengerBot, 14, 35)
        ]
        for bot_class, x, y in bot_coordinates:
            self.create_bot(bot_class, x, y)

    def create_object(self, object_class, x, y):
        object_id = self.object_id_counter  # Use object_id_counter for recharge stations
        obj = object_class(self, self.grid, x, y, object_id)  # Create a new object
        self.objects.append(obj)  # Add the object to the list
        self.grid.set_agent(obj, (x, y))  # Set the object in the grid
        self.object_id_counter += 1  # Increment the counter for the next object

    def create_bot(self, bot_class, x, y):
        bot_id = self.bot_id_counter  # Assign the current counter value as the bot ID
        bot = bot_class(self, self.grid, x, y, bot_id)  # Create a new bot of the specified class with the ID
        self.bots.append(bot)  # Add the bot to the list of bots
        self.grid.set_agent(bot, (x, y))  # Set the bot in the grid
        self.bot_id_counter += 1  # Increment the counter for the next bot

    def update(self):
        for bot in self.bots:
            # Store the current position before moving
            current_x, current_y = bot.get_x(), bot.get_y()
            bot.move()  # Call the move method of each bot
            # Get the new position after moving
            new_x, new_y = bot.get_x(), bot.get_y()
            # Update the grid with the new position
            self.grid.set_agent(bot, (new_x, new_y))  # Update the bot's position in the grid
            # Optionally clear the old position if needed
            if (current_x, current_y) != (new_x, new_y):
                self.grid.set_agent(None, (current_x, current_y))  # Clear the old position

# Simulation Branch repository commands:
# git checkout development
# git checkout feature/simulation
# git add "techburg_simulation/controller/simulation3.py"
# git commit -m ""
# git push origin feature/simulation
