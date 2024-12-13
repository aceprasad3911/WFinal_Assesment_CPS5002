# simulation.py: Create this file to handle the main simulation logic, including the
# simulation loop and the update of agent states. This will tie together the environment and agents.

# Simulation Parameters:
# - Starting Conditions: Begin with a populated grid including recharge stations, survivor bots, spare parts, drones, and scavenger swarms.
# - End Conditions: Simulation ends when all spare parts are collected or corroded, or all survivor bots are eliminated without possibility of replication.

# Responsibilities:
# Manages the overall simulation loop, including initialization, updates, and termination conditions.

import random
# Interactions:
# Coordinates interactions between Grid, Bots, RechargeStation, Drone, and ScavengerSwarm.
# Handles the simulation logic, including movement, energy depletion, and event handling.
# simulation.py
import time

import techburg_simulation.controller.config
from techburg_simulation.scratch.draft2.gatherer_bot import GathererBot
from techburg_simulation.scratch.draft2.cell import Cell
from techburg_simulation.scratch.draft2.grid import Grid
from techburg_simulation.scratch.draft2.location import Location
from techburg_simulation.scratch.draft2.gui import Gui  # Import the GUI class


# simulation.py


class Simulator:
    def __init__(self) -> None:
        self.__grid = Grid(techburg_simulation.controller.config.GRID_SIZE, techburg_simulation.controller.config.GRID_SIZE, )
        self.__agents = []
        self.__generate_initial_population()
        self.__is_running = False
        # Set Cell Content
        # Set Cell Content
        self.__cell = Cell("empty")  # Create a cell of type "empty"
        emoji = self.__cell.get_emoji(self.__cell.content)  # Call the get_emoji method
        self.__cell.set_content(emoji)  # Set the content to the emoji (if needed)

        # Initialize the GUI
        self.__gui = Gui(self.__grid)
        self.__gui.render()  # Render the initial state of the GUI

    def __generate_initial_population(self) -> None:
        """Generate the initial population of agents."""
        for _ in range(techburg_simulation.controller.config.INITIAL_COUNTS["recharge_stations"]):
            # Create and place recharge stations
            pass  # Implement recharge station placement

        for _ in range(techburg_simulation.controller.config.INITIAL_COUNTS["gatherer_bots"]):
            location = self.__get_random_free_location()
            agent = GathererBot(location, self.__grid, 29)  # Pass the grid
            self.__agents.append(agent)
            self.__grid.set_agent(agent, location)

    def __get_random_free_location(self) -> Location:
        """Get a random free location on the grid."""
        while True:
            x = random.randint(0, techburg_simulation.controller.config.GRID_SIZE - 1)
            y = random.randint(0, techburg_simulation.controller.config.GRID_SIZE - 1)
            location = Location(x, y)
            if self.__grid.get_agent(location) is None:  # Check if the cell is free
                return location

    def run(self) -> None:
        """Run the simulation."""
        self.__is_running = True
        while self.__is_running:
            self.__update()
            self.__render()
            time.sleep(1)
            if self.__gui.is_closed():
                self.__is_running = False

    def __render(self) -> None:
        """Render the current state of the simulation."""
        self.__gui.render()  # Call the render method of the GUI

    def __update(self) -> None:
        """Update the simulation state."""
        for agent in self.__agents:
            agent.act()  # Invoke the act method for each agent


if __name__ == "__main__":
    simulation = Simulator()
    simulation.run()
