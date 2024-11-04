import tkinter as tk


class Grid:
    def __init__(self, grid_size=20):  # Reduced size for better visibility
        self.grid_size = grid_size
        # Create a 2D list (grid) to represent the grid, initially filled with None
        self.grid = [[None for _ in range(grid_size)] for _ in range(grid_size)]

        # Initialize the Tkinter GUI
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=grid_size * 30, height=grid_size * 30)  # Create a canvas for drawing
        self.canvas.pack()  # Pack the canvas into the Tkinter window
        self.cell_size = 30  # Define the size of each cell in the grid
        self.update_display()  # Initial display update to show the grid

    def update_display(self):
        # Clear the canvas
        self.canvas.delete("all")
        # Draw the grid
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                x1 = col * self.cell_size
                y1 = row * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="white")

    def run(self):
        self.root.mainloop()


# Create a grid instance and run the application
grid = Grid(grid_size=20)
grid.run()
