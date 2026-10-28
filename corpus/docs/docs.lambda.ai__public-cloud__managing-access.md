# Managing access - Lambda Docs

Source: https://docs.lambda.ai/public-cloud/managing-access/

Skip to content

# Managing access#

This guide describes how to manage access to Lambda Cloud accounts,
workspaces, and resources from the Lambda Cloud console.

## User identities#

### Assign roles to a user identity#

If you have an account role with the Role Assignment: Create
permission, you can assign roles to a user identity.

To assign one or more roles to a user identity:

- Navigate to the Users tab on the IAM page in the Lambda Cloud console.

- In the identities list, click the user identity you want to assign a
 role to.

- Navigate to the Roles tab.

- To assign a role to the user identity, click the role's toggle to the on
 position.

### Unassign roles from a user identity#

If you have an account role with the Role Assignment: Delete
permission, you can unassign roles from a user identity.

To unassign one or more roles from a user identity:

- Navigate to the Users tab on the IAM page in the Lambda Cloud console.

- In the identities list, click the user identity you want to assign a role
 to.

- Navigate to the Roles tab.

- To unassign a role from the user identity, click the role's toggle to the
 off position.

### Add a user identity to a workspace#

You can add an existing user identity to a workspace if:

- You have an account role that includes the
 Workspace Membership: Create permission, or

- You have the Workspace Owner role in the target workspace.

To add a user identity to a workspace in your account:

- Navigate to the
 Workspaces page
 in the Lambda Cloud console.

- In the target workspace's row, click ⋮. A context menu appears.

- Click Manage access. A dialog appears.

- Click Add member. Another dialog appears.

- Click the Add users, service identities, and groups dropdown, and then
 select the user you want to add to the workspace.

- Click Add to add the user.

### Remove a user identity from a workspace#

You can remove a user identity from a workspace if:

- You have an account role that includes the
 Workspace Membership: Delete permission, or

- You have the Workspace Owner role in the target workspace.

To remove a user identity from a workspace:

- Navigate to the
 Workspaces page
 in the Lambda Cloud console.

- In the target workspace's row, click ⋮. A context menu appears.

- Click Manage access. A dialog appears.

- Find the user identity you want to remove.

- In that user identity's row, click Remove. A modal appears.

- Click Remove user to remove the identity from the workspace.

### View a user identity's effective access#

If you have an account role with the User Identity: Read permission, you can
view a user identity's effective access. Effective access refers to all of
the access an identity has been granted, including its direct role assignments
and any access it has inherited from groups it belongs to.

To view a user identity's effective access:

- Navigate to the Users tab on the IAM page in the Lambda Cloud console.

- In the identities list, click the user identity whose access you want to
 view.

- Navigate to the Roles tab.

- Click View effective access to see a list of the workspaces the user
 identity belongs to and the roles they have in each, as well as any
 account-level roles they have.

### Manage a user identity's API keys#

#### Delete a user identity's API key#

If you have an account role with the User Identity: API Key Delete
permission, you can delete a user identity's API key.

To delete a user identity's API key:

- Navigate to the Users tab on the IAM page in the Lambda Cloud console.

- In the identities list, click the user identity whose key you want to delete.

- Navigate to the API Keys tab.

- Find the row of the key you want to delete, then click the three-dot icon
 in its Actions column. A context menu appears.

- Click Delete. A modal appears.

- If you're sure you want to delete the key, click Delete API key to
 delete it permanently.

#### View a user identity's API keys#

If you have an account role with the User Identity: API Key Read
permission, you can view a user identity's API keys.

To view a user identity's API keys:

- Navigate to the Users tab on the IAM page in the Lambda Cloud console.

- In the identities list, click the user identity whose keys you want to view.

- Navigate to the API Keys tab to see a list of the user identity's keys.

## Service identities#

### Assign roles to a service identity#

If you have an account role with the Role Assignment: Create
permission, you can assign roles to a service identity.

To assign one or more roles to a service identity:

- Navigate to the Service identities tab on the IAM page in the
 Lambda Cloud console.

- In the identities list, click the service identity you want to assign
 a role to.

- Navigate to the Roles tab.

- For each role you want to assign, click the role's toggle to the on
 position.

### Unassign roles from a service identity#

If you have an account role with the Role Assignment: Delete
permission, you can unassign roles from a service identity.

To unassign one or more roles from a service identity:

- Navigate to the Service identities tab on the IAM page in the Lambda
 Cloud console.

- In the identities list, click the service identity you want to assign a
 role to.

- Navigate to the Roles tab.

- For each role you want to unassign, click the role's toggle to the off
 position.

### Add a service identity to a workspace#

You can add an existing service identity to a workspace if:

- You have an account role that includes the
 Workspace Membership: Create permission, or

- You have the Workspace Owner role in the target workspace.

To add a service identity to a workspace in your account:

- Navigate to the
 Workspaces page
 in the Lambda Cloud console.

- In the target workspace's row, click ⋮. A context menu appears.

- Click Manage access. A dialog appears.

- Click Add member. Another dialog appears.

- Click the Add users, service identities, and groups dropdown, and then
 select the service identity you want to add to the workspace.

- Click Add to add the service identity.

### Remove a service identity from a workspace#

You can remove a service identity from a workspace if:

- You have an account role that includes the
 Workspace Membership: Delete permission, or

- You have the Workspace Owner role in the target workspace.

To remove a service identity from a workspace:

- Navigate to the
 Workspaces page
 in the Lambda Cloud console.

