# Configuration (config.py)
# Develop: Define all constants and configuration settings.
# Test: Ensure that the values are correctly defined and accessible.

# Location (location.py)
# Develop: Implement the Location class with all necessary methods.
# Test: Create unit tests to verify that the location coordinates can be set and retrieved correctly, and that equality checks work as expected.

# Utilities (utility.py)
# Develop: Implement utility functions (e.g., random location generation, logging).
# Test: Write tests for utility functions to ensure they return expected results.

# Abstract Agent (abstract_agent.py)
# Develop: Create the abstract Agent class with common attributes and methods.
# Test: Verify that the abstract class cannot be instantiated and that subclasses must implement the act method.

# Environment (environment.py)
# Develop: Implement the Environment abstract class and the Grid class.
# Test: Write tests for the grid's ability to set and get agents, clear the grid, and find free locations.

# Specific Agent Classes (bots_mc.py)
# Develop: Start with one specific agent class (e.g., SurvivorBot).
# Test: Implement the act method and test the agent's behavior in isolation.

# Simulation (simulation.py)
# Develop: Implement the Simulator class, including the simulation loop and methods for updating and rendering.
# Test: Test the simulation loop with a simple setup to ensure agents can act and the simulation can run without errors.

# Main Entry Point (main.py)
# Develop: Set up the main entry point to initialize the simulation and start it.
# Test: Run the simulation to ensure that everything integrates correctly and that the simulation starts as expected.

# Integration Testing
# After developing and testing individual components, conduct integration tests to ensure that all parts of the simulation work together as intended. This includes checking interactions between agents, the environment, and the simulation loop.

# GUI Development (if applicable)
# If you plan to implement a graphical user interface (GUI), develop it after the core simulation logic is in place. This allows you to visualize the simulation effectively.
# Test the GUI to ensure it correctly represents the state of the simulation and responds to user inputs.