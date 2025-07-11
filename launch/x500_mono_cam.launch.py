#!/usr/bin/env python3


__author__ = "Uluhan Cem Kaya"
__contact__ = "uluhancem.kaya@uta.edu"

import launch
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch.actions import ExecuteProcess
import os


def generate_launch_description():
    # package_dir = get_package_share_directory('px4_launch')
    # bash_script_path = os.path.join(package_dir, 'scripts', 'TerminatorScript.sh')
    return LaunchDescription([
        # ExecuteProcess(cmd=['bash', bash_script_path], output='screen'),
        Node(
            package='px4_launch',
            namespace='px4_launch',
            executable='x500_mono_cam',
            name='x500_mono_cam',
            prefix='gnome-terminal --'
        ) 

        
    ])
