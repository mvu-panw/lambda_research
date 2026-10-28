# Access and security overview - Lambda Docs

Source: https://docs.lambda.ai/public-cloud/access-security/

Skip to content

# Access and security#

This page describes Lambda Cloud's access management and security features.

## Access management#

Lambda provides several access management mechanisms to help ensure secure
access to your account, workspaces, and cloud resources.

### Role-based access control (RBAC)#

Lambda Cloud's identity and access management (IAM) system uses role-based
access control (RBAC), in which you assign roles to identities or groups of
identities to grant sets of permissions. For more information on Lambda
Cloud's IAM system, see the IAM overview.

### Workspaces#

Workspaces allow you to group sets of related Lambda Cloud resources into
their own isolated environments within an account. To view, use,
or manage the resources in that workspace, an identity or group must first
be added to the workspace by an admin or owner with the proper permissions.
Resources deployed inside one workspace cannot see or directly access
resources in another workspace.

For more information about workspaces, see
Resource hierarchy > Workspaces.

### API keys#

The Lambda Cloud API uses API keys to authenticate incoming requests. You can
generate a new API key pair or view your existing API keys by visiting the
API keys page
in the Lambda Cloud console. API keys have full access to all Lambda API
operations.

### SSH keys#

Before you launch an instance, you must add an SSH key to your Lambda Cloud
account. When you go through the process of launching an instance, you'll be
prompted to supply this SSH key so you can securely connect to the instance
after launching. You can import an existing key if you have one, or you can
generate a new one in the Lambda Cloud console.

For guidance on setting up an SSH key, see
Connecting to an instance > Setting up SSH access.

### Firewall rulesets#

You can use global or per-instance firewall rulesets to allow only connections
from trusted source IPs. For more details about firewall rulesets, see
Firewalls.

## Compliance#

### Audit logs#

Lambda provides audit event logs through the Audit Events endpoint in the Lambda
Cloud API. These logs provide a detailed record of the user- and API-level
events that occur in your Lambda Cloud account. Lambda logs audit events
automatically and retains them for six months. For more details, see the
Audit Events section in the
Cloud API browser.

The following table outlines the current catalog of audit events.

 | Event
 | Description

 | cloud.api_key.created
 | An API key resource was created.

 | cloud.api_key.deleted
 | An API key resource was deleted.

 | cloud.billing.address_updated
 | The billing address associated with the account was updated.

 | cloud.cluster.launched
 | A 1-Click Cluster was launched.

 | cloud.cluster.terminated
 | A 1-Click Cluster was terminated.

 | cloud.firewall_ruleset.created
 | A firewall ruleset was created.

 | cloud.firewall_ruleset.deleted
 | A firewall ruleset was deleted.

 | cloud.firewall_ruleset.updated
 | A firewall ruleset was modified or updated.

 | cloud.identity.banned
 | An identity associated with the account was banned.

 | cloud.identity.created
 | An identity associated with the account was created.

 | cloud.identity.deactivated
 | An identity associated with the account was deactivated.

 | cloud.identity.email_verified
 | An identity associated with the account verified their email.

 | cloud.identity.roles_changed
 | The role of an identity associated with the account was modified.

 | cloud.identity.suspended
 | An identity associated with the account was suspended.

 | cloud.identity.unbanned
 | An identity associated with the account was unbanned.

 | cloud.identity.unsuspended
 | An identity associated with the account was unsuspended.

 | cloud.instance.launched
 | An On-Demand Cloud instance was launched.

 | cloud.instance.terminated
 | An On-Demand Cloud instance was terminated.

 | cloud.ssh_key.created
 | An SSH key resource was created.

 | cloud.ssh_key.deleted
 | An SSH key resource was deleted.

 | cloud.workspace.created
 | A workspace was created.

 | cloud.workspace.updated
 | A workspace's settings were updated.

 | cloud.workspace.deleted
 | A workspace was deleted.

 | cloud.workspace.membership_added
 | An identity was added as a member of a workspace.

 | cloud.workspace.membership_removed
 | An identity was removed from a workspace.

 | cloud.workspace.read
 | A workspace's details were retrieved.

 | cloud.workspace_member.read
 | A workspace member's details were retrieved.

### Trust portal#

The Lambda Trust Portal
documents Lambda's security posture, compliance certifications, data policies,
and more.

 Back to top
