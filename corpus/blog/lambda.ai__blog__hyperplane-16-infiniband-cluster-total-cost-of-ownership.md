# Hyperplane-16 InfiniBand Cluster Total Cost of Ownership Analysis

Source: https://lambda.ai/blog/hyperplane-16-infiniband-cluster-total-cost-of-ownership

Skip to main content

# Hyperplane-16 InfiniBand Cluster Total Cost of Ownership Analysis

 April 7, 2020

 (Updated on July 24, 2023)

 • 8 min read

In this post we'll walk through using our Total Cost of Ownership (TCO) calculator to examine the cost of a variety of Lambda Hyperplane-16 clusters. We have the option to include 100 Gb/s EDR InfiniBand networking, storage servers, and complete rack-stack-label-cable service. The purpose of this post is to give you a clearer picture of the costs involved when building a cluster, both fixed and variable.

## A TCO Calculator

All results in this post are generated using our Hyperplane-16 TCO Calculator. A Lambda engineer can walk you through how to use the TCO Calculator. Just send us an email: sales@lambdalabs.com to request a walkthrough.

## Trying out different configurations

Using the above calculator and the guidance of a Lambda engineer, we're able to quickly create a table showing the amortized cost / year / node of an InfiniBand networked Hyperplane-16 cluster. As you can see, the prices have automatically adjusted based on the costs and system specifications that we input into the calculator: in our case:

- InfiniBand networking set to TRUE

- system administration cost of $10,000 / year / four servers

- management node count to 0

- storage node count to 0

 |  
 |  
 | Hyperplane-16 Cluster with InfiniBand Networking
 |  

 |  
 | 1x Cluster
 | 8x Cluster
 | 16x Cluster

 | Upfront
 | $299,504
 | $2,297,388
 | $4,584,787

 | Annual Total Operating Costs
 | $26,146
 | $147,296
 | $294,436

 | Annual System Administration Cost
 | $10,000
 | $20,000
 | $40,000

 | Annual Co-location Cost
 | $16,146
 | $127,296
 | $254,436

 | Total Cost at Year 1
 | $325,650
 | $2,444,684
 | $4,879,223

 | Total Cost at Year 3
 | $377,942
 | $2,739,276
 | $5,468,095

 | Total Cost at Year 5
 | $430,234
 | $3,033,868
 | $6,056,967

 | Number of Systems
 | 1
 | 8
 | 16

 | Amortized Cost / Year / System (5 Years of Use)
 | $86,047
 | $75,847
 | $75,712

## A quick introduction to the Hyperplane-16

The Hyperplane-16 is a massive 10kW Deep Learning training appliance from Lambda. It includes:

- 16x NVIDIA Tesla V100 SXM3 GPUs

- NVLink & NVSwitch for fast GPU-to-GPU communication within the server

- 8x 100 Gb/s InfiniBand cards for fast GPU-to-GPU communication across multiple servers (using GPU-Direct RDMA) during distributed training

The default system price used in the TCO calculator is $240,000. This is the price for a Lambda Hyperplane-16 Premium, an HGX-2 platform configuration that exactly matches the specifications of the DGX-2.

For a more comprehensive hardware overview, you can check out the Hyperplane-16 landing page or see our Hyperplane-16 announcement blog post. We calculate the total cost of ownership for a complete Hyperplane-16 cluster including:

- Lambda Hyperplane-16s

- Sufficient 100 Gb/s EDR InfiniBand network (Mellanox MSB7800) + 10GBase-T Network (Arista 7050Tx-48)

- Some number of Lambda NVMe storage servers

- Some number of Lambda management nodes

- Sufficient Racks, PDUs, rack crates

- Complete cluster-level rack, stack, label, and cable services from Lambda

- Complete co-location costs & ongoing system administration costs

## 3x Hyperplane-16 Cluster Summary

Here's a cluster and TCO summary for a 3x Hyperplane-16 cluster:

 | Cluster Properties:
 |  

 | Cluster GPU Count
 | 48

 | Cluster SGEMM TFLOPS (FP32)
 | 720

 | Hyperplane-16 Size (RUs)
 | 10

 | Racks Required
 | 1

 | Full Cluster TDP (kW)
 | 31.85

 | Full Cluster Power Draw (kW) based on Util. Ratio
 | 15.925

 | NVMe Storage Node Capacity (TB)
 | 96

 | Total Cluster Raw Storage (TB)
 | 186

## Cluster TCO Summary

 | Total Cost of Ownership Summary:
 |  

 | Total Upfront Cost ($)
 | $868,939

 | Annual Operating Cost ($/year)
 | $114,578

 | Annual Co-location Cost (Including Power) ($/year)
 | $49,686

 | Annual Administration Cost ($/year)
 | $64,892

 | TCO over one year ($)
 | $983,517

 | TCO over three years ($)
 | $1,212,673

 | TCO over five years ($)
 | $1,441,829

## How we conducted the TCO analysis

- Our first step is to design the cluster. We've done that step for you.

