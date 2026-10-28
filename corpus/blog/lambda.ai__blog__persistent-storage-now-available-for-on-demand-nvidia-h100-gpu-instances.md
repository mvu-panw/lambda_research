# Persistent storage now available for on-demand NVIDIA H100 GPU instances

Source: https://lambda.ai/blog/persistent-storage-now-available-for-on-demand-nvidia-h100-gpu-instances

Skip to main content

# Persistent storage now available for on-demand NVIDIA H100 GPU instances

 December 19, 2023

 • 1 min read

Persistent storage for Lambda Cloud recently exited beta and became available in the majority of regions. We are excited to announce that filesystems are now available in all Lambda Cloud regions and for all on-demand instance types. This includes persistent storage on our NVIDIA H100 Tensor Core GPU instances, both 8x and 1x varieties, meaning on-demand customers can now create filesystems in ALL regions within Lambda Cloud to persist files and data when using Lambda’s compute. 

Storage for Lambda Cloud instances costs $0.20/GB/month, though filesystems in our Texas region will remain free until the end of 2023. There are no ingress or egress charges associated with Lambda’s storage solution. However, there may be ingress/egress charges from other services if you are moving data to and from other storage services.

There is also no quota or hard limit to how much you can store in your filesystems. This decision was made consciously to avoid creating artificial limits that could get in the way of your work. Customers should check the usage page in the Lambda Cloud dashboard to keep track of storage usage.

Keep in mind that filesystems are not global and cannot be attached across regions. For example, a filesystem in the California region cannot be attached to an instance in the Virginia region. 

Currently, data in filesystems cannot be accessed without attaching to a VM, so we recommend you download data that you anticipate needing (e.g., weights from your training job, etc.) before shutting down your instance.

For more information on billing, how to use Lambda Cloud’s filesystems, and other FAQs, check out our documentation page.

Happy training!

Lambda Team!

## AUTHORED BY

 Kathy Bui

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
