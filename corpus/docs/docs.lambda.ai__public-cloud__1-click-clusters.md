# Introduction - Lambda Docs

Source: https://docs.lambda.ai/public-cloud/1-click-clusters/

Skip to content

# Introduction#

1-Click Clusters (1CC) are high-performance clusters composed of both GPU and
CPU nodes, featuring 16 to 512 NVIDIA H100 or B200 SXM Tensor Core GPUs. GPU
nodes are interconnected using an NVIDIA Quantum-2 400 Gb/s InfiniBand
non-blocking fabric in a rail-optimized topology, enabling peer-to-peer
GPUDirect RDMA at up to 3200 Gb/s. All nodes (GPU and CPU) are equipped with
2×100 Gb/s Ethernet NICs for IP connectivity. Direct Internet Access (DIA) is
delivered over shared upstream capacity at the datacenter edge and is not
dedicated per tenant.

Each 1CC includes 3x CPU management (head) nodes for use as jump boxes (bastion hosts) and for cluster administration and job scheduling. These management nodes are assigned public IP addresses and are directly accessible over the Internet via SSH.

All nodes can be directly accessed using JupyterLab from the Lambda Cloud console.

1CC nodes are in an isolated private network and can communicate freely with each other using private IP addresses.

Generic CPU nodes can optionally be launched in the same regions as 1CCs. These generic CPU nodes run independently of 1CCs and don't terminate when 1CC reservations end.

Each compute node includes 24TB of usable local ephemeral NVMe storage. Each management node includes 208GB of usable local ephemeral NVMe storage. Lambda filesystems are automatically created and attached to each 1CC node, and can also be attached to Lambda On-Demand instances. Existing filesystems in the same region can additionally be attached. You’re billed only for the storage you actually use.

All 1CC nodes are preinstalled with Ubuntu 22.04 LTS and Lambda Stack, including NCCL, Open MPI, PyTorch® with DDP and FSDP support, TensorFlow, OFED, and other popular libraries and frameworks for distributed ML workloads, allowing ML engineers and researchers to begin their large-scale experiments and other work immediately after launching a 1CC.

Note

It's highly recommended that you use Lambda Stack's Python packages. Lambda
Stack packages are extensively tested for compatibility and reliability in
1CC environments. Packages installed outside of Lambda Stack might not work
properly, especially with newer GPUs.

See our documentation on
creating a Python virtual environment
to learn how to use Lambda Stack's Python packages.

## Reserving 1-Click Clusters#

See our video guide on how to reserve and launch a 1-Click Cluster.

To reserve a 1CC:

- If you haven’t already, generate or add an SSH key for your 1CC.

- Navigate to the 1-Click Clusters page in the Lambda Cloud console and click Reserve 1-Click Cluster.

- Use the 1CC reservation wizard to reserve your cluster.

- Type/Duration: Enter the duration in weeks that you want to reserve the cluster, and then select the cluster type you want to launch.

- Region: Select the region in which you want to launch your cluster.

- Filesystem: Optionally, select an existing file system that you want to attach to the cluster, or click Create a new filesystem to create a new file system. If you don’t want to attach an existing file system or create a new file system, click Don’t attach a filesystem (an empty one will be created).

- SSH Key: Select the SSH key that you want to use to access your cluster, then click Next.

- Cluster name: Enter a name for your cluster, then click Continue to Payment. You’re presented with a billing summary and the billing information you have saved to your Lambda Cloud account.

- 

If needed, update your billing information and change the email address where you’d like the invoice for your 1CC reservation to be sent.

Note

Only the invoice will be sent to this email address. All notifications and other information regarding your 1CC will be sent to the email address associated with your account.

- 

Review the listed policies and terms of service. If you agree to the policies and terms of service, click the checkbox under Terms and Conditions.

- Click Submit reservation request. Within a few minutes, you’ll receive an email confirming your 1CC reservation request.

You can check the status of your 1CC reservation request or cancel your request by visiting the Instances page in the Lambda Cloud console.

### Completing your 1-Click Cluster reservation#

When your reservation is approved, you’ll receive an email with your invoice and payment instructions.
This email will be sent to the address you entered when making your reservation, which might be different from the email associated with your Lambda Cloud
account.

The invoice must be paid within 10 days of approval of your 1CC reservation. Otherwise, you risk losing your reservation. Daily reminder emails will be sent until the invoice is paid or the reservation is canceled.

