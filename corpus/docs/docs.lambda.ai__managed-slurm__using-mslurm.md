# Using Managed Slurm - Lambda Docs

Source: https://docs.lambda.ai/managed-slurm/using-mslurm/

Skip to content

# Using Lambda's Managed Slurm#

This guide describes how to access your Managed Slurm (MSlurm) cluster and
perform common administrative tasks, such as managing users or running jobs.
For a general overview of MSlurm and how it compares to an unmanaged
Slurm deployment, see Slurm on Lambda Cloud.

## Accessing your cluster#

### Visit the Slurm console#

You can view details about the health of your MSlurm cluster, add user
accounts, manage and observe jobs, and more by visiting the Slurm console in
your web browser. For full details, see The Slurm console.

### Establish an SSH connection#

Your MSlurm cluster comes with a single user account: ubuntu. This account
is preconfigured with the SSH key you supplied when reserving the cluster and
functions as the cluster administrator user.

To access the MSlurm cluster as the ubuntu user, SSH into the login node.
Replace <LOGIN-NODE-IP> with the IP address of -login-001, available in the
Lambda Cloud console:

ssh ubuntu@<LOGIN-NODE-IP>

Other users access the MSlurm cluster in the same way, by using SSH to log into
the login node. Replace <USERNAME> with the appropriate username:

ssh <USERNAME>@<LOGIN-NODE-IP>

## Managing user accounts#

In an MSlurm cluster, user accounts and groups control both system access and
job submission permissions. LDAP provides consistent user and group management
across all nodes by acting as a centralized directory.

Like unmanaged Slurm installations, MSlurm doesn't maintain its own user
database. Instead, it relies on the underlying system's authentication and group
management.

Lambda provides two ways to manage user accounts: the Slurm console in your
browser, and the suser tool on the login node.

### Manage user accounts from the Slurm console#

The Cluster Users app in the Slurm console lists each
user account, as well as its status, associated Slurm accounts, and associated
SSH keys. You can add new user accounts by filling out a short form:

- Username: The account to create.

- SSH key (optional): Paste a public key, or import one directly from the
 user's GitHub account.

- Workspace email (optional): Link the user's console sign-in (SSO) to
 their cluster account.

- Slurm account (optional): Attach the user to a shared team account, or
 leave empty to give the user an account of their own.

Note

Only the username field is required. If you don't have the information
to fill in the other fields at hand, you can add the information later.

### Manage user accounts from your terminal#

This section describes how to use the suser command to perform basic user
management operations on your login node from your SSH terminal. To see the
full set of options available in susers, run suser --help.

#### Create a new user#

To create a new user using suser:

- 

SSH into the MSlurm login node using the ubuntu account. Replace
 <LOGIN-NODE-IP> with the IP address of the login node (-login-001):

ssh ubuntu@<LOGIN-NODE-IP>

- 

Create the user. Replace <USERNAME> with the desired username, and
 <SSH-KEY> with either the path to the user's SSH public key file or the
 public key string itself:

suser add <USERNAME> --key <SSH-KEY>

After the command completes, the message User <USERNAME> successfully added
will confirm the user was created.

#### Remove a user#

To remove a user using suser:

- 

SSH into the MSlurm login node using the ubuntu account. Replace
 <LOGIN-NODE-IP> with the IP address of the login node (-login-001):

ssh ubuntu@<LOGIN-NODE-IP>

- 

Remove the user. Replace <USERNAME> with the actual username:

suser remove <USERNAME>

After the command completes, the message User <USERNAME> successfully removed
will confirm the user was removed.

Note

suser remove does not delete the user's home directory.

## Running jobs on your cluster#

You can submit jobs to the MSlurm cluster by using the sbatch, srun, or
salloc command.

- 

sbatch is appropriate for jobs that don't require user interaction and can
 be scheduled to run when resources are available. It's commonly used for
 training and other long-running jobs. Since sbatch is non-interactive, it
 requires a job script to specify resource requirements and the commands to
 execute. For more information about using sbatch, see the
 sbatch man page in the official
 Slurm documentation.

