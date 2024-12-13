import random
from abc import abstractmethod, ABC
from techburg_simulation.scratch.draft2.location import Location
import techburg_simulation.controller.config


class Agent(ABC):
    def __init__(self, location: Location, grid) -> None:
        self.__location = location
        self.__grid = grid
        self.__bot_type = "TBC"
        self.__bot_energy = techburg_simulation.controller.config.BOT_INITIAL_ENERGY
        self.__bot_health = techburg_simulation.controller.config.BOT_INITIAL_HEALTH
        self.__bot_vision = techburg_simulation.controller.config.BOT_INITIAL_VISION
        self.__bot_movement_rate = techburg_simulation.controller.config.BOT_INITIAL_MOVEMENT
        self.__bot_status = "healthy"
        self.__bot_carry_status = "hands_empty"
        self.__bot_appetite = "full"

    def get_location(self) -> Location:
        return Location(self.__location[0], self.__location[1])  # Assuming Location takes row and col

    def get_energy(self) -> int:
        return self.__bot_energy

    def get_health(self) -> int:
        return self.__bot_health

    def get_vision(self) -> int:
        return self.__bot_vision

    def get_movement(self) -> int:
        return self.__bot_movement_rate

    def get_status(self) -> str:
        return self.__bot_status

    def get_type(self) -> str:
        return self.__bot_type

    def set_energy(self, energy: int) -> None:
        self.__bot_energy = energy

    def set_health(self, health: int) -> None:
        self.__bot_health = health

    def set_status(self, status: str) -> None:
        self.__bot_status = status

    def set_type(self, bot_type: str) -> None:
        self.__bot_type = bot_type

    def _move(self):
        if self.__bot_energy <= 5:
            pass
        # Get the current location
        row = self.__location.get_y()  # Use get_y() to get the row
        col = self.__location.get_x()  # Use get_x() to get the column

        # Example movement logic (random movement)
        dr, dc = random.choice([(-1, -1), (-1, 0), (-1, +1), (0, -1), (0, 0), (0, +1), (+1, -1), (+1, 0), (+1, +1)])  # Move in one of eight directions
        new_row, new_col = row + dr, col + dc
        # Check if the new position is within bounds
        if 0 <= new_row < self.__grid.get_height() and 0 <= new_col < self.__grid.get_width():
            # Clear the old position on the grid
            self.__grid.clear_agent(self.__location)  # Assuming you have a method to clear the agent from the grid
            # Update the agent's location
            self.__location.set_x(new_col)
            self.__location.set_y(new_row)

            # Place the agent in the new location on the grid
            self.__grid.set_agent(self, self.__location)  # Assuming you have a method to set the agent in the grid

        # Each move depletes bot energy by 5%.
        self.__bot_energy -= 5
        print("Energy reduced by 5, energy is now at:", self.__bot_energy)
        return self.__bot_energy


    def _carry(self):
        # Bots can carry only one part at a time.
        # Prioritize larger parts when selecting.
        pass

    def _charge(self, energy):
        # Energy is restored at recharge stations; bots can also rest to regenerate at a rate of 1% per simulation step without consuming parts.
        pass

    def _rest(self):
        # Energy is restored at recharge stations; bots can also rest to regenerate at a rate of 1% per simulation step without consuming parts.
        pass

    def _eat(self):
        # If energy drops to 5% or below, bots consume parts immediately to restore energy.
        pass

    def _super_boost(self):
        # Bots can enhance speed, vision, or energy based on spare parts consumed:
        # Speed: Default movement occurs every other simulation step; a speed enhancement of 51–100% allows movement every step, with a maximum enhancement of 100%.
        # Vision: Detects parts in adjacent cells; with 51–100% enhancement, bots detect two cells away, and up to three cells away with 101–150% enhancement. Maximum detection enhancement is 150%.
        pass

    # @abstractmethod
    # def _memory(self):
        # pass

    @abstractmethod
    def act(self):
        pass
