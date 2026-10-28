# Persistent storage for Lambda Cloud is expanding!

Source: https://lambda.ai/blog/persistent-storage-for-lambda-cloud-is-expanding

Skip to main content

# Persistent storage for Lambda Cloud is expanding!

 September 20, 2023

 • 2 min read

Persistent storage for Lambda Cloud has been in open beta within our Texas region since April 2022. We are excited to announce that Lambda persistent storage is exiting beta and is now available in the majority of regions within Lambda Cloud! 

This means that on-demand customers can now create filesystems in most regions within Lambda Cloud to persist files and data when using Lambda’s compute. At the time of this announcement, filesystems are available for all regions except for Utah, but rest assured that we’re working hard on getting persistent storage to this last region by the end of 2023.

With storage exiting beta, we will also start to charge for storage. However, filesystems in our Texas region will remain free until the end of 2023. We will send out reminders every month until then to make sure that customers have ample time to transition before we start charging. For all new regions available starting today, storage will cost $0.20/GB/month.

There are no ingress or egress charges associated with Lambda’s storage solution. However, if you are moving data to and from other storage services, please be mindful that there could be ingress/egress charges from other services even though there are no charges from Lambda Cloud.

There is also no quota or hard limit to how much you can store in your filesystems. This decision was made consciously to avoid creating artificial limits that could get in the way of your work. We encourage customers to check the usage page in the Lambda Cloud Dashboard to keep track of storage usage.

Keep in mind that filesystems are not global and cannot be attached across regions. For example, a filesystem in the California region cannot be attached to an instance in the Virginia region. 

Currently, data in filesystems cannot be accessed without attaching to a VM, so we recommend you download data that you anticipate needing (e.g. weights from your training job, etc.) before shutting down your instance.

For more information on billing, how to use Lambda Cloud’s filesystems, and other FAQs, check out our documentation page.

Happy training!

Lambda Team!

## AUTHORED BY

 Kathy Bui

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
