# Health checks - Lambda Docs

Source: https://docs.lambda.ai/managed-slurm/health-checks/

Skip to content

# Health checks#

Managed Slurm continuously validates your cluster's health, finding and fixing
problems before they reach your jobs. Validation happens at two levels:

- Passive checks constantly verify every node's hardware and connectivity,
 integrated directly with the Slurm scheduler.

- Active checks run deeper GPU diagnostics and stress tests on idle capacity,
 catching subtle degradation without touching your workloads.

Together with auto-remediation, these checks
help ensure your jobs automatically land on healthy hardware.

## Passive checks#

Passive checks detect cluster faults so that they can be automatically
remediated or, if necessary, escalated. Every node runs a comprehensive health
check every few minutes, wired into Slurm's native health check mechanism.
Each pass verifies the components your jobs depend on:

- GPU checks cover overall device health, driver responsiveness, and
 GPU-interconnect status, powered by NVIDIA Data Center GPU Manager (DCGM).

- Network checks confirm the high-speed fabric links on every node are
 present, up, and running at full speed.

- Storage checks confirm the shared filesystems (/home and /data) and
 local disks are mounted and healthy.

- System checks cover CPU, memory, and core operating system health.

If a node fails any of these checks, the node is automatically removed from
scheduling before it can affect new jobs and enters auto-remediation. For a
full overview of Managed Slurm's auto-remediation system, see
Auto-remediation.

## Active checks#

Your Managed Slurm cluster runs scheduled GPU diagnostics and stress tests,
such as NVIDIA DCGM diagnostics and GPU load tests, to surface thermal
problems, subtle memory faults, and other issues that only appear under
pressure. These checks are designed to be invisible to your work:

- They run as ordinary Slurm jobs in a dedicated, lowest-priority
 partition.

- They schedule only onto idle GPUs.

- The moment one of your jobs needs the hardware, the diagnostic is
 preempted immediately and returns to the queue.

The cluster publishes the results of these checks as metrics that the
auto-remediation system uses to detect related issues.

Tip

If you'd like to run these diagnostics yourself, you can find a set of
ready-made set of diagnostic and stress-test jobs, as well as compute,
storage, and network benchmarks, in /data/examples.

## Per-job GPU statistics#

For every GPU job, the cluster records per-GPU statistics (utilization,
memory, and energy) for each node the job used and saves them next to your
job's output in <JOBID>.gpu_stats/. This directory is a useful first stop
when a run behaves unexpectedly.

## Health at a glance#

The Slurm console shows the same information the checks
collect, including node states, health check pass/fail history and failure
detail, and live GPU telemetry (temperature, memory, and power) for every node
in the cluster. Lambda monitors the same signals around the clock as part of
Managed Slurm.

 Back to top
