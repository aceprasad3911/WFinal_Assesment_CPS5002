# Scavenger Swarms:
# - Decay Field: Reduces energy of nearby bots and drones by 3% per simulation step within one cell.
# - Merging: Nearby swarms merge to form larger swarms, enhancing their resource consumption rate.
# - Replication: Swarms can self-replicate if they gather enough material.

# Responsibilities:
# Represents swarms that can consume parts and affect nearby bots.

# Interactions:
# Interacts with SurvivorBot and Drone to reduce their energy.
# Can merge with other swarms and replicate based on resource availability.

class ScavengerSwarm:
    pass