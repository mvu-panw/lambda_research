# Security posture - Lambda Docs

Source: https://docs.lambda.ai/private-cloud/security-posture/

Skip to content

# Security posture for Lambda Private Cloud#

## Introduction#

This document outlines the physical and logical security posture of
Lambda Private Cloud.

## Overview#

Lambda Private Cloud provides single-tenant AI compute infrastructure with fully
dedicated hardware and network resources allocated exclusively to a single
customer. This architecture eliminates shared infrastructure risks and potential
resource contention through complete environmental separation.

This isolation model significantly reduces third-party risk exposure while
maintaining access to Lambda's infrastructure design expertise and operational
support services.

All clusters start with a common baseline reference design, which incorporates
well-reasoned and sensible security decisions. On top of this design, various
customizations are offered to tailor a cluster to specific customer
requirements. Common customizations and their impact on the cluster's security
posture are outlined below.

## Cluster Design#

A private cloud cluster contains several distinct types of server nodes. All
nodes are single-tenant bare-metal systems which are physically isolated from
other Lambda customers and dedicated to the customer's cluster.

- 

Compute (GPU) nodes: Optimized for GPU workloads. These nodes connect to
 the cluster's in-band Ethernet network and InfiniBand fabric.

- 

Head nodes: Used as control plane or CPU-only compute nodes. They connect
 solely to the cluster's in-band Ethernet network.

- 

Lambda Management nodes: Used by Lambda to provide observability into the
 health of the cluster and allow Lambda to provide operational support.

### BIOS, BMC, and firmware#

All nodes are deployed with the latest validated BIOS and BMC firmware. All
nodes have secure BMC passwords set.

### Operating system#

All compute and head nodes are provisioned with an up-to-date installation of an
Ubuntu LTS (Long-Term Support) release. The customer is responsible for OS-level
security and patch management, as well as monitoring logs and metrics.

Lambda provisions the cluster nodes with an initial SSH authorized key provided
by the customer. With this key, the customer receives administrator (root)
access to all compute and head nodes. Once the cluster is handed over, the
customer can install additional SSH keys, add or remove local user accounts, and
perform any other desired OS-level configuration changes.

## Network#

A private cloud cluster primarily utilizes two network fabrics that operate in
tandem: an in-band Ethernet network and an InfiniBand fabric. All
network connections and supporting infrastructure (including firewalls, routers,
and switches) are dedicated to the customer's cluster.

The in-band Ethernet network is connected to all compute and management
nodes, as well as the cluster's persistent storage. This network is the primary
path that compute and management nodes use to access persistent storage.

The in-band Ethernet network has internet connectivity provided through
redundant dedicated internet access (DIA) links. A firewall is placed at the
network perimeter and is initially configured with no internet-exposed ingress
ports. The customer has full control over this firewall and can implement their
own network policies.

The InfiniBand fabric provides high-speed, low-latency connectivity between
compute nodes in a spine-leaf topology, suitable for RDMA-enabled GPU
communication. All compute nodes have unrestricted access to each other on this
fabric.

Depending on the size of the cluster, an RoCE fabric (RDMA over Converged
Ethernet) may be used for RDMA traffic instead of InfiniBand. The security
properties of this technology are similar to InfiniBand; however, it uses
Ethernet as the underlying physical layer.

Each cluster also has a separate management network. The management network
connects to control plane systems, physical infrastructure (including smart
PDUs), dedicated management interfaces on server nodes (including BMCs and
DPUs), and dedicated management interfaces of network devices that support the
in-band Ethernet network and InfiniBand fabric. It has connectivity to the
in-band Ethernet network through a dedicated management firewall.

Finally, there is a small out-of-band (OOB) network. This network is used
for backup or emergency access to the dedicated management interfaces on network
devices in the management network (i.e., core switches and firewalls). The OOB
network has its own firewall that is connected to a backup low-bandwidth
internet link, which can be utilized to manage core management network devices
in an outage scenario. General routing is not permitted over the OOB backup
link.

### Hardware#

Lambda will deploy all network hardware with the latest firmware provided by the
respective vendors. Lambda can assist with ongoing firmware updates to these
devices at the customer's request, but will not (and generally cannot) take any
action on them without prior customer approval.

### VPN#

The cluster's perimeter firewall provides client VPN functionality, which allows
for secure remote connection to the cluster from individual client endpoints.
This is suitable either as a primary access path or a backup access path if the
primary preference is to use a site-to-site VPN or dedicated private links.

As part of the handoff process of a new cluster, Lambda will provision and share
an initial set of administrative VPN credentials with the customer. The customer
has the option to provision additional VPN accounts or integrate with their own
identity provider for single sign-on (SSO).

## Data storage and handling#

Each cluster includes persistent network-attached storage. As with other aspects
of a private cloud cluster, all hardware (including storage media) is dedicated
to the customer and not shared with others.

Data saved to persistent storage is encrypted at rest with 256-bit AES-XTS. A
unique encryption key is generated when the cluster is built and is not shared
with other customers. If a persistent storage drive is ever physically removed,
its data is unreadable and irrecoverable without this key.

