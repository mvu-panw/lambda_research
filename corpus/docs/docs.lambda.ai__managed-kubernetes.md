# Introduction - Lambda Docs

Source: https://docs.lambda.ai/managed-kubernetes/

Skip to content

# Using Lambda's Managed Kubernetes#

## Introduction#

This guide walks you through getting started with
Lambda's Managed Kubernetes
(MK8s) on a
1-Click Cluster
(1CC).

MK8s provides a Kubernetes environment with GPU and InfiniBand (RDMA) support,
and shared persistent storage across all nodes in a 1CC. Clusters are
preconfigured so you can deploy workloads without additional setup.

NVIDIA GPU Operator and NVIDIA Network Operator are preinstalled. The GPU
Operator automates deployment and management of NVIDIA drivers, CUDA, and
Kubernetes components required to run GPU-accelerated workloads, including
Multi-Instance GPU (MIG) support. The Network Operator configures and manages
high-performance networking, including RDMA over InfiniBand, enabling
low-latency, high-throughput communication between nodes.

NVIDIA Container Toolkit is also installed and kept up to date, ensuring that
containers can securely and reliably access GPUs at runtime.

MK8s includes continuous validation to verify that GPUs, networking, and storage
are functioning correctly across the cluster. These checks run regularly and
help detect performance degradation or misconfiguration before they impact
workloads.
See the continuous validation documentation for details.

MK8s also includes automated node remediation to detect and recover from
hardware issues.
See the auto-remediation system documentation for details.

In this guide, you'll learn how to:

- Access MK8s using kubectl.

- Grant access to additional users.

- Organize workloads using namespaces.

- Deploy and manage applications.

- Expose services using Ingresses.

- Use shared and node-local persistent storage.

- Monitor GPU usage with the NVIDIA DCGM Grafana dashboard.

This guide includes two examples:

In the first, you'll deploy a vLLM server to serve the
Nous Research Hermes 4
model. You'll:

- Create a namespace for the examples.

- Add a PersistentVolumeClaim (PVC) to cache model downloads.

- Deploy the vLLM server.

- Expose it with a Service.

- Configure an Ingress to make it accessible externally.

In the second example, you'll evaluate the multiplication-solving accuracy of
the
DeepSeek R1 Distill Qwen 7B
model using vLLM. You'll:

- Run a batch job that performs the evaluation.

- Monitor GPU utilization during the run.

## Prerequisites#

You need the Kubernetes command-line tool, kubectl, to interact with MK8s.
Refer to the Kubernetes documentation for
installation instructions.

You also need the kubelogin plugin for kubectl to authenticate to MK8s.
Refer to the
kubelogin README for installation instructions.

## Accessing MK8s#

To access MK8s, you need to:

- Configure firewall rules to allow connections to MK8s.

- Configure kubectl to use the provided kubeconfig file.

- Authenticate to MK8s using your
 Lambda Cloud account.

### Configure firewall rules#

To access MK8s, you must first create firewall rules for the MK8s API server and
Ingress Controller:

- 

Navigate to the Global rules tab on the
 Firewall settings page
 in the Lambda Cloud console.

- 

In the Rules section, click Edit rules to begin creating a rule.

- 

Click Add rule, then set up the following rule:

- Type: Custom TCP

- Protocol: TCP

- Port range: 6443

- Source: 0.0.0.0/0

- Description: MK8s API server

- 

Click Add rule again, then set up the following rule:

- Type: Custom TCP

- Protocol: TCP

- Port range: 443

- Source: 0.0.0.0/0

- Description: MK8s Ingress Controller

- 

Click Update firewall rules.

### Configure kubectl#

You're provided with a kubeconfig file when MK8s is provisioned. You need to
set up kubectl to use this kubeconfig file:

- 

Save the file to ~/.kube/config. Alternatively, set the KUBECONFIG
 environment variable to the path of the file.

- 

(Optional) Restrict access to the file:

chmod 600 ~/.kube/config

### Authenticate to MK8s#

- 

Run:

kubectl get nodes

A tab or new window opens in your default web browser, and you're prompted
to log in to your Lambda Cloud account.

- 

Log in to your Lambda Cloud account.

You're prompted to authorize Lambda Managed Kubernetes to access your Lambda
account.

- 

Click Accept to authenticate to MK8s.

In your terminal, you should see output similar to:

