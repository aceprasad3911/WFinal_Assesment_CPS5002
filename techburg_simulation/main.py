# main.py: Finally, develop this file to serve as the entry point for your program.
# It will import necessary modules and start the simulation.

# Responsibilities:
# Initialize the simulation.
# Set up the grid, populate it with cells, bots, recharge stations, drones, and spare parts.
# Run the simulation loop.

# Interactions:
# Imports the Simulation class from simulation.py to manage the overall simulation logic.
# Uses Grid from grid.py to create the grid structure.
# Initializes SurvivorBot, RepairBot, GathererBot, RechargeStation, Drone, and ScavengerSwarm as needed.

# main.py
from grid import Grid

if __name__ == "__main__":
    grid = Grid(techburg_grid_size=40, techburg_cell_size=15)  # Create an instance of Grid
