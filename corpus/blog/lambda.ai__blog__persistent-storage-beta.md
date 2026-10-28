# Lambda Cloud Storage is now in open beta: a high speed filesystem for our GPU instances

Source: https://lambda.ai/blog/persistent-storage-beta

Skip to main content

# Lambda Cloud Storage is now in open beta: a high speed filesystem for our GPU instances

 April 19, 2022

 (Updated on November 18, 2022)

 • 2 min read

After a period of closed beta, we're excited to announce that persistent storage for Lambda GPU Cloud is now available for all A6000 and V100 instances in an extended open beta period. 

During this open beta period, storage will be available free of charge and will be capped at 10TB per account.

Click the video below or read on to learn how to get started.

To create a persistent filesystem, log into your Lambda GPU Cloud dashboard. You’ll now see on the sidebar navigation an option for “Storage” with a Beta tag.

Click on “Storage” on the sidebar and hit “Create filesystem” in the upper right corner of the page. Give the filesystem a name using alpha-numeric characters (no underscores or spaces, dashes are allowed) then click “Create filesystem.”  

You should now see your new filesystem and its mount point appear in your dashboard.

Repeat this process to create more filesystems with different names if needed.

When launching an instance, you can now choose to attach a filesystem to your instance by selecting one from the drop down menu. The same filesystem can be attached to multiple instances at the same time if needed.

You’ll now see your persistent storage filesystem in the sidebar of the Cloud IDE.

Double click on the folder and save your files inside this folder.

Any files saved outside of this folder will not persist when you terminate your instance. All data inside this folder will be stored and will persist the next time you attach the same filesystem to a new instance. This applies to files as well as packages.

It’s important to note that dependencies will not persist and you will need to reinstall them upon launching a new instance with the same filesystem.

Happy training!

Lambda Team

## AUTHORED BY

 Kathy Bui

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