NAME STATUS ROLES AGE VERSION
mk8s-yns66blqnvvvffjc-mk8s--worker--gpu-8x-h100-sxm5gdr-cgkn46g Ready <none> 17d v1.32.3+rke2r1
mk8s-yns66blqnvvvffjc-mk8s--worker--gpu-8x-h100-sxm5gdr-cgwx5c7 Ready <none> 18d v1.32.3+rke2r1
mk8s-yns66blqnvvvffjc-ndcr6-728sh Ready control-plane,etcd,master 18d v1.32.3+rke2r1
mk8s-yns66blqnvvvffjc-ndcr6-p25c9 Ready control-plane,etcd,master 18d v1.32.3+rke2r1
mk8s-yns66blqnvvvffjc-ndcr6-vvrxc Ready control-plane,etcd,master 18d v1.32.3+rke2r1

### Grant access to additional users#

If you have the Workspace Membership: Create permission for the workspace
that contains your MK8s cluster, you can grant access to MK8s to other users
in the account. The type of access they receive depends on what role they
have in the account.

- If you grant access to a user who has the Account Member role, they receive
 an edit ClusterRole in MK8s, which allows read/write access to most
 objects in a namespace.

- If you grant access to a user who has the Account Admin role, they receive a
 cluster-admin ClusterRole in MK8s, which allows full control over every
 resource in all namespaces.

See the
Kubernetes documentation on user-facing ClusterRoles
to learn more about the edit and cluster-admin ClusterRoles. For more
information about the account roles available in Lambda Cloud, see
Predefined roles.

### Non-interactive authentication#

You can create
Service Accounts
to enable non-interactive authentication to MK8s. This can be useful for CI/CD
pipelines and automation scripts.

Note

The non-interactive authentication method described here is intended for
automation tools that run outside the cluster, such as a
CI/CD pipeline or external orchestration.

For workloads running inside the cluster, such as pods in a namespace,
you should instead create and assign a Service Account directly.

To create a Service Account, along with the necessary Secret (token) and
ClusterRoleBinding objects:

- 

Download the service-account-setup.yaml manifest file.

- 

In the manifest file, replace:

- <SERVICE-ACCOUNT-NAME> with the name you want for the Service Account.

- <NAMESPACE> with the namespace you want to create the objects in.

- <ROLE> with either edit or cluster-admin.

- 

Using an account with the cluster-admin user role, apply the manifest:

kubectl apply -f service-account-setup.yaml

You should see:

serviceaccount/cody-sa created
secret/cody-sa created
clusterrolebinding.rbac.authorization.k8s.io/cody-sa created

- 

Download the generate-sa-kubeconfig.sh script.

- 

Run the script. Replace <SERVICE-ACCOUNT-NAME>
 with the Service Account name you used in the manifest file. Replace
 <NAMESPACE> with the namespace you used in the manifest file:

bash generate-sa-kubeconfig.sh <SERVICE-ACCOUNT-NAME> <NAMESPACE>

The script generates a kubeconfig named
<SERVICE-ACCOUNT-NAME>-<NAMESPACE>.kubeconfig.

Example output:

Getting cluster details from current context...
Extracting token from Secret 'cody-sa' in 'mk8s-docs-examples'...
Creating kubeconfig file: cody-sa-mk8s-docs-examples.kubeconfig
---
Success! Wrote kubeconfig to cody-sa-mk8s-docs-examples.kubeconfig

- 

Test the kubeconfig. Replace <KUBECONFIG> with the path to the generated
 kubeconfig:

kubectl --kubeconfig <KUBECONFIG> get pods

Example output:

NAME READY STATUS RESTARTS AGE
vllm-server-566749d844-bnxsk 1/1 Running 0 3d6h

## Creating a Pod with access to GPUs and InfiniBand (RDMA)#

Worker (GPU) nodes in MK8s are tainted to prevent non-GPU workloads from being
scheduled on them by default. To run GPU-enabled or RDMA-enabled workloads on
these nodes, your Pod spec must include the appropriate tolerations and resource
requests.

To schedule a Pod on a GPU node using kubectl, include the following
toleration in your Pod spec:

spec:
 tolerations:
 - key: "nvidia.com/gpu"
 operator: "Equal"
 value: "true"
 effect: "NoSchedule"

This toleration matches the taint applied to GPU nodes and allows the scheduler
to place your Pod on them.

To allocate GPU resources to your container, specify them explicitly in the
resources.limits section. For example, to request one GPU:

resources:
 limits:
 nvidia.com/gpu: "1"

If your container also requires InfiniBand (RDMA) support, you must request the
RDMA device and include the following runtime configuration:

