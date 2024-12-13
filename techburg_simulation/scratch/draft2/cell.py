

# Responsibilities:
# Represents individual cells in the grid.
# Holds references to the objects (e.g., bots, parts) present in that cell.

# Interactions:
# Provides methods to add and remove objects from the cell.
# Interacts with Grid to update its state.
# cell.py

class Cell:
    def __init__(self, content="empty"):
        self.content = content
        self.emoji = self.get_emoji(content)

    @staticmethod
    def get_emoji(content):
        """Return the corresponding emoji for the cell's content."""
        emoji_map = {
            "empty": "",  # Empty space
            "spare_parts": "",  # Spare parts
            "survivor_bot": "",  # Survivor bot
            "repair_bot": "",  # Repair bot
            "gatherer_bot": "",  # Gatherer bot
            "recharge_station": "",  # Recharge station
            "malfunctioning_drone": "",  # Malfunctioning drone
            "scavenger_swarm": ""  # Scavenger swarm
        }
        return emoji_map.get(content, "")  # Default emoji for unknown content

    def set_content(self, content):
        self.content = content
        self.emoji = self.get_emoji(content)
