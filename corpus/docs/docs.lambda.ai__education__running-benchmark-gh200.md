# Running a PyTorch®-based benchmark on an NVIDIA GH200 instance - Lambda Docs

Source: https://docs.lambda.ai/education/running-benchmark-gh200/

Skip to content

# Running a PyTorch®-based benchmark on an NVIDIA GH200 instance#

This tutorial describes how to run an NGC-based benchmark on an On-Demand Cloud
(ODC) instance backed with the NVIDIA GH200 Grace Hopper Superchip. The tutorial
also outlines how to run the benchmark on other ODC instance types to compare
performance. The benchmark uses a variety of PyTorch® examples from
NVIDIA's
Deep Learning Examples
repository.

## Prerequisites#

To run this tutorial successfully, you'll need the following:

- A GitHub account and some familiarity with a Git-based workflow.

- The following tools and libraries installed on the machine or instance
 you plan to benchmark. These tools and libraries are installed by default
 on your ODC instances:

- NVIDIA driver

- Docker

- Git

- nvidia-container-toolkit

- Python

## Setting up your environment#

### Launch your GH200 instance#

Begin by launching a GH200 instance:

- In the Lambda Cloud console, navigate to the
 SSH keys page,
 click Add SSH Key, and then add or generate a SSH key.

- Navigate to the
 Instances page
 and click Launch Instance.

- 

Follow the steps in the instance launch wizard.

- Instance type: Select 1x GH200 (96 GB).

- Region: Select an available region.

- Filesystem: Don't attach a filesystem.

- SSH key: Use the key you created in step 1.

- 

Click Launch instance.

- Review the EULAs. If you agree to them, click I agree to the above to
 start launching your new instance. Instances can take up to five minutes to
 fully launch.

### Set the required environment variables#

Next, set the environment variables you need to run the benchmark:

- In the Lambda Cloud console, navigate to the
 Instances page,
 find the row for your instance, and then click Launch in the
 Cloud IDE column. JupyterLab opens in a new window.

- In JupyterLab's Launcher tab, under Other, click Terminal to
 open a new terminal.

- 

Open your .bashrc file for editing:

nano ~/.bashrc

- 

At the bottom of the file, set the following environment variables.
 Replace <GIT-USERNAME> with your GitHub username and <GIT-EMAIL> with
 the email address associated with your GitHub account:

Note

If desired, you can update the value of NAME_NGC below to
reflect the latest version of PyTorch®. This tutorial isn't pinned
to a specific version.

export NAME_NGC=pytorch:24.10-py3
export NAME_TYPE=ODC
export NAME_DATASET=all
export NAME_TASKS=all
export NUM_GPU=1
export NAME_GPU=GH200_96GB
export NAME_RESULTS=gh200_benchmark_results
export GIT_USERNAME=<GIT-USERNAME>
export GIT_EMAIL=<GIT-EMAIL>

- 

Save and exit.

- 

Update your environment with your new environment variables:

source ~/.bashrc

## Running the GH200 benchmark#

### Run the benchmark#

Now that you've set up your environment, you can run the benchmark on your GH200
instance:

- In your web browser, navigate to the
 lambdal/deeplearning-benchmark
 repository on GitHub and then fork the repository. By using your own fork
 instead of the original repository, you'll be able to push your benchmark
 results to a single location.

- 

In your ODC instance's JupyterLab terminal, pull the NGC PyTorch®
 Docker image:

sudo docker pull nvcr.io/nvidia/${NAME_NGC} 2>&1

- 

Clone the LambdaLabsML/DeepLearningExamples repository, check out
 its lambda/benchmark branch, and then clone your forked repository:

git clone https://github.com/LambdaLabsML/DeepLearningExamples.git &&
cd DeepLearningExamples &&
git checkout lambda/benchmark &&
cd .. &&
git clone https://github.com/${GIT_USERNAME}/deeplearning-benchmark.git

- 

Navigate to the pytorch directory, and then download and prepare the
 dataset that the benchmark will use. This step might take up to 20 minutes
 to complete:

cd deeplearning-benchmark/pytorch &&
mkdir ~/data &&
sudo docker run --gpus all --rm --shm-size=256g \
-v ~/DeepLearningExamples/PyTorch:/workspace/benchmark \
-v ~/data:/data \
-v $(pwd)"/scripts":/scripts \
nvcr.io/nvidia/${NAME_NGC} \
/bin/bash -c "cp -r /scripts/* /workspace; ./run_prepare.sh ${NAME_DATASET}"

- 

Create a PyTorch® configuration file for the benchmark:

cp scripts/config_v2/config_pytorch_${NUM_GPU}x${NAME_GPU}_v2.sh scripts/config_v2/config_pytorch_${NAME_TYPE}_${NUM_GPU}x${NAME_GPU}_$(hostname)_v2.sh

