# Giving robots 3D vision without depth sensors

Source: https://lambda.ai/blog/giving-robots-3d-vision-without-depth-sensors

Skip to main content

# Giving robots 3D vision without depth sensors

 September 9, 2026

 • 2 min read

## Giving robots better 3D perception

Robots are becoming increasingly capable of learning manipulation skills directly from images. Most robot policies still rely on monocular cameras, though, which struggle to estimate depth accurately. That makes precise tasks such as grasping objects in cluttered environments, inserting parts, or manipulating complex geometry hard to pull off.

Explicit 3D representations such as depth maps and point clouds can help, but they fail in specific, visible ways: depth estimation misses thin geometry like a cup handle or a rack; point clouds deform or lose transparent surfaces like glass entirely. The challenge: give robots 3D understanding without a fragile geometric reconstruction pipeline.

StereoPolicy addresses this challenge by enabling robot policies to learn 3D spatial understanding directly from stereo images. It is a collaboration between Fei-Fei Li’s lab at Stanford University, Northwestern University, and Lambda.

## Who needs it

StereoPolicy is built for robotics researchers and engineers developing manipulation systems, including teams working on warehouse automation, manufacturing, household robots, and embodied AI foundation models that need reliable real-world perception.

## How StereoPolicy works

StereoPolicy replaces single-camera observations with synchronized stereo image pairs. Instead of explicitly estimating depth, it processes the left and right images with pretrained 2D vision encoders, then fuses their features through a cross-attention Stereo Transformer that learns spatial correspondence and disparity between the two views, capturing 3D structure implicitly, without ever building a depth map or point cloud.

The stereo module drops into two existing setups without changing their backbones: StereoPolicy-DP, trained from scratch alongside a diffusion policy per task, and StereoPolicy-VLA, which fine-tunes on top of a pretrained vision-language-action model such as Physical Intelligence's π0.5 or NVIDIA Isaac GR00T N1.5.

## The results

On five real-world tabletop tasks, StereoPolicy-DP averages a 59% success rate, against 42% for RGB-only, 41% for RGB-D, and just 14% for point-cloud-based PointNet. The gap is starkest on the hardest task: hanging a glass cup. RGB-D and point-cloud baselines land at 0–1 successes out of 20 trials; StereoPolicy reaches 3. Still hard, but the only approach that doesn't fail outright on a transparent object.

The pattern holds in simulation across OmniGibson and RoboMimic, and on VLA fine-tuning: StereoPolicy-VLA's advantage over RGB is largest in the low-data regime, on RoboCasa-Kitchen's 24 tasks with as few as 30 demonstrations, which is the setting where most real teams actually operate.

StereoPolicy reflects the broader shift toward physical AI, where increasingly capable robots rely on foundation models that integrate perception, reasoning, and control. As these systems scale to larger models and more complex manipulation tasks, training and deployment demand substantially more GPU compute. At Lambda, we're building the GPU cloud infrastructure that lets researchers and robotics teams train, fine-tune, and deploy physical AI systems at scale.

Demos: https://stereopolicy.github.io/

Scientific article: https://arxiv.org/pdf/2605.09989

Credits: Stanford University, Northwestern University, Lambda.

Authors: Evans Han, Yunfan Jiang, Yingke Wang, Haoyue Xiao, Huang Huang, Jianwen Xie, Jiajun Wu, Fei Fei Li, Ruohan Zhang.

## AUTHORED BY

 Jianwen Xie

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
