# Repair Bots and Gatherer Bots.
# #   Collaboration among bots allows creation of new bots at stations:
# #   20% chance of creating a gatherer bot (costs 30% energy from each bot).
# #   5% chance of creating a repair bot (costs 50% energy from each bot).

# gatherer_bot.py
# Import the SurvivorBot class from the specified module.
# GathererBot will inherit from this class, gaining its properties and methods.
from techburg_simulation.src.bots.survivor_bot import SurvivorBot


# Define the GathererBot class, which inherits from the SurvivorBot class.
class GathererBot(SurvivorBot):
    def __init__(self, grid, row, col):
        # Call the constructor of the parent class (SurvivorBot) to initialize the bot.
        super().__init__(grid, row, col)
        # Set the initial location of the GathererBot in the grid by marking its position with the string 'gatherer_bot'.
        self.grid.set_cell(row, col, 'gatherer_bot')  # Set the initial location in the grid

    def act(self):
        # Define the action method for the GathererBot.
        # This method will be called to perform the bot's actions during each simulation step.
        self._move('gatherer_bot')  # Call the move method with the specific bot type