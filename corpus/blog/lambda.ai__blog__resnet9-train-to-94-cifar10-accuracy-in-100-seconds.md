# ResNet9: train to 94% CIFAR10 accuracy in 100 seconds with a single Turing GPU

Source: https://lambda.ai/blog/resnet9-train-to-94-cifar10-accuracy-in-100-seconds

Skip to main content

# ResNet9: train to 94% CIFAR10 accuracy in 100 seconds with a single Turing GPU

 January 7, 2019

 (Updated on August 12, 2022)

 • 4 min read

DAWNBench recently updated its leaderboard. Among the impressive entries from top-class research institutes and AI Startups, perhaps the biggest leap was brought by David Page from Myrtle. His ResNet9 achieved 94% accuracy on CIFAR10 in barely 79 seconds, less than half of the time needed by last year's winning entry from FastAI. 

More impressively, this performance was achieved with a single V100 GPU, as opposed to the 8xV100 setup FastAI used to win their competition. This means there is, in fact, an over 16-fold improvement in the FLOPs efficiency. This matters as it directly transfers to the dollar cost.

This blog tests how fast does ResNet9 run on Nvidia's latest Turing GPUs, including 2080 Ti and Titan RTX. We also include 1080 Ti as the baseline for comparison.

Without further ado, here are the results:

 | GPU 
 | 1080 Ti 
 | 2080 Ti 
 | Titan RTX 
 | V100 

 | Seconds to achieve 94% accuracy 
 | 201 
 | 131 
 | 101 
 | 75 

 | Training Epochs 
 | 24 
 | 24 
 | 24 
 | 24 

 | Number of GPU 
 | 1 
 | 1 
 | 1 
 | 1 

 | Precision 
 | FP16 
 | FP16 
 | FP 16 
 | FP 16 

You can jump to the code and the instructions from here. 

## Breakdown

Using 1080 Ti as the baseline reference, we see the speed-ups are 1.53, 1.99 and 2.68 from 2080 Ti, Titan RTX, and V100, respectively. Notice Half-Precision is used in all these tests. In fact, we have seen similar speed-ups with training FP16 models in our earlier benchmarks.

The author of ResNet9 has written a series of blogs to explain, step-by-step, how the network achieved such a significant speedup. Starting with the 356 seconds baseline, this is the breakdown of the improvement, sorted by the order of development:

 | Step 
 | Modification 
 | Reduction in Seconds 
 | Percentage in Percentage 

 | One 
 | Remove an unnecessary batchnorm layer + Fixed a kink in the learning rate schedule 
 | 33 
 | 12% 

 | Two 
 | Remove repetitive preprocessing jobs + Optimize random number generation 
 | 26 
 | 9% 

 | Three 
 | Use optimal batch size for CIFAR10 
 | 42 
 | 15% 

 | Four 
 | Use single-precision for batch norm (Related to a PyTorch Bug) 
 | 70 
 | 25% 

 | Five 
 | Use Cutout regularization to reduce the number of necessary training epochs 
 | 32 
 | 11.5% 

 | Six 
 | A slimmer residual network architecture 
 | 75 
 | 27% 

The breakdown shows that the most improvement comes from step six: the optimization of residual layers. Notice this is the last thing tried by the author in development, meaning its relative impact is actually a lot bigger than the above number suggested. 

## Future Work

Despite the impressive performance on CIFAR10, it is not clear how to generalize ResNet9's performance for other tasks, such as training ImageNet models or other models for different machine learning problems.

It is also non-trivial to generalize the FLOPS efficiency to a Multi-GPU setting. We have done some preliminary dual-GPU benchmarks with ResNet9. Results showed that at least on CIFAR10, no speedup can be achieved in comparison to the single-GPU setting. This is largely due to the overhead of communication between the GPUs has become the bottleneck of training such as small, frequently updating models.

Last but not least, despite a 16-fold improvement over last year's winning entry, there is still a lot of space for further improvement. According to David Page, the author of ResNet9:

"Assuming that we could realize 100% compute efficiency, training should complete in... 40 seconds (on a single V100)."

This means there can potentially be another 2X in training speed.

## Demo

You can reproduce the results with this repo. 

git clone https://github.com/lambdal/cifar10-fast.git

Then simply run the command:

python3 train_cifar10.py --batch_size=512 --num_runs=1 --device_ids=0

You'll need a GPU-ready machine and you'll also want to install Lambda Stack which installs GPU-enabled PyTorch in one line.

https://lambdalabs.com/lambda-stack-deep-learning-software

## AUTHORED BY

 Chuan Li

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
