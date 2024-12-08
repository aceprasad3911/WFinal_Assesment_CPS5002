# gui.py
from __future__ import annotations
import tkinter as tk
from tkinter import messagebox
import time

from techburg_simulation.model.space.environment import Environment
from techburg_simulation.model.space.location import Location


class Gui(tk.Tk):
    def __init__(self, environment: Environment, agent_colours: dict):
        super().__init__()
        self.__environment = environment
        self.__agent_colours = agent_colours
        self.__closed = False
        self.__init_gui()
        self.__init_world()

    def render(self):
        for row_index in range(self.__environment.get_height()):
            for col_index in range(self.__environment.get_width()):
                agent = self.__environment.get_agent(Location(col_index, row_index))
                color = self.__agent_colours.get(agent.__class__, "white")  # Default to white if no agent
                cell = self.grid_frame.grid_slaves(row=row_index, column=col_index)
                if cell:
                    # Update the existing cell's color
                    cell[0].config(bg=color)
                else:
                    # Create a new cell if it doesn't exist
                    cell = tk.Canvas(self.grid_frame, width=10, height=10, bg=color, borderwidth=1, relief="solid")
                    cell.grid(row=row_index, column=col_index)
        self.update_idletasks()

    def __init_gui(self):
        self.title("Techburg Simulation")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def __init_world(self):
        self.grid_frame = tk.Frame(self)
        self.grid_frame.grid(row=0, column=0)

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.__closed = True
            self.destroy()

    def is_closed(self) -> bool:
        return self.__closed
