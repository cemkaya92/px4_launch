#!/usr/bin/env python3

# Import the subprocess and time modules
import subprocess
import time

# Base directory for PX4
px4_base_dir = '~/mypx4/PX4-Autopilot'

# Lists for different parameters
autostart_id = 4102  # Autostart IDs for different models
gz_model = 'drop_drone'  # GZ models
sim_model = 'drop_drone'  # Simulation models
model_pose = "0,0,0.5,0,0,0"  # Model poses (x,y,z,r,p,y)
sim_world = 'default'  # Simulation world

# Run the Micro XRCE-DDS Agent (only once, not per instance)
subprocess.run(["gnome-terminal", "--", "bash", "-c", "MicroXRCEAgent udp4 -p 8888; exec bash"])

# Give some time for the agent to start
time.sleep(1)


# Launch PX4 instance
# Construct the command
command = (
    f"cd {px4_base_dir} && "
    f"PX4_SYS_AUTOSTART={autostart_id} "
    f"PX4_GZ_MODEL={gz_model} "
    f"PX4_GZ_MODEL_POSE=\"{model_pose}\" "
    f"PX4_SIM_MODEL={sim_model} "
    f"PX4_GZ_WORLD={sim_world} "
    f"./build/px4_sitl_default/bin/px4 "
)

# Launch in a new terminal tab
subprocess.Popen(["gnome-terminal", "--tab", "--", "bash", "-c", command + "; exec bash"])

# Short pause to prevent simultaneous launch issues
time.sleep(3)   

    

