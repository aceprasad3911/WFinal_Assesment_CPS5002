# cell3.py

class Cell:
    def __init__(self, __bot_type="TBC"):
        self.agent = None
        self.__bot_type = __bot_type
        self.emoji = self.get_emoji(__bot_type)

    @staticmethod
    def get_emoji(__bot_type):
        emoji_key = {
            "empty": "",  # Empty space
            "spare_part": "🔧",  # Spare parts
            "recharge_station": "🔋",  # Recharge station
            "repair_bot": "⛑️",  # Repair bot
            "gatherer_bot": "🤖",  # Gatherer bot
            "malfunction_bot": "👹",  # Malfunctioning drone
            "scavenger_bot": "🐝"  # Scavenger swarm
        }
        emoji = emoji_key.get(__bot_type, "")  # Default emoji for unknown content
        return emoji

    @staticmethod
    def get_background(__bot_type):
        background_key = {
            "TBC": "gray",  # Empty space
            "spare_part": "gray",  # Spare parts
            "recharge_station": "orange",  # Recharge station
            "recharge_station_area": "yellow",  # Recharge station area
            "repair_bot": "gray️",  # Repair bot
            "gatherer_bot": "gray",  # Gatherer bot
            "malfunction_bot": "gray",  # Malfunctioning drone
            "scavenger_bot": "gray"  # Scavenger swarm
        }
        background = background_key.get(__bot_type, "")  # Default emoji for unknown content
        return background

    def set_content(self, __bot_type):
        self.__bot_type = __bot_type
        self.emoji = self.get_emoji(__bot_type)

    def has_agent(self):
        return self.agent is not None  # Check if there is an agent in the cell
