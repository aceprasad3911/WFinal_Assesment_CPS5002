# grid.py
class Grid:
    def __init__(self, size):
        self.grid = None
        self.size = size
        self.techburg_grid_size = None
        self.cells = [[None for _ in range(size)] for _ in range(size)]  # Initialize a grid of None

    def get_height(self):
        return self.size

    def get_width(self):
        return self.size

    def set_agent(self, agent, location):
        self.cells[location[1]][location[0]] = agent  # Assuming location is [x, y]

    def clear_agent(self, location):
        self.cells[location[1]][location[0]] = None  # Clear the agent from the grid

    def get_cell(self, row, col):
        # Ensure that the row and col are within bounds
        if 0 <= row < self.techburg_grid_size and 0 <= col < self.techburg_grid_size:
            return self.grid.cells[row][col]  # Access the cell directly
        else:
            return None  # Return None if out of bounds
