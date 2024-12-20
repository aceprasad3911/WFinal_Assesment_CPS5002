import tkinter as tk  # Importing the tkinter library for GUI
from techburg_simulation.scratch.draft2.cell import Cell  # Importing the Cell class from cell module
from techburg_simulation.src.bots.survivor_bot import SurvivorBot  # Importing SurvivorBot from the bots module
from techburg_simulation.src.bots.repair_bot import RepairBot  # Importing RepairBot from the bots module
from techburg_simulation.src.bots.gatherer_bot import GathererBot  # Importing GathererBot from the bots module
from techburg_simulation.src.recharge_station import RechargeStation


class Grid:
    def __init__(self, techburg_grid_size=40, techburg_cell_size=15):
        self.grid_size = techburg_grid_size  # Set the size of the grid
        self.cell_size = techburg_cell_size  # Set the size of each cell
        # Create a 2D list (grid) of Cell objects
        self.grid = [[Cell() for _ in range(techburg_grid_size)] for _ in range(techburg_grid_size)]
        self.root = tk.Tk()  # Initialize the main window
        # Create a canvas for drawing the grid
        self.canvas = tk.Canvas(self.root, width=techburg_grid_size * techburg_cell_size, height=techburg_grid_size * techburg_cell_size)
        self.canvas.pack()  # Add the canvas to the window
        # Place bots and stations here
        self.gatherer_bot = GathererBot(self, 30, 30)  # Place the GathererBot at (30, 30)
        self.repair_bot = RepairBot(self, 10, 10)  # Place the RepairBot at (10, 10)
        self.recharge_station1 = RechargeStation(self, 7, 7)
        self.recharge_station2 = RechargeStation(self, 33, 14)
        self.recharge_station3 = RechargeStation(self, 15, 33)
        self.update_display()  # Initial display update to show the grid
        self.root.after(1000, self.recurring_update)  # Schedule the first update after 1000 ms
        self.root.mainloop()  # Start the Tkinter event loop

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
        # Set the content of a specific cell without changing the background
        cell = self.get_cell(row, col)  # Get the cell object
        cell.set_content(content)  # Set the content of the cell
        # No need to call update_display here; it will be called in recurring_update

    def set_cell_background(self, row, col, color):
        # Set the background color for the cell
        wrapped_row, wrapped_col = self.wrap(row, col)
        x1 = wrapped_col * self.cell_size  # Calculate the top-left x coordinate
        y1 = wrapped_row * self.cell_size  # Calculate the top-left y coordinate
        x2 = x1 + self.cell_size  # Calculate the bottom-right x coordinate
        y2 = y1 + self.cell_size  # Calculate the bottom-right y coordinate
        # Draw a rectangle for the cell with the specified background color
        self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=color)

    def update_display(self):
        self.canvas.delete("all")  # Clear the canvas
        for row in range(self.grid_size):  # Iterate through each row
            for col in range(self.grid_size):  # Iterate through each column
                cell = self.grid[row][col]  # Get the cell object
                # Set the background color based on cell content
                if cell.content == 'recharge_station':
                    self.set_cell_background(row, col, 'yellow')  # Color for recharge station
                else:
                    self.set_cell_background(row, col, 'gray')  # Default cell color
                # Draw the emoji/text in the center of the cell
                x1 = col * self.cell_size  # Calculate the top-left x coordinate
                y1 = row * self.cell_size  # Calculate the top-left y coordinate
                x2 = x1 + self.cell_size  # Calculate the bottom-right x coordinate
                y2 = y1 + self.cell_size  # Calculate the bottom-right y coordinate
                self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=cell.emoji, font=("Arial Unicode MS", 12))

    def recurring_update(self):
        # Update the state of all bots, stations, and parts at regular intervals
        self.survivor_bot.act()  # Allow the survivor bot to perform its action
        self.gatherer_bot.act()  # Allow the gatherer bot to perform its action
        self.repair_bot.act()  # Allow the repair bot to perform its action
        self.update_display()  # Update the display after all bots have acted
        self.root.after(1000, self.recurring_update)  # Schedule the next update after 1000 ms
