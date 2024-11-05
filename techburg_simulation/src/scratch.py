import random

class SurvivorBot:
    def __init__(self):
        self.energy = 100  # Start with full energy (100%)
        self.carrying_part = None  # Initially not carrying any part

    def move(self):
        """Move the bot, which depletes energy by 5%."""
        if self.energy > 5:
            self.energy -= 5
            print(f"{self.__class__.__name__} moved. Current energy: {self.energy}%")
        else:
            print(f"{self.__class__.__name__} has too low energy to move. Consuming parts to restore energy.")
            self.consume_parts()

    def consume_parts(self):
        """Restore energy by consuming parts if energy is 5% or below."""
        if self.energy <= 5:
            self.energy = 100  # Restoring energy to full
            self.carrying_part = None  # Assume part is consumed
            print(f"{self.__class__.__name__} restored energy by consuming parts. Current energy: 100%")

    def recharge(self):
        """Recharge energy at a recharge station."""
        self.energy = 100  # Restore energy to full
        print(f"{self.__class__.__name__} recharged. Current energy: 100%")

    def rest(self):
        """Rest to regenerate energy at a rate of 1% per simulation step."""
        if self.energy < 100:
            self.energy += 1
            print(f"{self.__class__.__name__} is resting... Current energy: {self.energy}%")
        else:
            print(f"{self.__class__.__name__} energy is already full. No need to rest.")

    def carry_part(self, part_size):
        """Carry a part, prioritizing larger parts."""
        if self.carrying_part is None:
            self.carrying_part = part_size
            print(f"{self.__class__.__name__} is carrying part of size: {part_size}")
        else:
            print(f"{self.__class__.__name__} is already carrying a part. Must drop it before carrying another.")

    def drop_part(self):
        """Drop the currently carried part."""
        if self.carrying_part is not None:
            print(f"{self.__class__.__name__} dropped part of size: {self.carrying_part}")
            self.carrying_part = None
        else:
            print(f"{self.__class__.__name__} is not carrying any part to drop.")

    def collaborate(self, other_bot):
        """Collaborate with another bot to potentially create new bots."""
        if isinstance(other_bot, SurvivorBot):
            # Calculate energy cost for collaboration
            energy_cost = 0
            if random.random() < 0.20:  # 20% chance of creating a gatherer bot
                energy_cost = 30
                print(f"{self.__class__.__name__} and {other_bot.__class__.__name__} created a Gatherer Bot!")
                return "GathererBot"
            elif random.random() < 0.05:  # 5% chance of creating a repair bot
                energy_cost = 50
                print(f"{self.__class__.__name__} and {other_bot.__class__.__name__} created a Repair Bot!")
                return "RepairBot"

            # Deduct energy from both bots if creation was successful
            if energy_cost > 0:
                self.energy -= energy_cost
                other_bot.energy -= energy_cost
                print(f"Both bots spent {energy_cost}% energy for collaboration.")

        return None