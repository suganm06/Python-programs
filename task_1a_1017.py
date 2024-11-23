#!/usr/bin/env python3

########################################################################################################################
########################################## eYRC 23-24 Hologlyph Bots Task 1A ###########################################
# Team ID:		1017
# Team Leader Name:	Sugavaneswar M
# Team Members Name:	Sankaran S, Thiruvengadam K, Aathish M
# College:		KCG College of Technology
########################################################################################################################
'''
# Team ID:          1017
# Theme:            Hologlyph Bots
# Author List:      Sugavaneswar M, Sankaran S, Aathish M, Thiruvengadam K
# Filename:         task_1a_1017.py
# Functions:        spawn_turtle, circle_1, pose_callback, circle_2, main
# Global variables: first_turtle_final_pose
'''

import rclpy
from turtlesim.srv import Spawn
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import math
import time

# Global variable to store the final pose of the first turtle
first_turtle_final_pose = None 									# Stores the final pose of the first turtle.

# Function to spawn a turtle
def spawn_turtle(node, client, name, x, y, theta):
    '''
    Spawns a turtle with the specified name, position, and orientation.

    Arguments:
    node: 	The ROS node for communication.
    client: 	The client for the 'spawn' service.
    name: 	The desired name for the turtle.
    x: 		The x-coordinate for the initial position of the turtle.
    y: 		The y-coordinate for the initial position of the turtle.
    theta: 	The initial orientation angle of the turtle.

    Returns:
    A future object to spawn the turtle.
    '''
    request = Spawn.Request()
    request.name = name										# Set the turtle's name.
    request.x = x										# Set the x-coordinate of the turtle to spawn.
    request.y = y										# Set the y-coordinate of the turtle to spawn.
    request.theta = theta									# Set the initial orientation angle of the turtle.
    future = client.call_async(request)
    return future										# Return the future object to spawn the turtle.

# Function to draw a circle with a specified speed and radius using a turtle    
def circle_1(turtle_name, node, speed, radius):
    '''
    Draws a circle in anticlockwise direction with a specified speed and radius using a turtle. 
    The circle is drawn by tracking the elapsed time since the start of the circle.
    If the elapsed time is less than the time needed for a circle, the turtle continues moving in a circle.

    Arguments:
    turtle_name: 	The name of the turtle to draw the circle.
    node: 		The ROS node for communication.
    speed: 		The speed at which the turtle moves.
    radius: 		The radius of the circle.

    Returns:
    None
    '''
    publisher = node.create_publisher(Twist, f'/{turtle_name}/cmd_vel', 10)			# Create a publisher to control the turtle.

    msg = Twist() 
    msg.linear.x = speed 									# Set the linear x velocity of the turtle to control speed.
    msg.angular.z = speed / radius 								# Set the angular z velocity of the turtle to control the circle radius.
    circle_time = 2 * math.pi * radius / speed 							# Calculate the time needed to complete a circle based on speed and radius.

    start_time = node.get_clock().now().to_msg()
    stop_turtle = False  									# Initialize a flag to control when to stop the turtle.
    node.get_logger().info('Drawing circle_1...')
    while not stop_turtle:
        elapsed_time = node.get_clock().now().to_msg().sec - start_time.sec
        if elapsed_time < circle_time:
            publisher.publish(msg) 								# Publish the message to control the turtle's movement.
        else:
            time.sleep(0.25) 									# delay to stop the turtle
            zero_msg = Twist() 									# Create a Twist message to stop the turtle.
            publisher.publish(zero_msg)
            stop_turtle = True 									# Set the flag to stop the turtle, indicating the circle is complete.

# Callback function to update the final pose of the first turtle            
def pose_callback(msg):
    '''
    Callback function to update the final pose of the first turtle.

    Arguments:
    msg: The Pose message containing the turtle's pose.

    Returns:
    None
    '''
    global first_turtle_final_pose 								# Access the global variable to store the final pose of the first turtle.
    first_turtle_final_pose = msg 								# Update the global variable with the latest pose message.

