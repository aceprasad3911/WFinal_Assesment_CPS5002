import tkinter as tk  # Import the tkinter library for GUI creation
from cell import Cell  # Import the Cell class from cell.py
import random

class Grid:
    def __init__(self, techburg_grid_size=20, techburg_cell_size=15):
        self.grid_size = techburg_grid_size
        self.cell_size = techburg_cell_size
        self.grid = [[Cell() for _ in range(techburg_grid_size)] for _ in range(techburg_grid_size)]
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=techburg_grid_size * techburg_cell_size, height=techburg_grid_size * techburg_cell_size)
        self.canvas.pack()
        self.update_display()  # Initial display update to show the grid
        self.root.after(100, self.recurring_update)  # Schedule the first update
        self.root.mainloop()

    def wrap(self, row, col):
        wrapped_row = row % self.grid_size
        wrapped_col = col % self.grid_size
        return wrapped_row, wrapped_col

    def update_display(self):
        self.canvas.delete("all")
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                x1 = col * self.cell_size
                y1 = row * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="gray")
                cell = self.grid[row][col]
                self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=cell.emoji, font=("Arial Unicode MS", 12))

    def get_cell(self, row, col):
        wrapped_row, wrapped_col = self.wrap(row, col)
        return self.grid[wrapped_row][wrapped_col]

    def set_cell(self, row, col, content):
        cell = self.get_cell(row, col)
        cell.set_content(content)
        self.update_display()

    def recurring_update(self):
        # Here you can put any logic that modifies the grid
        # For example, you might want to change the content of a cell periodically
        # This is just an example where we change a random cell to 'spare_parts'
        random_row = random.randint(0, self.grid_size - 1)
        random_col = random.randint(0, self.grid_size - 1)
        self.set_cell(random_row, random_col, 'spare_parts')  # Change a random cell to spare_parts
        self.set_cell(20, 20, 'survivor_bot')
        # Schedule the next update
        self.root.after(1000, self.recurring_update)  # Call this function again after 1000 ms (1 second)

# Example usage:
# grid = Grid()
# grid.set_cell(0, 0, 'Bot', 'emoji')  # Set the cell at (0, 0) with value 'Bot' and 'emoji'
# print(grid.get_cell(0, 0).value)  # Retrieve the value of the cell at (0, 0)
