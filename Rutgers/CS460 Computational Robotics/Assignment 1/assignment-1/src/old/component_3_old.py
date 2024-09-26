# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

# """
# function interpolate_rigid_body()
# """
# def interpolate_rigid_body(start_pose: np.array, goal_pose: np.array):
#     start_pose = np.array(start_pose)
#     goal_pose = np.array(goal_pose)
    
#     # Calculating the Euclidean distance between start and goal positions.
#     distance = np.linalg.norm(goal_pose[:2] - start_pose[:2])
    
#     # Setting the resolution (distance between interpolated points).
#     resolution = 0.1 # Distance between consecutive interpolated points.
    
#     # Number of steps based on the distance and resolution.
#     steps = int(distance / resolution)
    
#     # Create a path by linearly interpolating between start_pose and goal_pose.
#     path = [
#         start_pose + t * (goal_pose - start_pose) / steps for t in range(steps + 1)
#     ]
    
#     return np.array(path)

# """
# function forward_propagate_rigid_body()
# """
# def forward_propagate_rigid_body(start_pose, plan):
#     path = [np.array(start_pose)]
#     current_pose = np.array(start_pose)
    
#     # Iterate over the plan (velocity, duration) tuples.
#     for velocity, duration in plan:
#         vx, vy, v_theta = velocity
        
#         # Update the pose over the duration by applying the velocity.
#         for _ in range(int(duration)):
#             # Update the x, y, and theta using velocity.
#             current_pose[0] += vx # Update the x-position
#             current_pose[1] += vy # Update the y-position
#             current_pose[2] += v_theta # Update theta (orientation)
            
#             # Append the  updated pose to the path.
#             path.append(current_pose.copy())
    
#     return np.array(path)

# """
# function visualize_path
# """
# def visualize_path(path):
#     # Set up the figure and axis
#     fig, ax = plt.subplots()
#     ax.set_xlim(-10, 10)  # Set limits for the environment
#     ax.set_ylim(-10, 10)

#     # Plot the full path
#     x_data = path[:, 0]
#     y_data = path[:, 1]
#     ax.plot(x_data, y_data, 'b--', label="Path")

#     # Initialize the robot marker and orientation arrow
#     robot_marker, = ax.plot([], [], 'ro', label="Robot")
#     orientation_arrow = ax.quiver([], [], [], [], angles='xy', scale_units='xy', scale=1, color='r')

#     # Function to update the animation at each frame
#     def update(frame):
#         # Update robot's position
#         robot_marker.set_data(path[frame, 0], path[frame, 1])
        
#         # Update orientation (robot's heading direction)
#         theta = path[frame, 2]
#         dx = np.cos(theta)  # Change in x for orientation arrow
#         dy = np.sin(theta)  # Change in y for orientation arrow

#         # Update the position and orientation of the arrow
#         orientation_arrow.set_offsets(np.array([[path[frame, 0], path[frame, 1]]]))  # Set new offset
#         orientation_arrow.set_UVC([dx], [dy])  # Set new orientation vector

#         return robot_marker, orientation_arrow

#     # Create the animation
#     anim = FuncAnimation(fig, update, frames=len(path), interval=200, blit=True)
    
#     # Display the animation
#     plt.legend()
#     plt.show()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

"""
function interpolate_rigid_body()
"""
def interpolate_rigid_body(start_pose: np.array, goal_pose: np.array):
    start_pose = np.array(start_pose)
    goal_pose = np.array(goal_pose)
    
    # Calculating the Euclidean distance between start and goal positions.
    distance = np.linalg.norm(goal_pose[:2] - start_pose[:2])
    
    # Setting the resolution (distance between interpolated points).
    resolution = 0.1 # Distance between consecutive interpolated points.
    
    # Number of steps based on the distance and resolution.
    steps = int(distance / resolution)
    
    # Create a path by linearly interpolating between start_pose and goal_pose.
    path = [
        start_pose + t * (goal_pose - start_pose) / steps for t in range(steps + 1)
    ]
    
    return np.array(path)

