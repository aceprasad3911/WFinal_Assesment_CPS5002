# gatherer_bot3.py

from techburg_simulation.model.objects.abstract_agent3 import Agent


class GathererBot(Agent):
    def __init__(self, simulation, grid, x, y):
        super().__init__(simulation, grid, x, y)  # Call the parent constructor
        self.__bot_type = "gatherer_bot"

    def move(self):
        return super()._move()  # Call the move method from the Agent class

    def get_x(self):
        return self._location[0]  # Assuming _location is a list [x, y]

    def get_y(self):
        return self._location[1]  # Assuming _location is a list [x, y]
