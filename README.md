# Autonomous_Navigation
1. Define the Warehouse Environment
Represent the 10x10 meter warehouse as a grid.
Define the start point (0, 0) and the destination (7, 9).
2. Set Robot Movement Constraints
Robot speed: 0.1 m/s
Movement time: 0.1 seconds, followed by a 2-second pause.
Ensure movement stays within the grid boundaries.
3. Implement the Simulation Logic
Move the robot along the shortest path (using a direct path or grid-based movement).
Track the time and update the robot’s position every 0.1 seconds.
Pause for 2 seconds after every movement.
4. Visual Representation of Movement
Use Matplotlib to show the warehouse and the robot's position over time.
Display pauses and movements distinctly.
5. Optional Enhancements
Introduce obstacles and reroute the robot if you want a more complex scenario.


#Explanation of the Code
#Movement Function:

The move_robot function moves the robot step-by-step toward the destination, making adjustments to x or y coordinates based on the shortest path.
#Visualization:

We use plt.plot() to mark the start, destination, and intermediate positions.
plt.pause() shows movement in real-time with the 0.1-second interval.
#Time Delay:

time.sleep(pause_time) simulates the 2-second pause after each movement.
