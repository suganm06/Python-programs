#!/usr/bin/env python3

########################################################################################################################
########################################## eYRC 23-24 Hologlyph Bots Task 1B ###########################################
# Team ID:      	1017
# Team Leader Name: 	Sugavaneswar M
# Team Members Name: 	Sankaran S, Thiruvengadam K, Aathish M
# College:      	KCG College of Technology
########################################################################################################################

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import time
import math
from tf_transformations import euler_from_quaternion
from my_robot_interfaces.srv import NextGoal

class HBTask1BController(Node):

    def __init__(self):
        super().__init__('hb_task1b_controller')     
        self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)						# Initialize Publisher for cmd_vel
        
        self.vel = Twist()											# Declare a Twist message
        
        self.x_robot_pose = 0.0 										# Initialize attributes for robot pose
        self.y_robot_pose = 0.0
        self.theta_robot_pose = 0.0
        
        self.Kp_x_velocity = 1.25										# P controller gains
        self.Kp_y_velocity = 1.25
        self.Kp_theta_velocity = 1.0

        self.goal_flag = 0											# Initialize variables for flag and index
        self.goal_index = 0
        
        self.goal_service_client = self.create_client(NextGoal, 'next_goal')                                    # Initialize client for the "next_goal" service
        while not self.goal_service_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting again...')
        self.goal_service_request = NextGoal.Request()

        self.odom_subscription = self.create_subscription(							# Subscribe to the odometry topic to get robot pose updates
            Odometry,
            'odom',
            self.odom_callback,
            10
        )

    def send_goal_request(self, goal_index):
        self.goal_service_request.request_goal = goal_index
        self.goal_service_future = self.goal_service_client.call_async(self.goal_service_request)

    def control_loop(self):
        while rclpy.ok():
            if self.goal_service_future.done():
                try:
                    goal_response = self.goal_service_future.result()
                except Exception as e:
                    self.get_logger().info(f'Service call failed: {e}')
                else:
                    self.x_goal = goal_response.x_goal
                    self.y_goal = goal_response.y_goal
                    self.theta_goal = goal_response.theta_goal
                    self.goal_flag = goal_response.end_of_list

                    error_x = self.x_goal - self.x_robot_pose							# Calculate errors in global frame
                    error_y = self.y_goal - self.y_robot_pose
                    error_theta = self.theta_goal - self.theta_robot_pose

                    self.vel.linear.x = self.Kp_x_velocity * error_x						# Implement P controller to compute velocities
                    self.vel.linear.y = self.Kp_y_velocity * error_y
                    self.vel.angular.z = self.Kp_theta_velocity * error_theta

                    self.publisher.publish(self.vel)								# Publish the control commands

                    self.goal_index += 1									# Update index and reset if needed
                    if self.goal_flag == 1:
                        self.goal_index = 0
          
                    self.send_goal_request(self.goal_index)							# Send the next request

            rclpy.spin_once(self)

    def odom_callback(self, msg):										# Update robot pose based on odometry data
        self.x_robot_pose = msg.pose.pose.position.x
        self.y_robot_pose = msg.pose.pose.position.y
        orientation = msg.pose.pose.orientation
        (_, _, self.theta_robot_pose) = euler_from_quaternion(
            [orientation.x, orientation.y, orientation.z, orientation.w]
        )

def main(args=None):
    rclpy.init(args=args)

    x_goals_list = [10, -9, -1, -20, 0]										# Define the goals using the provided x, y, and theta values
    y_goals_list = [20, 1, 9, -10, 0]
    theta_goals_list = [0, math.pi / 2, math.pi, -math.pi / 2, 0]

    goals_list = [(x_goals_list[i], y_goals_list[i], theta_goals_list[i]) for i in range(len(x_goals_list))]	# Create a list of goal tuples (x, y, theta)

    ebot_controller = HBTask1BController()									# Initialize the controller

    for goal_index, goal_coordinates in enumerate(goals_list):							# Send each goal to the controller
        ebot_controller.send_goal_request(goal_index)
        ebot_controller.x_goal = goal_coordinates[0]
        ebot_controller.y_goal = goal_coordinates[1]
        ebot_controller.theta_goal = goal_coordinates[2]

        while not ebot_controller.goal_flag:									# Control the robot to reach the current goal
            ebot_controller.control_loop()

    ebot_controller.destroy_node()										# Shutdown when all goals have been reached
    rclpy.shutdown()

if __name__ == '__main__':
    main()

