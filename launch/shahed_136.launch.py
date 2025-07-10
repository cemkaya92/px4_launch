#!/usr/bin/env python3


__author__ = "Cem Kaya"
__contact__ = "cem@galaxyuas.com"

import launch
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch.actions import ExecuteProcess
import os


def generate_launch_description():
    # bash_script_path = os.path.join(package_dir, 'scripts', 'TerminatorScript.sh')
    return LaunchDescription([
        # ExecuteProcess(cmd=['bash', bash_script_path], output='screen'),
        Node(
            package='px4_launch',
            namespace='px4_launch',
            executable='shahed_136_default',
            name='shahed_136_default',
            prefix='gnome-terminal --'
        ),

        DeclareLaunchArgument(
            'airdata_listener_topic',
            default_value='/shahed_136_0/gazebo/sensor/adc10_data',
            description='ROS topic that airspeed sensor serial data is being published to'
        ),
        
        DeclareLaunchArgument(
            'airdata_px4_advertiser_topic',
            default_value='/fmu/in/adc10_data',
            description='ROS topic that airdata is advertised to PX4 uORB message'
        ),

        Node(
            package='px4_ros_com',
            executable='airdata_advertiser',
            output='screen',
            shell=True,
            name='airdata_advertiser_node',
            prefix='gnome-terminal --',
            parameters=[{'airdata_listener_topic': LaunchConfiguration('airdata_listener_topic')},
                        {'airdata_px4_advertiser_topic': LaunchConfiguration('airdata_px4_advertiser_topic')}]
        )

    ])
