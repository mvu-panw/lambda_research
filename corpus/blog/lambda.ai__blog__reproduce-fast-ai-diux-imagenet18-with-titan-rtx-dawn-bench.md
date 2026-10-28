# Reproduce Fast.ai/DIUx imagenet18 with a Titan RTX server

Source: https://lambda.ai/blog/reproduce-fast-ai-diux-imagenet18-with-titan-rtx-dawn-bench

Skip to main content

# Reproduce Fast.ai/DIUx imagenet18 with a Titan RTX server

 January 15, 2019

 (Updated on July 24, 2023)

 • 7 min read

Last, tyear, Fast.ai won the first ImageNet training cost challenge as part of the DAWN benchmark. Their customized ResNet50 takes 3.27 hours to reach 93% Top-5 accuracy with an AWS p3.16xlarge (8 x V100 GPUs). This year, Fast.ai teamed up with DIUx and cut down the training time to 18 minutes with a cluster of sixteen p3.16xlarge machines. This was the quickest solution at the time it was announced (Sep 2018). 

In this blog, we reproduce the latest Fast.ai/DIUx's ImageNet result with a single 8 Turing GPUs (Titan RTX) server. It takes 2.36 hours to achieve 93% Top-5 accuracy. 

Here are the details of the statistics:

 | Epoch 
 | Training Time (hour) 
 | Top-1 Acc 
 | Top-5 Acc 

 | 1 
 | 0.0539 
 | 7.2800 
 | 19.1979 

 | 2 
 | 0.0921 
 | 18.3619 
 | 39.6699 

 | 3 
 | 0.1306 
 | 26.1700 
 | 50.2779 

 | 4 
 | 0.1691 
 | 29.9260 
 | 54.5460 

 | 5 
 | 0.2078 
 | 32.3339 
 | 58.0260 

 | 6 
 | 0.2465 
 | 27.2560 
 | 50.7680 

 | 7 
 | 0.2852 
 | 30.0799 
 | 54.3160 

 | 8 
 | 0.3240 
 | 39.1959 
 | 65.4260 

 | 9 
 | 0.3627 
 | 42.8860 
 | 69.2040 

 | 10 
 | 0.4014 
 | 45.1940 
 | 70.9100 

 | 11 
 | 0.4402 
 | 49.3839 
 | 74.9639 

 | 12 
 | 0.4788 
 | 54.9459 
 | 79.5660 

 | 13 
 | 0.5174 
 | 58.5820 
 | 81.8980 

 | 14 
 | 0.6433 
 | 57.3959 
 | 81.5960 

 | 15 
 | 0.7569 
 | 53.0480 
 | 77.7799 

 | 16 
 | 0.8703 
 | 58.9599 
 | 82.7979 

 | 17 
 | 0.9845 
 | 60.4039 
 | 83.8259 

 | 18 
 | 1.0982 
 | 62.3779 
 | 84.8720 

 | 19 
 | 1.2124 
 | 64.9540 
 | 86.6080 

 | 20 
 | 1.3258 
 | 65.9520 
 | 87.2919 

 | 21 
 | 1.4390 
 | 68.3700 
 | 88.7060 

 | 22 
 | 1.5529 
 | 71.4420 
 | 90.4820 

 | 23 
 | 1.6673 
 | 72.0479 
 | 90.6679 

 | 24 
 | 1.7826 
 | 72.8679 
 | 91.1559 

 | 25 
 | 1.8957 
 | 73.5739 
 | 91.4960 

 | 26 
 | 2.1455 
 | 75.8519 
 | 92.9879 

 | 27 
 | 2.3657 
 | 75.9179 
 | 93.0179 

You can jump to the code and the instructions from here. 

## Notes 

Jeremy Howard wrote a brilliant blog about the technical details behind their approach. Our takeaways are:

