# grid.py
import tkinter as tk
from cell import Cell
from techburg_simulation.src.bots.survivor_bot import SurvivorBot
from techburg_simulation.src.bots.repair_bot import RepairBot
from techburg_simulation.src.bots.gatherer_bot import GathererBot


class Grid:
    def __init__(self, techburg_grid_size=20, techburg_cell_size=15):
        self.grid_size = techburg_grid_size
        self.cell_size = techburg_cell_size
        self.grid = [[Cell() for _ in range(techburg_grid_size)] for _ in range(techburg_grid_size)]
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=techburg_grid_size * techburg_cell_size, height=techburg_grid_size * techburg_cell_size)
        self.canvas.pack()
        # Place bots, stations and parts here
        self.survivor_bot = SurvivorBot(self, 20, 20)  # Place the bot at (20, 20)
        self.gatherer_bot = GathererBot(self, 30, 30)
        self.repair_bot = RepairBot(self, 10, 10)
        self.update_display()  # Initial display update to show the grid
        self.root.after(1000, self.recurring_update)  # Schedule the first update
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
        self.update_display()  # This should refresh the display

    def recurring_update(self):
        # make sure all bots, stations and parts that are initialized are then set to act here
        self.survivor_bot.act()  # Allow the survivor bot to act
        self.gatherer_bot.act()  # Allow the survivor bot to act
        self.repair_bot.act()  # Allow the survivor bot to act
        self.update_display()  # Update the display after the bot acts
        self.root.after(1000, self.recurring_update)  # Schedule the next update
