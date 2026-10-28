# Managing identities and groups - Lambda Docs

Source: https://docs.lambda.ai/public-cloud/managing-identities-groups/

Skip to content

# Managing identities and groups#

This guide describes how to manage user identities, service identities, and
groups from the Lambda Cloud console.

## Managing user identities#

### Invite a user identity to your account#

If you have an account role with the Identity Invite: Create
permission, you can invite users to join the account.

To invite other users to your account:

- Navigate to the Users tab on the
 IAM page in the Lambda Cloud
 console.

- Click Invite new user. A modal appears.

- In the Invite teammate dialog, enter the email of the person you'd
 like to invite.

- Click Send invitation to send the invite.

If the invitee accepts the request, they're prompted to join Lambda Cloud.
When they join, they become a member of your account and its default workspace,
and receive the following roles:

- Account Member

- Workspace Member in the default workspace

### Delete an invite#

If you have an account role with the Identity Invite: Delete
permission, you can delete an invite that was previously sent from your account.

To delete an invite:

- Navigate to the Users tab on the
 IAM page in the Lambda Cloud
 console.

- Find the invite in the identities list. The status column will say
 Invited.

- Click the three-dot icon in its Actions column. A context menu appears.

- Click Delete invitation.

- If you're sure you want to delete the invite, click Delete.

### Remove a user identity from your account#

If you have an account role with the User Identity: Deactivate
permission, you can remove other user identities from the account.

To remove a user identity from your account:

- Navigate to the Users tab on the
 IAM page in the Lambda Cloud
 console.

- Find the row containing the user's details, and then click its
 three-dot menu icon in the Actions column. A context menu appears.

- Click Remove member. A modal appears.

- Review the warning text.

- If you still want to proceed, type remove member into the input field
 and then click Remove member to finish removing the user.

## Managing service identities#

### Create a service identity#

If you have an account role with the Service Identity: Create
permission, you can create a service identity in your account.

To create a new service identity:

- Go to the Service Identities tab on the
 IAM page in the Lambda Cloud
 console.

- Click Create service identity. A modal appears.

- Enter a name for the new identity.

- Click Create to create the new identity. On success, you're taken to
 the identity's details page.

### Rename a service identity#

If you have an account role with the Service Identity: Update
permission, you can rename an existing service identity in your account.

To rename a service identity:

- Go to the Service Identities tab on the
 IAM page in the Lambda Cloud
 console.

- Find the identity in the list, and then click the row for the identity.

- On the identity details page, click Rename.

- Replace the existing name.

- Click Rename to apply the new name.

### Delete a service identity#

If you have an account role with the Service Identity: Delete
permission, you can delete an existing service identity from your account.

To delete a service identity:

- Go to the Service Identities tab on the
 IAM page in the Lambda Cloud
 console.

- Find the row of the identity you want to delete, and then click its
 three-dot menu icon in the Actions column. A context menu appears.

- Click Delete service identity. A modal appears.

- If you're sure you want to delete the service identity, click Delete
 to finish deleting it.

## Managing groups#

### Create a group#

If you have an account role with the Group: Create permission, you
can create a new group in your account.

To create a new group:

- Navigate to the Groups tab on the
 IAM page in the Lambda Cloud
 console.

- Click Create new group.

- Enter a name for the group.

- Click Create group to finish creating the group.

### Add an identity to a group#

If you have an account role with the Group Membership: Create
permission, you can add an identity to an existing group in your account.

To add an existing identity to a group:

- Navigate to the Groups tab on the
 IAM page in the Lambda Cloud
 console.

- Find the group in the list, and then click its three-dot menu icon in the
 Actions column. A context menu appears.

- Click Manage identities.

- Click Add an identity.

- Click the Select identity dropdown and select the identity you want to
 add to the group.

- Click Add identity to finish adding the identity to the group.

### Remove an identity from a group#

If you have an account role with the Group Membership: Delete
permission, you can remove an identity from a group.

To remove an identity from a group:

- Navigate to the Groups tab on the
 IAM page in the Lambda Cloud
 console.

- Find the group in the list, and then click its three-dot menu icon in the
 Actions column. A context menu appears.

- Click Manage identities.

- Find the identity you want to remove in the list, and then click its
 three-dot menu icon in the Actions column. A context menu appears.

- Click Remove from group.

- If you're sure you want to remove the identity from the group, click
 Remove to finish removing it.

### Rename a group#

If you have an account role with the Group: Update permission, you
can rename an existing group in your account.

To rename a group:

- Navigate to the Groups tab on the
 IAM page in the Lambda Cloud
 console.

- Find the group in the list and then click its row.

- On the group details page, click Rename. A modal opens.

- Enter the new name.

- Click Rename to finish renaming the group.

### Delete a group#

If you have an account role with the Group: Delete permission, you
can delete a group from your account.

To delete a group:

- Navigate to the Groups tab on the
 IAM page in the Lambda Cloud
 console.

- Find the group in the list and then click its row.

- On the group details page, click Delete. A modal opens.

- If you're sure you want to delete the group, click Delete to finish
 deleting it.

Note

When you delete a group, its members lose any access they inherited
from the group.

## Next steps#

- Learn more about identity and access management (IAM) on Lambda Cloud

- Learn how to manage access to accounts, workspaces, and cloud resources

- Learn what roles are available and which permissions they grant

 Back to top
