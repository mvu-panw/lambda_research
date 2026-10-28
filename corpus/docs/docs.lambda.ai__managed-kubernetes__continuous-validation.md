# Continuous validation - Lambda Docs

Source: https://docs.lambda.ai/managed-kubernetes/continuous-validation/

Skip to content

# Lambda's Managed Kubernetes continuous validation#

Lambda's Managed Kubernetes (MK8s) features a fully automated continuous
validation framework designed to maintain cluster performance, detect hardware
degradation, and improve overall reliability.

The system validates cluster health at two levels:

- Passive level: Constantly monitors individual nodes for hardware failures,
 registering anomalies directly to native Kubernetes Node Conditions.

- Active level: Automatically triggers non-destructive benchmarks on idle
 hardware to test compute, memory, and cross-node communication fabric.

## Architecture and workload safety#

Continuous validation runs entirely within your workload cluster utilizing
native Kubernetes primitives (such as CronJobs and DaemonSets). The
architecture does not deploy third-party custom resource definitions (CRDs) or
controllers that could conflict with your deployments.

### Zero-impact preemption#

To guarantee that validation benchmarks never degrade or delay production AI/HPC
workloads, all validation pods run under a specialized lowest-priority
PriorityClass. This ensures validation workloads schedule opportunistically on
idle hardware and are immediately preempted the moment a customer workload
requests those resources.

The preemption logic relies entirely on native Kubernetes eviction primitives
and is fully compatible with out-of-the-box alternative queue schedulers like
Kueue and Volcano, which are commonly used for distributed HPC and AI training
workloads.

If a node is required for a tenant job, the validation pods are terminated
immediately to prevent scheduling latency. In the event of a temporary
disconnection from the Lambda management plane, health checks continue to
execute locally; results are buffered on the node and forwarded upstream once
connectivity is restored.

## Passive health checks: node conditions#

Potential node hardware failures are surfaced within the node's statuses
conditions. These may be checked at any time via kubectl:

kubectl describe node <node-name>

Under normal operational parameters, these conditions return a status of
False. If any condition transitions to True, it indicates a health or
performance regression.

### Hardware status matrix#

 | Condition name
 | Monitored failure
 | Technical vector / command underlying

 | GpuXid
 | Critical NVIDIA XID errors
 | dmesg | grep -i 'xid|nvidia' (e.g., XID 79 / GPU Lost)

 | GpuSXid
 | NVIDIA SXid fabric errors
 | Monitors uncorrectable fabric errors

 | GpuTemperature
 | GPU thermal anomalies
 | Tracked via DCGM field ID 150 (dcgmi dmon)

 | GpuRemappedRows
 | Impending hardware memory failure
 | Monitors pending row remappings needing a system reset

 | GpuNvlink
 | Bandwidth interconnect loss
 | Tracking connectivity on NVLink/NVSwitch meshes

 | GpuCount
 | Missing accelerator hardware
 | Discrepancy between found vs. expected node GPU counts

 | GpuInfiniband
 | InfiniBand RDMA port degradation
 | Validates if ports are active and negotiating at specified speeds

 | GpuLinkWidth
 | Degraded PCIe bus speeds
 | Detects if a card drops below max width (e.g., running at x1 instead of x16)

 | ReadonlyFilesystem
 | Host OS storage faults
 | Catches read-only file system lockups and XFS shutdowns

 | NodeConnectivityError
 | Cluster network interface drops
 | Validates core host networking paths

## Active health checks and benchmarking#

Active checks run deep diagnostics to catch subtle performance regressions that
passive monitoring cannot detect, such as degraded cross-node communication or
storage IOPS decay.

### 1. Node-level diagnostics (reboots and maintenance)#

These tests execute automatically at cluster handoff, following designated
maintenance windows, and upon every individual node reboot. If these tests fail,
the node is isolated immediately.

- NVIDIA DCGM diag level 3 (EUD): Runs extensive compute and memory cell
 validation (dcgmi diag -r 3).

- Thermal and load stressing: Short, high-intensity 15-minute runs using
 gpu-burn and gpu-fryer to confirm thermal margins under peak power draw.

- Host-to-device transfer: Executes nvbandwidth to benchmark PCIe
 Gen/width performance between host CPUs and GPUs.

### 2. Scheduled fabric validation (continuous workspace CronJobs)#

Operating via CronJobs on a configurable cadence (typically hourly or weekly),
these workloads target only idle nodes.

- Distributed multi-node benchmarking: Executes an MPI all-reduce operation
 (mpirun all-reduce-perf) verifying NVLink, NVSwitch, and InfiniBand fabrics
 simultaneously.

- Network isolation testing: Leverages NCCL_P2P_DISABLE=1 alongside
 bidirectional RDMA perftests (ib_write_bw) to isolate raw fabric throughput
 independent of local node routing.

- Shared storage benchmarking: Launches non-destructive fio workloads
 mapping to the cluster's primary storage class, measuring sustained IOPS,
 bandwidth (GB/s), and latency (ms) without consuming physical drive lifespan.

### Topology-aware scoping#

Using native Kubernetes node selector labels, tests automatically adapt to
cluster architecture:

- Zone-scoped tests: Validate local intra-rack InfiniBand loops.

- Cluster-wide tests: Validate cross-zone fabric backbones.

## Automated remediation workflow#

Lambda's Managed Kubernetes implements a deterministic, rule-based loop to
automatically handle node faults without administrative intervention.

- Detection: A passive node condition transitions to True or an active
 validation benchmark fails.

- Isolation: The system instantly cordons the node, preventing new
 workloads from scheduling to it.

- Drain period: Running pods are safely evicted and drained. A
 remediation.k8s.lambda.ai/pending-drain label is appended during this phase
 to protect active application data.

- 

Targeted correction: The system triggers rule-mapped hardware actions:

- Power-cycle: A controlled system reboot.

- Flea-drain: A hardware-level cold reset to clear persistent auxiliary register loops.

- 

Resolution or escalation: If the node returns to a healthy status, it is
 uncordoned and the internal incident is closed. If automated correction
 routines are exhausted and the node fails to recover, it is placed into a
 permanent maintenance state and a high-severity alert is dispatched directly
 to Lambda Support Operations for physical hardware replacement.

## Metrics and observability#

All cluster validation metrics are exposed natively to your environment's
Prometheus instance and visualized on your pre-configured Grafana dashboard.

### Prometheus metrics reference#

- lambda_validation_job_result: Tracks overall test success. Emits SUCCESS,
 SKIPPED (preemption occurrence), or ERROR.

- lambda_validation_job_metrics: Exposes granular benchmark numbers over time
 (e.g., busbw_gbps, throughput_gbps, iops, latency_ms).

- lambda_validation_node: A binary flag (0 or 1) per node demonstrating
 overall test coverage inside the active window.

To view your cluster's historical active validation jobs directly from the
command line, run:

kubectl get job -n lambda-system

 Back to top
