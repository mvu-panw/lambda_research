# Cloud Console - Lambda Docs

Source: https://docs.lambda.ai/public-cloud/console/

Skip to content

# Lambda Cloud console#

You can use the
Lambda Cloud console
to manage your Lambda Cloud account and resources. This doc provides an
overview of the available features.

## Launch, restart, reboot, or terminate instances#

### Launch instances#

To launch an instance into your current workspace:

- Navigate to the Instances page in
 the Lambda Cloud console.

- Click Launch instance. A modal appears.

- 

Follow the Launch instance wizard to configure your instance:

- Instance type: Select the instance type that you want to launch.

- Region: Select the region in which you want to launch the instance.

- Base image: Select your preferred base image and then click Next.
 For a list of available images, see
 Alternative images.

- Filesystem: Optionally, select the filesystem you
 want to attach to your instance, or select Create a new filesystem
 to create and attach a new filesystem. If you'd prefer not to attach a
 filesystem, select Don't attach a filesystem.

- Security: Optionally, select an existing per-instance firewall ruleset
 to use or create a new one, then click Confirm.

- 

Select the SSH key that
 you want to use for your instance. If you haven't added a key to your
 account already, the wizard prompts you to add or generate one.

Tip

You can
add additional SSH keys
to your instance once the instance has launched.

- 

Click Launch instance.

- Review the license agreements and terms of service. If you agree to them,
 click Confirm and launch to launch your instance.

The newly launched instance appears in the instance list. After the instance
finishes booting, its external IP address appears in the list, and its status changes
from Booting to Running.

Tip

You can also use the Lambda Cloud API to
launch instances
or
get details of a running instance.

### Restart instances#

To restart one or more instances:

- Navigate to the
 Instances page
 in the Lambda Cloud console.

- In the instance list, click the checkbox for each instance you want to
 restart.

- Click Restart to restart your instances. The Restart button is
 located on the right side of the page above the instance list.

Tip

You can also use the Lambda Cloud API to restart instances. For details,
see Restart instances
in the Lambda Cloud API browser.

### Cold reboot instances#

A cold reboot is equivalent to:

- Pulling the plug on a physical server.

- Plugging the server back in and turning it on.

Warning

Only cold reboot your instance if it's completely frozen and
unresponsive. This action erases all data currently in the instance's
memory and bypasses the operating system's safe-shutdown mechanisms,
potentially resulting in additional issues.

To cold-reboot an instance:

- Navigate to the
 Instances page
 in the Lambda Cloud console.

- In the instance list, find the row of the instance you want to reboot and
 click ⋮. A context menu appears.

- Choose Cold reboot.

- When prompted, confirm your intent to reboot by typing cold reboot
 into the input field.

- Click Cold reboot instance to start the reboot process.

### Terminate instances#

Warning

Do not use commands such as sudo shutdown -h now or sudo systemctl
poweroff to try to terminate or suspend your instances. These commands will
not work as expected and will cause your instances to go into Alert status,
and billing will continue.

To terminate one or more instances:

- Navigate to the
 Instances page
 in the Lambda Cloud console.

- In the instance list, click the checkbox for each instance you want to
 terminate.

- Click Terminate. A modal appears.

- When prompted, confirm your intent to terminate by typing
 erase data on instance into the input field.
 to terminate.

- Click Terminate instances to terminate your instances.

Tip

You can also use the Lambda Cloud API to terminate one or more instances.
For details, see
Terminate instances
in the Lambda Cloud API browser.

## Create and manage Lambda filesystems#

### Create a Lambda filesystem#

In most cases, you create and attach a filesystem when you create a new
instance or 1-Click Cluster (1CC). To create a filesystem in your current
workspace without immediately attaching it to an instance or 1CC:

Important

You can't attach filesystems to an instance or 1CC after the instance
or 1CC has been created.

- Navigate to the
 Storage page in the Lambda Cloud
 console.

- Click Create filesystem. A dialog appears.

- Name your filesystem and select the region in which you want to create the
 filesystem. You must create your filesystem in the same region and workspace
 as the instance or 1CC you plan to attach it to.

- Click Create filesystem.

You should now see your filesystem listed in the console.

## Add, generate, and delete SSH keys#

### Add an existing SSH key#

To add an existing SSH key to your current workspace:

- Navigate to the SSH keys page
 in the Lambda Cloud console.

- Click Add SSH key. A dialog appears.

- Fill out the form:

- Name: Enter a name for the key you're adding.

- SSH public key: Paste your public SSH key.

- Click Add SSH key.

### Generate a new SSH key#

To generate a new SSH key in your current workspace:

- Navigate to the SSH keys page
 in the Lambda Cloud console.

- Click Add SSH key. A dialog appears.

- Click Generate a new SSH key.

- In the Name field, enter a name for your new key.

- Click Create. The private key for your new SSH key begins downloading
 automatically.

Tip

You can also use the Lambda Cloud API to
add and generate SSH keys.

### Delete SSH keys#

To delete an SSH key resource from your current workspace:

- Navigate to the SSH keys page
 in the Lambda Cloud console.

- In your key's row, in the Actions column, click Delete. A dialog
 appears.

- Click Delete SSH key.

## Generate and delete API keys#

### Generate an API key#

To generate a new API key:

- Navigate to Cloud API keys in the
 Lambda Cloud console.

- Click Generate API Key. A dialog appears.

- In the Generate API key dialog, provide a name for the new key.

- Click Generate API key to finish creating the key.

- Copy or download your key to a safe location. After you close the dialog,
 you won't be able to retrieve the key again.

### Delete an API key#

To delete an existing API key:

- Navigate to Cloud API keys in the
 Lambda Cloud console.

- In the table, find the row for the key you want to delete.

- In that row, click Delete. A dialog appears.

- If you're certain you want to delete the key, click Delete API key
 to delete it permanently.

## View usage#

To view your monthly resource usage and costs, navigate to the
Usage page in the console.

## Manage personal settings#

You can reset your password, set up multi-factor authentication, and generate
API keys by visiting the
User settings page in the
console.

## Modify account settings#

If you're an Account Admin or have another account role with the relevant
permissions, you can update your account's payment details, invite
or remove account users, manage user roles, create and manage workspaces,
and more from the Lambda Cloud console. For more information, see:

- IAM overview

- Managing your account

- Managing billing

- Managing identities and groups

- Managing access

- Managing your workspaces.

 Back to top
