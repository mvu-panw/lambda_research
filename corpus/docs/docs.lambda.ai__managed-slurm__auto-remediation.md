# Auto-remediation system - Lambda Docs

Source: https://docs.lambda.ai/managed-slurm/auto-remediation/

Skip to content

# Lambda's Managed Slurm auto-remediation#

Managed Slurm pairs its health checks with an automated
remediation loop that detects, isolates, and repairs unhealthy nodes, often
before you notice any issues at all.

## The remediation loop#

- 

Detect. Passive and active health checks validate
 every node continuously and publish their results as cluster metrics. Both
 the remediation system and Lambda's 24/7 monitoring watch these metrics.

- 

Isolate. Any node that fails validation is immediately taken out of
 scheduling, ensuring the remaining queued jobs flow to healthy nodes.

- 

Remediate. If the node's remediation agent detects issues with the node,
 the system begins remediation. It drains the node, reboots the node, and then
 returns the node to service. The node rejoins the pool only after it passes
 its health checks again.

- 

Escalate. If a node can't recover on its own, the remediation system
 automatically initiates hands-on repair with Lambda's data center operations
 team. Lambda then handles repairs or replacements based on the terms of
 your service level agreement (SLA).

## Impact on your jobs#

Usually, you should see little or no impact on your jobs. Capacity dips
briefly while a node is repaired, then returns automatically. If you look
closely, you might see a node marked as drained or down in sinfo, or its
state change in the Slurm console, with no action needed
on your part.

Tip

For multi-day training runs, checkpoint regularly and make your batch
jobs requeueable. If a node fault interrupts a job, Slurm can requeue it
automatically, and the job resumes from your latest checkpoint on healthy
hardware.

 Back to top
