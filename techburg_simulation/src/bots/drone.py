# Malfunctioning Drones:
# - Pursuit Range: Drones detect survivor bots within three cells.
# - Pursuit Energy Cost: Chasing depletes a drone’s energy by 20%.
# - Attack Mechanics:
#   Shock attack: Reduces bot energy by 5% and causes it to drop its part.
#   Disable attack: Reduces bot energy by 20% and causes it to drop its part.
# - Hibernation: Drones enter hibernation when energy drops to 20%, recharging at 10% per simulation step.

# Responsibilities:
# Represents malfunctioning drones that can attack bots.
# Manages energy and attack mechanics.

# Interactions:
# Checks for nearby SurvivorBot using methods that interact with Grid.
# Interacts with SurvivorBot to apply attack effects.

class Drone:
    pass
