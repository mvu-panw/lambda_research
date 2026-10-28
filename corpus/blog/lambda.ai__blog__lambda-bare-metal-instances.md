# Lambda Bare Metal Instances: full hardware control with API-driven operations

Source: https://lambda.ai/blog/lambda-bare-metal-instances

Skip to main content

# Lambda Bare Metal Instances: full hardware control with API-driven operations

 May 21, 2026

 (Updated on June 5, 2026)

 • 4 min read

The unit of AI compute has shifted from single hosts to rack-scale systems that integrate NVIDIA GPUs, CPUs, scale-up networking fabrics, and liquid cooling, such as the NVIDIA GB300 NVL72 and NVIDIA Vera Rubin NVL72. 

Teams at the frontier of training and serving models have three common needs: leading-edge compute for the best tokens per watt per dollar, bare-metal access for uncompromised performance and security, and cloud-grade usability so engineers can focus on building models rather than operating data centers.

Today’s market forces a compromise. Teams can either deploy solutions on bare-metal servers and operate increasingly complex infrastructure themselves, or use virtualized cloud instances that offer ease of use but introduce a third-party hypervisor.

Our largest customers have chosen bare-metal servers and accepted that trade-off for specific reasons. 

- Performance-focused customers, such as quantitative traders and frontier labs, want deterministic hardware behavior and direct firmware control that virtualization can't guarantee. 

- Those running large-scale production inference have sensitive data that requires zero abstraction layers and full-stack attestation. 

- The largest AI organizations operate their own clouds and need Lambda hardware to integrate seamlessly into their existing global operations stack. 

There is now a third option.

Starting with NVIDIA GB300 NVL72, Lambda Supercluster with Bare Metal Instances combines the key characteristics of both: direct access to hardware, no third-party hypervisor, and an API-driven lifecycle.

Launching a Lambda Bare Metal Instance looks nearly identical to launching a virtualized one. Instead of selecting an instance type like gpu_8x_b200_sxm6, you select a bare metal type like gpu_metal-4x_gb300. Once provisioned, the difference is significant: you have direct, unmediated access to the CPU, memory, GPU, disk, and TPM. 

Bare Metal Instances roll out first on Superclusters (physically isolated, shared-nothing, single-tenant clusters co-engineered for the workload), where the operational benefits matter most.

## How Lambda Bare Metal Instances work

Lambda's bare-metal instance architecture combines bare-metal control with reduced ops burden by offloading infrastructure management to two hardware components already present in every modern NVIDIA GPU server. 

- NVIDIA BlueField Data Processing Unit (DPU). Lambda operates the DPU in zero-trust mode, restricting the host from performing operations that could compromise the DPU itself. Key provisioning flows, such as establishing network identity, presenting an emulated NVMe boot device, and managing storage volumes, run entirely on the DPU and don’t touch the host OS.

- Baseboard Management Controller (BMC). Lambda operates the BMC to monitor hardware health and control boot sequencing out-of-band, enabling monitoring, alerting, and break-fix work on the underlying hosts.

The result: a fully API-driven instance lifecycle with direct hardware control. 

Compared to virtualized instances, Bare Metal Instances provide:

- Direct hardware access. CPU, memory, GPU, disk, and TPM with no hypervisor in between 

- Hardware-rooted security. NVIDIA BlueField DPUs in Zero Trust Mode make the DPU inaccessible from the host OS. Customers can access the TPM for full-stack attestation to satisfy stringent security requirements. 

Compared to bare metal hosts, Bare Metal Instances enable: 

- Programmability for global fleets. At the frontier scale, Lambda is rarely a customer's only infrastructure provider. Bare Metal Instances, coupled with self-service APIs covering the instance lifecycle, VPCs, storage volumes, and resource governance, enable Lambda compute to integrate with a customer's existing control planes and orchestration across a global fleet. 

Bare Metal Instances shift teams from manually operating a cluster to using a cluster without giving up the performance and control that made bare metal the right choice in the first place.

## Why Bare Metal Instances

## What's next

Lambda’s Supercluster Bare Metal Instances production deployments on NVIDIA GB300 NVL72 followed with general availability on NVIDIA Vera Rubin NVL72 rack system. We expect to be among the first neoclouds to offer Bare Metal Instances on NVIDIA GB300 NVL72.

To learn more about Bare Metal Instances, talk to our team or watch our NVIDIA GTC 2026 presentation.

## AUTHORED BY

 Khushboo Goel

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
