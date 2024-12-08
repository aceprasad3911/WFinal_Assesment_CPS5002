# config.py: Start with this file to define configuration settings such as grid size,
# initial agent counts, energy values, and any other constants needed throughout the simulation.
# This will provide a centralized place for configuration that can be easily modified.

# Grid Configuration
GRID_SIZE = 50  # Techburg grid size (50x50 cells)

# Initial Agent Counts
INITIAL_COUNTS = {
    "recharge_stations": 3,
    "repair_bots": 3,
    "gatherer_bots": 2,
    "scavenger_bots": 4,
    "drones": 10,
    "spare_parts": 20
}

# Bot MIN/MAX Values
BOT_INITIAL_ENERGY = 100
BOT_MAX_ENERGY = 100
BOT_MIN_ENERGY = 0
BOT_INITIAL_HEALTH = 100
BOT_MAX_HEALTH = 100
BOT_MIN_HEALTH = 0
BOT_INITIAL_MOVEMENT = 0.5
BOT_MAX_MOVEMENT = 1
BOT_MIN_MOVEMENT = 0
BOT_INITIAL_VISION = 1
BOT_MAX_VISION = 3
BOT_MIN_VISION = 1

# Movement and Vision Rates
BOT_MOVEMENT_ENERGY_COST = -5  # Energy cost per movement
BOT_RECHARGE_RATE = 1  # (1% Energy per loop)
BOT_STANDARD_MOVEMENT_RATE = 0.5  # (1 square per 2 loops)
BOT_CURRENT_MOVEMENT_RATE = BOT_STANDARD_MOVEMENT_RATE
BOT_STANDARD_VISION_RANGE = 1  # (1 square perimeter)
BOT_CURRENT_VISION_RANGE = BOT_STANDARD_VISION_RANGE

# Movement and Vision Rates
BOT_STATUSES = {"healthy", "hurt", "sleepy", "resting", "charging"}
BOT_TYPES = {"repair_bot", "gatherer_bot", "TBC"}
BOT_CARRY_STATUS = {"hands_full", "hands_empty"}
BOT_APPETITE = {"starving", "hungry", "normal", "full"}

# Bot Energy Costs and Reproduction Probabilities
BOT_ENERGY_COSTS = {
    "gatherer": {
        "production_probability": 0.2,  # (20%)
        "energy_cost": -30
    },
    "repair": {
        "production_probability": 0.05,  # (5%)
        "energy_cost": -50
    }
}

# Survivor Bot Behavior
SBOT_CRITICAL_ENERGY_THRESHOLD = 5  # Energy level at which bots consume parts immediately

# Recharge Station Values
RECHARGE_STATION_BOT_CAPACITY = 5  # Max number of bots per station
RECHARGE_STATION_PART_CAPACITY = 40  # Max parts a station can hold

# Scavenger's Behavior
SCAVENGER_MERGE_THRESHOLD = 3  # Number of scavenger's needed to merge swarm
SCAVENGER_DECAY_FIELD_EFFECT = 0.03  # Energy loss per step for nearby bots

# Malfunctioning Drone Values
DRONE_ENERGY_COST_PER_PURSUIT = -20
DRONE_PURSUIT_RANGE = 5  # (5 loops, 5 steps)
DRONE_HIBERNATION_THRESHOLD = 20  # Energy threshold for hibernation
DRONE_RECHARGE_RATE = 0.10  # Recharge rate per simulation step

# Spare Part Values
SPARE_PARTS = {
    "small": {"sbot_enhancement": 0.03, "sbot_consumption": 0.01, "scavenger_consumption":  0.01, "consumption_time": 6},
    "medium": {"sbot_enhancement": 0.05, "sbot_consumption": 0.02, "scavenger_consumption": 0.02, "consumption_time": 10},
    "large": {"sbot_enhancement": 0.07, "sbot_consumption": 0.03, "scavenger_consumption": 0.03, "consumption_time": 14}
}

SPARE_PART_CORROSION_RATE = -0.001  # (-0.1% per step)
SPARE_PART_RECHARGE_RATE = 0.005  # (+0.5% per step)

# Simulation Control
SIMULATION_END_CONDITIONS = {
    "all_parts_collected": True,
    "all_bots_eliminated": False
}
