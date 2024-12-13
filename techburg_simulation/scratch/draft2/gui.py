# gui.py
from __future__ import annotations

import tkinter as tk

from techburg_simulation.scratch.draft2.grid import Grid


class Gui(tk.Tk):
    def __init__(self, grid: Grid, techburg_cell_size=15):
        super().__init__()
        self.grid = grid  # Store the Grid object
        self.grid_size = len(grid.cells)  # Set the size of the grid based on the Grid object
        self.cell_size = techburg_cell_size  # Set the size of each cell
        # Create a canvas for drawing the grid
        self.canvas = tk.Canvas(self, width=self.grid_size * techburg_cell_size, height=self.grid_size * techburg_cell_size)
        self.canvas.pack()  # Add the canvas to the window
        self.update_display()  # Initial display update to show the grid
        self.after(1000, self.recurring_update)  # Schedule the first update after 1000 ms

    def wrap(self, row, col):
        # Wrap the row and column indices to ensure they stay within the grid boundaries
        wrapped_row = row % self.grid_size
        wrapped_col = col % self.grid_size
        return wrapped_row, wrapped_col  # Return the wrapped indices

    def get_cell(self, row, col):
        # Get the cell at the specified row and column, wrapping if necessary
        wrapped_row, wrapped_col = self.wrap(row, col)
        return self.grid[wrapped_row][wrapped_col]  # Return the cell object

    def set_cell(self, row, col, content):
        # Set the content of a specific cell
        cell = self.get_cell(row, col)  # Get the cell object
        cell.set_content(content)  # Set the content of the cell
        # No need to call update_display here; it will be called in recurring_update

    def update_display(self):
        self.canvas.delete("all")  # Clear the canvas
        for row in range(self.grid_size):  # Iterate through each row
            for col in range(self.grid_size):  # Iterate through each column
                cell = self.get_cell(row, col)  # Get the cell object
                # Draw the emoji/text in the center of the cell
                x1 = col * self.cell_size  # Calculate the top-left x coordinate
                y1 = row * self.cell_size  # Calculate the top-left y coordinate
                x2 = x1 + self.cell_size  # Calculate the bottom-right x coordinate
                y2 = y1 + self.cell_size  # Calculate the bottom-right y coordinate
                self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=cell.emoji, font=("Arial Unicode MS", 12))

    def recurring_update(self):
        # Update the state of all bots, stations, and parts at regular intervals
        self.update_display()  # Update the display after all bots have acted
        self.after(1000, self.recurring_update)  # Schedule the next update after 1000 ms
