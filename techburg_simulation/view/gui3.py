# gui3.py (Functional)

import tkinter as tk  # Import the tkinter module for GUI creation
from techburg_simulation.controller.simulation3 import Simulation  # Import the Simulation class from the simulation module
from techburg_simulation.model.space.cell3 import Cell


class GUI:
    def __init__(self):
        # Initialize instance variables for GUI components
        self.simulation_window = None
        self.grid_size = None
        self.cell_size = None
        self.grid = None
        self.running = None
        self.canvas = None
        self.label = None  # Label to prompt user for input
        self.entry = None  # Entry widget for user input
        self.run_button = None  # Button to trigger the simulation
        self.result_label = None  # Label to display results
        self.root = tk.Tk()  # Create the main window for the GUI
        self.simulation = Simulation()  # Create an instance of the Simulation class
        self.setup_gui()  # Call the method to set up the GUI components

    def setup_gui(self):
        # Set up the GUI components
        self.label = tk.Label(self.root, text="Enter simulation parameters\n(grid size):")
        self.label.pack()  # Add the label to the main window
        self.entry = tk.Entry(self.root)  # Create an entry widget for user input
        self.entry.pack()  # Add the entry widget to the main window
        # Create a button that runs the simulation when clicked
        self.run_button = tk.Button(self.root, text="Run Simulation", command=self.run_simulation)
        self.run_button.pack()  # Add the button to the main window

    def run_simulation(self):
        # This method is called when the run button is clicked
        try:
            grid_size = int(self.entry.get())
            techburg_grid_size = self.simulation.run_simulation(grid_size)  # Call the simulation's run method with grid_size
            print(f"techburg_grid_size: {techburg_grid_size}")  # Debugging line
            # Close the initial window
            self.root.withdraw()
            # Open a new window to display the results
            self.techburg_gui(techburg_grid_size)
        except ValueError:
            # Handle the case where the input is not a valid integer
            error_window = tk.Tk()
            error_window.title("Input Error")
            error_label = tk.Label(error_window, text="Please enter a valid integer for grid size.")
            error_label.pack(pady=20)
            error_window.mainloop()

    def techburg_gui(self, techburg_grid_size, techburg_cell_size=15):
        # Create a new window to display the output
        self.simulation_window = tk.Toplevel(self.root)  # Create a new Toplevel window
        self.simulation_window.title("Techburg Simulation")  # Set the title of the new window
        screen_size = techburg_grid_size * techburg_cell_size
        screen_window = str(screen_size) + "x" + str(screen_size)  # dynamic window based on screen size
        self.simulation_window.geometry(screen_window)  # Set the size of the new window
        self.grid_size = techburg_grid_size  # Set the size of the grid
        self.cell_size = techburg_cell_size  # Set the size of each cell
        self.grid = [[Cell() for _ in range(techburg_grid_size)] for _ in range(techburg_grid_size)]
        self.canvas = tk.Canvas(self.simulation_window, width=techburg_grid_size * techburg_cell_size, height=techburg_grid_size * techburg_cell_size)
        self.canvas.pack()  # Add the canvas to the new window
        self.update_display()  # Initial display update to show the grid
        self.running = True
        self.recurring_update()

    def run(self):
        # Start the GUI event loop, which waits for user interaction
        self.root.mainloop()  # This keeps the window open and responsive ```python

    def update_display(self):
        self.canvas.delete("all")  # Clear the canvas
        for row in range(self.grid_size):  # Iterate through each row
            for col in range(self.grid_size):  # Iterate through each column
                cell = self.grid[row][col]  # Get the cell object
                # Set the background color based on cell content
                self.set_cell_background(row, col, 'gray')  # Default cell color

                # Initialize cell content to "TBC"
                cell.set_content("TBC")  # Set it to empty by default

                # Check for each bot type and update the cell content accordingly
                for bot in self.simulation.bots:
                    if (row, col) == (bot.get_y(), bot.get_x()):
                        cell.set_content(bot.__class__.__name__.lower().replace("bot", "_bot"))
                        break  # Exit the loop once the bot is found

                # Draw the emoji/text in the center of the cell
                x1 = col * self.cell_size  # Calculate the top-left x coordinate
                y1 = row * self.cell_size  # Calculate the top-left y coordinate
                x2 = x1 + self.cell_size  # Calculate the bottom-right x coordinate
                y2 = y1 + self.cell_size  # Calculate the bottom-right y coordinate
                self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=cell.emoji, font=("Arial Unicode MS", 12))

    def recurring_update(self):
        # Update the state of all bots, stations, and parts at regular intervals
        if self.running:
            print("Updating simulation...")  # Debugging line
            self.simulation.update()  # Update the simulation state
            self.update_display()  # Update the display after all bots have acted
            self.simulation_window.after(1000, self.recurring_update)  # Call this method again after 1000ms

    def set_cell_background(self, row, col, color):
        # Set the background color for the cell
        wrapped_row, wrapped_col = self.wrap(row, col)
        x1 = wrapped_col * self.cell_size  # Calculate the top-left x coordinate
        y1 = wrapped_row * self.cell_size  # Calculate the top-left y coordinate
        x2 = x1 + self.cell_size  # Calculate the bottom-right x coordinate
        y2 = y1 + self.cell_size  # Calculate the bottom-right y coordinate
        # Draw a rectangle for the cell with the specified background color
        self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=color)

    def wrap(self, row, col):
        # Wrap the row and column indices to ensure they stay within the grid boundaries
        wrapped_row = row % self.grid_size
        wrapped_col = col % self.grid_size
        return wrapped_row, wrapped_col  # Return the wrapped indices

    def close_simulation(self):
        self.running = False  # Set running False to stop the recurring update
        self.simulation_window.destroy()  # Close the simulation window
        self.root.deiconify()  # Show the main window again
