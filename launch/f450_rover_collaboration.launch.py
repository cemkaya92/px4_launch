#!/usr/bin/env python3


__author__ = "Uluhan Cem Kaya"
__contact__ = "uluhancem.kaya@uta.edu"

from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import Command, PathJoinSubstitution
from ament_index_python.packages import get_package_share_directory
import os


namePackage = 'px4_launch'

bridge_params = PathJoinSubstitution([
    FindPackageShare(namePackage),
    'config',
    'uav_rover_collaboration_bridge_parameters.yaml'
])


def generate_launch_description():
    package_dir = get_package_share_directory(namePackage)
    # bash_script_path = os.path.join(package_dir, 'scripts', 'TerminatorScript.sh')
    return LaunchDescription([
        # ExecuteProcess(cmd=['bash', bash_script_path], output='screen'),
        Node(
            package='px4_launch',
            namespace='px4_launch',
            executable='f450_rover_collaboration',
            name='f450_rover_collaboration',
            prefix='gnome-terminal --'
        ),

        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            arguments=[
                '--ros-args',
                '-p',
                f'config_file:={bridge_params}',
            ],
            output='screen',
        ),

        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            name='gz_camera_bridge',
            output='screen',
            arguments=[
                # Bridge the image topic
                '/world/default/model/f450_mono_cam_0/link/camera_link/sensor/imager/image'
                '@sensor_msgs/msg/Image@gz.msgs.Image',
                
                # Bridge the camera_info topic
                '/world/default/model/f450_mono_cam_0/link/camera_link/sensor/imager/camera_info'
                '@sensor_msgs/msg/CameraInfo@gz.msgs.CameraInfo'
            ]
        )
    ])
