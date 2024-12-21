# repair_bot3.py

from techburg_simulation.model.objects.bots.abstract_agent3 import Agent


class RepairBot(Agent):
    def __init__(self, simulation, grid, x, y, bot_id):
        super().__init__(simulation, grid, x, y, bot_id)  # Call the parent constructor
        self._object_type = "repair_bot"

    def __str__(self):
        return self._object_type  # Return the object type as a string

    def _move(self):
        return super()._move()  # Call the move method from the Agent class

    def _eat(self):
        return super()._eat()

    def _scan(self):
        return super()._scan()

    def get_x(self):
        return self._location[0]  # Assuming _location is a list [x, y]

    def get_y(self):
        return self._location[1]  # Assuming _location is a list [x, y]