Inference with dynamic-size images: A key idea from the latest Fast.ai/DIUx entry is to reduce the information loss in the preprocessing stage of the inference. Let's first take a look at a common practice in running inference for image classification: Due to the use of fully connected layers, images are first transformed to a fixed size before processed by the network. This usually involves either perspective distortion (via image resizing) or losing a significant part of the image content (via cropping). In the second case, people often use multiple random crops to increase the accuracy. 

It is clear that such preprocessing will have a big impact on the network's performance: the network needs to be robust enough to recognize "distorted" or "cropped" objects, which often requires more epochs in training.

The key observation made by the Fast.ai/DIUx team is to remove unnecessary preprocessing by getting rid of the fix-size restriction. This is achieved by replacing the fully connected layers by global pooling layers, which have no restriction on the size of the input. Now inference becomes an "easier" task because it deals with input images that have not been severely distorted nor cropped. In consequence, less training epochs are required to reach a certain testing accuracy. According to the authors doing so brought in 23% reduction of the training time for reaching the target accuracy.

Progressive training: Another interesting technique adopted by the Fast.ai/DIUx team is progressive training with images of multiple resolutions. The training started with a low resolution (128 x 128) for input images and a larger batch size to quickly achieve certain accuracy; it then increased the resolution (first to 244 x 244 and then 288 x 288) for the expensive fine-tuning. This allows overall fewer epochs to achieve the target test accuracy. Notice this is only possible due to the replacement of fully connected layers by the global pooling layers, so the network trained with low-resolution images can work with the higher resolution images without modification. In the meantime, the batch size and learning rate are carefully scheduled for each resolution to get the desired performance as quickly as possible.

## Conclusion

In this post, we reproduced the current state of the art ImageNet training performance on a single Turing GPU server. It is exciting to see only 2.4 hours are required to achieve 93% Top-5 accuracy. Next time we will reproduce the training in a multi-node distributed fashion within a local network.

## Demo

You can reproduce the results with this repo. 

First, clone the repo and setup a Python 3 virtual environment: 

git clone https://github.com/lambdal/imagenet18.git

cd imagenet18

virtualenv -p python3 env
source env/bin/activate

pip install -r requirements_local.txt

Then download the data to your local machine (be aware that the tar files are about 200 GB in total):

wget https://s3.amazonaws.com/yaroslavvb/imagenet-data-sorted.tar

wget https://s3.amazonaws.com/yaroslavvb/imagenet-sz.tar

tar -xvf imagenet-data-sorted.tar -C /mnt/data/data

tar -xvf imagenet-sz.tar -C /mnt/data/data

Finally run the following command to reproduce the results on a 8-GPU server. Set the "nproc_per_node" to match the number of GPUs on your machine.

python -m torch.distributed.launch --nproc_per_node=8 --nnodes=1 --node_rank=0 \
training/train_imagenet_nv.py /mnt/data/data/imagenet \
--fp16 --logdir ./ncluster/runs/lambda-blade --distributed --init-bn0 --no-bn-wd \
--phases "[{'ep': 0, 'sz': 128, 'bs': 512, 'trndir': '-sz/160'}, {'ep': (0, 7), 'lr': (1.0, 2.0)}, {'ep': (7, 13), 'lr': (2.0, 0.25)}, {'ep': 13, 'sz': 224, 'bs': 224, 'trndir': '-sz/320', 'min_scale': 0.087}, {'ep': (13, 22), 'lr': (0.4375, 0.043750000000000004)}, {'ep': (22, 25), 'lr': (0.043750000000000004, 0.004375)}, {'ep': 25, 'sz': 288, 'bs': 128, 'min_scale': 0.5, 'rect_val': True}, {'ep': (25, 28), 'lr': (0.0025, 0.00025)}]"

To print out the statics, locate the events.out file in the "logdir" folder and simply run this command:

python dawn/prepare_dawn_tsv.py \
--events_path=<logdir>/<events.out>

## AUTHORED BY

 Chuan Li

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