# Function to draw a circle in the opposite direction with a specified speed and radius using a turtle    
def circle_2(turtle_name, node, speed, radius):
    '''
    Draws a circle in clockwise direction with a specified speed and radius using a turtle. 
    The circle is drawn by tracking the elapsed time since the start of the circle.
    If the elapsed time is less than the time needed for a circle, the turtle continues moving in a circle.

    Arguments:
    turtle_name: 	The name of the turtle to draw the circle.
    node: 		The ROS node for communication.
    speed: 		The speed at which the turtle moves.
    radius: 		The radius of the circle.

    Returns:
    None
    '''
    publisher = node.create_publisher(Twist, f'/{turtle_name}/cmd_vel', 10)			# Create a publisher to send Twist messages to control the turtle.

    msg = Twist()
    msg.linear.x = speed 									# Set the linear x velocity of the turtle to control speed.
    msg.angular.z = -speed / radius								# Set the angular z velocity of the turtle to control the circle radius in the opposite direction.
    circle_time = 2 * math.pi * radius / speed							# Calculate the time needed to complete a circle based on speed and radius.

    start_time = node.get_clock().now().to_msg()
    stop_turtle = False										# Initialize a flag to control when to stop the turtle.
    node.get_logger().info('Drawing circle_2...')
    while not stop_turtle:
        elapsed_time = node.get_clock().now().to_msg().sec - start_time.sec
        if elapsed_time < circle_time:
            publisher.publish(msg)								# Publish the Twist message to control the turtle's movement. 
        else:
            zero_msg = Twist()									# Create a Twist message to stop the turtle.
            publisher.publish(zero_msg)
            stop_turtle = True									# Set the flag to stop the turtle, indicating the circle is complete.
        

def main():
    '''
    Main function to spawn turtles and draw circles.

    Arguments:
    None

    Returns:
    None
    '''
    global first_turtle_final_pose								# Access the global variable to store the final pose of the first turtle.
    rclpy.init()
    
    node = rclpy.create_node('spawn_turtle_node')
    client = node.create_client(Spawn, '/spawn')
    
    node.pose_sub = node.create_subscription(Pose, '/turtle1/pose',pose_callback, 10)		# Create a subscription to listen for pose messages from the first turtle.

    while not client.wait_for_service(timeout_sec=1.0):
        print('Service not available, waiting...')

    turtle_name = 'turtle1'									# Specify the name of the first turtle.
    speed = 0.5											# the speed for first turtle
    radius = 1.5										# the radius for first circle
    circle_1(turtle_name, node, speed, radius)							# Call the function to draw a circle with the first turtle.

    while first_turtle_final_pose is None:
        rclpy.spin_once(node)

    turtle1_end_pose = first_turtle_final_pose							# Store the final pose of the first turtle.

    x_position = turtle1_end_pose.x								# Get the x-coordinate of the final position of the first turtle.
    y_position = turtle1_end_pose.y								# Get the y-coordinate of the final position of the first turtle.

    turtle_name = 'turtle2'									# Specify the name of the second turtle.
    theta_angle = 0.0										# Specify the initial orientation angle for the second turtle.
    future = spawn_turtle(node, client, turtle_name, x_position, y_position, theta_angle)	# Call the function to spawn the second turtle.
    node.get_logger().info('Spawned turtle_2...')
    rclpy.spin_until_future_complete(node, future)

    speed = 0.5											# the speed for second turtle
    radius = 2.0										# the radius for second circle
    circle_2(turtle_name, node, speed, radius)							# Call the function to draw a circle with the second turtle.
    rclpy.spin_once(node)
    rclpy.shutdown()

# Function Name:    main (built in)
#        Inputs:    None
#       Outputs:    None
#       Purpose:    Call the main function to execute directly.

if __name__ == '__main__':
    main()
