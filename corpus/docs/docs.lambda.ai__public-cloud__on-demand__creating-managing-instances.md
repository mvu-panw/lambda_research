# Creating and managing instances - Lambda Docs

Source: https://docs.lambda.ai/public-cloud/on-demand/creating-managing-instances/

Skip to content

# Creating and managing instances#

This doc outlines how to create and manage On-Demand Cloud (ODC) instances. For
general guidance on managing your ODC instance's system environment, see
Managing your system environment.

## Viewing available instance types#

To view available instance types, navigate to the
Instances page
in the Lambda Cloud console and click Launch instance to start the
instance creation wizard. The first page of the wizard dialog lists all of
the instance types Lambda currently offers.

You can also programmatically view available instance types by using the Lambda
Cloud API. For details, see
List available instance types
in the Lambda Cloud API browser.

## Launching instances#

To launch a new instance, navigate to the
Instances page
in the Lambda Cloud console, click Launch instance, and then follow the
steps in the instance creation wizard.

You can also launch instances programmatically by using the Lambda Cloud API.
For details, see
Launch instances
in the Lambda Cloud API browser.

Instances might take several minutes to launch.

Note

New accounts have a limit on the number of instances you can launch. This
quota helps prevent abuse and increases automatically as you pay your
invoices. If you attempt to launch an instance that exceeds this limit, you
will see a notification that your quota has been reached.

### Use a different base image#

In addition to the options provided through the Lambda Cloud console, the
API allows you to use a different base image for your instance. For a list of
available images, see the Alternative images
section in the On-Demand Cloud overview. You can also
programmatically list all available images by calling the
List available images
endpoint in the Lambda Cloud API browser.

### Automatically configure your instance at launch time#

If you're launching your instance with the Lambda Cloud API, you can add
launch-time configuration instructions using
cloud-init.

## Viewing instance metadata#

### List your instances#

To view a list of your running instances, visit the
Instances page
in the Lambda Cloud console.

You can also retrieve more detailed information about your instances, including
their IDs, private IPs, and attached filesystems, by using the Lambda Cloud API.
For details, see
List running instances
in the Lambda Cloud API browser.

### View instance usage#

To view your monthly usage, navigate to the
Usage page
in the Lambda Cloud console and then click the Instances tab.

## Restarting an instance#

To restart one or more instances:

- Navigate to the
 Instances page
 in the Lambda Cloud console.

- In the instance list, click the checkbox for each instance you want to
 restart.

- Click Restart to restart your instances. The Restart button is
 located on the right side of the page above the instance list.

You can also restart instances programmatically by using the Lambda Cloud API.
For details, see
Restart instances
in the Lambda Cloud API browser.

## Terminating an instance#

To terminate one or more instances:

- Navigate to the
 Instances page
 in the Lambda Cloud console.

- In the instance list, click the checkbox for each instance you want to
 terminate.

- Click Terminate to terminate your instances. The Terminate button is
 located on the right side of the page above the instance list.

You can also terminate instances programmatically by using the Lambda Cloud API.
For details, see
Terminate instances
in the Lambda Cloud API browser.

Warning

Do not use commands such as sudo shutdown -h now or sudo systemctl
poweroff to try to terminate or suspend your instances. These commands will
not work as expected and will cause your instances to go into Alert status,
and billing will continue.

## Suspending an instance#

At the moment, Lambda Cloud instances can only be launched, restarted, or
terminated. To preserve state, we recommend using Docker to containerize your
environment and performing regular backups of important data. For detailed
guidance, see Importing and exporting data.

Warning

Do not use commands such as sudo shutdown -h now or sudo systemctl
poweroff to try to terminate or suspend your instances. These commands will
not work as expected and will cause your instances to go into Alert status,
and billing will continue.

## Next steps#

- New to ODC? Check out the ODC Overview.

- For more information on the endpoints available in the Lambda Cloud API, see
 the
 Lambda Cloud API browser.

 Back to top
