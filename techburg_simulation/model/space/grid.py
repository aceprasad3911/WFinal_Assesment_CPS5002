# grid.py
from typing import List
from techburg_simulation.model.objects.abstract_agent import Agent
from techburg_simulation.model.space.environment import Environment
from techburg_simulation.model.space.location import Location

class Grid(Environment):
    def __init__(self, width: int, height: int) -> None:
        super().__init__(width, height)
        self.__grid = [[None for _ in range(width)] for _ in range(height)]

    def clear(self):
        self.__grid = [[None for _ in range(self.get_width())] for _ in range(self.get_height())]

    def clear_agent(self, location: Location):
        """Clear the agent from the specified location."""
        row = location.get_y()
        col = location.get_x()
        if 0 <= row < self.get_height() and 0 <= col < self.get_width():
            self.__grid[row][col] = None  # Set the specific cell to None

    def get_agent(self, location: Location) -> Agent:
        return self.__grid[location.get_y()][location.get_x()]

    def set_agent(self, agent: Agent, location: Location) -> None:
        self.__grid[location.get_y()][location.get_x()] = agent

    def is_within_bounds(self, location: Location) -> bool:
        return 0 <= location.get_x() < self.get_width() and 0 <= location.get_y() < self.get_height()

    def count_agents(self, agent_type: type) -> int:
        count = 0
        for row in self.__grid:
            for cell in row:
                if isinstance(cell, agent_type):
                    count += 1
        return count

    def find_free_locations(self, location: Location) -> List[Location]:
        x = location.get_x()
        y = location.get_y()

        free_locations = []

        for offset_y in range(-1, 2):
            for offset_x in range(-1, 2):
                loc_x = x + offset_x
                loc_y = y + offset_y

                if loc_x < 0:
                    loc_x = self.get_width() - 1

                if loc_y < 0:
                    loc_y = self.get_height() - 1

                if loc_x >= self.get_width():
                    loc_x = 0

                if loc_y >= self.get_height():
                    loc_y = 0

                if self.__grid[loc_y][loc_x] is None:
                    free_locations.append(Location(loc_x, loc_y))

        return free_locations

    def handle_collisions(self):
        """Check for collisions between agents and handle interactions."""
        for y in range(self.get_height()):
            for x in range(self.get_width()):
                agent = self.__grid[y][x]
                if agent is not None:
                    # Implement collision logic here
                    pass