Data accessed from persistent storage is not encrypted in-transit over the
network, but the traffic is fully contained within the cluster's physical
footprint. This design optimizes for I/O performance while still protecting the
data through physical isolation and controlled datacenter access. Customers with
stricter requirements can implement object-level encryption.

Storage drives that fail or reach end-of-life are carefully removed and secured
within the datacenter until they are destroyed. Lambda relies on a certified
third-party vendor for this process and can provide proof of destruction upon
request.

At the conclusion of a Private Cloud contract, Lambda performs a secure wipe of
all cluster drives. This sanitization process complies with NIST 800-88 "purge"
requirements, ensuring that customer data is permanently removed.

## Physical site#

Lambda Private Cloud infrastructure is housed in secure datacenter facilities
featuring:

- Perimeter and internal CCTV surveillance, with a minimum 90-day retention

- Multiple security checkpoints, minimally including:

- Main lobby access that is restricted by a security door with a biometric
 reader, badge reader, and/or security personnel

- Multi-factor authentication (PIN/badge + biometric) for entry into the data
 hall

Physical access to the infrastructure is limited to Lambda employees and data
center providers with a specific need for access. In the event of emergencies or
planned maintenance, Lambda documents all access and reviews it to ensure
compliance with these protocols.

Authorized Lambda employees may access data centers for maintenance, upgrades,
or other hardware-related work. Local authorities or authorized data center
providers may access the hall space as required by local codes.

## Ongoing maintenance and support#

It is understood that every customer has unique infrastructure management
requirements. Lambda Private Cloud offers different levels of maintenance
options, allowing customers to select the level of support that best suits their
needs. Regardless of the chosen model, the customer will have access to Lambda's
expert support staff.

- 

Physical only - After handoff, Lambda will not retain any logical access
 to the customer's cluster or data. The customer will be able to submit support
 and maintenance requests, and has the option to provide Lambda with logical
 access as-needed for assistance. This model provides the most robust level of
 access reduction for the cluster, while still retaining access to Lambda's
 support expertise.

- 

Managed Private Cloud - Lambda will retain logical access to the cluster
 to provide best-in-class support at all layers of the stack. The customer can
 revoke Lambda's access at any time and will have access to robust audit logs
 that provide visibility into the actions Lambda takes on the cluster. Lambda
 will never take action on the cluster without prior notification and
 permission, and will work with the customer to establish requirements for
 maintenance windows.

## Customizations#

### Managed Kubernetes#

A fully-managed Kubernetes stack can be
provisioned into the cluster. This Platform-as-a-Service (PaaS) offering adheres
to Kubernetes best practices for cluster configuration and security, removing
management overhead and enabling customers to leverage Kubernetes effectively.
Lambda will handle ongoing cluster maintenance, including updates and patching
(subject to the customer's requirements for maintenance window coordination).

SSO authentication is supported for Managed Kubernetes out-of-the-box. Customers
can authenticate against their own identity provider via OIDC or SAML.

For clusters with Managed Kubernetes, customers will not have direct SSH access
to cluster nodes; instead, Kubernetes tooling is used to manage workloads.

### Dedicated cage#

A cage can be constructed within the datacenter to physically isolate the
cluster hardware. The cage will be exclusively dedicated to the customer and
will not contain any hardware allocated to other customers.

Important: If a dedicated cage is desired, Lambda needs to be informed early
in the cluster build process so that space can be allocated and the cage can be
physically constructed prior to cluster hardware installation.

The cage is constructed with a tight mesh and a ceiling, and can extend below
the raised floor to the underlying concrete. Customers can install their own
badging infrastructure at the entrance to the cage and will have full control
over who has access and when they have access. Additionally, customers have the
option to install their own security cameras within the cage, with full control
over placement to get any angle within the cage.

The cluster will have external network links (including DIA links) that leave
the cage. These links can optionally use armored cabling for increased
protection against physical tampering.

### Site-to-site IPsec VPN#

The cluster can be securely connected to the customer's infrastructure via a
site-to-site VPN tunnel over the internet (or alternatively, through dedicated
private links). The cluster's perimeter firewall terminates an IPsec tunnel with
the customer's on-premises or self-hosted firewall/router, establishing secure
and encrypted connectivity between the two environments.

The security of this tunnel relies heavily on the protection of the IPsec
credentials (either a pre-shared key or certificates). The cluster firewall
utilizes encrypted credential storage; however, the customer is responsible for
secure storage of the credentials on their own infrastructure.

If additional protection is required for tunnels running over the internet, an
IP allowlist can be added to the outer tunnel connection to restrict it to
traffic from specified source IPs.

### Private cloud connectivity#

The cluster can be configured with dedicated private network links to major
cloud providers, including AWS DirectConnect, Azure ExpressRoute, GCP
Dedicated/Partner Interconnect, and OCI FastConnect. These links are terminated
on the cluster's perimeter firewall, allowing the customer to implement desired
network security policies.

### Custom hardware#

Additional custom hardware (such as network appliances or server nodes) can be
deployed into a cluster to meet specific needs if the baseline components are
not suitable. This is useful, for example, when there are requirements to run
specific network appliances or a need for special-purpose functionality that
must run in close proximity to the rest of the cluster. Lambda will be
responsible for establishing physical network connectivity for custom hardware,
and the customer will be responsible for its configuration and operation.

 Back to top
