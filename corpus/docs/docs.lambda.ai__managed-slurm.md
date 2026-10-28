# Overview - Lambda Docs

Source: https://docs.lambda.ai/managed-slurm/

Skip to content

# Slurm on Lambda Cloud#

Lambda offers two Slurm deployment options for 1-Click Clusters (1CC):

- Managed Slurm (MSlurm): Lambda installs, manages, and maintains a
 Slurm environment on your cluster. You interact with the environment using
 standard Slurm tooling.

- Unmanaged Slurm: Lambda preinstalls a Slurm environment on your cluster.
 After cluster handoff, you are responsible for managing and maintaining
 the environment.

This document provides overviews of both options and compares their respective
feature sets.

## What is Slurm?#

Slurm is a widely used open-source workload manager optimized for
high-performance computing (HPC) and machine learning (ML) workloads. Slurm
allows administrators to create user accounts with controlled access, enabling
individual users to submit, monitor, and manage their workloads.

Slurm automatically schedules workloads, maximizing cluster
utilization while preventing resource contention.

## Feature comparison#

The table below summarizes the key differences between MSlurm and unmanaged
Slurm:

 | Feature
 | MSlurm
 | Unmanaged Slurm

 | Slurm-managed compute node access
 | ✓
 | ✗ (out-of-band access allowed)

 | User sudo/root privileges
 | ✗
 | ✓

 | Lambda monitors Slurm daemons
 | ✓
 | ✗ (customer is responsible)

 | Lambda applies patches and upgrades
 | ✓ (on request)
 | ✗ (customer is responsible)

 | Slurm support with SLAs
 | ✓
 | ✗

 | Lambda Slurm configuration
 | ✓
 | ✓

 | Slurm configured for high availability
 | ✓
 | ✓

 | Shared /home across all nodes
 | ✓
 | ✓

 | Shared /data across all nodes
 | ✓
 | ✓

### Managed Slurm (MSlurm)#

When MSlurm is deployed:

- 

Slurm handles all interactions with the cluster resources. Access to
 other nodes is restricted to help ensure cluster integrity and reliability.

- 

Lambda monitors and maintains the health of Slurm daemons such as slurmctld
 and slurmdbd.

- 

Lambda coordinates with the customer to apply security patches and upgrade to
 new Slurm releases, if requested.

- 

Lambda provides support according to the service level agreements (SLAs) in
 place with the customer.

### Unmanaged Slurm#

In contrast, in an unmanaged Slurm deployment:

- 

All nodes are directly accessible, and users have system administrator
 privileges (sudo or root) across the cluster.

Warning

Workloads that run outside of Slurm might interfere with the resources
managed by Slurm. Additionally, users with administrator access can make
changes that render the cluster unrecoverable. In such cases, Lambda might
need to "repave" the cluster, fully wiping and reinstalling the system.

- 

The customer is responsible for monitoring and maintaining the health of Slurm
 daemons.

- 

The customer is responsible for applying security patches and upgrading to new
 Slurm releases.

- 

Support is provided on a best-effort basis, with no guaranteed SLAs.

### Shared features#

Both MSlurm deployments and unmanaged Slurm deployments include:

- 

Identical Slurm configurations: Slurm is installed the same way whether
 the customer is using MSlurm or unmanaged Slurm.

- 

Container and HPC software: Open MPI, CUDA, Podman, Apptainer, Pyxis, and
 Enroot are preinstalled.

- 

Lmod for environment management: Use Lmod to dynamically load and unload
 software modules available on the cluster, such as HPC-X, Node.js, and uv.

- 

High availability (HA): Slurm is configured for HA, so jobs continue to
 be schedulable and continue running even if a head node goes down.

- 

Shared /home filesystem: Provides a consistent user environment across
 all nodes, for example, personal scripts, virtual environments, and model
 checkpoints.

- 

Shared /data filesystem: Intended for storing resources such as
 libraries, datasets, and tools that aren't user-specific.

Note

It's recommended to stage data, such as datasets and models, on local
storage before running a job. Accessing files directly from shared storage
during a job can lead to degraded performance due to I/O bottlenecks.

## Next steps#

- For guidance on using your MSlurm cluster, see
 Using Managed Slurm.

 Back to top
