# Techburg City Layout:
# - Grid Size: Minimum 30x30 cells.
# - Grid Wrap-around: The grid should wrap around at the edges (toroidal structure).
# - Cell Contents: Cells may contain empty spaces, spare parts, survivor bots, recharge stations, malfunctioning drones, or scavenger swarms.

import tkinter as tk


class Grid:
    def __init__(self, grid_size=40, cell_size=15):  # Set grid size to 40 and cell size to 15
        self.grid_size = grid_size
        self.cell_size = cell_size
        # Create a 2D list (grid) to represent the grid, initially filled with None
        self.grid = [[None for _ in range(grid_size)] for _ in range(grid_size)]
        # Initialize the Tkinter GUI
        self.root = tk.Tk()
        # Set the window size to fit the grid
        self.canvas = tk.Canvas(self.root, width=grid_size * cell_size, height=grid_size * cell_size)
        self.canvas.pack()  # Pack the canvas into the Tkinter window
        self.update_display()  # Initial display update to show the grid

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
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="grey")  # Change fill color to grey

    def run(self):
        self.root.mainloop()


# Create a grid instance and run the application
grid = Grid(grid_size=40, cell_size=15)  # 40x40 grid with 15 pixels per cell
grid.run()