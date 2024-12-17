# gui3.py (Functional)

import tkinter as tk  # Import the tkinter module for GUI creation
import time

from techburg_simulation.controller import config
from techburg_simulation.controller.simulation3 import Simulation  # Import the Simulation class from the simulation module
from techburg_simulation.model.objects.bots.malfunction_bot3 import MalfunctionBot
from techburg_simulation.model.objects.bots.repair_bot3 import RepairBot
from techburg_simulation.model.objects.bots.gatherer_bot3 import GathererBot
from techburg_simulation.model.objects.bots.scavenger_bot3 import ScavengerBot
from techburg_simulation.model.objects.recharge_station3 import RechargeStation
from techburg_simulation.model.objects.spare_part3 import SparePart
from techburg_simulation.model.space.cell3 import Cell


class GUI:
    def __init__(self):
        # Initialize instance variables for GUI components
        self.dynamic_widget_placeholder = None
        self.graph_placeholder = None
        self.status_label = None
        self.dashboard_frame = None
        self.simulation_window = None
        self.grid_size = config.GRID_SIZE
        self.repairbot_population = config.INITIAL_COUNTS["repair_bots"]
        self.gathererbot_population = config.INITIAL_COUNTS["gatherer_bots"]
        self.recharge_station_num = config.INITIAL_COUNTS["recharge_stations"]
        self.spare_part_num = config.INITIAL_COUNTS["spare_parts"]
        self.malfunctionbot_population = config.INITIAL_COUNTS["malfunction_bots"]
        self.scavengerbot_population = config.INITIAL_COUNTS["scavenger_bots"]
        self.cell_size = None
        self.grid = None
        self.running = None
        self.canvas = None
        self.label = None  # Label to prompt user for input
        self.entry = None  # Entry widget for user input
        self.run_button = None  # Button to trigger the simulation
        self.result_label = None  # Label to display results
        self.root = tk.Tk()  # Create the main window for the GUI
        self.root.title("AI Simulation Setup")  # Set the title of the main window
        self.simulation = Simulation()  # Create an instance of the Simulation class
        self.setup_gui()  # Call the method to set up the GUI components

    def setup_gui(self):
        # Set up the GUI components
        tk.Label(self.root, text="Simulation Parameters:").pack(pady=10)  # Title label
        # Display preset parameters
        tk.Label(self.root, text=f"Grid Size: {self.grid_size}").pack()
        tk.Label(self.root, text=f"RepairBot Population: {self.repairbot_population}").pack()
        tk.Label(self.root, text=f"GathererBot Population: {self.gathererbot_population}").pack()
        tk.Label(self.root, text=f"Number of Spare Parts: {self.spare_part_num}").pack()
        tk.Label(self.root, text=f"Number of Recharge Stations: {self.recharge_station_num}").pack()
        tk.Label(self.root, text=f"MalfunctionBot Population: {self.malfunctionbot_population}").pack()
        tk.Label(self.root, text=f"ScavengerBot Population: {self.scavengerbot_population}").pack()
        # Create a button that runs the simulation when clicked
        self.run_button = tk.Button(self.root, text="Run Simulation", command=self.run_simulation)
        self.run_button.pack(pady=20)  # Add the button to the main window

    def run_simulation(self):
        # This method is called when the run button is clicked
        techburg_grid_size = self.grid_size  # Use the preset grid size
        self.simulation.run_simulation(techburg_grid_size)
        self.root.withdraw()  # Close the initial window
        self.techburg_gui(techburg_grid_size)

    def techburg_gui(self, techburg_grid_size, techburg_cell_size=15):
        # Create a new window to display the output
        self.simulation_window = tk.Toplevel(self.root)  # Create a new Toplevel window
        self.simulation_window.title("Techburg Simulation")  # Set the title of the new window
        screen_size = techburg_grid_size * techburg_cell_size
        dashboard_size = 400  # Fixed width for the dashboard
        screen_window = f"{dashboard_size + techburg_grid_size * techburg_cell_size}x{screen_size}"  # dynamic window based on screen size
        self .simulation_window.geometry(screen_window)  # Set the size of the new window
        self.grid_size = techburg_grid_size  # Set the size of the grid
        self.cell_size = techburg_cell_size  # Set the size of each cell
        self.grid = [[Cell() for _ in range(techburg_grid_size)] for _ in range(techburg_grid_size)]

        # Create a frame for the grid and dashboard
        main_frame = tk.Frame(self.simulation_window)
        main_frame.pack(side=tk.LEFT)  # Pack the main frame to the left

        # Create the canvas for the grid
        self.canvas = tk.Canvas(main_frame, width=techburg_grid_size * techburg_cell_size, height=techburg_grid_size * techburg_cell_size)
        self.canvas.pack(side=tk.LEFT)  # Pack the canvas to the left side of the main frame

        # Create a frame for the dashboard
        self.dashboard_frame = tk.Frame(self.simulation_window, width=dashboard_size, height=screen_size)  # Fixed width for the dashboard
        self.dashboard_frame.pack(side=tk.RIGHT, fill=tk.Y)  # Pack the dashboard frame to the right

        # Use grid layout for the dashboard
        self.result_label = tk.Label(self.dashboard_frame, text="Dashboard", font=("Arial", 16))
        self.result_label.grid(row=0, column=0, columnspan=2, pady=10)  # Center the title across two columns

        # Example of adding more dashboard elements
        self.status_label = tk.Label(self.dashboard_frame, text="Status: Running", font=("Arial", 12))
        self.status_label.grid(row=1, column=0, columnspan=2, pady=5)

        # Placeholder for dynamic widgets (e.g., graphs)
        self.graph_placeholder = tk.Label(self.dashboard_frame, text="Graph Placeholder", bg="lightgray", width=20, height=10)
        self.graph_placeholder.grid(row=2, column=0, padx=5, pady=5)

        self.dynamic_widget_placeholder = tk.Label(self.dashboard_frame, text="Dynamic Widget Placeholder", bg="lightblue", width=20, height=10)
        self.dynamic_widget_placeholder.grid(row=2, column=1, padx=5, pady=5)

        self.update_display()  # Initial display update to show the grid
        self.running = True
        self.recurring_update()
    def center_dashboard_text(self):
        # Center the text in the dashboard frame
        for widget in self.dashboard_frame.winfo_children():
            widget.pack_configure(anchor='center')  # Center all widgets in the dashboard frame

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
                # Initialize a flag to check if an object is found
                # Initialize a flag to check if an object is found
                object_found = False
                # Check for each object in the objects list and update the cell content accordingly
                for obj in self.simulation.objects:
                    if (row, col) == (obj.get_y(), obj.get_x()):  # Check if the object's position matches the cell
                        if isinstance(obj, RechargeStation):
                            cell.set_content("recharge_station")  # Set content for recharge station
                        elif isinstance(obj, SparePart):
                            cell.set_content("spare_part")  # Set content for GathererBot
                        object_found = True
                        break  # Exit the loop once the object is found

                for bot in self.simulation.bots:
                    if (row, col) == (bot.get_y(), bot.get_x()):  # Check if the object's position matches the cell
                        if isinstance(bot, GathererBot):
                            cell.set_content("gatherer_bot")  # Set content for recharge station
                        elif isinstance(bot, RepairBot):
                            cell.set_content("repair_bot")  # Set content for GathererBot
                        elif isinstance(bot, MalfunctionBot):
                            cell.set_content("malfunction_bot")  # Set content for GathererBot
                        elif isinstance(bot, ScavengerBot):
                            cell.set_content("scavenger_bot")  # Set content for GathererBot
                        object_found = True
                        break  # Exit the loop once the object is found

                # Draw the emoji/text in the center of the cell
                x1 = col * self.cell_size  # Calculate the top-left x coordinate
                y1 = row * self.cell_size  # Calculate the top-left y coordinate
                x2 = x1 + self.cell_size  # Calculate the bottom-right x coordinate
                y2 = y1 + self.cell_size  # Calculate the bottom-right y coordinate
                self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=cell.emoji, font=("Arial Unicode MS", 12))

                # Only draw the text if an object was found
                if object_found:
                    self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=cell.emoji, font=("Arial Unicode MS", 12))

    def recurring_update(self):
        # Update the state of all bots, stations, and parts at regular intervals
        if self.running:
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

# GUI Branch repository commands:
# git checkout main
# git checkout -b gui
# git add "techburg_simulation/view/gui3.py"
# git commit -m ""
# git push origin gui