- We then list out all components of the designed cluster: nodes, InfiniBand HCAs, switches, cables, PDUs, racks, rack crates, etc. We then assign a price to all components. This document is known as our "priced bill of materials" or "priced BoM".

- We then assign a power draw to all IT equipment in the cluster, this is our "Cluster kW draw".

- We dynamically modify the rack, switch, and cable counts to accommodate the number of nodes.

- We assign a price to the annual salary for a data center system administrator.

- We assign a $ / kW / mo figure to the co-location service. In this TCO, we use $260 / kW / month. We multiply this with our Cluster kW draw to arrive at our monthly co-location bill. We assume that you will be at near 100% utilization.

We can now calculate the TCO as:

Cluster kW draw (power) = Sum of all component TDPs in the cluster

Annual Co-location cost ($) = $/kW/mo * Cluster kW draw * 12 months

TCO for N Years ($) = N * (Annual Co-location Cost + Annual Administration Cost) + Total Upfront Cost

## Generating a Network Topology

Within the TCO calculator, we dynamically generate a 100% port-to-port bandwidth spine & leaf network topology based on the components in the cluster. An example spine & leaf network topology looks like this:

A non-blocking 100% port-to-port bandwidth InfiniBand spine and leaf network topology with MSB7800 switches.

As the number of nodes in the cluster model is increased, this topology is expanded to accommodate for additional usable ports. Note: as the number of nodes approaches 20, we would recommend switching to a CS7520 director switch instead of a manual spine & leaf topology using multiple MSB7800s. The CS7520 is a director switch that can provide full port-to-port bandwidth for up to 216-ports. It has an internal backplane that allows it to create a similar spine and leaf topology as seen above but without any additional cables.

## Generated Cluster Priced BOM

 | Item
 | Model Number
 | Description
 | Qty
 | MSRP
 | Extended MSRP
 | Item TDP (W)
 | Extended TDP (W)

 | Server
 | Hyperplane-Premium
 | Lambda Hyperplane-16 Premium Server (HGX-2 Platform matching DGX-2 Specs)
 | 3
 | $240,000
 | $720,000
 | 10000
 | 30000

 | IB HCA
 | MCX555A-ECAT
 | Infiniband HCAs (8x / server)
 | 26
 | $813
 | $21,125
 | 0
 | 0

 | IB Cables
 | MFS1S00-H030E
 | Infiniband 30m HDR cables (8x / server)
 | 26
 | $1,289
 | $33,508
 | 0
 | 0

 | IB Adapter Warranty
 | SUP-ADPTR-1S
 | Mellanox Warranty
 | 26
 | $52
 | $1,349
 | 0
 | 0

 | IB Switch
 | MSB7800
 | Mellanox 36-port 100 Gb/s InfiniBand Switch
 | 1
 | $18,000
 | $18,000
 | 250
 | 250

 | 1U Management Node
 | LMB-MGMT
 | 1U Management Bastion Node
 | 1
 | $2,500
 | $2,500
 | 750
 | 750

 | Lambda NVMe IB Connected Storage Node
 | LMB-STORAGE
 | 96 TB NVMe Storage Node
 | 1
 | $48,080
 | $48,080
 | 750
 | 750

 | PDU
 | AP8966
 | APC Rack PDU 2G, Switched, ZeroU, 17.2kW,
 | 4
 | $2,552
 | $10,207
 | 0
 | 0

 | Switch
 | DCS-7050TX-48-F
 | Arista 7050TX-48 port 10GBase-Tswitch
 | 1
 | $9,990
 | $9,990
 | 100
 | 100

 | Cable
 | SNX-23298
 | 10pcs/pack Cat6 Color Label Numeric Cable Wire Marker Identification
 | 5
 | $7
 | $34
 | 0
 | 0

 | Cable Management
 | SNX-64186
 | 5U 3'' Wide Plastic Vertical Cable Manager with Bend Radius Finger
 | 4
 | $6
 | $25
 | 0
 | 0

 | Cable Management
 | C6P-S24FT1U
 | 1U 24 Ports Cat6 Shielded Feed-Through High Quality Patch Panel
 | 1
 | $75
 | $75
 | 0
 | 0

 | RJ45 Cables
 | CTG-03986
 | RJ45 Cat6 12ft Snagless
 | 10
 | $6
 | $55
 | 0
 | 0

 | Power Cables
 | STA-PXT1002
 | 2 ft C19 to C14 - StarTech PXT100146
 | 18
 | $5
 | $82
 | 0
 | 0

 | Blanking Panel
 | AR8136BLK
 | 10 Pack 1U Blanking Panel (Black)
 | 1
 | $66
 | $66
 | 0
 | 0

 | Rack
 | AR3300
 | Lambda 42U Rack
 | 1
 | $2,344
 | $2,344
 | 0
 | 0

 | Rack Crate
 | LLB‐AR3300
 | Rack Crate for SX 42U AR3300
 | 1
 | $1,500
 | $1,500
 | 0
 | 0

## AUTHORED BY

 Stephen Balaban

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