- 

srun is appropriate for interactive jobs and quick execution of commands
 without writing a job script for sbatch. It's useful for debugging code,
 testing scripts, or running short tasks interactively on compute (GPU) nodes
 before submitting a batch job. For more information about using srun, see
 the srun man page in the official
 Slurm documentation.

- 

salloc is appropriate for requesting compute resources interactively, then
 launching a shell session where multiple commands can be executed manually.
 It's useful for development, testing, and running interactive applications on
 compute nodes before submitting a batch job. For more information about using
 salloc, see the salloc man page
 in the official Slurm documentation.

The MSlurm cluster supports Pyxis and Enroot, enabling srun to run containers,
including those based on Docker images, on compute nodes.

The following examples demonstrate how you might use sbatch, srun, or
salloc in context.

### Run batch jobs with sbatch#

#### Example 1: Run nvidia-smi -L on compute nodes#

This first example runs nvidia-smi -L on your compute nodes and displays its
output, as well as the hostnames of the compute nodes on which the command
was executed.

- Establish an SSH connection to your login node.

- 

Create a file named nvidia_smi_batch.sh containing the following:

#!/bin/bash
#SBATCH --nodes=2
#SBATCH --gpus=2
#SBATCH --ntasks=2
#SBATCH --ntasks-per-node=1
#SBATCH --output="sbatch_output_direct_%x_%j.out"
#SBATCH --error="sbatch_output_direct_%x_%j.err"
#SBATCH --time=00:01:00

echo "Job ID: $SLURM_JOB_ID"
echo "Running on nodes: $SLURM_NODELIST"
echo
srun --ntasks=$SLURM_NTASKS nvidia-smi -L

- 

Submit the job using sbatch:

sbatch nvidia_smi_batch.sh

This command submits the job and performs the following steps:

- 

Requests cluster resources:

- --nodes=2: Reserves 2 compute nodes.

- --gpus=2: Requests a total of 2 GPUs across all nodes.

- --ntasks=2: Runs 2 parallel tasks in total.

- --ntasks-per-node=1: Assigns 1 task per node (2 tasks across 2 nodes).

- 

Configures job output:

- --output="sbatch_output_direct_%x_%j.out": Saves standard output to a
 file named with the job name (%x) and job ID (%j).

- --error="sbatch_output_direct_%x_%j.err": Saves standard error to a
 similar file.

- 

Sets a job time limit:

- --time=00:01:00: Limits the job runtime to 1 minute.

- 

Prints the job information:

- echo "Job ID: $SLURM_JOB_ID": Displays the assigned job ID.

- echo "Running on nodes: $SLURM_NODELIST": Displays the list of allocated
 nodes.

- 

Runs nvidia-smi -L:

- srun --ntasks=$SLURM_NTASKS nvidia-smi -L: Runs nvidia-smi -L on all
 tasks to list visible GPUs.

After the job completes, two files are created:

- 

sbatch_output_direct_<JOBNAME>_<JOBID>.out

Contains the job ID, allocated nodes, and the output of nvidia-smi -L from
each task.

- 

sbatch_output_direct_<JOBNAME>_<JOBID>.err

Contains any error messages. This file is usually empty unless something
went wrong.

#### Example 2: Evaluate a large language model (LLM)#

This second example runs a Slurm batch job that evaluates how well an LLM
solves basic multiplication problems. As with the first example, this
example also prints the hostnames of the compute nodes on which the job
was executed.

- Establish an SSH connection to your login node.

- 

Download the Python script and the Slurm batch script:

curl -sSLO https://docs.lambda.ai/assets/code/eval_multiplication.py
curl -sSLO https://docs.lambda.ai/assets/code/run_eval.sh

Both scripts are annotated with comments explaining their structure and
purpose.

- 

Submit the job using a Hugging Face model ID:

sbatch run_eval.sh deepseek-ai/DeepSeek-R1-Distill-Llama-70B

The model ID can be replaced with any other compatible model.

- 

To follow the job's progress in real time:

tail -F eval_results.out

This log shows when the model is loading, prompts are being processed, and
sampling is running.

