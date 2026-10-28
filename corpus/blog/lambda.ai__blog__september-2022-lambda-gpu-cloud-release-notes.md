# September 2022 Lambda GPU Cloud Release Notes

Source: https://lambda.ai/blog/september-2022-lambda-gpu-cloud-release-notes

Skip to main content

# September 2022 Lambda GPU Cloud Release Notes

 October 11, 2022

 (Updated on November 3, 2022)

 • 2 min read

While we continue to add more NVIDIA A100s to our cloud, the Lambda GPU cloud team is also making upgrades and improvements to make our cloud platform easier to use. Here is a  summary of what you can expect from the most recent upgrades.

## Tripled the speed of persistent storage

Depending on the specific machine learning workload, persistent storage is up to 3x faster than it was in September, 2022. Our engineers implemented both hardware and software changes to our Cloud storage infrastructure to increase both read/write speeds. In certain cases, the number of IOPS (input/operations per second) is higher, providing higher performance.

## Increased our Cloud's Internet connection bandwidth from 1 Gbps to 10 Gbps

The links that connect our Cloud to the Internet underwent a major overhaul, increasing our bandwidth to 10 Gbps—10x what our bandwidth used to be.

## Added the ability to choose what region an instance launches in

It’s now possible to choose the region in which an instance is launched. You can launch an instance in a region that’s physically close to you, which often reduces latency and increases transfer speeds between your system and your instance.

Currently, persistent storage is only available in our Texas region while we work on adding it to all regions. Persistent storage can only be attached to instances that are in the same region.

## Added instance start and termination times to the resource usage dashboard

You can now analyze the start and termination times of your instances to better understand your instance usage and billing.

## Simplified copying of SSH login information

You can now easily copy your instance’s SSH login information with a single click.

Stay tuned for more release notes as we continue to make improvements and add new features to the Lambda GPU Cloud platform.

## AUTHORED BY

 Cody Brownstein

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
