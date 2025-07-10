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
            executable='drop_drone_default',
            name='drop_drone_default',
            prefix='gnome-terminal --'
        )

    ])
