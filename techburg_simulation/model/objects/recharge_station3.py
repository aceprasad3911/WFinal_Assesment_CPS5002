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

        # Create the perimeter around the recharge station
        self.create_perimeter()

    def create_perimeter(self):
        # Define the perimeter cells (for example, one cell around the station)
        perimeter_coords = [
            (self.get_x() - 1, self.get_y()),  # Up
            (self.get_x() + 1, self.get_y()),  # Down
            (self.get_x(), self.get_y() - 1),  # Left
            (self.get_x(), self.get_y() + 1),  # Right
            (self.get_x() - 1, self.get_y() - 1),  # Up-Left
            (self.get_x() - 1, self.get_y() + 1),  # Down-Left
            (self.get_x() + 1, self.get_y() - 1),  # Up-Right
            (self.get_x() + 1, self.get_y() + 1)  # Down-Right
        ]

        for px, py in perimeter_coords:
            if 0 <= px < self.__grid.size and 0 <= py < self.__grid.size:  # Check bounds
                perimeter = RechargeStationPerimeter(self.simulation, self.__grid, px, py)
                self.simulation.objects.append(perimeter)  # Add perimeter to the simulation

    def get_x(self):
        return self._location[0]  # Return x-coordinate

    def get_y(self):
        return self._location[1]  # Return y-coordinate


class RechargeStationPerimeter:
    def __init__(self, simulation, grid, x, y):
        self.simulation = simulation
        self.__grid = grid  # Store the grid reference
        self._location = [x, y]  # Store the location

    def get_x(self):
        return self._location[0]  # Return x-coordinate

    def get_y(self):
        return self._location[1]  # Return y-coordinate
