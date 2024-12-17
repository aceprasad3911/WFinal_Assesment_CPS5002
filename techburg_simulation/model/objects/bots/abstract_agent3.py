# abstract_agent3.py
from abc import ABC
import random
import techburg_simulation.controller.config
import techburg_simulation.view.gui3


class Agent(ABC):
    def __init__(self, simulation, grid, x, y, bot_id):
        self.__grid = None
        self.simulation = simulation
        self.__grid = grid  # Store the grid reference
        self.id = bot_id  # Assign the bot ID
        self._location = [x, y]
        self.__object_type = "TBC"
        self.__bot_energy = techburg_simulation.controller.config.BOT_INITIAL_ENERGY
        self.__bot_health = techburg_simulation.controller.config.BOT_INITIAL_HEALTH
        self.__bot_vision = techburg_simulation.controller.config.BOT_INITIAL_VISION
        self.__bot_movement_rate = techburg_simulation.controller.config.BOT_INITIAL_MOVEMENT
        self.__bot_status = "healthy"
        self.__bot_carry_status = "hands_empty"
        self.__bot_appetite = "full"

    def _move(self):
        if self.__bot_energy <= 5:
            print(f"Bot ID {self.id}: Not enough energy to move.")
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
        print(f"Bot ID {self.id}: Energy reduced by 5, energy is now at: {self.__bot_energy}")
        # techburg_simulation.view.gui3.GUI.update_display(self)
        return self.__bot_energy

    def _carry(self):
        if self.__bot_carry_status == "hands_empty":
            pass

    def _eat(self):
        # If energy drops to 5% or below, bots consume parts immediately to restore energy.
        if self.__bot_energy <= 5 and self.__bot_carry_status == "hands_full":
            pass

    def _rest(self):
        # Energy is restored at recharge stations; bots can also rest to regenerate at a rate of 1% per simulation step without consuming parts.
        pass

    def _charge(self, energy):
        # Energy is restored at recharge stations; bots can also rest to regenerate at a rate of 1% per simulation step without consuming parts.
        pass

    def _super_boost(self):
        # Bots can enhance speed, vision, or energy based on spare parts consumed:
        # Speed: Default movement occurs every other simulation step; a speed enhancement of 51–100% allows movement every step, with a maximum enhancement of 100%.
        # Vision: Detects parts in adjacent cells; with 51–100% enhancement, bots detect two cells away, and up to three cells away with 101–150% enhancement. Maximum detection enhancement is 150%.
        pass

    # @abstractmethod
    # def _memory(self):
        # pass

    # @abstractmethod
    # def act(self):
        # pass


def get_x(self):
    return self._location[0]  # Return x-coordinate


def get_y(self):
    return self._location[1]  # Return y-coordinate
