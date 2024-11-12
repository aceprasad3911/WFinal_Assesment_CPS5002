# agent.py: Once you have the abstract base class, you can create specific agent classes
# (e.g., SurvivorBot, Drone, ScavengerSwarm) in this file. These classes will inherit from
# AbstractAgent and implement their specific behaviors.

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model.location import Location


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