# grid.py
from techburg_simulation.model.space.cell3 import Cell


class Grid:
    def __init__(self, size):
        self.simulation = None
        self.size = size
        self.cells = [[Cell() for _ in range(size)] for _ in range(size)]  # Initialize a grid of None

    def get_height(self):
        return self.size

    def get_width(self):
        return self.size

    def set_agent(self, agent, location):
        self.cells[location[1]][location[0]] = agent  # Assuming location is [x, y]

    def clear_agent(self, location):
        self.cells[location[1]][location[0]] = None  # Clear the agent from the grid

    def add_agent(self, agent_class, x, y, agent_id):
        agent = agent_class(self.simulation, self, x, y, agent_id)  # Create the agent
        self.set_agent(agent, (x, y))  # Place it in the grid
        return agent

    def move_agent(self, agent):
        current_x, current_y = agent.get_x(), agent.get_y()
        agent._move()  # Call the agent's move method
        new_x, new_y = agent.get_x(), agent.get_y()
        self.clear_agent((current_x, current_y))  # Clear the old position
        self.set_agent(agent, (new_x, new_y))  # Set the new position
