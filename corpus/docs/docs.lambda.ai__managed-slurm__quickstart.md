# Quickstart - Lambda Docs

Source: https://docs.lambda.ai/managed-slurm/quickstart/

Skip to content

# Managed Slurm quickstart#

This guide takes you from a fresh user account to running multi-node GPU jobs
on a Managed Slurm cluster. For an overview of how Lambda's Managed Slurm
works, and how it compares to an unmanaged deployment, see
Using Lambda's Managed Slurm.

## Before you begin#

To follow this guide, you need:

- The IP address of your cluster's login node, available in the Lambda Cloud
 console.

- A user account on the cluster. Administrators can create accounts from the
 Slurm console or from the command line. See
 Creating and removing MSlurm users.

## Connect to your cluster#

Begin by connecting to your cluster's login node:

ssh <USERNAME>@<LOGIN-NODE-IP>

The login node functions as a home base where you can edit code, manage data,
and submit jobs to your cluster. These jobs are then scheduled onto the
cluster's compute nodes.

Note

Node-to-node connectivity is automatic. The first time you log in, the
cluster configures SSH between nodes for your account. Multi-node jobs and
tools that rely on node-to-node SSH work without any key setup. While one
of your jobs is running on a node, you can also SSH from the login node
directly into that node to inspect it:

ssh <NODE-NAME>

## Get your bearings#

Begin by viewing the state of your cluster. The following commands give you a
complete picture:

 | Command
 | What it shows

 | sinfo -N -l
 | Every node, its partition, and its state.

 | scontrol show partition
 | Partitions, their limits, and their defaults.

 | squeue -u $USER
 | Your pending and running jobs.

 | scontrol show topology
 | The cluster's network topology.

Jobs run in the cluster's default partition unless you select another with
--partition. Scheduling is topology-aware. Slurm knows how nodes connect to
the network fabric and places multi-node jobs to maximize communication
performance.

Note

You might notice a low-priority partition dedicated to automated health
checks, along with its jobs in squeue output. These diagnostics run
only on idle capacity and yield immediately when your jobs need the
nodes. See Know how your cluster stays healthy.

## Know your storage#

 | Path
 | Scope
 | Best for

 | /home
 | Shared across all nodes
 | Code, environments, checkpoints

 | /data
 | Shared across all nodes
 | Datasets, shared tools, examples

 | /scratch
 | Local NVMe on each compute node
 | Fast temporary space during a job

Your home directory is the same on every node, so your code, virtual
environments, and outputs follow your jobs wherever they're scheduled.

Note

Stage data on local storage before running I/O-heavy jobs. Reading
directly from shared storage during a job can bottleneck on I/O. Treat
/scratch as ephemeral, and copy results back to shared storage before
your job ends.

## Run your first jobs#

### Run a command with srun#

srun --gpus=1 nvidia-smi -L

srun runs a command on a compute node and streams the output back to
your terminal. It's a quick way to test something on a GPU.

Tip

You usually only need to request GPUs. Defaults allocate CPU cores and
memory automatically, in proportion to the GPUs you request. Override them
anytime with options such as --cpus-per-task and --mem.

### Submit a script with sbatch#

sbatch --wrap 'hostname'

sbatch queues a script (here, a one-liner) and returns immediately.
Output lands in slurm-<JOBID>.out. Your cluster also includes
ready-made job scripts in /data/examples:

sbatch /data/examples/hostname.sbatch

Each example is a readable template. Open one to see how a job script is
structured.

### Work interactively with salloc#

salloc --gpus=1

salloc reserves resources and drops you into a shell on the allocated
compute node. Run commands directly, then press Ctrl + D to release
the allocation.

## Watch and manage your work#

To view your queued jobs, run squeue:

squeue -u $USER

You can cancel a job by locating its job ID and then running scancel on the
job:

scancel <JOBID>

The cluster records every job in its accounting database. Review your history
and resource usage any time by running sacct:

sacct -o JobID,JobName,Partition,AllocTRES%35,State,Elapsed

## Set up your software#

Clusters come ready for GPU development. Each cluster includes:

- The CUDA toolkit, including the nvcc compiler.

- NCCL and HPC-X MPI, ready in your default environment for distributed
 workloads.

