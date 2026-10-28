# Fine-tuning the Mochi video generation model on GH200 - Lambda Docs

Source: https://docs.lambda.ai/education/fine-tune-mochi-gh200/

Skip to content

# Fine-tuning the Mochi video generation model on GH200#

This guide helps you get started fine-tuning
Genmo's Mochi video generation model
using a
Lambda On-Demand Cloud
GH200 instance.

## Launch your GH200 instance#

Begin by launching a GH200 instance:

- In the Lambda Cloud console, navigate to the
 SSH keys page,
 click Add SSH Key, and then add or generate a SSH key.

- Navigate to the
 Instances page
 and click Launch Instance.

- Follow the steps in the instance launch wizard.

- Instance type: Select 1x GH200 (96 GB).

- Region: Select an available region.

- Filesystem: Don't attach a filesystem.

- SSH key: Use the key you created in step 1.

- Click Launch instance.

- Review the EULAs. If you agree to them, click I agree to the above to
 start launching your new instance. Instances can take up to five minutes to
 fully launch.

## Install dependencies#

- 

Install the dependencies needed for this guide by running:

git clone https://github.com/genmoai/mochi.git
cd mochi-tune
pip install --upgrade pip setuptools wheel packaging
pip install -e . --no-build-isolation
pip install moviepy==1.0.3 pillow==9.5.0 av==13.1.0
sudo apt -y install bc

## Download the model weights#

- 

Download the model weights by running:

python3 ./scripts/download_weights.py weights/

## Prepare your dataset#

- Prepare your dataset by following the
README for Genmo's Mochi 1 LoRA Fine-tuner.

## Begin fine-tuning#

- 

Begin fine-tuning by running:

bash ./demos/fine_tuner/run.bash -c ./demos/fine_tuner/configs/lora.yaml -n 1

You should see output similar to:

Starting training with 1 GPU(s), mode: single_gpu
Using config: ./demos/fine_tuner/configs/lora.yaml
model=weights/dit.safetensors, optimizer=, start_step_num=0
Found 44 training videos in videos_prepared
Loaded 44/44 valid file pairs.
Loading model
Training type: LoRA
Attention mode: sdpa
Loading eval pipeline ...
Timing load_text_encoder
Timing load_vae
Stage Time(s) Percent
load_text_encoder 0.21 17.34%
load_vae 1.01 82.66%

[…]

Sampling: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 64/64 [03:33<00:00, 3.33s/it]
moving model from cpu -> cuda:0████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 64/64 [03:33<00:00, 1.09it/s]
moving model from cuda:0 -> cpu
Moviepy - Building video finetunes/my_mochi_lora/samples/0_200.mp4.
Moviepy - Writing video finetunes/my_mochi_lora/samples/0_200.mp4

Note

During the fine-tuning, you'll see messages similar to:

W1126 16:46:47.939000 265211801175072 torch/fx/experimental/symbolic_shapes.py:4449] [2/0_1] xindex is not in var_ranges, defaulting to unknown range.
W1126 16:46:51.271000 265211801175072 torch/fx/experimental/symbolic_shapes.py:4449] [2/1_1] xindex is not in var_ranges, defaulting to unknown range.
W1126 16:46:53.847000 265211801175072 torch/fx/experimental/symbolic_shapes.py:4449] [2/2_1] xindex is not in var_ranges, defaulting to unknown range.
W1126 16:46:56.411000 265211801175072 torch/fx/experimental/symbolic_shapes.py:4449] [2/3_1] xindex is not in var_ranges, defaulting to unknown range.

These messages can safely be disregarded.

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

- To learn how to benchmark your GH200 instance against other instances, see
 Running a PyTorch®-based benchmark on an NVIDIA GH200 instance.

- For more tips and tutorials, visit the Education landing page.

 Back to top