"""
function forward_propagate_rigid_body()
"""
def forward_propagate_rigid_body(start_pose, plan):
    path = [np.array(start_pose)]
    current_pose = np.array(start_pose)

    # Iterate over the plan (velocity, duration) tuples.
    for velocity, duration in plan:
        vx, vy, v_theta = map(float, velocity)  # Ensure velocities are floats
        
        # Debugging output
        print(f"Velocity: {velocity}, Duration: {duration}")
        
        # Update the pose over the duration by applying the velocity.
        for _ in range(int(duration)):
            # Update the x, y, and theta using velocity.
            current_pose[0] += vx  # Update the x-position
            current_pose[1] += vy  # Update the y-position
            current_pose[2] += v_theta  # Update theta (orientation)
            
            # Append the updated pose to the path.
            path.append(current_pose.copy())
            print(f"Updated Pose: {current_pose}")  # Debugging output
    
    return np.array(path)

"""
function visualize_path
"""
def visualize_path(path):
    # Set up the figure and axis
    fig, ax = plt.subplots()
    ax.set_xlim(-10, 10)  # Set limits for the environment
    ax.set_ylim(-10, 10)

    # Plot the full path
    x_data = path[:, 0]
    y_data = path[:, 1]
    ax.plot(x_data, y_data, 'b--', label="Path")

    # Initialize the robot marker and orientation arrow
    robot_marker, = ax.plot([], [], 'ro', label="Robot")
    orientation_arrow = ax.quiver([], [], [], [], angles='xy', scale_units='xy', scale=1, color='r')

    # Function to update the animation at each frame
    def update(frame):
        # Update robot's position
        robot_marker.set_data([path[frame, 0]], [path[frame, 1]])
        
        # Update orientation (robot's heading direction)
        theta = path[frame, 2]
        dx = np.cos(theta)  # Change in x for orientation arrow
        dy = np.sin(theta)  # Change in y for orientation arrow

        # Update the position and orientation of the arrow
        orientation_arrow.set_offsets([[path[frame, 0], path[frame, 1]]])  # Set new offset
        orientation_arrow.set_UVC([dx], [dy])  # Set new orientation vector

        return robot_marker, orientation_arrow

    # Create the animation
    anim = FuncAnimation(fig, update, frames=len(path), interval=200, blit=False)  # Turn off blit for debugging
    
    # Display the animation
    plt.legend()
    plt.show()

# def visualize_path(path):
#     # Set up the figure and axis
#     fig, ax = plt.subplots()
#     ax.set_xlim(-10, 10)  # Set limits for the environment
#     ax.set_ylim(-10, 10)

#     # Plot the full path
#     x_data = path[:, 0]
#     y_data = path[:, 1]
#     ax.plot(x_data, y_data, 'b--', label="Path")

#     # Initialize the robot marker and orientation arrow
#     robot_marker, = ax.plot([], [], 'ro', label="Robot", markersize=8)
    
#     # Length and scale of the orientation arrow (to make the orientation more visible)
#     arrow_length = 10  # Length of the orientation arrow (increase if needed)
    
#     # Create an orientation arrow (initially zero-length)
#     orientation_arrow = ax.quiver([], [], [], [], angles = 'xy', scale_units = 'xy', scale = 10, color = 'green')

#     # Function to update the animation at each frame
#     def update(frame):
#         # Update robot's position
#         robot_marker.set_data([path[frame, 0]], [path[frame, 1]])
        
#         # Update orientation (robot's heading direction)
#         theta = path[frame, 2]
        
#         # Calculate direction vector based on theta (orientation)
#         dx = arrow_length * np.cos(theta)  # Change in x for orientation arrow
#         dy = arrow_length * np.sin(theta)  # Change in y for orientation arrow

#         # Update the position and orientation of the arrow
#         orientation_arrow.set_offsets([path[frame, 0], path[frame, 1]])  # Set new offset (position)
#         orientation_arrow.set_UVC([dx], [dy])  # Set new orientation vector (direction)
        
#         return robot_marker, orientation_arrow

#     # Create the animation
#     anim = FuncAnimation(fig, update, frames=len(path), interval = 100, blit = False)  # Turn off blit for debugging
    
#     # Display the animation
#     plt.legend()
#     plt.show()