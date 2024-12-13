# cell.py

class Cell:
    def __init__(self, __bot_type="TBC"):
        self.__bot_type = __bot_type
        self.emoji = self.get_emoji(__bot_type)

    @staticmethod
    def get_emoji(__bot_type):
        """Return the corresponding emoji for the cell's content."""
        emoji_key = {
            "TBC": "",  # Empty space
            "spare_parts": "",  # Spare parts
            "survivor_bot": "",  # Survivor bot
            "repair_bot": "",  # Repair bot
            "gatherer_bot": "🧺",  # Gatherer bot
            "recharge_station": "",  # Recharge station
            "malfunctioning_drone": "",  # Malfunctioning drone
            "scavenger_swarm": ""  # Scavenger swarm
        }
        return emoji_key.get(__bot_type, "")  # Default emoji for unknown content

    def set_content(self, __bot_type):
        self.__bot_type = __bot_type
        self.emoji = self.get_emoji(__bot_type)