- 

After the job completes, the accuracy is saved to a file in the accuracies/
 directory. To view it:

cat accuracies/deepseek-ai_DeepSeek-R1-Distill-Llama-70B.txt

The filename matches the model ID with slashes replaced by underscores.

### Run commands directly using srun#

You can run nvidia-smi -L with srun in the following ways:

- Direct execution on compute nodes: Runs nvidia-smi -L directly on the
 assigned nodes.

- Execution inside containers: Runs nvidia-smi -L within a containerized
 environment on the compute nodes.

#### Direct execution on compute nodes#

srun --gpus=2 --nodes=2 --ntasks-per-node=1 \
 --output="srun_output_direct_%N.txt" \
 bash -c 'printf "\n===== Node: $(hostname) =====\n"; nvidia-smi -L'

This command runs nvidia-smi -L directly on two compute nodes and saves the
output in separate text files. The filenames are based on the hostnames of the
respective nodes, for example:

- srun_output_direct_slurm-compute001.txt

- srun_output_direct_slurm-compute002.txt

Each file contains the nvidia-smi -L output from its corresponding compute
node.

#### Execution inside containers#

srun --gpus=2 --nodes=2 --ntasks-per-node=1 \
 --output="srun_output_container_%N.txt" \
 --container-image=nvidia/cuda:12.8.1-runtime-ubuntu22.04 \
 bash -c 'printf "\n===== Node: $(hostname) =====\n"; nvidia-smi -L'

This command performs the same task as above but runs nvidia-smi -L inside an
NVIDIA CUDA container instead of directly on the compute nodes. The output is
saved in separate files, such as:

- srun_output_container_slurm-compute001.txt

- srun_output_container_slurm-compute002.txt

Each file contains the nvidia-smi -L output from its respective node while
running within a containerized environment.

### Run an interactive session with salloc#

Unlike srun and sbatch, salloc doesn't run a single specified task.
Instead, it allocates resources and opens an interactive shell directly on the
allocated compute node. Run commands as you like, then exit the shell to
release the allocation.

In contrast with previous examples, this example requests one node with two
GPUs rather than two nodes with one GPU each. In addition, the output appears
directly in the terminal instead of being saved to a file.

- 

Establish an SSH connection to your login node.

- 

Allocate one node with two GPUs and start an interactive shell on the
 allocated node:

salloc --gpus=2 --nodes=1

- 

Print the node's hostname and run nvidia-smi -L:

printf "\n===== Node: $(hostname) =====\n"; nvidia-smi -L

- 

Exit the interactive shell and release the allocated resources by pressing
 Ctrl + D.

## Managing software using Lmod#

Both MSlurm and unmanaged Slurm include the Lmod module system by default. You
can use Lmod's module command-line tool to dynamically load and unload
software modules. When you load a module, Lmod updates your shell environment so
the selected software is available.

When you load a module on the login node, that environment is exported to your
Slurm jobs automatically. For example, if you run module load uv on the login
node and then submit a job using srun or sbatch, uv will be available on
the compute nodes without needing to reload it.

Common Lmod commands:

 | Command
 | Description

 | module avail
 | List all modules available to be loaded.

 | module spider
 | List and describe every module available on the cluster, including those hidden by the current hierarchy.

 | module load <MODULE>
 | Load a specific module into your current environment.

 | module list
 | Show all modules currently loaded in your session.

 | module unload <MODULE>
 | Remove a specific module from your environment.

 | module purge
 | Unload all modules to start with a clean environment.

Tip

When submitting jobs using sbatch, include the module load commands
inside your batch script. By including these commands in the script, you
ensure that the compute nodes have the correct environment configured
before your code executes.

## Next steps#

- Follow the quickstart to connect to your cluster and run
 your first GPU jobs.

- Learn how health checks and
 auto-remediation keep your cluster healthy without
 touching your jobs.

- Explore the Slurm console, your browser window into
 cluster health, jobs, and users.

- Learn more about using Lmod.

- See SchedMD's Slurm documentation
 to learn more about using Slurm.

 Back to top