- In the target workspace's row, click ⋮. A context menu appears.

- Click Manage access. A dialog appears.

- Find the service identity you want to remove.

- In that service identity's row, click Remove. A modal appears.

- Click Remove service identity to remove the identity from the workspace.

### View a service identity's effective access#

If you have an account role with the Service Identity: Read
permission, you can view a service identity's effective access.
Effective access refers to all of the access an identity has been granted,
including its direct role assignments and any access it has inherited from
groups it belongs to.

To view a service identity's effective access:

- Navigate to the Service identities tab on the IAM page in the Lambda
 Cloud console.

- In the identities list, click the service identity whose access you want
 to view.

- Navigate to the Roles tab.

- Click View effective access to view a list of the workspaces the
 service identity belongs to and the roles it has in each, as well as any
 account-level roles it has.

### Manage a service identity's API keys#

#### Generate an API key for a service identity#

If you have an account role with the Service Identity: API Key Create
permission, you can generate an API key for a service identity.

- Navigate to the Service identities tab on the IAM page in the Lambda
 Cloud console.

- In the identities list, click the service identity you want to create an
 API key for.

- Navigate to the API Keys tab.

- Click Generate API key. A modal appears.

- Enter a name for the new key.

- Click Generate API key to finish creating the key.

- Copy or download the key to a safe location. After you close the dialog,
 you won't be able to retrieve the key again.

#### Delete a service identity's API key#

If you have an account role with the Service Identity: API Key Delete
permission, you can delete a service identity's existing API key.

- Navigate to the Service identities tab on the IAM page in the Lambda
 Cloud console.

- In the identities list, click the service identity you want to delete the
 API key from.

- Click the API Keys tab.

- Find the row of the key you want to delete, then click the three-dot icon
 in the Actions column. A context menu appears.

- Click Delete. A modal appears.

- If you're sure you want to delete the key, click Delete API key to
 delete it permanently.

## Groups#

### Assign roles to a group#

If you have an account role with the Role Assignment: Create
permission, you can assign roles to a group.

To assign one or more roles to a group:

- Navigate to the Groups tab on the IAM page in the Lambda Cloud console.

- In the identities list, click the group you want to assign a role to.

- Navigate to the Roles tab.

- For each role you want to assign, click the role's toggle to the on
 position.

### Unassign roles from a group#

If you have an account role with the Role Assignment: Delete
permission, you can unassign roles from a group.

To unassign one or more roles from a group:

- Navigate to the Groups tab on the IAM page in the Lambda Cloud console.

- In the identities list, click the group you want to assign a role to.

- Navigate to the Roles tab.

- For each role you want to unassign, click the role's toggle to the off
 position.

### Add a group to a workspace#

You can add an existing group to a workspace if:

- You have an account role that includes the
 Workspace Membership: Create permission, or

- You have the Workspace Owner role in the target workspace.

To add a group to a workspace in your account:

- Navigate to the
 Workspaces page
 in the Lambda Cloud console.

- In the target workspace's row, click ⋮. A context menu appears.

- Click Manage access. A dialog appears.

- Click Add member. Another dialog appears.

- Click the Add users, service identities, and groups dropdown, and then
 select the group you want to add to the workspace.

- Click Add to add the group.

### Remove a group from a workspace#

You can remove a group from a workspace if:

- You have an account role that includes the
 Workspace Membership: Delete permission, or

- You have the Workspace Owner role in the target workspace.

To remove a group from a workspace:

- Navigate to the
 Workspaces page
 in the Lambda Cloud console.

- In the target workspace's row, click ⋮. A context menu appears.

- Click Manage access. A dialog appears.

- Find the group you want to remove.

- In that group's row, click Remove. A modal appears.

- Click Remove group to remove the group from the workspace.

### View a group member's effective access#

If you have an account role with the Group Membership: Read and
Role Assignment: Read permissions, you can view a group member's effective
access. Effective access refers to all of the access an identity has been
granted, including its direct role assignments and any access it has inherited
from groups it belongs to.

To view a group member's effective access:

- Navigate to the Groups tab on the IAM page in the Lambda Cloud console.

- In the identities list, click the group you want to assign a role to.

- Navigate to the Identities tab.

- In the identities list, click the group member.

- Navigate to the Roles tab.

- Click View effective access to view a list of the workspaces the
 group belongs to and the roles it has in each, as well as any
 account-level roles it has.

### View all groups a member belongs to#

If you have an account role with the Group Membership: Read permissions,
you can view all groups a group member belongs to.

To view all groups a group member belongs to:

- Navigate to the Groups tab on the IAM page in the Lambda Cloud console.

- In the identities list, click the group you want to assign a role to.

- Navigate to the Identities tab.

- In the identities list, click the group member.

- Navigate to the Groups tab to view the groups the identity belongs to.

### View a member's API keys#

If you have an account role with the Group Membership: Read,
User Identity API Key: Read and Service Identity API Key: Read
permissions, you can view a group member's API keys.

To view a group member's effective access:

- Navigate to the Groups tab on the IAM page in the Lambda Cloud console.

- In the identities list, click the group you want to assign a role to.

- Navigate to the Identities tab.

- In the identities list, click the group member.

- Navigate to the API keys tab to view the identity's API keys.

## Next steps#

- Learn more about identity and access management (IAM) on Lambda Cloud

- Learn how to manage identities and groups in your account

- Learn what roles are available and which permissions they grant

 Back to top
