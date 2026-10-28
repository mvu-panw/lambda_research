# Managing your system environment - Lambda Docs

Source: https://docs.lambda.ai/public-cloud/on-demand/managing-system-environment/

Skip to content

# Managing your system environment#

This document provides general guidance for managing your On-Demand Cloud (ODC)
instance's system environment.

## Isolating environments on your instance#

You can use virtual environments to isolate different jobs or experiments from
each other on the same machine. This section details a few ways you can create
virtual environments on your ODC instance.

Tip

Because they centralize large parts of your working environment in a
small number of locations, virtual environments can also help simplify
the process of backing up and restoring your work.

### Isolating your environment using a Docker image#

Your ODC instance has Docker and the NVIDIA Container Toolkit
installed by default. To create and run a Docker container on your instance:

- In the Lambda Cloud console, navigate to the
 Instances page.

- In the row for your instance, in the Cloud IDE column, click
 Launch to launch JupyterLab.

- In JupyterLab, in the Launcher tab, click Terminal to open a new
 terminal.

- 

In the JupyterLab terminal, add your user to the docker group:

sudo adduser "$(id -un)" docker

- 

Start a new shell session in your terminal to pick up the current state of
 your user groups:

exec bash

- 

Locate the Docker image for the container you want to create. Replace
 <IMAGE> with the URL to the image for the container you want to create,
 and replace <COMMAND> with the command you want to run in the container.

docker run --gpus all -it <IMAGE> <COMMAND>

### Isolating your Python environment with venv#

In standard Python, you can create an isolated virtual Python environment by
using the built-in venv module. To create and activate a Python virtual
environment using venv:

- Navigate to the directory in which you'd like to store your virtual
 environment.

- 

Create the environment, adding the --system-site-packages flag to pull
 in your instance's preinstalled Lambda Stack modules. Replace <NAME> with
 the name you want to give your virtual environment.

python -m venv --system-site-packages <NAME>

- 

Activate your environment. Replace <NAME> with the name you defined in
 the previous step:

source <NAME>/bin/activate

Note

This command assumes you're using a POSIX-compatible system, such as
Linux, macOS, and WSL2. For details on activating your virtual
environment in Windows PowerShell or other non-POSIX environments, see
venv
in the Python docs.

You can exit your virtual environment by typing deactivate. To return to the
environment, run step 3 from the directory you selected in step 1.

### Isolating your environment using conda#

To install and configure conda:

- 

Download the latest version of Miniconda3:

curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

- 

Run the Miniconda3 installer. Use the following settings as you work
 through the installer prompts:

- Install Miniconda3 in the default location.

- Allow the installer to initialize Miniconda3.

sh Miniconda3-latest-Linux-x86_64.sh

- 

After the installer has finished, update your terminal environment with
 the changes the installer made to your .bashrc file:

source ~/.bashrc

- 

Disable automatic activation of the conda base environment. This step
 ensures that your conda installation remains compatible with the Python
 venv module.

conda config --set auto_activate_base false

Now that you've installed and configured conda, you can create and activate a
new conda environment:

- 

Create a conda virtual environment using Miniconda3. Replace <NAME>
 with the name you want to give your virtual environment, and replace
 <PACKAGES> with the list of packages you want to install in your virtual
 environment:

conda create -n <NAME> <PACKAGES>

Note

You can set additional options for your environment, such as your
target training framework, while creating the environment. For example, the
following command creates a PyTorchⓇ environment with CUDA 11.8:

conda create -c pytorch -c nvidia -n pytorch+cuda_11-8 pytorch torchvision torchaudio pytorch-cuda=11.8

For more information, see
conda create
in the conda documentation.

- 

Activate your environment. Replace with the name you chose in the
 previous step.

conda activate <NAME>

- 

Test that your environment is working as expected:

python -c 'import torch ; print("\nIs available: ", torch.cuda.is_available()) ; print("Pytorch CUDA Compiled version: ", torch._C._cuda_getCompiledVersion()) ; print("Pytorch version: ", torch.__version__) ; print("pytorch file: ", torch.__file__) ; num_of_gpus = torch.cuda.device_count(); print("Number of GPUs: ",num_of_gpus)'

You should see output similar to the following:

Is available: True
Pytorch CUDA Compiled version: 11080
Pytorch version: 2.0.1
pytorch file: /home/ubuntu/miniconda3/envs/pytorch+cuda_11-8/lib/python3.11/site-packages/torch/__init__.py
Number of GPUs: 1

## Creating and managing users#

You can manage access and permissions on your instance by creating user
accounts. User accounts allow your team members to manage their own files,
datasets, and programs, as well as their own Python virtual environments,
conda virtual environments, and Docker containers.

To add new user accounts:

- Establish an SSH connection to your instance or open a terminal in
 your instance's JupyterLab.

- 

Add a new user. Replace <USERNAME> with the name the user will use to
 log into the system. This name will also be the name of the user's
 home directory—for example, /home/<USERNAME>.

sudo adduser <USERNAME>

- 

Set a password.

- Supply the full name of your user.

- Answer any additional prompts, or press Enter to skip them.

- 

If you want to give the user administrator-level permissions, add them to
 the sudo group. Replace <USERNAME> with your user's username:

Warning

Be conservative about granting adminstrator-level permissions.
sudo users can create, modify, and delete system files and other
users' files, as well as change other users' settings.

sudo usermod -aG sudo <USERNAME>

You can verify that the user was added by listing the users in the system:

cat /etc/passwd

## Updating your operating system#

Don't try to upgrade to the latest Ubuntu release. Doing so will
break JupyterLab, which has been configured and tested for the preinstalled
version of Python.

## Preventing your instance from suspending or sleeping#

To prevent your system from going to sleep or suspending, establish an SSH
connection to your instance and run the following command:

sudo systemctl mask hibernate.target hybrid-sleep.target \
suspend-then-hibernate.target sleep.target suspend.target

## Emptying .Trash-* directories#

Applications that follow the Freedesktop.org
Trash Specification,
such as JupyterLab, create hidden .Trash-* directories on your mounted
filesystems. These soft-deleted files remain on your filesystem, taking up
billable storage, until you permanently delete them.

You can delete the contents of these .Trash-* directories by running the
following command. Replace <PATH-TO-FILESYSTEM> with the actual path to your
filesystem mount point:

rm -rf /<PATH-TO-FILESYSTEM>/.Trash-*/

### Configuring JuypterLab to hard-delete files#

JupyterLab places deleted files in a .Trash-* directory by default. To
configure JupyterLab to immediately delete files instead:

- Connect to your instance and open /home/ubuntu/.jupyter/jupyter_config.py
for editing.

- 

Add the following line and then save the file.

c.FileContentsManager.delete_to_trash = False

- 

Restart the JupyterLab service:

sudo systemctl restart lambda-jupyter

## Next steps#

- New to ODC? Check out the ODC Overview.

- For information on managing your ODC virtual machine instances,
 see Creating and managing instances.

 Back to top
