import unittest

from techburg_simulation.model.space.cell3 import Cell


# Mock Grid class for testing
class MockGrid:
    def __init__(self, size):
        self.size = size
        self.cells = [[Cell() for _ in range(size)] for _ in range(size)]

    def get_height(self):
        return self.size

    def get_width(self):
        return self.size

    def set_cell_content(self, row, col, content):
        self.cells[row][col] = content

    def get_cell_content(self, row, col):
        return self.cells[row][col] if 0 <= row < self.size and 0 <= col < self.size else None


# Mock Agent class for testing
class MockAgent:
    def __init__(self, grid, x, y):
        self._grid = grid
        self._location = [x, y]

    def _scan(self):
        col = self._location[0]
        row = self._location[1]
        directions = [(-1, -1), (-1, 0), (-1, +1), (0, -1), (0, +1), (+1, -1), (+1, 0), (+1, +1)]
        neighbour_contents = []
        for dr, dc in directions:
            new_row = (row + dr) % self._grid.get_height()
            new_col = (col + dc) % self._grid.get_width()
            content = self._grid.get_cell_content(new_row, new_col)
            neighbour_contents.append((new_row, new_col, content))
        return neighbour_contents


class TestScanMethod(unittest.TestCase):
    def setUp(self):
        # Create a mock grid and agent for testing
        self.grid = MockGrid(5)  # 5x5 grid
        self.agent = MockAgent(self.grid, 2, 2)  # Place agent at (2, 2)

    def test_scan_empty_cells(self):
        # Test scanning when all neighboring cells are empty
        expected = [
            (1, 1, None), (1, 2, None), (1, 3, None),
            (2, 1, None), (2, 2, None), (2, 3, None),
            (3, 1, None), (3, 2, None), (3, 3, None)
        ]
        result = self.agent._scan()
        self.assertEqual(result, expected)

    def test_scan_with_spare_parts(self):
        # Set some cells with spare parts
        self.grid.set_cell_content(1, 2, "spare_part")
        self.grid.set_cell_content(2, 3, "spare_part")

        expected = [
            (1, 1, None), (1, 2, "spare_part"), (1, 3, None),
            (2, 1, None), (2, 2, None), (2, 3, "spare_part"),
            (3, 1, None), (3, 2, None), (3, 3, None)
        ]
        result = self.agent._scan()
        self.assertEqual(result, expected)

    def test_scan_with_wrapping(self):
        # Set some cells with spare parts at the edges to test wrapping
        self.grid.set_cell_content(0, 0, "spare_part")  # Top-left corner
        self.grid.set_cell_content(4, 4, "spare_part")  # Bottom-right corner

        # Place agent at (0, 0) to test wrapping
        self.agent = MockAgent(self.grid, 0, 0)

        expected = [
            (4, 4, " spare_part"), (4, 0, None), (4, 1, None),
            (0, 4, None), (0, 0, None), (0, 1, None),
            (1, 4, None), (1, 0, None), (1, 1, None)
        ]
        result = self.agent._scan()
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
