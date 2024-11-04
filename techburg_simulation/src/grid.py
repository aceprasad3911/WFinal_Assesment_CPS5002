# grid.py
import tkinter as tk
import random
from cell import Cell  # Import the Cell class from cell.py

class Grid:
    def __init__(self, grid_size=40, cell_size=15):
        self.grid_size = grid_size
        self.cell_size = cell_size
        # Create a 2D list (grid) to represent the grid, initializing with Cell objects
        self.grid = [[self.random_cell() for _ in range(grid_size)] for _ in range(grid_size)]
        # Initialize the Tkinter GUI
        self.root = tk.Tk()
        # Set the window size to fit the grid
        self.canvas = tk.Canvas(self.root, width=grid_size * cell_size, height=grid_size * cell_size)
        self.canvas.pack()  # Pack the canvas into the Tkinter window
        self.update_display()  # Initial display update to show the grid

    def random_cell(self):
        # Randomly assign a cell type from the available types
        cell_types = ['empty', 'spare_part', 'survivor_bot', 'recharge_station',
                      'malfunctioning_drone', 'scavenger_swarm']
        cell_type = random.choice(cell_types)  # Choose a random cell type
        return Cell(cell_type)  # Return a new Cell instance

    def update_display(self):
        # Clear the canvas
        self.canvas.delete("all")
        # Draw the grid
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                x1 = col * self.cell_size
                y1 = row * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                cell = self.grid[row][col]  # Get the Cell object
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=cell.color)  # Use cell's color

    def run(self):
        self.root.mainloop()


# Create a grid instance and run the application
if __name__ == "__main__":
    grid = Grid(grid_size=40, cell_size=15)  # 40x40 grid with 15 pixels per cell
    grid.run()