# Overview - Lambda Docs

Source: https://lambda.ai/blog/getting-started-with-lambda-cloud-gpu-instances

Skip to content

# Overview#

On-Demand Cloud (ODC) provides on-demand access to Linux-based, GPU-backed
virtual machine instances.

## Instance types#

ODC offers a variety of predefined instance types to support different workload
requirements. Available GPUs include the state-of-the-art NVIDIA HGX B200 GPU,
NVIDIA GH200 Grace Hopper Superchip, and NVIDIA H100 Tensor Core GPU, as well
as several earlier models. Each instance you create is tied to a specific
geographical region. For a list of available regions, see the
Regions section below.

Select instance types are backed by GPUs that feature NVIDIA SXM. SXM offers
improved bandwidth between the NVIDIA GPUs in a single physical server.

Warning

Lambda prohibits cryptocurrency mining on ODC instances.

As of December 2025, ODC offers the following instance types:

 | GPU
 | Number of GPUs
 | VRAM per GPU
 | vCPU cores
 | RAM
 | Root volume size

 | B200
 | 8
 | 180 GB
 | 208
 | 2900 GiB
 | 22 TiB

 | 
 | 4
 | 180 GB
 | 104
 | 1440 GiB
 | 11 TiB

 | 
 | 2
 | 180 GB
 | 52
 | 720 GiB
 | 5.5 TiB

 | 
 | 1
 | 180 GB
 | 26
 | 360 GiB
 | 2.75 TiB

 | GH2001
 | 1
 | 96 GB
 | 64
 | 432 GiB
 | 4 TiB

 | H100 SXM
 | 8
 | 80 GB
 | 208
 | 1800 GiB
 | 22 TiB

 | 
 | 4
 | 80 GB
 | 104
 | 900 GiB
 | 11 TiB

 | 
 | 2
 | 80 GB
 | 52
 | 450 GiB
 | 5.5 TiB

 | 
 | 1
 | 80 GB
 | 26
 | 225 GiB
 | 2.75 TiB

 | H100 PCIe
 | 1
 | 80 GB
 | 26
 | 225 GiB
 | 1 TiB

 | A100 SXM
 | 8
 | 80 GB
 | 240
 | 1800 GiB
 | 19.5 TiB

 | 
 | 8
 | 40 GB
 | 124
 | 1800 GiB
 | 5.8 TiB

 | 
 | 1
 | 40 GB
 | 30
 | 220 GiB
 | 512 GiB

 | A100 PCIe
 | 4
 | 40 GB
 | 120
 | 900 GiB
 | 1 TiB

 | 
 | 2
 | 40 GB
 | 60
 | 450 GiB
 | 1 TiB

 | 
 | 1
 | 40 GB
 | 30
 | 225 GiB
 | 512 GiB

 | A10
 | 1
 | 24 GB
 | 30
 | 226 GiB
 | 1.3 TiB

 | A6000
 | 4
 | 48 GB
 | 56
 | 400 GiB
 | 1 TiB

 | 
 | 2
 | 48 GB
 | 28
 | 200 GiB
 | 1 TiB

 | 
 | 1
 | 48 GB
 | 14
 | 100 GiB
 | 512 GiB

 | Tesla V100
 | 8
 | 16 GB
 | 88
 | 448 GiB
 | 5.8 TiB

 | RTX 6000
 | 1
 | 24 GB
 | 14
 | 46 GiB
 | 512 GiB

## Base images#

### Default image#

By default, each ODC instance runs Ubuntu 22.04 LTS. Lambda also preinstalls
Lambda Stack, a standard set of AI/ML-related drivers, tools, and
frameworks, on the instance:

- NVIDIA tools, libraries, and drivers: CUDA, cuDNN, NCCL, NVIDIA container
 toolkit, NVIDIA driver

- Deep learning frameworks and libraries: TensorFlow, torchvision, Keras,
 PyTorch®, JAX, Triton

- Dev tools: Git, Vim, Emacs, Valgrind, tmux, screen, htop, build-essential

For more information on Lambda Stack, see
Lambda Stack.

In addition, each ODC instance provides a JupyterLab installation for creating
and managing Jupyter notebooks. You can access your instance's JupyterLab by
visiting the
Instances page
in the Lambda Cloud console and clicking Launch in your instance's row.

Note

JupyterLab
can take a few minutes after an instance launches to become accessible.

### Alternative images#

If you launch your instance using the Lambda Cloud API, you can choose to use
an alternative base image instead. Available image types include:

- Lambda Stack: The default image used on most ODC instances.

- Includes: NVIDIA driver, CUDA toolkit, OFED, cuDNN, NCCL, Lambda Stack
 Python packages (PyTorch, TensorFlow, JAX), Docker, JupyterLab

- Use if: You want something that "just works" and don't need deep
 configurability.

- Lambda Stack Legacy: The default image on V100-backed ODC instances.

- Includes: NVIDIA driver (closed-source), CUDA toolkit, OFED, cuDNN,
 NCCL, Lambda Stack Python packages (PyTorch, TensorFlow, JAX), Docker,
 JupyterLab

- Use if: You're running an instance that requires NVIDIA's legacy
 closed-source driver stack, such as a V100 instance.

