# abstract_agent3.py
from abc import ABC
import random
import techburg_simulation.controller.config
import techburg_simulation.view.gui3


class Agent(ABC):
    def __init__(self, simulation, grid, x, y):
        self.__grid = None
        self.simulation = simulation
        self.__grid = grid  # Store the grid reference
        self._location = [x, y]
        self.__bot_type = "TBC"
        self.__bot_energy = techburg_simulation.controller.config.BOT_INITIAL_ENERGY
        self.__bot_health = techburg_simulation.controller.config.BOT_INITIAL_HEALTH
        self.__bot_vision = techburg_simulation.controller.config.BOT_INITIAL_VISION
        self.__bot_movement_rate = techburg_simulation.controller.config.BOT_INITIAL_MOVEMENT
        self.__bot_status = "healthy"
        self.__bot_carry_status = "hands_empty"
        self.__bot_appetite = "full"

    def _move(self):
        if self.__bot_energy <= 5:
            print("Not enough energy to move.")
            return self.__bot_energy
        # Get the current location
        col = self._location[0]  # Use the x-coordinate
        row = self._location[1]  # Use the y-coordinate
        # Example movement logic (random movement)
        dr, dc = random.choice([(-1, -1), (-1, 0), (-1, +1), (0, -1), (0, 0), (0, +1), (+1, -1), (+1, 0), (+1, +1)])  # Move in one of eight directions
        new_row = (row + dr) % self.__grid.get_height()  # Wrap around vertically
        new_col = (col + dc) % self.__grid.get_width()  # Wrap around horizontally
        # Check if the new position is within bounds
        if 0 <= new_row < self.__grid.get_height() and 0 <= new_col < self.__grid.get_width():
            # Clear the old position on the grid
            self.__grid.clear_agent(self._location)  # Assuming you have a method to clear the agent from the grid
            # Update the agent's location
            self._location[0] = new_col  # Update x-coordinate
            self._location[1] = new_row  # Update y-coordinate
            # Place the agent in the new location on the grid
            self.__grid.set_agent(self, self._location)  # Assuming you have a method to set the agent in the grid
        # Each move depletes bot energy by 5%.
        self.__bot_energy -= 5
        print("Energy reduced by 5, energy is now at:", self.__bot_energy)
        # techburg_simulation.view.gui3.GUI.update_display(self)
        return self.__bot_energy


def get_x(self):
    return self.__location[0]  # Return x-coordinate


def get_y(self):
    return self.__location[1]  # Return y-coordinate
