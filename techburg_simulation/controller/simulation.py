# simulation.py: Create this file to handle the main simulation logic, including the
# simulation loop and the update of agent states. This will tie together the environment and agents.

# Simulation Parameters:
# - Starting Conditions: Begin with a populated grid including recharge stations, survivor bots, spare parts, drones, and scavenger swarms.
# - End Conditions: Simulation ends when all spare parts are collected or corroded, or all survivor bots are eliminated without possibility of replication.

# Responsibilities:
# Manages the overall simulation loop, including initialization, updates, and termination conditions.

# Interactions:
# Coordinates interactions between Grid, Bots, RechargeStation, Drone, and ScavengerSwarm.
# Handles the simulation logic, including movement, energy depletion, and event handling.

import time

from view.gui import Gui


class Simulator:
    """Class representing a simulator."""

    def __init__(self) -> None:
        """
        Initialise the Simulator object.

        Initialises the environment, and generates the initial population of agents.
        """
        self.__ocean = Ocean()
        self.__agents = []
        self.__generate_initial_population()
        self.__is_running = False

        # TODO: Define a dictionary, agent_colours, containing colours for each agent (class name - colour string pairs)
        # TODO: Initialise a new Gui object
        # TODO: Render the Gui by invoking the appropriate method

    def __generate_initial_population(self) -> None:
        """
        Generate the initial population of agents.
        """
        # TODO: Generate the initial population
        pass

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
        # TODO: Render the Gui by invoking the appropriate method

    def __update(self) -> None:
        """Update the simulation state."""
        # TODO: Invoke the act method for each agent


if __name__ == "__main__":
    """
    Entry point for running the simulation.
    """
    simulation = Simulator()
    simulation.run()