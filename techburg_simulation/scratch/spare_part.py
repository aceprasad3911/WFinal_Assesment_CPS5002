# Spare Parts:
# - Sizes and Enhancements:
#   Small: Provides a 3% enhancement to survivor bots.
#   Medium: Provides a 5% enhancement.
#   Large: Provides a 7% enhancement.
# - Corrosion:
#   Parts lose 0.1% of their enhancement value per simulation step.
#   Once placed in a recharge station, parts stop corroding and gradually recharge to full enhancement.
# - Scavenger Swarm Consumption:
#   Small parts increase swarm energy by 1%.
#   Medium parts by 2%.
#   Large parts by 3%.
#   Parts are removed from the grid upon being consumed.

# Responsibilities:
# Represents spare parts with attributes like size and enhancement value.

# Interactions:
# Bots interact with this class to collect and use parts.
# Recharge stations manage the storage and recharging of parts.

class SparePart:
    def __init__(self, grid, row, col):
        self.grid = grid
        self.__location = [row, col]
        self.grid.set_cell(row, col, 'recharge_station')