Your 1CC will automatically launch on the day your reservation begins. You’ll be sent an email informing you that your cluster is launching, and that you should check your Lambda Cloud console to monitor the status of your 1CC.

## Accessing your 1-Click Cluster#

See our video guide on accessing your 1-Click Cluster.

Your 1CC's management nodes have public IP addresses and can be accessed directly via SSH. You can access your compute nodes via SSH using a management node as a jump box. You can also access both your management nodes and your compute nodes using JupyterLab.
If you want to access your management nodes through SSH, make sure your Firewall rules are configured to allow SSH traffic.

To access your management nodes and compute nodes via SSH:

- 

Navigate to the 1-Click Clusters page in the Lambda Cloud console.

- 

At the top of the table of your 1CC’s nodes, next to SSH LOGIN, click SETUP.

Follow the instructions in the INITIAL CLUSTER SETUP dialog, then click Next.

Tip

Follow these instructions on any other computers you want to use to access your 1CC. Make sure those computers have the SSH key that you chose when you reserved your 1CC.

- 

Follow the instructions in the SETUP INTER-NODE PASSWORDLESS SSH dialog. You can now SSH into each of your nodes using their names, which you can obtain from the Lambda Cloud console. You can also SSH from each of your nodes into the other nodes.

Warning

The computer where you’re running the script must have both your cluster SSH config, downloaded in the previous step, and the SSH key that you chose when you reserved your 1CC.

- 

Click Done to close the dialog.

### Adding SSH keys#

You can add SSH keys to your 1CC to allow others to log in.

To add another SSH key:

- 

From the Lambda Cloud console, save the names of your 1CC nodes into a text file. You can do this by copy and pasting from the console. The file should contain the names of your nodes, each on a separate line, and should look like:

us-east-2-1cc-node-1
us-east-2-1cc-node-2
us-east-2-1cc-node-3
us-east-2-1cc-node-4
us-east-2-1cc-head-1
us-east-2-1cc-head-2
us-east-2-1cc-head-3

- 

Add the additional SSH key to your 1CC by running:

while read node; \
do ssh -n -F CLUSTER-SSH-CONFIG "$node" "echo 'PUBLIC-KEY' >> ~/.ssh/authorized_keys" && echo "Key added to $node"; \
done < LIST-OF-NODES

In this command:

- Replace CLUSTER-SSH-CONFIG with the path to your cluster SSH config. The path should look like ~/.ssh/config.d/config.us-east-2-1cc.

- 

Replace PUBLIC-KEY with the public key you want to add to your 1CC nodes. Public keys look like:

ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIK5HIO+OQSyFjz0clkvg+48YAihYMo5J7AGKiq+9Alg8 user@hostname

- 

Make sure to keep the single quotes (' ').

- Replace LIST-OF-NODES with the name of the file containing the names of your nodes.

## Copying data to your 1-Click Cluster#

See our video guide on copying data to your 1-Click Cluster.

### Using the Filesystem S3 Adapter#

As of April 2025, Lambda has begun rolling out the Filesystem S3 Adapter, which
allows you to use S3-compatible tools like rclone and s5cmd to copy
files to your attached filesystems. This feature is currently available
in select regions only. To read more about the Filesystem S3 Adapter and to
see if it's available in your region, see
Filesystem S3 Adapter.

### Using rsync#

If the Filesystem S3 Adapter isn't available in your region yet, we recommend
using rsync to copy data to your 1CC. rsync allows you to copy files from
your computer to your 1CC, as well as directly from a running on-demand instance
to your 1CC.

See our documentation to learn how to use rsync. When following the instructions, replace SERVER-IP with the name of one of your management nodes.
Unless you copy your data to a Lambda filesystem, your data will only be accessible from the nodes your data was copied to.

If your data isn’t saved to a Lambda filesystem, you can copy your data from one node to another by following our instructions on copying files directly between remote servers.
For higher performance, you can also use rsync to copy data from your Lambda filesystem to your nodes’ local ephemeral storage.

## Ending your 1-Click Cluster reservation#

See our video guide on ending your 1-Click Cluster reservation.

Beginning three days prior to your 1CC reservation ending, you’ll be sent a daily email reminding you that your reservation is ending.

Warning

All data saved to ephemeral local storage will be deleted and unrecoverable once your reservation ends! You’re responsible for backing up your data, for example, to a Lambda filesystem.

It’s not currently possible to extend or renew your 1CC reservation. You’ll need to request a new reservation.

 Back to top
