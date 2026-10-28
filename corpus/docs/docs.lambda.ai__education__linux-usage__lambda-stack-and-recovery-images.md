# Lambda Stack and recovery images - Lambda Docs

Source: https://docs.lambda.ai/education/linux-usage/lambda-stack-and-recovery-images/

Skip to content

# Lambda Stack and recovery images#

## Removing and reinstalling Lambda Stack#

To remove and reinstall Lambda Stack:

Uninstall (purge) the existing Lambda Stack by running:

sudo rm -f /etc/apt/sources.list.d/{graphics,nvidia,cuda}* && \
dpkg -l | \
awk '/cuda|lib(accinj64|cu(blas|dart|dnn|fft|inj|pti|rand|solver|sparse)|magma|nccl|npp|nv[^p])|nv(idia|ml)|tensor(flow|board)|torch/ { print $2 }' | \
sudo xargs -or apt -y remove --purge

Then, install the latest Lambda Stack by running:

wget -nv -O- https://lambda.ai/install-lambda-stack.sh | sh -

## Recovery images#

Note

See the Install Ubuntu desktop tutorial, specifically steps 3 and 4, to learn how to create and boot a USB stick (flash drive) using the below recovery images.

### Workstations#

Recovery ISO images for Vector
and Vector One can be
downloaded using the following links:

- Lambda Recovery (Focal) (based on Ubuntu 20.04 LTS focal)

- Lambda Recovery (Jammy) (based on Ubuntu 22.04 LTS jammy)

### Tensorbook#

The recovery ISO image for
Tensorbook can be
downloaded using the following link:

- Lambda Recovery for Tensorbook (Jammy) (based on Ubuntu 22.04 LTS jammy)

Note

This recovery image is for the Razer x Lambda Tensorbook only and won't work on older Tensorbook models.

Note

The recovery images contain software distributed under various licenses, including the Software License Agreement (SLA) for NVIDIA cuDNN. The licenses can be viewed in the recovery images at /usr/share/doc/*/copyright. By using the software contained in the recovery images, you agree to these licenses.

### Servers#

Recovery images aren't available for servers.

To reinstall Ubuntu and Lambda Stack on your Lambda server, download the Ubuntu
22.04 Server install image, then follow
Ubuntu's Server installation
instructions.

Install the latest Lambda Stack by logging into Ubuntu and running:

wget -nv -O- https://lambda.ai/install-lambda-stack.sh | I_AGREE_TO_THE_CUDNN_LICENSE=1 sh -

 Back to top
