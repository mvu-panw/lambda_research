# How Kodiak doubled AI training performance on Lambda

Source: https://lambda.ai/customer-stories/kodiak

Skip to main content

# How Kodiak doubled AI training performance on Lambda

Contact sales

Time to compute
Days
vs Months

Training iteration speed
2x
faster

Experiment throughput
2x
more experiments

## How Kodiak doubled AI training speed on Lambda

## Executive summary

Kodiak deployed the world's first customer-owned fleet of driverless Class 8 trucks. Key to the achievement was training GigaFusionNet, a unified foundation model that reasons across cameras, LiDAR, and radar simultaneously. To train it, Kodiak needed to quickly scale compute beyond its existing infrastructure without the complexity of migrating petabytes of sensor data. With Lambda's NVIDIA HGX H100 1-Click Clusters, Kodiak was up and training in a week, doubling their iteration speed.

Customer
 
Kodiak

Website

 kodiak.ai

Vertical
 
Physical AI

Products
 
1-Click Cluster

## Intro

Kodiak was founded with a singular focus to become the trusted world leader in autonomous ground transportation. Today, Kodiak operates the world's largest fleet of customer-owned autonomous trucks: as of the end of 2025, the company operated 20 customer-owned driverless vehicles actively delivering freight in Texas, logging over 15,600+ driverless hours and completing more than 23,500+ deliveries in real-world commercial operations. Kodiak's next milestone is driverless operation on public highways, a goal that requires AI capable of understanding the physical world well enough to handle anything it hasn't seen before. Getting there required a different kind of compute. 

## Going driverless meant training a bigger model, faster

Kodiak built its perception stack with numerous specialized models: one for 3D object detection, another for road-surface understanding, and another for occupancy prediction. Each was precise by design. But scaling to fully driverless systems required something fundamentally different: a unified world foundation model capable of reasoning across all of these tasks simultaneously, ingesting data from cameras, LiDAR, and radar in a single architecture. Kodiak has developed these models and enabled joint training of multiple tasks with a combination of unsupervised, semi-supervised, and fully supervised training regimes.
Some of these models are fully trained with unlabeled data collected over millions of miles of operation.

Training their next-generation unified world foundation model, GigaFusionNet, in a week required tens of gigabytes more GPU memory and higher inter-node bandwidth, all while handling a significant volume of data, more than what their existing on-prem hardware could deliver. When the team explored a hyperscaler cloud option, they ran into a fundamental challenge: GPU nodes were geographically separated from their petabytes of data, making both data transport and training slow. Also, the hyperscaler networking solution, built for general-purpose workloads, couldn’t deliver the inter-node throughput needed for distributed training. Even with these trade-offs, they had months of wait times to access this hyperscale compute. 

“We build AI that drives vehicles without anyone in the cab. We are not GPU training infrastructure experts.”Shubham Shrivastava, Head of AI

## From months of waiting to training in a week

Using Lambda's NVIDIA HGX H100 1-Click Clusters connected with NVIDIA InfiniBand networking, Kodiak's team began pre-training GigaFusionNet jointly across every perception task the truck needs to navigate the real world. Kodiak’s team was able to start training their large foundation model jointly in a week, compared to months of waiting with other alternatives. 

GigaFusionNet does more than just detect objects. It builds a continuous understanding of how the 3D world behaves across time and space. Where and how the vehicle should drive. Where objects are and how they're moving. What regions of ground are drivable, including real-time prediction of lanes and other road structure. It's the difference between a truck that recognizes a vehicle and a truck that understands and reasons about the 3D world. 

Training a model to reason across all of Kodiak’s sensor modalities and tasks simultaneously requires a shared backbone, and a shared backbone requires high-performance compute with high GPU memory, inter-node bandwidth, and faster throughput. Since Lambda’s 1-Click Clusters are designed for large-scale AI workloads, Kodiak didn’t need to spend any time setting up the compute for pre-training. They were able to stay focused on the only problem that mattered to them: building more powerful, safer autonomous ground transportation using GigaFusionNet. Kodiak was also able to accelerate data loading using Lambda's S3 adapter, streaming hundreds of terabytes of sensor data at the latency their training workload required. And the support model mattered more than Kodiak expected. 

The iteration pace changed, too. Shubham's team went from testing one hypothesis per training cycle to testing multiple hypotheses twice as fast, compressing the feedback loop that turns a model from good to better.

“Having a direct line to Lambda's team across multiple real-time communication channels means downtime is not something we stress about. We flag an issue, and they are on it immediately.”Shubham Shrivastava

## 2x faster experiments. Twice the iterations.

Kodiak's path to fully driverless highways depends on a model that understands the physical world well enough to handle what it hasn't seen before. Getting those results requires efficiency and care. Every training cycle that takes longer than it should, and additional time spent waiting on infrastructure access, is time further from that goal.

With Lambda, Kodiak closed that gap, doubling the speed at which it can test a hypothesis, run it through real-world data, and decide what to build next.

And they did it without diverting engineering attention from the actual problem: Physical AI-powered ground autonomy solutions that enable reliable, efficient driverless movement across a wide range of environments. 

Read more about how Kodiak trains GigaFusionNet on Lambda, and Lambda’s GPU clusters for your workloads.

“With Lambda, the iteration speed was twice the previous speed.”Shubham Shrivastava
