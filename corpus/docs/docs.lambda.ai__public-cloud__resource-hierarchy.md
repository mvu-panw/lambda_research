# Resource hierarchy - Lambda Docs

Source: https://docs.lambda.ai/public-cloud/resource-hierarchy/

Skip to content

# Resource hierarchy#

Lambda Cloud's resource hierarchy provides a top-down structure for organizing
your cloud resources, enabling both hierarchical access management and policy
inheritance. The hierarchy consists of:

- A top-level account.

- One or more workspaces within that account.

- One or more Lambda Cloud resources, such as instances or filesystems,
 within each workspace.

## Accounts#

Accounts serve as the top-level nodes in the Lambda Cloud resource hierarchy.
Each account provides a secure, isolated administrative boundary with its own
users, policies, resources, quotas, billing, and governance. Lambda bills
resource usage at the account level.

### Account membership#

When you join Lambda Cloud, you automatically join a Lambda Cloud account.
The exact account depends on how you join Lambda Cloud:

- If you accept another user's invitation to join Lambda, you become a
 member of that user's account.

- If you log in using your company's SSO, you join your company's account.

- If you sign up through Lambda's standard signup flow, you receive your
 own account and are automatically assigned the Account Admin role in that
 account.

You can join exactly one account per email address. If you want to join a
different account, you must use a different eligible email address.
Alternatively, you can ask an Account Admin or IAM Admin in your current
account to remove you from the account, and then use the email address to
join the other account.

### Account administration#

You manage IAM, workspaces, and billing at the account level. You must have
an account role to perform account-level tasks. For more information,
see Identity and access management (IAM) > Role types.

## Workspaces#

Workspaces allow you to group sets of related Lambda Cloud resources into
their own isolated environments within an account. For example, you can
create distinct workspaces for your team's production, staging, and
development environments, or separate unrelated workloads from each other.

Workspaces have the following properties:

- They serve as the primary containers for Lambda Cloud resources in your
 account. When you deploy a new resource, you deploy it into a workspace.

- They serve as an access boundary within your account. To view or manage
 resources in a specific workspace, a user must a member of that workspace.

- They serve as a resource isolation boundary within your account. Resources
 deployed inside one workspace cannot see or directly access resources in
 another workspace.

You can create up to 200 workspaces per account. Each Lambda Cloud account
includes a default workspace that cannot be deleted. By default, newly added
account users become members of the account's default workspace.

### Workspace administration and management#

If you have an Account Admin or IAM Admin role within your account, you can:

- Create, modify, and delete workspaces

- Add users to, or remove users from, any workspace

If you have the Workspace Owner role in a workspace, you can add identities to
and remove identities from that workspace as well. When you add an identity to
a workspace, it receives the Workspace Member role by default.

For details on managing workspaces, see
Managing your workspaces.

## Next steps#

- Learn more about identity and access management (IAM) on Lambda Cloud

- Learn how to manage your account

- Learn how to manage your workspaces

- See what roles are available and which permissions they grant

 Back to top
