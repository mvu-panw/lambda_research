# Using Lambda's Managed Kubernetes - Lambda Docs

Source: https://docs.lambda.ai/managed-kubernetes/managed-kubernetes-legacy/

Skip to content

# Using Lambda's Managed Kubernetes#

## Introduction#

This guide walks you through getting started with
Lambda's Managed Kubernetes
(MK8s) on a
1-Click Cluster
(1CC).

MK8s provides a Kubernetes environment with GPU support, InfiniBand (RDMA), and
shared persistent storage across all nodes in a 1CC. Clusters are preconfigured
so you can deploy workloads without additional setup.

You'll learn how to:

- Access MK8s using the Rancher Dashboard and kubectl.

- Organize workloads using projects and namespaces.

- Deploy and manage applications.

- Expose services using Ingresses.

- Use shared and node-local persistent storage.

- Monitor GPU usage with the NVIDIA DCGM Grafana dashboard.

The guide includes two examples.

In the first, you'll deploy a vLLM server to serve the
NousResearch Hermes 3
model:

- Create a namespace for the examples.

- Add a PersistentVolumeClaim (PVC) to cache model downloads.

- Deploy the vLLM server.

- Expose it with a Service.

- Configure an Ingress to make it accessible externally.

In the second, you'll evaluate the multiplication-solving accuracy of the
DeepSeek R1 Distill Llama 70B
model using vLLM:

- Run a batch job that performs the evaluation.

- Monitor GPU utilization during the run.

## Prerequisites#

You need the Kubernetes command-line tool, kubectl, to interact with the
cluster. Refer to the Kubernetes documentation for
installation instructions.

## Accessing MK8s#

After your 1CC with MK8s is provisioned, you'll receive credentials to access
MK8s. These include the Rancher Dashboard URL, username, and password.

To access MK8s using either the Rancher Dashboard or kubectl, you must first
configure a firewall rule:

- 

In the Cloud dashboard, go to the
 Firewall page.

- 

Click Edit to modify the inbound firewall rules.

- 

Click Add rule, then set up the following rule:

- Type: Custom TCP

- Protocol: TCP

- Port range: 443

- Source: 0.0.0.0/0

- Description: Managed Kubernetes dashboard

- 

Click Update and save.

### Rancher Dashboard#

To access the MK8s Rancher Dashboard:

- 

In your browser, go to the URL provided along with your MK8s credentials.
 You'll see a login screen.

- 

Enter your username and password, then click Log in with Local User.

- 

In the left sidebar, click the Local Cluster button:

### kubectl#

To access MK8s using kubectl:

- 

Open the Rancher Dashboard as described above.

- 

In the top-right corner, click the Download KubeConfig button:

- 

Save the file to ~/.kube/config. Alternatively, set the KUBECONFIG
 environment variable to the path of the file.

- 

(Optional) Restrict access to the file:

chmod 600 ~/.kube/config

- 

Test the connection:

kubectl get nodes

You should see output similar to the following:

NAME STATUS ROLES AGE VERSION
head-01 Ready control-plane,etcd,master 8d v1.32.3+rke2r1
head-02 Ready control-plane,etcd,master 8d v1.32.3+rke2r1
head-03 Ready control-plane,etcd,master 8d v1.32.3+rke2r1
worker-01 Ready <none> 8d v1.32.3+rke2r1
worker-02 Ready <none> 8d v1.32.3+rke2r1

## Managing projects and namespaces#

MK8s is configured with a single Rancher project, where you have the
Project Owner role.

As a Project Owner, you can create and manage namespaces, assign roles to other
users, and configure most project-level settings.

Within this project, use Kubernetes namespaces to group related resources, such
as pods, services, deployments, ConfigMaps, secrets, and persistent volume
claims.

For more details, see
Rancher's documentation on projects and namespaces.

To create and manage namespaces:

- 

Log in to the Rancher Dashboard.

- 

In the left sidebar, go to Cluster > Projects/Namespaces.

Warning

Avoid creating namespaces with kubectl. Namespaces created this way aren't
associated with any Rancher project and won't function correctly in MK8s.

## Creating a Pod with access to GPUs and InfiniBand (RDMA)#

Worker (GPU) nodes in MK8s are tainted to prevent non-GPU workloads from being
scheduled on them by default. To run GPU-enabled or RDMA-enabled workloads on
these nodes, your Pod spec must include the appropriate tolerations and resource
requests.

### kubectl#

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
 memory: 1Ti
 requests:
 nvidia.com/gpu: "8"
 rdma/rdma_shared_device_a: "1"
 volumeMounts:
 - name: dev-shm
 mountPath: /dev/shm
 securityContext:
 capabilities:
 add:
 - IPC_LOCK

volumes:
- name: dev-shm
 emptyDir:
 medium: Memory
 sizeLimit: 100Gi

Note

