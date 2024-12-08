# repair_bot.py

from abc import ABC
from techburg_simulation.model.objects.abstract_agent import Agent
from techburg_simulation.model.space.location import Location


class RepairBot(Agent, ABC):
    def __init__(self, location: Location, grid) -> None:
        super().__init__(location, grid)
        self.set_type("repair_bot")

    def act(self):
        # Define behavior for RepairBot
        self._move()
