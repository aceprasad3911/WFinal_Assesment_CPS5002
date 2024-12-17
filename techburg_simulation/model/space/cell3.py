# cell.py

class Cell:
    def __init__(self, __bot_type="TBC"):
        self.agent = None
        self.__bot_type = __bot_type
        self.emoji = self.get_emoji(__bot_type)

    @staticmethod
    def get_emoji(__bot_type):
        emoji_key = {
            "TBC": "",  # Empty space
            "spare_part": "🔧",  # Spare parts
            "recharge_station": "🔋",  # Recharge station
            "repair_bot": "⛑️",  # Repair bot
            "gatherer_bot": "🤖",  # Gatherer bot
            "malfunction_bot": "👹",  # Malfunctioning drone
            "scavenger_bot": "🐝"  # Scavenger swarm
        }
        emoji = emoji_key.get(__bot_type, "")  # Default emoji for unknown content
        return emoji

    def set_content(self, __bot_type):
        self.__bot_type = __bot_type
        self.emoji = self.get_emoji(__bot_type)

    def has_agent(self):
        return self.agent is not None  # Check if there is an agent in the cell
