# Filesystems - Lambda Docs

Source: https://docs.lambda.ai/public-cloud/filesystems/

Skip to content

# Filesystems#

A filesystem is a high-capacity regional file store you can attach to your
instance to store datasets and back up system state. In most regions, each
filesystem has a capacity of 8 EB (8,000,000 TB), and you can create up to
24 total filesystems. In the Texas, USA (us-south-1) region, filesystems are
currently limited to 10 TB of capacity.

For information on how filesystems are billed, see the
Billing overview.

## Accessing your filesystem#

### Accessing from another instance or a 1-Click Cluster#

To access a filesystem from within Lambda Cloud:

- The filesystem must reside in the same region as the instance or cluster.

- You must attach the filesystem to your instance or cluster at the time that
 the instance or cluster is launched.

- You must have access to the workspace in which the filesystem resides.

Note

Filesystems cannot currently be transferred between regions.

### Accessing remotely#

You can remotely access your filesystem in two ways:

- Filesystem S3 Adapter (select regions only): This adapter allows you to
 use S3-compatible tools like rclone and s5cmd to copy files to and from
 your filesystems and perform common file operations. For more information,
 including a list of supported regions, see
 Filesystem S3 Adapter.

- rsync: If your filesystem's region doesn't support the Filesystem S3
 Adapter yet, you can use rsync to copy files to and from your instance
 and any filesystem mounted on that instance. For more information, see
 Importing and exporting data.

Note

Filesystems can't be attached to running instances and can't be mounted
remotely using NFS or similar protocols.

## Managing your filesystems#

### Creating a new filesystem#

In most cases, you create and attach a filesystem when you create a new
instance or 1-Click Cluster (1CC). To create a filesystem without immediately
attaching it to an instance or 1CC:

Important

You can't attach filesystems to an instance or 1CC after the instance
or 1CC has been created.

- In the Lambda Cloud console, navigate to the
 Storage page.

- Click Create filesystem. A dialog appears.

- Name your filesystem and select the region in which you want to create the
 filesystem. You must create your filesystem in the same region and workspace
 as the instance or 1CC you plan to attach it to.

- Click Create filesystem.

You can also create and filesystems using the Cloud API. For more
information, see
Create filesystem in the
Cloud API docs.

### Viewing your existing filesystems#

To view your existing filesystems, visit the
Storage page in the Lambda Cloud
console.

You can also list existing filesystems using the Cloud API. For more
information, see
List filesystems
in the Cloud API docs.

### Deleting a filesystem#

To delete a filesystem:

- If needed, back up any important data on the instance your filesystem is
 connected to, and then terminate that instance. Your filesystem must be
 detached from all instances before it can be deleted.

- If needed, back up any important data from your filesystem. For guidance on
 how to back up data, see
 Importing and exporting data.

- In the Lambda Cloud console, navigate to the
 Storage page.

- In the row for the filesystem you want to delete, in the Actions
 column, click Delete. A dialog appears.

- Follow the instructions in the dialog and click Delete filesystem.

You can also delete a filesystem using the Cloud API. For more
information, see
Delete filesystem in the
Cloud API docs.

## Managing cost#

### Viewing filesystem usage#

To view your monthly usage, navigate to the
Usage page in the Lambda Cloud console and
then click the Filesystems tab.

### Setting usage limits#

Currently, you can't set a limit (quota) on your filesystem usage. You can see
the usage of a filesystem from within an instance by running df -h -BG. This
command produces output similar to:

Filesystem 1G-blocks Used Available Use% Mounted on
tmpfs 44G 1G 44G 1% /run
efivarfs 1G 1G 1G 2% /sys/firmware/efi/efivars
/dev/vda1 3969G 24G 3946G 1% /
tmpfs 216G 1G 216G 1% /dev/shm
tmpfs 1G 0G 1G 0% /run/lock
/dev/vda15 1G 1G 1G 7% /boot/efi
10.12.69.11:/768f824a-2608-4200-8a6a-3d2996d10587 6792422G 0G 6792422G 0% /lambda/nfs/persistent-storage
tmpfs 44G 1G 44G 1% /run/user/1000

In the example output, above:

- The name of the filesystem is persistent-storage.

- The size of the filesystem is 6792422G.

- The available capacity of the filesystem is 6792422G.

- The used percentage of the filesystem is 0%.

- The filesystem is mounted on /lambda/nfs/persistent-storage.

Note

You can also use the Cloud API's /file-systems endpoint to find out your
filesystem usage. For details, see
List filesystems
in the Cloud API browser.

### Managing auto-generated application data#

Applications that follow the Freedesktop.org
Trash Specification,
such as JupyterLab, might create hidden .Trash-* directories on your mounted
filesystems. Files moved to these directories are not automatically
deleted and will count towards your billed storage usage until you
permanently delete them. For guidance on managing your .Trash-* directories,
see
Emptying .Trash-* directories.

## Next steps#

- For guidance on transferring data to and from your Lambda filesystems, see
 Importing and exporting data.

 Back to top
