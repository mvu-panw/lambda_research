# Troubleshooting - Lambda Docs

Source: https://docs.lambda.ai/public-cloud/on-demand/troubleshooting/

Skip to content

# Troubleshooting#

## apt full-upgrade fails on Lambda Stack 24.04 and GPU Base 24.04 images#

As of December 2025, running sudo apt full-upgrade or sudo apt dist-upgrade
on the Lambda Stack 24.04 or GPU Base 24.04 base images produces an error:

Error! Bad return status for module build on kernel: 6.14.0-1013-nvidia (x86_64)
Consult /var/lib/dkms/mlnx-ofed-kernel/24.10.OFED.24.10.3.2.5.1/build/make.log for more information.

To avoid this error:

- 

Update the DOCA repository entry to the latest version:

sudo sed -i 's/2.9.3/3.2.0/' /etc/apt/sources.list.d/doca.list

- 

Update your package lists:

sudo apt update

- 

Upgrade the DOCA OFED kernel utilities:

sudo apt install -y -o Dpkg::Options::="--force-confnew" mlnx-ofed-kernel-utils

Then, run sudo apt full-upgrade or sudo apt dist-upgrade. The command
should now produce the following expected error:

Errors were encountered while processing:
 linux-headers-6.14.0-1015-nvidia
 linux-headers-nvidia-hwe-24.04
 linux-nvidia-hwe-24.04

Run sudo apt full-upgrade or sudo apt dist-upgrade again to complete the
upgrade.

## Program doesn't find the NVIDIA cuDNN library#

The NVIDIA cuDNN license limits how cuDNN can be used on our
instances.

On our instances, cuDNN can only be used by the PyTorch® framework and
TensorFlow library installed as part of Lambda Stack.

Other software, including PyTorch and TensorFlow installed outside of Lambda
Stack, won't be able to find and use the cuDNN library installed on our
instances.

Tip

Software outside of Lambda Stack usually looks for the cuDNN library files
in /usr/lib/x86_64-linux-gnu. However, on our instances, the cuDNN library
files are in /usr/lib/python3/dist-packages/tensorflow.

Creating symbolic links, or "symlinks," for the cuDNN library files might
allow your program to find the cuDNN library on our instances.

Run the following command to create symlinks for the cuDNN library files:

for cudnn_so in /usr/lib/python3/dist-packages/tensorflow/libcudnn*; do
 sudo ln -s "$cudnn_so" /usr/lib/x86_64-linux-gnu/
done

## GH200#

### Unable to install PyTorch#

PyTorch doesn’t have an officially supported build for the ARM architecture, and so pip install torch doesn't work out of the box on GH200. To address this, Lambda has compiled PyTorch 2.4.1 for ARM and distributes it as part of Lambda Stack.

To access the version of PyTorch included with Lambda Stack, we recommend creating a virtual environment using the --system-site-packages option. This approach allows the virtual environment to have access to the system-wide installation of PyTorch. See Virtual environments and Docker containers > Creating a Python virtual environment for step by step details.

If you require a later version of pytorch (>2.4.1), you must compile the specific PyTorch version for ARM to run on GH200.

### AssertionError: Torch not compiling with CUDA enabled#

This error often occurs when a specific PyTorch version is pinned. For example, a requirements.txt file may contain torch==2.2.0, which conflicts with the PyTorch version (2.4.1) compiled for ARM on GH200.

As PyTorch is largely backwards compatible, changing torch==2.2.0 to torch>=2.2.0 can address this issue.

Note

There are situations where a specific PyTorch version is required, such as PyTorch extensions (which are version-specific). In such a case, you have to compile the required PyTorch version for ARM to run on GH200.

### Why Lambda's GH200 specifications differ from NVIDIA's#

Lambda GH200 specifications differ from NVIDIA (i.e. 64 CPU cores vs 72 GPU cores, 432 GiB DDR5 vs 480 GiB DDR5) because our GH200s are virtualized instances. The difference between the two is due to resources set aside for virtualization overhead.

### Operational tenancy of GH200 instances#

Lambda GH200s are single-tenant instances. However, networking and file storage are multi-tenant.

 Back to top
