#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
import time

# Set up the warehouse dimensions
warehouse_width = 10
warehouse_height = 10

# Starting and destination points
start_position = (0, 0)
destination_position = (7, 9)

# Robot parameters
robot_speed = 0.1  # in meters per second
move_time = 0.1    # time for each movement in seconds
pause_time = 2     # pause time after each movement in seconds

# Initialize the robot's position
robot_position = list(start_position)
path = [tuple(robot_position)]  # to keep track of the path

# Function to update robot's position
def move_robot(robot_position, destination_position):
    dx, dy = destination_position[0] - robot_position[0], destination_position[1] - robot_position[1]
    if dx != 0:
        robot_position[0] += 0.1 if dx > 0 else -0.1
    elif dy != 0:
        robot_position[1] += 0.1 if dy > 0 else -0.1
    robot_position[0] = round(robot_position[0], 1)
    robot_position[1] = round(robot_position[1], 1)
    path.append(tuple(robot_position))
    return robot_position

# Visualization setup
plt.figure(figsize=(6, 6))
plt.xlim(0, warehouse_width)
plt.ylim(0, warehouse_height)

# Plot the warehouse layout
plt.plot(*start_position, 'go', label="Start Position")
plt.plot(*destination_position, 'ro', label="Destination")

# Run the simulation
while tuple(robot_position) != destination_position:
    # Move the robot towards the destination
    robot_position = move_robot(robot_position, destination_position)
    
    # Plot current robot position
    plt.plot(robot_position[0], robot_position[1], 'bo')
    plt.pause(0.1)
    
    # Wait for the pause time (simulation of robot stop)
    time.sleep(pause_time)

# Final path plot
plt.plot(*zip(*path), marker='o', color='b', linestyle='-', label="Path")
plt.legend()
plt.show()


# In[ ]:




