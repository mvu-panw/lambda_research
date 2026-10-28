# How to Transfer Data to Lambda Cloud GPU Instances

Source: https://lambda.ai/blog/downloading-data-sets-lambda-cloud

Skip to main content

# How to Transfer Data to Lambda Cloud GPU Instances

 May 3, 2020

 (Updated on August 12, 2022)

 • 7 min read

 You can now use Lambda Cloud High Speed Filesystems to permanently store data on the Lambda Cloud. 
 Click here to learn how to use Lambda Cloud Filesystems.

This guide will walk you through how to load data from various sources onto your Lambda Cloud GPU instance. If you're looking for how to get started and SSH into your instance for the first time, check out our Getting Started Guide. 

In this guide we'll cover how to copy data onto and off of your instance from: 

- A local desktop or laptop using SCP 
 
- Publicly accessible urls and buckets using Wget 
 
- Private S3 Buckets 
 
- Private Google Cloud Storage Buckets 
 
- Private Azure Blob Storage Containers 

## Copying files to or from your desktop or laptop 

This specific section assumes you're using either MacOSX or Linux. If you're using Windows, you can install Windows Subsystem for Linux (WSL) and continue following along as normal. 

In order to copy files from your local machine to your Lambda Cloud instance, you will first need to have SSH setup correctly on your local machine. If you haven't done that yet, you can follow our guide. 

Once you have SSH setup, it only takes a single command to copy files to your Lambda Cloud instance. However, you'll need to modify it slightly first. This command should be run in your local terminal (while not connected via SSH to your instance). 

scp -i ~/.ssh/my-key.pem ~/path/to/local_file ubuntu@instance-ip-address:~/.

To use this command you'll need to replace my-key with the name of the SSH key you created to connect to your instance (don't forget the .pem). 

Next you'll need to replace ~/path/to/local_file with the local file on your machine. Remember that ~ is short hand for your home directory, so if you wanted to upload a data set in your Documents folder you would type something like: ~/Documents/my-data-set.csv. 

After that you'll need to replace instance-ip-address with the IP address listed for your instance in the Lambda Cloud Dashboard. 

Optionally, you can also replace the ~/. with whatever path you would like to copy the data to on your cloud instance. If you leave it as is, it will be copied into your home directory on the instance. 

### Copying results from your instance back to your local machine 

Copying files back to your local machine is nearly the same as before. However, you have to flip the local and remote paths. 

scp -i ~/.ssh/my-key.pem ubuntu@instance-ip-address:~/results.ckpt .

You still need to update the my-key.pem well as instance-ip-address with your own. This time you specify the remote file you would like to copy e.g. ~/results.ckpt and then tell scp where to send it e.g. . (. being the current directory). 

## Copying files from publicly accessible URLs and cloud storage buckets 

To copy files from a public url or cloud storage bucket we recommend using wget. 

First make sure you're connected via SSH to your cloud instance and then run: 

wget https://example.com/example-data-set.tar.gz

where https://example.com/example-data-set.tar.gz is the publicly accessible url of the data set you'd like to download. This works for publicly accessible S3, Azure, or Google Cloud bucket urls. 

If you need to download files from private buckets, we cover that a little further down. 

### Opening compressed data sets 

If the data set you've downloaded is compressed as a file with the .tar.gz extension you can decompress it using the tar command like so: 

tar -xvf example-data-set.tar.gz

If your data set is compressed as a file with the .zip extension you'll have to first install unzip using the command: 

sudo apt-get install unzip

After installation you can then unzip the data set in its current folder using the unzip command: 

unzip example-data-set.zip

If you'd like to move the data set to a new directory when you unzip it, you can use the command: 

unzip example-data-set.zip -d /path/to/new/directory

## Copying files from private S3, Azure, or Google Cloud buckets 

To copy files from a private cloud storage bucket we recommend installing the CLI of the specific cloud provider on your Lambda Cloud instance. 