- GPU Base: An image based on Ubuntu Server that includes a minimal set of
 key AI/ML tools and drivers.

- Includes: NVIDIA driver, CUDA toolkit, OFED, cuDNN, NCCL, Docker

- Use if: You want a minimal working setup with a high degree of control
 over your Python environment.

- Ubuntu Server: A standard, unmodified Ubuntu Server image.

- Includes: No additional packages.

- Use if: You're an expert user who prefers maximum customizability, or
 you have unique tool or driver requirements.

The table below lists the available versions for each of the above image types,
the architectures each version supports, and the default Python version each
includes.

 | Image name
 | Image family
 | Architectures supported
 | Python version

 | Lambda Stack 24.04
 | lambda-stack-24-04
 | x86-64, arm64
 | 3.12

 | Lambda Stack 22.04
 | lambda-stack-22-04
 | x86-64, arm64
 | 3.10

 | Lambda Stack Legacy 22.04
 | lambda-stack-legacy-22-04
 | x86-64
 | 3.10

 | GPU Base 24.04
 | gpu-base-24-04
 | x86-64
 | 3.12

 | GPU Base 22.04
 | gpu-base-22-04
 | x86-64
 | 3.10

 | Ubuntu Server 24.04
 | ubuntu-24-04
 | x86-64
 | 3.12

 | Ubuntu Server 22.04
 | ubuntu-22-04
 | x86-64
 | 3.10

Note

As of December 2025, running sudo apt full-upgrade or sudo apt
dist-upgrade on the Lambda Stack 24.04 or GPU Base 24.04 base images
produces an error that prevents the upgrade from completing successfully. For
instructions on how to avoid the error, see
Troubleshooting > apt full-upgrade fails on Lambda Stack 24.04 and GPU Base 24.04 images.

## Storage#

### Root volume#

Each new instance comes with a root volume of a predefined size. The specific
volume size depends on which instance type you choose. To see which volume sizes
are associated with each instance type, check out the instance type table above.

### Filesystems#

When you create a new instance, you're prompted to attach a filesystem. A
filesystem is a unit of networked persistent storage you can connect to your
instance. Filesystems are typically several orders of magnitude larger than your
root volume, and are an ideal place to store both your instance state and your
large datasets.

To use a filesystem with your instance, you must attach it during the instance
creation process. The filesystem must also reside in the same region and
workspace as your instance.

For more information about filesystems, see Filesystems.

#### Mount point#

When you mount a filesystem to your instance, the filesystem is available at:

/lambda/nfs/<FILESYSTEM_NAME>

By default, the filesystem is symlinked in the ubuntu user's home directory,
using the filesystem's name. You can safely remove the symlink if it's not
needed.

#### Billing#

Filesystems are billed per GB used per month, in increments of one hour. If you
delete an instance but not its associated filesystem, you'll continue to be
billed for the filesystem. For more details on filesystem pricing, see
Filesystems.

#### Size limits#

ODC filesystem size limits vary by region. In general, filesystems have a
capacity of 8 EB (8,000,000 TB), and you can have a total of 24 filesystems. In
the Texas, USA (us-south-1) region, filesystem size is limited to 10 TB.

## Network#

### Connection options#

You connect to your instance through a standard SSH connection. For information
on creating and managing SSH keys, see Lambda Cloud console > Add, generate,
and delete SSH keys
or the
SSH keys
section of the Lambda Cloud API browser.

### Firewall defaults#

You can define inbound TCP and UDP firewall rules on the Firewall
page in the
Lambda Cloud console. By default, only port 22 (SSH) is open.

ODC allows ICMP traffic by default, as many network diagnostic tools rely on
ICMP to determine where connectivity issues are occurring. If you'd prefer to
restrict ICMP traffic, you can do so on the Firewall page.

### Regions#

Lambda resources are hosted in multiple locations worldwide. Not every instance
type will be available in every region.

 | Region
 | Physical location

 | asia-northeast-1
 | Tokyo, Japan

 | asia-northeast-2
 | Osaka, Japan

 | asia-south-1
 | India

 | europe-central-1
 | Germany

 | me-west-1
 | Israel

 | us-east-1
 | Virginia, USA

 | us-east-2
 | Washington DC, USA

 | us-midwest-1
 | Illinois, USA

 | us-south-1
 | Texas, USA

 | us-south-2
 | North Texas, USA

 | us-south-3
 | Central Texas, USA

 | us-west-1
 | California, USA

 | us-west-2
 | Arizona, USA

 | us-west-3
 | Utah, USA

## Instance management#

### Lambda Cloud console#

In addition to the firewall settings mentioned earlier, you can manage your
instances, filesystems, SSH keys, API keys, and more through the Lambda Cloud
console. For more information, see Lambda Cloud console.

### Cloud API#

You can perform administrative tasks such as creating, restarting, listing, and
terminating your instances through the Lambda Cloud API. For more details, visit
the
Lambda Cloud API browser.

## Next steps#

- Visit the Lambda Cloud portal

- Explore the Lambda Cloud API

- 

The NVIDIA GH200 Grace Hopper Superchip features an onboard ARM CPU.
Verify that your intended workloads run on ARM before choosing this instance
type. ↩

 Back to top
