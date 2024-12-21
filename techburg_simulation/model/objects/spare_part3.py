# spare_part3.py

class SparePart:
    def __init__(self, simulation, grid, x, y, object_id):
        self._grid = None
        self._simulation = simulation
        self._grid = grid  # Store the grid reference
        self._location = [x, y]  # Store the location
        self._id = object_id  # Assign the bot ID
        self._object_type = "spare_part"

    def __str__(self):
        return self._object_type

    def get_x(self):
        return self._location[0]  # Return x-coordinate

    def get_y(self):
        return self._location[1]  # Return y-coordinate