- Everyday tools such as Python, Git, and common editors and utilities.

- Lmod modules for additional toolchains. List them with module avail.

For example, manage Python projects and virtual environments with uv:

module load uv
uv venv ~/venvs/demo && source ~/venvs/demo/bin/activate

See Managing software using Lmod
for more on modules.

Note

Lambda restricts system-level access to cluster administrators and Lambda
support. If you use isolation mechanisms like modules, uv-managed Python
environments, and containers, your everyday workflows generally won't
need this level of access. If you do need to perform an operation that
requires system-level access, such as installing a system package, reach
out to your cluster administrator or contact Lambda support.

## Run containers#

Run any container image straight through Slurm. Pyxis and Enroot are
preconfigured, and the NVIDIA Container Toolkit ensures containers get GPU
access:

srun --gpus=1 --container-image=nvidia/cuda:12.8.1-runtime-ubuntu22.04 \
 nvidia-smi -L

Slurm pulls the image, starts the container on a compute node, and runs the
command.

If you prefer a workflow that more closely matches the standard Docker
workflow, Managed Slurm also includes Podman, which includes a
Docker-compatible docker CLI, and Apptainer on its compute nodes.

Tip

You can find several container-based job scripts, such as a two-node NCCL
test that runs entirely in containers (pyxis_2x_all_reduce.sbatch), in
/data/examples.

## Check your cluster's performance#

The /data/examples directory includes benchmark jobs you can run as-is.
For example, to verify multi-node GPU communication across the cluster's
GPUDirect RDMA-capable fabric, submit the provided NCCL all-reduce test:

sbatch /data/examples/full_cluster_all_reduce.sbatch

The job builds NVIDIA's nccl-tests in /data/$USER and runs a cluster-wide
all-reduce. Results land in ~/<JOBID>.nccl-test.out.

The same directory covers the rest of the stack: gemm.sbatch measures each
GPU's raw compute (TFLOPS), fio.sbatch benchmarks the shared and local
filesystems, and additional variants and GPU stress tests sit alongside them.

After any GPU job finishes, look for a <JOBID>.gpu_stats/ directory next
to your job's output. The cluster automatically records per-job GPU statistics
(utilization, memory, and energy) for every node the job used.

## Profile your workloads#

Every user gets full access to GPU hardware performance counters, with no
root required. Run NVIDIA Nsight Compute (ncu) on your own kernels under
srun, or start from the ready-made example:

sbatch /data/examples/ncu.sbatch

The job profiles a small GPU kernel and saves a report you can open in the
Nsight Compute UI. CPU-side profiling with perf also works, so you can
investigate host-side bottlenecks such as data loading and launch overhead
alongside device-side ones.

## See your cluster in the browser#

Every Managed Slurm cluster includes the Slurm console,
which allows you to view and manage your Slurm cluster. You can:

- Watch cluster health live, including node states, job flow, and GPU
 temperature, memory, and power for every node.

- Work with your jobs. Watch the queue, browse history and per-user
 accounting, drill into any job's output and GPU metrics, or submit new jobs
 without leaving the browser.

- Review access at a glance, from login activity to a full audit trail of
 cluster changes.

- Manage users, SSH keys, and Slurm accounts.

For more details, see The Slurm console.

## Know how your cluster stays healthy#

Managed Slurm monitors the hardware for you:

- Continuous node health checks are wired directly into
 Slurm and run on every node every few minutes. A node that fails a check is
 automatically taken out of scheduling before it can affect your jobs, and
 automated remediation works to return it to service.

- Deep GPU diagnostics and stress tests run continuously in the background,
 using only idle capacity in a dedicated low-priority partition that yields
 instantly to user jobs.

- Lambda continuously collects and monitors cluster telemetry, covering
 hardware, GPU, and scheduler metrics. Lambda coordinates patches, upgrades,
 and repairs with you according to your service level agreement (SLA).

## Get help#

- Lambda's support team is available 24/7. See
 Support for scope and
 contact details.

- Using Lambda's Managed Slurm covers user management, job
 submission, and Lmod in more depth.

- SchedMD's Slurm documentation
 and man pages cover every
 Slurm command and option.

 Back to top