- 

Create a new directory named gh200_benchmark_results to store the
 benchmark results in:

mkdir -p ${NAME_RESULTS}

- 

Run the benchmark:

sudo docker run --rm --shm-size=1024g \
--gpus all \
-v ~/DeepLearningExamples/PyTorch:/workspace/benchmark \
-v ~/data:/data \
-v $(pwd)"/scripts":/scripts \
-v $(pwd)/${NAME_RESULTS}:/results \
nvcr.io/nvidia/${NAME_NGC} \
/bin/bash -c "cp -r /scripts/* /workspace; ./run_benchmark.sh ${NAME_TYPE}_${NUM_GPU}x${NAME_GPU}_$(hostname)_v2 ${NAME_TASKS} 3000"

### Compile the results to CSV#

When the benchmark completes, it publishes the results to a subdirectory of your
results_v2 directory. You can compile a summary of these results to CSV by
running the following scripts from the pytorch folder:

python scripts/compile_results_pytorch_v2.py --path ${NAME_RESULTS} --precision fp32 &&
python scripts/compile_results_pytorch_v2.py --path ${NAME_RESULTS} --precision fp16

The resulting CSV files appear in the pytorch directory:

pytorch-train-throughput-v2-fp16.csv
pytorch-train-throughput-v2-fp32.csv

### Push the results to GitHub#

Finally, push the results to your GitHub repository:

- 

In your web browser, log into GitHub and
 create a new fine-grained personal access token
 with the following configuration. Make sure to copy the token and paste it
 somewhere safe for future use:

- Token name: GH200 benchmarking

- Respository access: Select Only select repositories, and
 then select your deeplearning-benchmark fork from the dropdown.

- Permissions: Under Repository permissions, set Contents
 to Read and write.

- 

In your terminal in JupyterLab, set an environment variable for your
 GitHub token. Replace <GIT-TOKEN> with the personal access token you
 created in step 1:

export GIT_TOKEN=<GIT-TOKEN>

- 

Configure your Git credentials:

git config --global user.name "${GIT_USERNAME}" &&
git config --global user.email "${GIT_EMAIL}"

- 

Navigate to the pytorch directory, and then fetch the latest changes
 from the repo's master branch and merge them into your current branch:

cd ~/deeplearning-benchmark/pytorch &&
git pull origin master

- 

Navigate to the pytorch directory and then commit your results:

git add scripts/config_v2 &&
git add ${NAME_RESULTS} &&
git add pytorch-train-throughput-v2-fp16.csv &&
git add pytorch-train-throughput-v2-fp32.csv &&
git commit -m "Update from $(hostname)"

- 

Set origin to your forked repository:

git remote set-url origin https://${GIT_USERNAME}:${GIT_TOKEN}@github.com/${GIT_USERNAME}/deeplearning-benchmark.git

- 

Push the results to your forked repository.

git push origin master

That's it! To see your benchmarks, navigate to the pytorch folder in your
forked repo on GitHub, and then click on one of the two CSV files. GitHub
renders your CSV files in an easy-to-scan tablular format by default.

## Running the benchmark on other instance types#

Without other data to compare it to, your GH200 benchmark data is of limited
use. You can run the benchmark on other ODC instance types by modifying the
instructions in the Setting up your environment
section above. Make the following changes:

- When launching your instance, select the instance type you want to
 benchmark.

- 

When setting your environment variables, set NAME_GPU to the
 appropriate string for your GPU and NUM_GPU to the number of GPUs
 attached to the instance. The naming pattern for NAME_GPU is as follows:

<GPU-TYPE>_<GPU-VRAM>GB_<GPU-CONNECTION-TYPE>

For example, if you're planning to benchmark an 8xH100 80GB SXM instance,
you should set NAME_GPU and NUM_GPU as follows:

export NAME_GPU=H100_80GB_SXM
export NUM_GPU=8

Important

If the instance type doesn't explicitly state a GPU connection type,
omit _<GPU-CONNECTION-TYPE> from the naming pattern.

After you've launched and set up your instance, you can run the instructions in
the Running the GH200 benchmark section as
normal. As before, you can compare results by clicking on each of the CSV file
you generated.

## Cleaning up#

When you're done with your instances, terminate them to avoid incurring
unnecessary costs:

- In the Lambda Cloud console, navigate to the
 Instances page.

- Select the checkboxes of the instances you want to delete.

- Click Terminate. A dialog appears.

- Follow the instructions and then click Terminate instances to
 terminate your instances.

## Next steps#

- To learn how to use Hugging Face's Diffusers and Transformers libraries on
 a GH200 instance, see
 Running Hugging Face Transformers and Diffusers on an NVIDIA GH200 instance.

- For more tips and tutorials, visit the Education landing page.

 Back to top