### S3 — using the AWS CLI 

We recommend installing the AWS CLI via pip which comes preinstalled on the base image for Lambda Cloud. 

To get the AWS CLI up and running for syncing files from S3 you'll need to SSH into your Lambda Cloud instance and then: 

- Install the AWS CLI via pip by following the instructions for Linux. 
 
- Configure the CLI to use the correct credentials for accessing the desired bucket. 
 
- Follow the S3 CLI documentation on using the aws s3 sync command to copy the desired files. 

The most common errors we see with using the AWS CLI to download files from or upload files to S3 involve incorrect IAM roles and permissions. It's important to make sure that the IAM user associated with the access key you use has the correct permissions to read from and write to the desired bucket. 

### Google Cloud Storage — working with gcloud and gsutil 

The recommended command line tool for working with Google Cloud Storage is gsutil which can be installed either standalone or as part of the larger Google Cloud SDK (recommended). 

To get the Google Cloud SDK up and running for syncing files from Google Cloud Storage you'll need to SSH into your Lambda Cloud instance and then: 

- Install the Google Cloud SDK using the Ubuntu Quickstart Guide. 
 
- Login to the account that has permissions to access the bucket holding the desired files. 
 
- Follow the documentation for the gsutil cp command to upload and download the desired files. 

When initializing the Google Cloud SDK you'll need to use the --console-only flag. 

gcloud init --console-only

If you don't use this flag, the SDK will fail to open a web browser on your Lambda Cloud instance. By using the command, the Google Cloud SDK will provide you with a link that can be opened on your local machine. Once you authenticate with Google Cloud, you will be given a code that can be provided to the SDK. 

### Azure Blob Storage — working with AzCopy 

Working with the AzCopy CLI for Azure Blob storage requires a bit more effort than the other two providers. 

First you'll need to go to the AzCopy documentation and copy the link to the latest Linux tar file. Once you have the link, you should SSH into your Lambda Cloud instance and run the following command with your copied URL to download the file. 

wget https://aka.ms/downloadazcopy-v10-linux

At time of writing I'm downloading AzCopy v10, but you should use the URL you copied as it may have changed. 

After downloading, if you run the ls command, you should see a file that looks like downloadazcopy-v10-linux. Next you'll want decompress this file using the tar command. Replacing downloadazcopy-v10-linux with the name version that was downloaded to your machine. 

tar -xvf downloadazcopy-v10-linux

After decompressing the file, if you run the ls command again you should now see a folder with a name similar to azcopy_linux_amd64_10.4.1. Inside should be the azcopy binary and third party license notice. 

To have the azcopy command available everywhere you're going to need to make a ~/.local/bin directory and move the binary there. This can be done by running the commands (remember to replace azcopy_linux_amd64_10.4.1 with the name you see on your machine): 

mkdir ~/.local/bin
mv ~/azcopy_linux_amd64_10.4.1/azcopy ~/.local/bin/azcopy

Finally, we can clean everything up with the commands (remembering to replace the file and folder names appropriately): 

rm -r ~/azcopy_linux_amd64_10.4.1/
rm downloadazcopy-v10-linux

You should now be able to run the command azcopy from anywhere on your machine, but it still needs to be authorized following the instructions in the Azure documentation. 

Once you've authorized correctly, you can use the azcopy copy command instructions to download files from your private blob storage containers. 

## Final thoughts 

Now that you have your data downloaded it's time to start training! Don't forget to check out our Jupyter Notebook environment in the Lambda Cloud dashboard. 

Lambda Cloud instances are billed by the hour from the time you spin them up to the time you terminate them in the dashboard. We do not currently offer persistent storage, so if you do decide to terminate your instance, all data will be deleted and you will have to re-download it next time you spin up an instance. 

Any feedback or questions? Reach out to us at cloud@lambdalabs.com 

## AUTHORED BY

 Remy Guercio

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
