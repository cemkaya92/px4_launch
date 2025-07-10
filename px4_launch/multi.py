#!/usr/bin/env python3

# Import the subprocess and time modules
import subprocess
import time

# Base directory for PX4
px4_base_dir = '~/mypx4/PX4-Autopilot'

# Lists for different parameters
instance_ids = [1, 2]  # Instance IDs
autostart_ids = [4001, 4001]  # Autostart IDs for different models
gz_models = ['x500', 'x500']  # GZ models
sim_models = ['x500', 'x500']  # Simulation models
model_poses = ["0,0,0.5,0,0,0", "10,0,0.5,0,0,0"]  # Model poses (x,y,z,r,p,y)

# Run the Micro XRCE-DDS Agent (only once, not per instance)
subprocess.run(["gnome-terminal", "--", "bash", "-c", "MicroXRCEAgent udp4 -p 8888; exec bash"])

# Give some time for the agent to start
time.sleep(2)


# Launch each PX4 instance
for idx, instance_id in enumerate(instance_ids):
    # Construct the command
    command = (
        f"cd {px4_base_dir} && "
        f"PX4_SYS_AUTOSTART={autostart_ids[idx]} "
        f"PX4_GZ_MODEL={gz_models[idx]} "
        f"PX4_GZ_MODEL_POSE=\"{model_poses[idx]}\" "
        f"PX4_SIM_MODEL={sim_models[idx]} "
        f"./build/px4_sitl_default/bin/px4 -i {instance_id}"
    )

    # Launch in a new terminal tab
    subprocess.Popen(["gnome-terminal", "--tab", "--", "bash", "-c", command + "; exec bash"])

    # Short pause to prevent simultaneous launch issues
    time.sleep(3)
    

    

