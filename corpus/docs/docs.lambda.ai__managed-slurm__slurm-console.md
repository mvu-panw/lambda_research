# Slurm console - Lambda Docs

Source: https://docs.lambda.ai/managed-slurm/slurm-console/

Skip to content

# The Slurm console#

You can view and manage your Managed Slurm cluster by visiting the Slurm
console, which you can access from the Lambda Cloud console.

## Live views#

The console provides live views of your cluster, including:

- Cluster health: node states, job flow, and failures at a glance.

- GPU fleet: per-GPU telemetry for every node, including temperature,
 power, and memory.

- Health checks: pass/fail history for every automated check on every
 node, with detail on what is failing and why. See
 Health checks for how the checks work.

## Job management and observability#

The console lets you work with the scheduler directly:

- Watch the live queue, filtered to your own jobs or everyone's.

- Browse job history and per-user accounting, powered by the cluster's
 accounting database.

- Drill into any job to see its state, its nodes, its output, and its per-GPU
 metrics.

- Submit new jobs straight from the browser.

## User and access management#

The Slurm console also lets you manage and review user access for your cluster.
Available operations include:

- Adding and managing cluster users, their SSH keys, and their Slurm accounts.
 For details, see
 Manage users from the Slurm console.

- Reviewing sign-in activity and a full audit trail of changes to the
 cluster's control plane.

 Back to top
