# abstract_agent.py: Define the base class for agents here. This class will include common attributes and methods
# that all agent types (e.g., survivor bots, drones, scavenger swarms) will inherit from.

from abc import ABC, abstractmethod


class Agent(ABC):
    def __init__(self, location: Location) -> None:
        """
        Constructor for the Agent class.

        Parameters:
        - location: A Location object representing the agent's initial location.
        """
        self.__location = location

    def set_location(self, location: Location) -> None:
        """
        Set the location of the agent.

        Parameters:
        - location: A Location object representing the new location of the agent.
        """
        self.__location = location

    def get_location(self) -> Location:
        """
        Get the current location of the agent.

        Returns:
        A Location object representing the agent's current location.
        """
        return self.__location

    @abstractmethod
    def act(self):
        """
        The agent performs some actions.
        """
        pass