containers:
 - name: <CONTAINER-NAME>
 image: <CONTAINER-IMAGE>
 resources:
 limits:
 nvidia.com/gpu: "8"
 rdma/rdma_shared_device_a: "1"
 memory: 16Gi
 requests:
 nvidia.com/gpu: "8"
 rdma/rdma_shared_device_a: "1"
 volumeMounts:
 - name: dshm
 mountPath: /dev/shm
 securityContext:
 capabilities:
 add:
 - IPC_LOCK

volumes:
 - name: dshm
 emptyDir:
 medium: Memory
 sizeLimit: 16Gi

Note

Setting volumes.emptyDir.sizeLimit to 16Gi ensures that sufficient
RAM-backed shared memory is available at /dev/shm for RDMA and
communication libraries such as NCCL. (See, for example,
NVIDIA's documentation on troubleshooting NCCL shared memory issues.)

Note that if no memory limit is set on a container using a /dev/shm mount,
the cluster will reject the pod with an error:
ValidatingAdmissionPolicy 'workload-policy.lambda.com' with binding
'workload-policy-binding.lambda.com' denied request:
(requireDevShmMemoryLimit) Pods are not allowed to have containers that
mount /dev/shm and do not configure any memory resource limits (e.g.
spec.containers[*].resources.limits.memory=1536G).

Defining a memory limit ensures the kernel memory allocator can function
efficiently, helping maintain overall node stability.

## Creating Ingresses to access services#

MK8s comes preconfigured with the
Traefik Proxy
and
ExternalDNS.
MK8s includes a pre-provisioned wildcard TLS certificate for
*.<CLUSTER-ZONE>.k8s.lambda.ai, which is used by the Ingress Controller
by default. This setup allows you to expose services securely via public URLs in
the format https://<SERVICE>.<CLUSTER-ZONE>.k8s.lambda.ai.

### Obtain the CLUSTER-ZONE#

To obtain the <CLUSTER-ZONE> using kubectl:

kubectl get -n kube-system configmap cluster-configuration -o jsonpath='{.data.zone}'

### Create an Ingress#

To create an Ingress:

- 

Create an Ingress manifest. For example:

apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
 name: <NAME>
 namespace: <NAMESPACE>
spec:
 ingressClassName: traefik-public
 rules:
 - host: <SERVICE>.<CLUSTER-ZONE>.k8s.lambda.ai
 http:
 paths:
 - path: /
 pathType: Prefix
 backend:
 service:
 name: <SERVICE>
 port:
 name: http

 tls:
 - hosts:
 - <SERVICE>.<CLUSTER-ZONE>.k8s.lambda.ai

- 

Apply the Ingress manifest. Replace <INGRESS-MANIFEST> with the path to
 your manifest file:

kubectl apply -f <INGRESS-MANIFEST>

Example output:

ingress.networking.k8s.io/vllm-ingress created

- 

Verify the Ingress was created. Replace <NAMESPACE> and <NAME> with
 your values:

kubectl describe -n <NAMESPACE> ingress <NAME>

You should see output similar to:

Name: vllm-ingress
Labels: <none>
Namespace: mk8s-docs-examples
Address: 192.222.48.194,192.222.48.250,192.222.48.39
Ingress Class: traefik-public
Default backend: <default>
TLS:
 SNI routes vllm.mk8s-yns66blqnvvvffjc.us-east.k8s.lambda.ai
Rules:
 Host Path Backends
 ---- ---- --------
 vllm.mk8s-yns66blqnvvvffjc.us-east.k8s.lambda.ai
 / vllm-service:http (10.42.2.16:8000)
Annotations: <none>
Events: <none>

## Shared and node-local persistent storage#

MK8s provides 6 StorageClasses for persistent storage:

- 

lambda-shared: Shared storage backed by a
 Lambda Filesystem on a network-attached
 storage cluster. It's accessible from all nodes and provides robust, durable
 storage. Lambda Filesystems in the us-east-2 and us-midwest-2 regions can
 also be accessed externally via the Lambda
 S3 Adapter.

- 

lambda-shared-retain: Identical to lambda-shared, but uses the Retain
 reclaim policy. When the PVC is deleted, the underlying volume and its data
 are preserved rather than removed, and must be reclaimed or cleaned up
 manually. Use this for shared data you want to protect against accidental PVC
 deletion.

- 

lambda-local: Local NVMe-backed storage on the node. It's fast and useful
 for scratch space but isn't accessible from other nodes. Data is lost if the
 node or NVMe drive fails.

- 

lambda-local-retain: Identical to lambda-local, but uses the Retain
 reclaim policy. The underlying volume and its data persist after the PVC is
 deleted. Note that because this storage is node-local, retained data is still
 lost if the node or NVMe drive fails; Retain only protects against deletion,
 not hardware failure.

- 

lambda-nfs: Shared NFS-backed storage provisioned through the NFS CSI
 driver. Accessible from all nodes and durable across node failures. Volumes
 bind immediately on PVC creation. When the PVC is deleted, the underlying
 volume and its data are also deleted.

- 

lambda-nfs-retain: Identical to lambda-nfs, but uses the Retain reclaim
 policy. The underlying volume and its data persist after the PVC is deleted,
 requiring manual reclamation. Use this for NFS-backed data that must survive
 PVC deletion.

Note

The lambda-nfs and lambda-nfs-retain StorageClasses should be preferred.
lambda-shared and lambda-shared-retain are mostly kept for backwards
compatibility with existing workloads.

These StorageClasses let you persist data across pod restarts or rescheduling.
However, lambda-local and lambda-local-retain do not persist across node
failures.

To use persistent storage in MK8s, workloads must request a
PersistentVolumeClaim (PVC). You can specify the size, access mode, and
StorageClass in the PVC. By default, the lambda-shared StorageClass is used.

Volumes created from PVCs bind immediately, rather than waiting for a pod to
consume them. This ensures that volume provisioning and scheduling happen up
front.

Persistent storage is useful for:

- Saving model checkpoints.

- Storing datasets.

- Writing logs shared across workloads.

To create and manage PVCs:

- 

Create a PVC manifest file. For example, to create a PVC using the
 lambda-shared storage class and a capacity of 128 GiB:

apiVersion: v1
kind: PersistentVolumeClaim
metadata:
 name: <NAME>
 namespace: <NAMESPACE>
spec:
 storageClassName: lambda-shared
 accessModes:
 - ReadWriteMany
 resources:
 requests:
 storage: 128Gi

- 

Apply the manifest:

kubectl apply -f <PVC-MANIFEST>

Replace <PVC-MANIFEST> with the path to your YAML file.

- 

Verify that the PVC was created:

kubectl get -n <NAMESPACE> pvc

Example output:

NAME STATUS VOLUME CAPACITY ACCESS MODES STORAGECLASS VOLUMEATTRIBUTESCLASS AGE
huggingface-cache Bound pvc-972f79ff-7afd-42ee-897b-e18f0788a620 128Gi RWX lambda-shared <unset> 3d9h

Tip

If your container only needs to read data from a PVC, such as loading a
static dataset or pretrained model weights, you can mount the volume as
read-only to prevent accidental writes:

spec:
 containers:
 - name: <CONTAINER-NAME>
 volumeMounts:
 - name: <VOLUME-NAME>
 mountPath: <MOUNT-PATH>
 readOnly: true
 volumes:
 - name: <VOLUME-NAME>
 persistentVolumeClaim:
 claimName: <PVC-NAME>

## Example 1: Deploy a vLLM server to serve Hermes 4#

In this example, you'll deploy a vLLM server in MK8s to serve Nous Research's
Hermes 4 LLM.

Before you begin, make sure you've
set up kubectl access to the MK8s cluster.

### Create a Namespace to group resources#

First, create a namespace for this example and the following example:

- 

Run:

kubectl create namespace mk8s-docs-examples

Expected output:

namespace/mk8s-docs-examples created

### Create a PVC to cache downloaded models#

Next, create a PVC to cache model files downloaded from Hugging Face:

- 

Apply the huggingface-cache.yaml PVC manifest:

kubectl apply -f https://docs.lambda.ai/assets/code/huggingface-cache.yaml

Expected output:

persistentvolumeclaim/huggingface-cache created

- 

Confirm the PVC was created:

kubectl get -n mk8s-docs-examples pvc

Expected output:

NAME STATUS VOLUME CAPACITY ACCESS MODES STORAGECLASS VOLUMEATTRIBUTESCLASS AGE
huggingface-cache Bound pvc-972f79ff-7afd-42ee-897b-e18f0788a620 128Gi RWX lambda-shared <unset> 20s

### Deploy a vLLM server in the cluster#

- 

Apply the vllm-deployment-lks.yaml manifest:

kubectl apply -f https://docs.lambda.ai/assets/code/vllm-deployment-lks.yaml

Expected output:

deployment.apps/vllm-server created

### Create a Service to expose the vLLM server#

- 

Apply the vllm-service.yaml manifest:

kubectl apply -f https://docs.lambda.ai/assets/code/vllm-service.yaml

Expected output:

service/vllm-service created

### Create the Ingress to expose the vLLM service publicly#

To expose the vLLM server over the internet:

- 

Download the vllm-ingress-lks.yaml manifest file.

- 

In the manifest file, replace <CLUSTER-ZONE> with your actual cluster zone.

- 

Apply the manifest:

kubectl apply -f vllm-ingress-lks.yaml

- 

Confirm the Ingress was created:

kubectl get -n mk8s-docs-examples ing

Expected output:

NAME CLASS HOSTS ADDRESS PORTS AGE
vllm-ingress traefik-public vllm.mk8s-yns66blqnvvvffjc.us-east.k8s.lambda.ai 192.222.48.194,192.222.48.250,192.222.48.39 80, 443 2m12s

MK8s will automatically create a DNS record and obtain a TLS certificate,
enabling secure access to the vLLM service.

Note

It can take up to an hour for the DNS record to propagate to your DNS
servers. To check the propagation status, run:

dig <HOSTNAME> +short

If the record has propagated, you'll see three IP addresses. These are the
IPs of your 1CC head nodes.

### Submit a prompt to the vLLM server#

- 

To verify that the vLLM server is working, submit a prompt using curl.
 Replace <CLUSTER-ZONE> with the value you obtained from the kubectl get
 configmap cluster-configuration command.

curl -X POST https://vllm.<CLUSTER-ZONE>.k8s.lambda.ai/v1/completions \
 -H "Content-Type: application/json" \
 -d "{
 \"prompt\": \"What is the name of the capital of France?\",
 \"model\": \"NousResearch/Hermes-4-14B\",
 \"temperature\": 0.0,
 \"max_tokens\": 100
 }"

