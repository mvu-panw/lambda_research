# Set lower gpu power limits - Lambda Docs

Source: https://docs.lambda.ai/hardware/servers/set-lower-gpu-power-limits/

Skip to content

Notice

Lambda sunset its consumer hardware business in Summer 2025. This
documentation is no longer maintained and is provided for reference only.

# Set lower power limits (TDPs) for NVIDIA GPUs#

You can set lower power limits (TDPs) for your NVIDIA GPUs using nvidia-smi
and a simple script. You can configure the script to run automatically at boot
using a systemd service.

Lowering power limits can reduce power usage and heat output, which is helpful
for thermally constrained systems or energy-aware environments.

- 

Check your GPU's minimum power limit. Run:

nvidia-smi -q -d POWER

Look for the Min Power Limit line. For example:

==============NVSMI LOG==============

Timestamp : Thu Jun 26 21:48:46 2025
Driver Version : 570.153.02
CUDA Version : 12.8

Attached GPUs : 1
GPU 00000000:01:00.0
 GPU Power Readings
 Average Power Draw : 43.91 W
 Instantaneous Power Draw : 43.19 W
 Current Power Limit : 480.00 W
 Requested Power Limit : 480.00 W
 Default Power Limit : 480.00 W
 Min Power Limit : 150.00 W
 Max Power Limit : 530.00 W

The lowest value you can safely configure in this case is 150 W.

- 

Create the script. Replace 150 below with your desired power limit:

sudo tee /usr/local/bin/set-nvidia-tdp.sh > /dev/null <<'EOF'
#!/bin/bash

# Set GPU power limit in watts
POWER_LIMIT=150

# Wait for nvidia-smi daemon to initialize
sleep 10

# Apply the power limit to all GPUs
for i in $(/usr/bin/nvidia-smi --query-gpu=index --format=csv,noheader); do
 echo "Setting NVIDIA GPU $i to ${POWER_LIMIT}W TDP."
 /usr/bin/nvidia-smi -i "$i" -pl "$POWER_LIMIT"
done
EOF

sudo chmod +x /usr/local/bin/set-nvidia-tdp.sh

- 

Create and enable the systemd service.

sudo tee /etc/systemd/system/nvidia-tdp.service > /dev/null <<EOF
[Unit]
Description=Set NVIDIA GPU Power Limit at Boot
Requires=nvidia-persistenced.service
After=nvidia-persistenced.service

[Service]
Type=oneshot
ExecStart=/usr/local/bin/set-nvidia-tdp.sh

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable nvidia-tdp.service

To run the script immediately:

sudo systemctl start nvidia-tdp.service

- 

Verify the result. Check that the service ran successfully:

sudo systemctl status nvidia-tdp.service

You should see output similar to:

Jun 27 16:12:12 lambda-v1 set-nvidia-tdp.sh[549231]: Setting NVIDIA GPU 0 to 150W TDP.
Jun 27 16:12:12 lambda-v1 set-nvidia-tdp.sh[549255]: Power limit for GPU 00000000:01:00.0 was set to 150.00 W from 480.00 W.
Jun 27 16:12:12 lambda-v1 set-nvidia-tdp.sh[549255]: All done.
Jun 27 16:12:12 lambda-v1 systemd[1]: nvidia-tdp.service: Deactivated successfully.
Jun 27 16:12:12 lambda-v1 systemd[1]: Finished Set NVIDIA GPU Power Limit at Boot.

To view logs:

sudo journalctl -u nvidia-tdp.service

To confirm the new power limit:

nvidia-smi --query-gpu=power.limit --format=csv

## Next steps#

Learn more about Lambda's servers:

- NVIDIA DGX

- Hyperplane

- Scalar

Workstations and desktops:

- Vector Pro

- Vector

- Vector One

 Back to top
