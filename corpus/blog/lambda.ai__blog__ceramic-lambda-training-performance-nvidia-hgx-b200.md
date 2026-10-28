# Ceramic Training Infrastructure Delivers Superior Performance on Lambda's NVIDIA HGX B200

Source: https://lambda.ai/blog/ceramic-lambda-training-performance-nvidia-hgx-b200

Skip to main content

# Ceramic Training Infrastructure Delivers Superior Performance on Lambda's NVIDIA HGX B200

 July 15, 2025

 • 4 min read

Ceramic is rethinking AI training infrastructure from first principles, and in partnership with Lambda, we now have the data to show why that matters

At Ceramic, we are dedicated to reimagining AI infrastructure from the ground up. Our latest benchmark results demonstrate that Ceramic's training platform achieves exceptional Model FLOPS Utilization (MFU) performance on Lambda's NVIDIA HGX B200 clusters, with our long-context training capabilities delivering unprecedented efficiency compared to traditional training approaches.

### NVIDIA HGX B200 Benchmark Results

To validate our approach, we conducted comprehensive testing on Lambda’s NVIDIA HGX B200 GPU clusters, training Llama 3.1 8B models across multiple context lengths. The results demonstrate consistently high MFU performance that scales effectively with longer contexts.

#### Performance Metrics: 8B Model Training on 8 NVIDIA Blackwell GPUs

 | 

Context Size

 | 

MFU

 | 

MFU as a Percent of GEMM

 | 

FLOPs Per Token

 | 

2,048

 | 

53%

 | 

118.51%

 | 

47.7B

 | 

4,096

 | 

55%

 | 

92.44%

 | 

50.4B

 | 

8,192

 | 

61%

 | 

91.37%

 | 

55.7B

 | 

16,384

 | 

73%

 | 

101.46%

 | 

66.5B

 | 

32,768

 | 

85%

 | 

114.43%

 | 

88.0B

 | 

65,536

 | 

82%

 | 

111.20%

 | 

130.9B

#### Note on the GEMM MFU Calculation Approach

Our GEMM Adjusted MFU calculations are based on the actual matrix multiplication operations encountered during training runs at each specific context size, providing a more accurate representation of system efficiency. The calculation uses the formula: ( (Num_Layers*(2MFU of Attention Multiply+3MFU of MLP Param) + 2MFU of embedding) / (Num_layers5+2)) ). This uses actual numbers rather than an idealized benchmark.

### Competitive Advantage in Long-Context Training

 | 

Context Size

 | 

# of Blackwell GPUs

 | 

8K

 | 

16K

 | 

32K

 | 

64K

 | 

Foundry MFU

 | 

16

 | 

37%

 | 

N/A

 | 

31%

 | 

29%

 | 

Ceramic MFU

 | 

8

 | 

61%

 | 

73%

 | 

85%

 | 

82%

### Bridging the AI Training Efficiency Gap

These results demonstrate how Ceramic's architecture successfully addresses the complexity of training large language models at scale, where significant compute capacity is typically lost to system inefficiencies. Ceramic's architecture has been specifically designed to maximize utilization across varying context lengths and model sizes.

Our innovations focus on three key areas:

- Mathematical optimization: Reimagined computation boundaries for improved scalability

- Network efficiency: Optimized communication patterns for distributed training

- Long-context specialization: Maintaining or improving efficiency as context windows increase

The benchmark results validate that these innovations translate into measurable performance advantages for AI model training.

Ceramic is setting a new standard for LLM training infrastructure and with Lambda's Blackwell-powered clusters, that performance is now just a click away. 

Launch your own NVIDIA HGX B200 cluster instantly.

About Ceramic

Ceramic is redefining the foundations of ai infrastructure. Founded by Anna Patterson, whose 20+ years journey in ai span groundbreaking research at Google and Stanford, leading critical ai initiatives in big tech, and driving transformative advancement in the field, Ceramic is revolutionizing large-scale model training with faster, more efficient systems and cutting-edge capabilities, including very long-context training. 

About Lambda

Lambda was founded in 2012 by AI engineers with published research at the top machine learning conferences in the world. Our goal is to become the #1 Superintelligence compute platform serving enterprises across the entire AI development lifecycle. We enable large-scale Enterprises to easily, securely and affordably build, test and deploy AI products at scale. Our product portfolio spans from on-prem GPU hardware to hosted GPUs in the cloud. Lambda’s mission is to create a world where access to computation is as effortless and ubiquitous as electricity.

## AUTHORED BY

 Ceramic AI

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
