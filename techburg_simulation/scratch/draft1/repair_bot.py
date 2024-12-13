# Repair Bots and Gatherer Bots.
# #   Collaboration among bots allows creation of new bots at stations:
# #   20% chance of creating a gatherer bot (costs 30% energy from each bot).
# #   5% chance of creating a repair bot (costs 50% energy from each bot).

# repair_bot.py
# Import the SurvivorBot class from the specified module.
# RepairBot will inherit from this class, gaining its properties and methods.
from techburg_simulation.src.bots.survivor_bot import SurvivorBot


# Define the RepairBot class, which inherits from the SurvivorBot class.
class RepairBot(SurvivorBot):
    def __init__(self, grid, row, col):
        # Call the constructor of the parent class (SurvivorBot) to initialize the bot.
        super().__init__(grid, row, col)
        # Set the initial location of the RepairBot in the grid by marking its position with the string 'repair_bot'.
        self.grid.set_cell(row, col, 'repair_bot')  # Set the initial location in the grid

    def act(self):
        # Define the action method for the RepairBot.
        # This method will be called to perform the bot's actions during each simulation step.
        self._move('repair_bot')  # Call the move method with the specific bot type

    def _create_bot(self):
        pass
