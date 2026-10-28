# Filesystem S3 Adapter - Lambda Docs

Source: https://docs.lambda.ai/public-cloud/s3-adapter-filesystems/

Skip to content

# Filesystem S3 Adapter#

See our video guide on using the Filesystem S3 Adapter.

The Filesystem S3 Adapter allows you to interact with your Lambda filesystems
using rclone, s5cmd, mc, and other S3-compatible tools. Supported
operations include:

- Listing the files and folders on your filesystem.

- Transferring or copying files and folders to and from your filesystem.

- Deleting files and folders from your filesystem.

As of April 2025, this feature is available in select regions only. For
the current list of supported regions, see
API regions and endpoints below.

Note

While the Filesystem S3 Adapter is designed to be compatible with S3
tooling, it is not designed to be a replacement for a full-fledged object
storage offering.

Important

The API works with Lambda filesystems created in March 2025 or later.
Filesystems created earlier might not be supported.

## API regions and endpoints#

Lambda currently provides Filesystem S3 Adapter endpoints in the following
regions:

 | Endpoint
 | Region
 | Physical location

 | files.us-east-2.lambda.ai
 | us-east-2
 | Washington DC, USA

 | files.us-east-3.lambda.ai
 | us-east-3
 | Washington DC, USA

 | files.us-midwest-2.lambda.ai
 | us-midwest-2
 | Ohio, USA

## Setting up API access#

### Creating your API credentials#

To create your credentials:

- Navigate to the
 Filesystem S3 Adapter Keys page
 in the Lambda Cloud console.

- Click Generate access key pair. A modal dialog appears.

- Select your filesystem's region in the Region list, and then click
 Generate access key pair.

- Copy or download your credentials.

Important

Copy or download your credentials while the dialog is open. You won't
be able to view your secret key again after you close the dialog.

### Obtaining the bucket name for your filesystem#

Each filesystem has a UUID that also serves as its bucket name. To obtain this
name:

- Navigate to the
Filesystems page
in the Lambda Cloud console.

- Locate your filesystem in the table.

- In the Bucket name column, click your filesystem's bucket name to copy
it.

### Setting up access to your filesystem#

After you've obtained your credentials and bucket name, you can configure
an S3-compatible file management tool to access your filesystem.

rclones5cmd

In rclone, you set up an S3-compatible endpoint as a remote
and then address that remote when you run S3 operations. To
set up your Lambda filesystem as a remote:

- 

Start the rclone configuration wizard:

rclone config

- 

Type N and press Enter to start creating a new remote.

- 

Fill out the requested information:

- Name: Provide a name for your remote.

- Option storage: Select the option that begins with Amazon S3
 Compliant Storage Providers.

- Option provider: Select
 Any other S3 compatible provider (other).

- Option env_auth: Choose Enter AWS credentials in the next step.

- Option access_key_id: Enter the access key you generated earlier.

- Option secret_access_key: Enter the secret key you generated
 earlier.

- Option region: Enter the region in which your filesystem
 resides—for example, us-east-2.

- Option endpoint: Enter the API endpoint you're using. This endpoint
 should match your filesystem's region. For example, if your
 filesystem is in us-east-2, your endpoint should be
 files.us-east-2.lambda.ai.

- Option location_constraint: Use the default.

- Option acl: Choose permissions that are appropriate for your use
 case.

- 

When prompted to Edit advanced config?, press Enter to move on to the
 next step. A summary
 of your configuration appears.

- Press Enter to keep your remote, and then type Q and press Enter to exit
 the wizard.

To configure s5cmd to access your filesystem/bucket:

- 

Open .bashrc or, if you're using a Mac, .zshrc:

nano $HOME/.bashrc

- 

Add the following environment variables to the file. Replace each
 placeholder variable with your credentials, filesystem region, and
 regional endpoint.

export AWS_ACCESS_KEY_ID='<ACCESS-KEY>'
export AWS_SECRET_ACCESS_KEY='<SECRET-KEY>'
export AWS_REGION='<FILESYSTEM-REGION>'
export S3_ENDPOINT_URL='https://<REGIONAL-ENDPOINT>'

- 

If needed, update your terminal to reflect the changes. As before,
 if you're using a Mac, replace .bashrc with .zshrc:

source $HOME/.bashrc

Note

s5cmd supports other methods of specifying credentials as well.
For details, see the
Specifying credentials
section of the s5cmd documentation.

## Performing common operations#

This section shows how to use rclone or s5cmd to perform common
operations supported by the adapter. For detailed guidance on using these tools,
see the
Rclone documentation and
s5cmd documentation.

### Listing your filesystem data#

rclones5cmd

To list your filesystem's top-level files:

rclone ls <REMOTE>:<BUCKET-NAME>

To list only your filesystem's directories:

rclone lsd <REMOTE>:<BUCKET-NAME>

Tip

You can list of all of the filesystems you have in the region by
omitting <BUCKET-NAME>.

To list your files and their detailed metadata:

rclone lsl <REMOTE>:<BUCKET-NAME>

To list your filesystem's top-level files:

s5cmd ls s3://<BUCKET-NAME>/

To list your filesystem's files and directories recursively:

s5cmd ls "s3://<BUCKET-NAME>/*"

### Transferring files to and from another cloud#

rclones5cmd

To copy files from an S3-compatible object store to your Lambda filesystem,
set up the source store as an additional remote, and then use the following
pattern:

rclone copy <SOURCE-REMOTE>:<BUCKET-NAME>/<PATH> <TARGET-REMOTE>:<BUCKET-NAME>/<PATH> --progress

s5cmd doesn't support cloud-to-cloud data transfer. However, if you have
a local machine with sufficient storage capacity, you can copy your
files to that machine, and then copy from that machine to your Lambda
filesystem. For details, see
Transferring files to and from your local machine
below.

### Transferring files to and from your local machine#

rclones5cmd

To copy a local file or directory to a directory on your filesystem:

rclone copy <PATH-TO-LOCAL-FILE-OR-DIR> <REMOTE>:<BUCKET-NAME>/<PATH> --s3-no-check-bucket --progress

To copy a file or directory from your filesystem to a local directory:

rclone copy <REMOTE>:<BUCKET-NAME>/<PATH-TO-FILE-OR-DIR> <PATH-TO-LOCAL-FILE-OR-DIR> --progress

To copy files from a local directory to a directory on your filesystem:

s5cmd cp "<PATH-TO-LOCAL-DIR>/*" "s3://<BUCKET-NAME>/<PATH-TO-DIR>"

To copy files from a directory on your filesystem to a local directory:

s5cmd cp "s3://<BUCKET-NAME>/<PATH-TO-DIR>/*" "<PATH-TO-LOCAL-DIR>"

### Deleting files and folders from your filesystem#

rclones5cmd

To delete a specific file or directory:

rclone delete <REMOTE>:<BUCKET-NAME>/<PATH-TO-FILE-OR-DIR>

To delete a specific file:

s5cmd rm s3://<BUCKET-NAME>/<PATH-TO-FILE>

To delete a specific directory:

s5cmd rm "s3://<BUCKET-NAME>/<PATH-TO-DIR>/*"

## Troubleshooting#

### aws s3 cp returns a NotImplemented error#

As of April 2025, aws s3's default checksum behavior is currently
incompatible with the Filesystem S3 Adapter. To fix this issue:

- Open ~/.aws/config for editing.

- 

Under the profile for your Lambda filesystem, add the following lines:

request_checksum_calculation = 'WHEN_REQUIRED'
response_checksum_validation = 'WHEN_REQUIRED'

## Next steps#

- Read more about Filesystems.

 Back to top
