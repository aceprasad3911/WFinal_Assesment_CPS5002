# repair_bot.py

from techburg_simulation.scratch.draft2.abstract_agent import Agent
from techburg_simulation.scratch.draft2.location import Location


class RepairBot(Agent):
    def __init__(self, gui, row: int, col: int) -> None:
        col = int(0)
        row = int(0)
        location = Location(col, row)  # Assuming Location takes (x, y) as (col, row)
        super().__init__(location, gui)  # Pass the GUI instance as the grid
        self.set_type("repair_bot")

    def act(self):
        # Define behavior for RepairBot
        self._move()
        # Additional repair bot logic can be added here
