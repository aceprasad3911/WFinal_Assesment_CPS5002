# Techburg City Layout:
# - Grid Size: Minimum 30x30 cells.
# - Grid Wrap-around: The grid should wrap around at the edges (toroidal structure).
# - Cell Contents: Cells may contain empty spaces, spare parts, survivor bots, recharge stations, malfunctioning drones, or scavenger swarms.

# Spare Parts:
# - Sizes and Enhancements:
#   Small: Provides a 3% enhancement to survivor bots.
#   Medium: Provides a 5% enhancement.
#   Large: Provides a 7% enhancement.
# - Corrosion:
#   Parts lose 0.1% of their enhancement value per simulation step.
#   Once placed in a recharge station, parts stop corroding and gradually recharge to full enhancement.
# - Scavenger Swarm Consumption:
#   Small parts increase swarm energy by 1%.
#   Medium parts by 2%.
#   Large parts by 3%.
#   Parts are removed from the grid upon being consumed.

# Survivor Bots:
# - Movement and Energy:
#   Each move depletes bot energy by 5%.
#   If energy drops to 5% or below, bots consume parts immediately to restore energy.
#   Energy is restored at recharge stations; bots can also rest to regenerate at a rate of 1% per simulation step without consuming parts.
# - Carrying and Collecting:
#   Bots can carry only one part at a time.
#   Prioritize larger parts when selecting.
# - Bot Types:
#   Repair Bots and Gatherer Bots.
#   Collaboration among bots allows creation of new bots at stations:
#   20% chance of creating a gatherer bot (costs 30% energy from each bot).
#   5% chance of creating a repair bot (costs 50% energy from each bot).
# - Enhancements:
#   Bots can enhance speed, vision, or energy based on spare parts consumed:
#   Speed: Default movement occurs every other simulation step; a speed enhancement of 51–100% allows movement every step, with a maximum enhancement of 100%.
#   Vision: Detects parts in adjacent cells; with 51–100% enhancement, bots detect two cells away, and up to three cells away with 101–150% enhancement. Maximum detection enhancement is 150%.

# Recharge Stations:
# - Capacity: Can hold up to five survivor bots.
# - Part Storage: Bots store collected parts in stations for recharging and enhancement.
# - Information Sharing: Bots at a station share data on locations of parts, recharge stations, drones, and swarms.

# Malfunctioning Drones:
# - Pursuit Range: Drones detect survivor bots within three cells.
# - Pursuit Energy Cost: Chasing depletes a drone’s energy by 20%.
# - Attack Mechanics:
#   Shock attack: Reduces bot energy by 5% and causes it to drop its part.
#   Disable attack: Reduces bot energy by 20% and causes it to drop its part.
# - Hibernation: Drones enter hibernation when energy drops to 20%, recharging at 10% per simulation step.

# Scavenger Swarms:
# - Decay Field: Reduces energy of nearby bots and drones by 3% per simulation step within one cell.
# - Merging: Nearby swarms merge to form larger swarms, enhancing their resource consumption rate.
# - Replication: Swarms can self-replicate if they gather enough material.

# Simulation Parameters:
# - Starting Conditions: Begin with a populated grid including recharge stations, survivor bots, spare parts, drones, and scavenger swarms.
# - End Conditions: Simulation ends when all spare parts are collected or corroded, or all survivor bots are eliminated without possibility of replication.

# Permitted Libraries: enum, math, os, pytest, random, sklearn, tkinter, textblob, unittest, and standard Python data structures.
# Development Tools: PyCharm, Python 3.11+, Git, Draw.io, and Microsoft Word/Adobe PDF for documentation.

# Deadline: January 17, 2024.
