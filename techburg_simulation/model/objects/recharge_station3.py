# Recharge Stations:
# - Capacity: Can hold up to five survivor bots.
# - Part Storage: Bots store collected parts in stations for recharging and enhancement.
# - Information Sharing: Bots at a station share data on locations of parts, recharge stations, drones, and swarms.

# Responsibilities:
# Manage the recharging of bots and storage of spare parts.
# Facilitate information sharing among bots.

# Interactions:
# Interacts with SurvivorBot to recharge their energy.
# Provides methods to store and retrieve SparePart objects.

# recharge_station.py

class RechargeStation:
    def __init__(self, simulation, grid, x, y, object_id):
        self.__grid = None
        self.simulation = simulation
        self.__grid = grid  # Store the grid reference
        self._location = [x, y]  # Store the location
        self.id = object_id  # Assign the bot ID
        self.__object_type = "recharge_station"

    def get_x(self):
        return self._location[0]  # Return x-coordinate

    def get_y(self):
        return self._location[1]  # Return y-coordinate
