# cell.py

class Cell:
    def __init__(self, cell_type=None):
        self.cell_type = cell_type  # Type of the cell (e.g., 'empty', 'spare_part', 'survivor_bot', etc.)
        self.color = self.get_color()  # Color representation based on cell type

    def get_color(self):
        # Define colors based on cell type
        if self.cell_type == 'empty':
            return 'gray'
        elif self.cell_type == 'spare_part':
            return 'blue'
        elif self.cell_type == 'survivor_bot':
            return 'green'
        elif self.cell_type == 'recharge_station':
            return 'yellow'
        elif self.cell_type == 'malfunctioning_drone':
            return 'red'
        elif self.cell_type == 'scavenger_swarm':
            return 'purple'
        else:
            return 'white'

    def __repr__(self):
        return f"Cell(type={self.cell_type})"