# Cluster upgrades - Lambda Docs

Source: https://docs.lambda.ai/managed-kubernetes/cluster-upgrades/

Skip to content

# Kubernetes cluster upgrades#

Lambda is committed to keeping Managed Kubernetes clusters up to date with most
recent Kubernetes versions.

## Upstream versions#

When a new Kubernetes version is released, Lambda does internal validation and
runs full end-to-end tests to validate that there are no regressions based on
existing software configurations.

Upon validation, the new Kubernetes version is made available for customer
clusters.

## Upgrading an existing cluster#

By default, Lambda launches new clusters on the latest
known-supported version of Kubernetes that has been validated by Lambda.
You're in full control of when and how your cluster version is updated.
As Lambda validates newly released versions of Kubernetes and makes them
available:

- If your cluster is running on an old or end-of-life Kubernetes version,
 Lambda actively reaches out and asks you to schedule an upgrade to a
 supported version.

- If your want to use features that require a newer Kubernetes version, you
 can reach out to your Lambda team and schedule an upgrade.

In both cases, Lambda manages the upgrade process following the steps below:

- 

Lambda offers upgrade notes comparing the current and the target Kubernetes
 version, such as a list of breaking API changes and any feature deprecations.
 You validate that your workloads are compatible with the new version,
 and then sign off on the upgrade.

- 

You work with Lambda to schedule a maintenance window that works you.

- 

During the maintenance window, Lambda performs the version upgrade and
 monitors to ensure that system components remain healthy. Lambda performs
 in-place upgrades on the cluster nodes, so general, long-running
 workloads such as inference will only experience temporary disruption
 during the cluster upgrade, if they experience any disruption at all.

 Back to top
