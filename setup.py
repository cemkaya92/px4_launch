import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'px4_launch'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    install_requires=['setuptools'],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/ament_index/resource_index/packages',
            ['resource/' + 'visualize.rviz']),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*launch.[pxy][yma]*')),
        (os.path.join('share', package_name), glob('resource/*rviz'))
        # (os.path.join('share', package_name), ['scripts/TerminatorScript.sh'])
    ],
    zip_safe=True,
    maintainer='cem',
    maintainer_email='uluhancem.kaya@uta.edu',
    description='TODO: Package description',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'px4_launch = px4_launch.px4_launch:main',
            'visualizer = px4_launch.visualizer:main',
            'gc35_e4b = px4_launch.gc35_e4b:main',
            'gc50_e4b = px4_launch.gc50_e4b:main',
            'mooring_platform = px4_launch.mooring_platform:main',
            'shahed_136_default = px4_launch.shahed_136_default:main',
            'flying_wing_default = px4_launch.flying_wing_default:main',
            'rc_cessna_default = px4_launch.rc_cessna_default:main',
            'standard_vtol_default = px4_launch.standard_vtol_default:main',
            'multi = px4_launch.multi:main',
            'swarm_7_shahed = px4_launch.swarm_7_shahed:main',
            'swarm_3_shahed = px4_launch.swarm_3_shahed:main',
            'swarm_2_shahed = px4_launch.swarm_2_shahed:main',
            'x500 = px4_launch.x500:main',
            'x500_mono_cam = px4_launch.x500_mono_cam:main',
            'f450 = px4_launch.f450:main',
            'f450_x8 = px4_launch.f450_x8:main',
            'x35_munition = px4_launch.x35_munition:main',
            'drop_drone_default = px4_launch.drop_drone_default:main',
            'crazyflie = px4_launch.crazyflie:main',
            'asl_rover = px4_launch.asl_rover:main',
            'f450_rover_collaboration = px4_launch.f450_rover_collaboration:main'

        ],
    },
)
