# grid.py
class Grid:
    def __init__(self, size):
        self.size = size
        self.cells = [[None for _ in range(size)] for _ in range(size)]  # Initialize a grid of None

    def get_height(self):
        return self.size

    def get_width(self):
        return self.size

    def set_agent(self, agent, location):
        self.cells[location[1]][location[0]] = agent  # Assuming location is [x, y]

    def clear_agent(self, location):
        self.cells[location[1]][location[0]] = None  # Clear the agent from the grid
