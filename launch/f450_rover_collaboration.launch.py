#!/usr/bin/env python3


__author__ = "Uluhan Cem Kaya"
__contact__ = "uluhancem.kaya@uta.edu"

from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():
    package_dir = get_package_share_directory('px4_launch')
    # bash_script_path = os.path.join(package_dir, 'scripts', 'TerminatorScript.sh')
    return LaunchDescription([
        # ExecuteProcess(cmd=['bash', bash_script_path], output='screen'),
        Node(
            package='px4_launch',
            namespace='px4_launch',
            executable='f450_rover_collaboration',
            name='f450_rover_collaboration',
            prefix='gnome-terminal --'
        )
    ])