### Clean up the example resources#

- 

To delete the Ingress, Service, and Deployment created in this example:

kubectl delete -f https://docs.lambda.ai/assets/code/vllm-ingress-lks.yaml
kubectl delete -f https://docs.lambda.ai/assets/code/vllm-service.yaml
kubectl delete -f https://docs.lambda.ai/assets/code/vllm-deployment-lks.yaml

Note

If you don't plan to continue to the next example or no longer need the
cached model files, you can also delete the PVC using:

kubectl delete -f https://docs.lambda.ai/assets/code/huggingface-cache.yaml

## Example 2: Evaluate multiplication-solving abilities of the DeepSeek R1 Distill Qwen 7B model#

This example assumes you've already completed the following steps in the
previous example:

- Set up kubectl access to your MK8s cluster.

- Created the mk8s-docs-examples namespace.

- Created the huggingface-cache PVC.

### Run a Job to evaluate the multiplication-solving accuracy of the model#

- 

Apply the multiplication-eval-deepseek-r1-distilll-qwen-7b.yaml manifest:

kubectl apply -f https://docs.lambda.ai/assets/code/multiplication-eval-deepseek-r1-distilll-qwen-7b.yaml

Expected output:

job.batch/multiplication-eval-deepseek-r1-distilll-qwen-7b created

