# abstract_agent3.py
from abc import ABC
import random
import techburg_simulation.controller.config
import techburg_simulation.view.gui3


class Agent(ABC):
    def __init__(self, simulation, grid, x, y, bot_id):
        self._grid = None
        self._simulation = simulation
        self._grid = grid  # Store the grid reference
        self.id = bot_id  # Assign the bot ID
        self._location = [x, y]
        self._object_type = "abstract_agent_bot"
        self._bot_energy = techburg_simulation.controller.config.BOT_INITIAL_ENERGY
        self._bot_health = techburg_simulation.controller.config.BOT_INITIAL_HEALTH
        self._bot_vision = techburg_simulation.controller.config.BOT_INITIAL_VISION
        self._bot_movement_rate = techburg_simulation.controller.config.BOT_INITIAL_MOVEMENT
        self._bot_status = "healthy"
        self._bot_carry_status = "hands_empty"
        self._bot_appetite = "full"

    def __str__(self):
        return self._object_type  # Return the object type as a string

    def _act(self):  # super method that implements all behaviours
        # TODO: [create & implement]
        pass

    def _move(self):
        # TODO: [Make _move method sentient]
        if self._bot_energy <= 5:
            print(f"Bot ID {self.id}: Not enough energy to move.")
            return self._bot_energy
        # Get the current location
        col = self._location[0]  # Use the x-coordinate
        row = self._location[1]  # Use the y-coordinate
        # Example movement logic (random movement)
        dr, dc = random.choice([(-1, -1), (-1, 0), (-1, +1), (0, -1), (0, 0), (0, +1), (+1, -1), (+1, 0), (+1, +1)])  # Move in one of eight directions
        new_row = (row + dr) % self._grid.get_height()  # Wrap around vertically
        new_col = (col + dc) % self._grid.get_width()  # Wrap around horizontally
        # Check if the new position is within bounds
        if 0 <= new_row < self._grid.get_height() and 0 <= new_col < self._grid.get_width():
            # Clear the old position on the grid
            self._grid.clear_agent(self._location)  # Assuming you have a method to clear the agent from the grid
            # Update the agent's location
            self._location[0] = new_col  # Update x-coordinate
            self._location[1] = new_row  # Update y-coordinate
            # Place the agent in the new location on the grid
            self._grid.set_agent(self, self._location)  # Assuming you have a method to set the agent in the grid
        # Each move depletes bot energy by 5%.
        self._bot_energy -= 5
        print(f"Bot ID {self.id}: Energy reduced by 5, energy is now at: {self._bot_energy}")
        # techburg_simulation.view.gui3.GUI.update_display(self)
        return self._bot_energy

    def _scan(self):
        # TODO: [Make _scan method sentient]
        col = self._location[0]  # Use the x-coordinate
        row = self._location[1]  # Use the y-coordinate
        # Define the relative positions of the neighboring cells
        directions = [(-1, -1), (-1, 0), (-1, +1), (0, -1), (0, +1), (+1, -1), (+1, 0), (+1, +1)]
        # Initialize a list to hold the contents of neighboring cells
        neighbour_contents = []
        # Iterate through each direction to check neighboring cells
        for dr, dc in directions:
            new_row = (row + dr) % self._grid.get_height()  # Wrap around vertically
            new_col = (col + dc) % self._grid.get_width()  # Wrap around horizontally
            # Get the content of the neighboring cell
            content = self._grid.get_cell_content(new_row, new_col)  # Assuming you have a method to get cell content
            neighbour_contents.append((new_row, new_col, content))
        return neighbour_contents

    def _eat(self):
        pass

    def _carry(self):
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
