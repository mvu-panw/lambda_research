# Predefined roles - Lambda Docs

Source: https://docs.lambda.ai/public-cloud/predefined-roles/

Skip to content

# Predefined roles#

This page lists the predefined roles Lambda Cloud maintains as part of its IAM
system, describes the access each role grants, and lists the permissions each
role includes.

## Account roles#

 | Role name
 | Role description
 | Included permissions

 | Account Admin (account-admin)
 | Has full access to all account-level operations and resources, as
 well as all workspace-level operations and resources in workspaces the
 assignee belongs to.
 | 
 Account: Read, Update, Close

 Audit Event: Read

 Billing Address: Read, Update

 Billing Profile: Read

 Billing Account: Update

 Credit: Read, Download

 Group: Create, Read, Update, Delete

 Group Membership: Create, Read, Delete

 Identity Invite: Create, Read, Delete

 Invoice: Read, Pay, Download

 Payment Method: Create, Read, Delete

 Service Identity: Create, Read, Update, Delete

 Service Identity API Key: Create, Read, Delete

 Support Ticket: Create, Read, Update

 Support Ticket Attachment: Create, Read, Update, Delete

 Role: Read

 Role Assignment: Create, Read, Delete

 Usage: Read

 User Identity: Read, Deactivate

 User Identity API Key: Read, Delete

 Workspace: Create, Read, Update, Delete

 Workspace Membership: Create, Read, Delete

 All permissions included in the Workspace Owner role

 | Account Member (account-member)
 | Can view most account-level resources, and can create and update support tickets.
 | 
 Account: Read

 Audit Event: Read

 Billing Profile: Read

 Service Identity: Read

 Service Identity API Key: Read

 Support Ticket: Create, Read, Update

 Support Ticket Attachment: Create, Read, Update, Delete

 User Identity: Read

 Usage: Read

 | IAM Admin (iam-admin)
 | Can create and manage identities and groups, their workspace memberships, and their role assignments.
 | 
 Account: Read, Update

 Audit Event: Read

 Group: Create, Read, Update, Delete

 Group Membership: Create, Read, Delete

 Identity Invite: Create, Read, Delete

 Role: Read

 Role Assignment: Create, Read, Delete

 Service Identity: Create, Read, Update, Delete

 Service Identity API Key: Create, Read, Delete

 User Identity: Read, Deactivate

 User Identity API Key: Read, Delete

 Workspace: Create, Read, Update, Delete

 Workspace Membership: Create, Read, Delete

 | Billing Admin (billing-admin)
 | Can view and manage account billing.
 | 
 Billing Address: Read, Update

 Billing Profile: Read

 Billing Account: Update

 Usage: Read

 Credit: Read, Download

 Payment Method: Create, Read, Delete

 Invoice: Read, Pay, Download

 | Support Ticketing Admin (support-ticketing-admin)
 | Can view and manage support tickets and their attachments.
 | 
 Support Ticket: Create, Read, Update

 Support Ticket Attachment: Create, Read, Update, Delete

 | Support Ticketing Reader (support-ticketing-reader)
 | Can view support tickets and their attachments.
 | 
 Support Ticket: Read

 Support Ticket Attachment: Read

## Workspace roles#

 | Role name
 | Role description
 | Included permissions 

 | Workspace Owner (workspace-owner)
 | Has full access to all operations and resources in the workspace. Can also add identities and groups to the workspace.
 | 
 Cluster Metrics: Read

 Cluster Type: Read

 Compute Support Ticket: Create

 Image: Read

 Instance: Launch, Read, Update, Restart, Terminate

 Instance Metrics: Read

 Instance Type: Read

 Firewall Rule: Read, Update

 Firewall Ruleset: Create, Read, Update, Delete

 Filesystem: Create, Read, Delete, Mount

 Filesystem S3 Adapter Key: Create, Read, Delete

 SSH Key: Create, Read, Delete

 Workspace Membership: Create, Read, Delete

 | Workspace Member (workspace-member)
 | Has access to most operations and resources in the workspace.
 | 
 Cluster Metrics: Read

 Cluster Type: Read

 Compute Support Ticket: Create

 Filesystem: Create, Read, Delete, Mount

 Filesystem S3 Adapter Key: Read

 Firewall Rule: Read, Update

 Firewall Ruleset: Create, Read, Update, Delete

 Image: Read

 Instance: Launch, Read, Update, Restart, Terminate

 Instance Metrics: Read

 Instance Type: Read

 SSH Key: Create, Read, Delete

 Workspace Membership: Read

 | Instance Reader (instance-reader)
 | Can list all instances in the specified workspace and view their metadata.
 | 
 Instance: Read

 | Instance Terminate (instance-terminate)
 | Can terminate instances in the specified workspace.
 | 
 Instance: Terminate

## Deprecated roles#

Prior to the introduction of the IAM system, Lambda Cloud had two roles:
Admin and Member. These roles have been superseded by the following
IAM equivalents:

- Admin: Account Admin

- Member: Account Member

 Back to top