### View the Job logs#

To follow the Job logs as the job runs:

kubectl logs -f jobs/multiplication-eval-deepseek-r1-distilll-qwen-7b

You should see output from vLLM as the job runs.

When the job finishes, you should see a line displaying the accuracy of the
job:

Processed prompts: 100%|██████████| 1000/1000 [00:10<00:00, 97.89it/s, est. speed input: 1652.09 toks/s, output: 28255.96 toks/s]
Model deepseek-ai/DeepSeek-R1-Distill-Qwen-7B accuracy: 0.8900

### Monitor 1CC utilization during evaluation#

To monitor 1CC utilization as the evaluation Job runs:

- 

Navigate to https://grafana.<CLUSTER-ZONE>.k8s.lambda.ai.
 Replace <CLUSTER-ZONE> with the actual cluster zone of your MK8s cluster.

- 

At the login prompt, click Sign in with lambda.

- 

In the left nav, click Dashboards.

- 

Click NVIDIA DCGM Exporter Dashboard.

### Clean up the example resources#

The Job is configured to delete itself five minutes after it completes. If you
want to delete it immediately, run:

kubectl delete -f https://docs.lambda.ai/assets/code/multiplication-eval-deepseek-r1-distilll-qwen-7b.yaml

If you're finished with the examples and no longer need the cached model data,
you can also delete the huggingface-cache PVC:

kubectl delete -f https://docs.lambda.ai/assets/code/huggingface-cache.yaml

## Next steps#

- Learn more about using Kubernetes.

- Learn more about using Traefik Proxy.

- Learn more about using Grafana.

 Back to top
