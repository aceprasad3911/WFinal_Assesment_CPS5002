# environment.py: Develop this file to create the Environment class, which will manage the grid
# (using the Location class) and the overall simulation state. This class will handle the placement of
# agents and other entities in the grid.

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model.agent import Agent
    from model.location import Location


class Environment(ABC):
    """
    Abstract base class representing an environment.
    """

    def __init__(self, width: int, height: int) -> None:
        """
        Initialises an Environment object with the given width and height.

        Args:
            width (int): The width of the environment grid.
            height (int): The height of the environment grid.
        """
        self.__width = width
        self.__height = height

    @abstractmethod
    def clear(self) -> None:
        """
        Clears the environment by removing all agents.
        """
        pass

    @abstractmethod
    def get_agent(self, location: Location) -> Agent:
        """
        Returns the agent at location in the environment grid.

        Args:
            location (Location): The location of the agent.

        Returns:
            Agent: The agent at the location.
        """
        pass

    @abstractmethod
    def set_agent(self, agent: Agent, location: Location) -> None:
        """
        Sets the agent at position (x, y) in the environment grid.

        Args:
            agent (Agent): The agent to set.
            location (Location): The location to set the agent.
        """
        pass

    def get_width(self) -> int:
        """
        Returns the width of the environment grid.

        Returns:
            int: The width of the environment grid.
        """
        return self.__width

    def get_height(self) -> int:
        """
        Returns the height of the environment grid.

        Returns:
            int: The height of the environment grid.
        """
        return self.__height
