#!/usr/bin/env python3


__author__ = "Uluhan Cem Kaya"
__contact__ = "uluhancem.kaya@uta.edu"

import launch
from launch import LaunchDescription
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch.actions import DeclareLaunchArgument
from launch.actions import ExecuteProcess
import os

namePackage = 'px4_launch'

bridge_params = PathJoinSubstitution([
    FindPackageShare(namePackage),
    'config',
    'rover_bridge_parameters.yaml',
])

def generate_launch_description():
    # package_dir = get_package_share_directory('px4_launch')
    # bash_script_path = os.path.join(package_dir, 'scripts', 'TerminatorScript.sh')
    return LaunchDescription([
        # ExecuteProcess(cmd=['bash', bash_script_path], output='screen'),
        Node(
            package='px4_launch',
            namespace='px4_launch',
            executable='asl_rover',
            name='asl_rover',
            prefix='gnome-terminal --'
        ),

        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            parameters=[{'config_file': bridge_params}],
            output='screen',
        ),

        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            arguments=[
                '0.0', '0', '0.0', '0', '3.14159', '0',
                'map', 'asl_rover_0/rplidar_a2/link/gpu_lidar'
            ],
            output='screen'
        )

        
    ])
