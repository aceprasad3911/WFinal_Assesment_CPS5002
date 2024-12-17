# spare_part3.py

class SparePart:
    def __init__(self, simulation, grid, x, y, object_id):
        self.__grid = None
        self.simulation = simulation
        self.__grid = grid  # Store the grid reference
        self._location = [x, y]  # Store the location
        self.id = object_id  # Assign the bot ID
        self.__object_type = "spare_part"

    def get_x(self):
        return self._location[0]  # Return x-coordinate

    def get_y(self):
        return self._location[1]  # Return y-coordinate