Setting volumes.emptyDir.sizeLimit to 100Gi ensures that sufficient
RAM-backed shared memory is available at /dev/shm for RDMA and
communication libraries such as NCCL. (See, for example,
NVIDIA's documentation on troubleshooting NCCL shared memory issues.)

Note that if no memory limit is set on a container using a /dev/shm mount,
the cluster will reject the pod with an error similar to:
ValidatingAdmissionPolicy 'workload-policy.lambda.com' with binding
'workload-policy-binding.lambda.com' denied request:
(requireDevShmMemoryLimit) Pods are not allowed to have containers that
mount /dev/shm and do not configure any memory resource limits (e.g.
spec.containers[*].resources.limits.memory=1536G).

Defining a memory limit ensures the kernel memory allocator can function
efficiently, helping maintain overall node stability.

## Creating an Ingress to access services#

MK8s comes preconfigured with the
Traefik Proxy
and
ExternalDNS.
The cluster includes a pre-provisioned wildcard TLS certificate for
*.<CLUSTER-NAME>.clusters.gpus.com, which is used by the Ingress Controller by
default. This setup allows you to expose services securely via public URLs in
the format https://<SERVICE>.<CLUSTER-NAME>.clusters.gpus.com.

### kubectl#

To create an Ingress using kubectl:

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
 - host: <SERVICE>.<CLUSTER-NAME>.clusters.gpus.com
 http:
 paths:
 - path: /
 pathType: Prefix
 backend:
 service:
 name: <SERVICE>
 port:
 name: http
 path: /
 pathType: Prefix
 tls:
 - hosts:
 - <SERVICE>.<CLUSTER-NAME>.clusters.gpus.com

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
Address: 192.222.48.191,192.222.48.194,192.222.48.220
Ingress Class: traefik-public
Default backend: <default>
TLS:
 SNI routes vllm.setest-onecc-mk8s01.clusters-stg.gpus.com
Rules:
 Host Path Backends
 ---- ---- --------
 vllm.setest-onecc-mk8s01.clusters-stg.gpus.com
 / vllm-service:http (10.42.2.45:8000)
Annotations: field.cattle.io/publicEndpoints:
 [{"addresses":["192.222.48.191","192.222.48.194","192.222.48.220"],"port":443,"protocol":"HTTPS","serviceName":"mk8s-docs-examples:vllm-se...

## Shared and node-local persistent storage#

MK8s provides two StorageClasses for persistent storage:

- 

lambda-shared: Shared storage backed by a
 Lambda Filesystem on a network-attached storage
 cluster. It's accessible from all nodes and provides robust, durable storage.
 The Lambda Filesystem can also be accessed externally via the Lambda
 S3 Adapter.

- 

lambda-local: Local NVMe-backed storage on the node. It's fast and useful
 for scratch space but isn't accessible from other nodes. Data is lost if the
 node or NVMe drive fails.

These StorageClasses let you persist data across pod restarts or rescheduling.
However, only lambda-shared persists across node failures.

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

### kubectl#

To create and manage PVCs using kubectl:

- 

Create a PVC manifest file. For example, to create a PVC using the
 lambda-shared storage class and a capacity of 400 GiB:

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
 storage: 400Gi

- 

Apply the manifest:

kubectl apply -f <PVC-MANIFEST>

Replace <PVC-MANIFEST> with the path to your YAML file.

- 

Verify that the PVC was created:

kubectl get -n <NAMESPACE> pvc

Example output:

NAME STATUS VOLUME CAPACITY ACCESS MODES STORAGECLASS VOLUMEATTRIBUTESCLASS AGE
huggingface-cache Bound pvc-8463f8d7-ca83-4dfd-8b21-a42edf09948b 400Gi RWX lambda-shared <unset> 45m

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

### Rancher Dashboard#

To create and manage PVCs using the Rancher dashboard:

- 

Log in to the Rancher Dashboard.

- 

In the left sidebar, navigate to Storage > PersistentVolumeClaims.

- 

Click Create in the top right corner.

- 

In the Storage Class dropdown, select either lambda-shared or
 lambda-local:

- 

Configure the PVC settings, such as name, namespace, access mode, and
 requested capacity.

- 

Click Create in the bottom right corner to finish.

## Example 1: Deploy a vLLM server to serve Hermes 3#

In this example, you'll deploy a vLLM server in MK8s to serve Nous Research's
Hermes 3 LLM. You'll use the Rancher Dashboard to create a namespace and use
kubectl to create a PVC, Service, and Ingress.

Before you begin, make sure you've
set up kubectl access to the MK8s cluster.

### Create a namespace to group resources#

First, create a namespace for this example and the following example:

- 

Log in to the Rancher Dashboard.

- 

Navigate to Cluster > Projects/Namespaces.

- 

Click Create Namespace:

- 

Enter mk8s-docs-examples as the namespace name.

- 

Click Create in the bottom right corner.

### Create a PVC to cache downloaded models#

Next, create a PVC to cache model files downloaded from Hugging Face:

- 

Download the huggingface-cache.yaml PVC manifest file.

- 

Apply the manifest using kubectl:

kubectl apply -f huggingface-cache.yaml

Expected output:

persistentvolumeclaim/huggingface-cache created

- 

In the Rancher Dashboard, navigate to Storage >
 PersistentVolumeClaims to confirm the PVC was created:

### Deploy a vLLM server in the cluster#

- 

Download the vllm-deployment.yaml manifest file.

- 

Apply the manifest:

kubectl apply -f vllm-deployment.yaml

- 

In the Rancher Dashboard, go to Workloads > Deployments to confirm
 that the Deployment is running:

### Create a Service to expose the vLLM server#

- 

Download the vllm-service.yaml manifest file.

- 

Apply the manifest:

kubectl apply -f vllm-service.yaml

- 

In the Rancher Dashboard, go to Service Discovery > Services to
 confirm the Service was created:

### Create the Ingress to expose the vLLM service publicly#

To expose the vLLM server over the internet:

- 

Download the vllm-ingress.yaml manifest file.

- 

In the manifest, replace <CLUSTER-NAME> with the name of your cluster.

- 

Apply the manifest:

kubectl apply -f vllm-ingress.yaml

MK8s will automatically create a DNS record and obtain a TLS certificate,
enabling secure access to the vLLM service.

Note

It can take up to an hour for the DNS record to propagate to your DNS
servers. To check the propagation status, run:

dig <HOSTNAME> +short

If the record has propagated, you'll see three IP addresses. These are
the IPs of your 1CC head nodes.

- 

In the Rancher Dashboard, go to Service Discovery > Ingresses to
 confirm the Ingress was created. Under Target, you'll find the URL to
 access the vLLM service:

### Submit a prompt to the vLLM server#

- 

To verify that the vLLM server is working, submit a prompt using curl.
 Replace <CLUSTER-NAME>with the name of your MK8s cluster:

curl -X POST https://vllm.<CLUSTER-NAME>.clusters.gpus.com/v1/completions \
 -H "Content-Type: application/json" \
 -d "{
 \"prompt\": \"What is the name of the capital of France?\",
 \"model\": \"NousResearch/Hermes-3-Llama-3.1-8B\",
 \"temperature\": 0.0,
 \"max_tokens\": 1
 }"

### Clean up the example resources#

- 

To delete the Ingress, Service, and Deployment created in this example:

kubectl delete -f vllm-ingress.yaml
kubectl delete -f vllm-service.yaml
kubectl delete -f vllm-deployment.yaml

Note

If you don't plan to continue to the next example or no longer need the
cached model files, you can also delete the PVC using:

kubectl delete -f huggingface-cache.yaml

## Example 2: Evaluate multiplication-solving abilities of the DeepSeek R1 Distill model#

This example assumes you've already completed the following steps in the
previous example:

- Set up kubectl access to your MK8s cluster.

- Created the mk8s-docs-examples namespace.

- Created the huggingface-cache PVC.

### Run a Job to evaluate multiplication-solving accuracy#

- 

Download the Job manifest
 for the DeepSeek R1 Distill model.

- 

Apply the manifest using kubectl:

kubectl apply -f multiplication-eval-deepseek-r1-distill-llama-70b.yaml

You should see:

job.batch/multiplication-eval-deepseek-r1-distill-llama-70b created

### View the Job logs#

To follow the evaluation output in real time:

- 

In the Rancher Dashboard, go to Workloads > Jobs.

- 

Click the Job name,
 multiplication-eval-deepseek-r1-distill-llama-70b:

- 

Click ⋮ at the right of the container row and select View Logs:

When the Job completes, you'll see the final accuracy value printed in the logs.
In the example below, the model achieved an accuracy of 0.6010:

### Monitor 1CC utilization during evaluation#

To monitor GPU utilization while the Job runs:

- 

In the Rancher Dashboard sidebar, navigate to Monitoring > Grafana.

- 

In the Grafana sidebar, go to Dashboards > NVIDIA DCGM Exporter
 Dashboard.

- 

In the instance dropdown, select all available instances.

- 

In the gpu dropdown, select All.

- 

Set the time range to Last 5 minutes.

- 

Set the auto-refresh interval to 5s.

While the Job runs, you should see a dashboard similar to:

### Clean up the example resources#

The Job is configured to delete itself five minutes after it completes. If you
want to delete it immediately, run:

kubectl delete -f multiplication-eval-deepseek-r1-distill-llama-70b.yaml

If you're finished with the examples and no longer need the cached model data,
you can also delete the huggingface-cache PVC:

kubectl delete -f huggingface-cache.yaml

## Next steps#

- Learn more about using Kubernetes.

- Learn more about using Rancher.

- Learn more about using Traefik Proxy.

- Learn more about using Grafana.

 Back to top
