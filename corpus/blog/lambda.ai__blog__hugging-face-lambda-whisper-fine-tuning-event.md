# Hugging Face x Lambda: Whisper Fine-Tuning Event

Source: https://lambda.ai/blog/hugging-face-lambda-whisper-fine-tuning-event

Skip to main content

# Hugging Face x Lambda: Whisper Fine-Tuning Event

 December 1, 2022

 • 12 min read

Lambda is thrilled to team up with Hugging Face, a community platform that enables users to build, train, and deploy ML models based on open source code, for a two-week community event to build state-of-the-art speech recognition systems in as many languages as possible. The goal is to fine-tune at least 70 languages, but we are hoping that we will get closer to 100 languages (or more!). To achieve this goal during the two-week sprint, Lambda, Hugging Face, and all the participants will work together as a community, fine-tuning Open AI's Whisper model. Hugging Face is providing the training scripts, notebooks, talks, and more, and Lambda is providing free access to A100 (40 GB SXM4) GPUs on Lambda Cloud.

For those joining the event or those who want a document summarizing ALL the relevant information required for the event, please make sure to:

- Sign-up using the Google form

- Join the Hugging Face Discord server and make sure you have access to the #events channel

- Read the GitHub README thoroughly - sections covered there that are not covered in the blog post include Set Up an Environment, Data and Pre-Processing, Evaluation, Building a Demo, Communication and Problems, Tips and Tricks, and Feedback

## Table of Contents

- Introduction

- Important Dates

- Launch a Lambda Cloud GPU

- Fine-Tune a Whisper Model

- Talks

## Introduction

Whisper is a pre-trained model for automatic speech recognition (ASR) published in September 2022 by the authors Radford et al. from OpenAI. Pre-trained on 680,000 hours of labelled data, it demonstrates a strong ability to generalize to different datasets and domains. Through fine-tuning, the performance of this model can be significantly boosted for a given language.

In this event, Hugging Face and Lambda are bringing the community together to fine-tune Whisper in as many languages as possible. Our aim is to achieve state-of-the-art on the languages spoken by the community. Together, we can democratize speech recognition for all.

Hugging Face is providing training scripts, notebooks, blog posts, talks and Lambda is providing the A100 compute, so you have all the resources you need to participate! You are free to chose your level of participation, from using the template script and setting it to your language, right the way through to exploring advanced training methods. We encourage you to participate to level that suits you best. We'll be on hand to facilitate this!

Participants are allowed to fine-tune their systems on the training data of their choice, including datasets from the Hugging Face Hub, web-scraped data from the internet, or private datasets. Whisper models will be evaluated on the "test" split of the Common Voice 11 dataset for the participant's chosen language.

We believe that framing the event as a competition is fun! But at the core, the event is about fine-tuning Whisper in as many languages as possible as a community. We want to foster an environment where we work together, help each other solve bugs, share important findings and ultimately learn something new.

This blog serves as an introduction to our Hugging Face x Lambda collaboration, and a sneak peek into the event details. For complete event instructions and all the information you need to get started, please visit Hugging Face's README. The README is structured such that you can read it sequentially, section-by-section. We recommend that you read the document once from start to finish before running any code. This will give you an idea of where to look for the relevant information and an idea of how the event is going to run.

Note: This blog post had major contributions from many members of the Hugging Face and Lambda teams.  From Hugging face we have Sanchit Gandhi (@sanchitgandhi99), Vaibhav Srivastav (@reach_vb), Omar Sanseviero (@osanseviero), Patrick von Platen (@PatrickPlaten), Julien Chaumond (@julien_c), Lysandre (@LysandreJik), and from Lambda we have Mitesh Agrawal (@mitesh711), and Jaimie Renner.

## Important Dates

- Introduction Talk: December 1st, 2022

- Sprint start: December 5th, 2022

- Speaker Events: December 5th, 2022

- Sprint end: December 19th, 2022

- Results: December 23rd, 2022

## Launch a Lambda Cloud GPU

Where possible, we encourage you to fine-tune Whisper on a local GPU machine. This will mean a faster set-up and more familiarity with your device. If you are running on a local GPU machine, you can find it in the Set Up an Environment of the GitHub README.

The training scripts can also be run as a notebook through Google Colab. We recommend you train on Google Colab if you have a "Colab Pro" or "Pro+" subscription. This is to ensure that you receive a sufficiently powerful GPU on your Colab for fine-tuning Whisper. If you wish to fine-tune Whisper through Google Colab, you can find it in the GitHub README.

If you do not have access to a local GPU or Colab Pro/Pro+, we'll provide you with a cloud GPU instance for this event. We're offering the latest NVIDIA A100 (40 GB SXM4) GPUs, so you'll be loaded with some serious firepower! Our Cloud API makes it easy to spin-up and launch a GPU instance. In this Section, we'll go through the steps for spinning up an instance one-by-one.

This Section is split into three parts:

- Signing-Up with Lambda

- Creating a Cloud Instance

- Deleting a Cloud Instance

### Signing Up with Lambda

- Create an account with Lambda using your email address of choice: https://cloud.lambdalabs.com/sign-up. If you already have an account, skip to the next section.

### Creating a Cloud Instance

Estimated time to complete: 5 mins

- Click the link: https://cloud.lambdalabs.com/instance

- You'll be asked to sign in to your Lambda Cloud account (if you haven't done so already).

- Once on the GPU instance page, click the purple button "Launch instance" in the top right.

- Verify a payment method if you haven't done so already. IMPORTANT: if you have followed the instructions in the previous section, you will have received $110 in GPU credits. Exceeding 100 hours of 1x A100 usage may incur charges on your credit card.

- Launching an instance:

- In "Instance type", select the instance type "1x A100 (40 GB SXM4)"

- In "Select region", select the region with availability closest to you.

- In "Select filesystem", select "Don't attach a filesystem".

- You will be asked to provide your public SSH key. This will allow you to SSH into the GPU device from your local machine.

- If you’ve not already created an SSH key pair, you can do so with the following command from your local device:

ssh-keygen

- You can find your public SSH key using the command:

cat ~/.ssh/id_rsa.pub

(Windows: type C:UsersUSERNAME.sshid_rsa.pub where USERNAME is the name of your user)

- Copy and paste the output of this command into the first text box

- Give your SSH key a memorable name (e.g. sanchits-mbp)

- Click "Add SSH Key"

- Select the SSH key from the drop-down menu and click "Launch instance"

- Read the terms of use and agree

- We can now see on the "GPU instances" page that our device is booting up!

- Once the device status changes to "✅ Running", click on the SSH login ("ssh ubuntu@..."). This will copy the SSH login to your clipboard.

- Now open a new command line window, paste the SSH login, and hit Enter.

- If asked "Are you sure you want to continue connecting?", type "yes" and press Enter.

- Great! You're now SSH'd into your A100 device! We're now ready to set up our Python environment!

You can see your total GPU usage from the Lambda Cloud interface: https://cloud.lambdalabs.com/usage

Here, you can see the total charges that you have incurred since the start of the event. We advise that you check your total on a daily basis to make sure that it remains below the credit allocation of $110. This ensures that you are not inadvertently charged for GPU hours.

### Deleting a Cloud Instance

100 1x A100 hours should provide you with enough time for 5-10 fine-tuning runs (depending on how long you train for and which size models). To maximize the GPU time you have for training, we advise that you shut down GPUs over prolonged periods of time when they are not in use. Leaving a GPU running accidentally over the weekend will incur 48 hours of wasted GPU hours. That's nearly half of your compute allocation! So be smart and shut down your GPU when you're not training.

Creating an instance and setting it up for the first time may take up to 20 minutes. Subsequently, this process will be much faster as you gain familiarity with the steps, so you shouldn't worry about having to delete a GPU and spinning one up the next time you need one. You can expect to spin-up and delete 2-3 GPUs over the course of the fine-tuning event!

We'll quickly run through the steps for deleting a Lambda Cloud GPU. You can come back to these steps after you've performed your first training run and you want to shut down the GPU:

- Go to the instances page: https://cloud.lambdalabs.com/instances

- Click the checkbox on the left next to the GPU device you want to delete

- Click the button "Terminate" in the top right-hand side of your screen (under the purple button "Launch instance")

- Type "erase data on instance" in the text box and press "ok"

## Fine-Tune Whisper

Please read the Fine-Tune Whisper GitHub README for a full walk through on how-to execute the fine-tuning code on Python Script, Jupyter Notebook, and Google Colab. A complete guide to Whisper fine-tuning can be found in the blog post: Fine-Tune Whisper with 🤗 Transformers. While it is not necessary to have read this blog post before fine-tuning Whisper, it is strongly advised to gain familiarity with the fine-tuning code. Read on below for a sneak peek into what's covered in the event README.

Throughout the event, participants are encouraged to leverage the official pre-trained Whisper checkpoints. The Whisper checkpoints come in five configurations of varying model sizes. The smallest four are trained on either English-only or multilingual data. The largest checkpoint is multilingual only. The checkpoints are summarized in the following table with links to the models on the Hugging Face Hub:

 | Size
 | Layers
 | Width
 | Heads
 | Parameters
 | English-only
 | Multilingual

 | tiny
 | 4
 | 384
 | 6
 | 39 M
 | ✓
 | ✓

 | base
 | 6
 | 512
 | 8
 | 74 M
 | ✓
 | ✓

 | small
 | 12
 | 768
 | 12
 | 244 M
 | ✓
 | ✓

 | medium
 | 24
 | 1024
 | 16
 | 769 M
 | ✓
 | ✓

 | large
 | 32
 | 1280
 | 20
 | 1550 M
 | x
 | ✓

The English-only checkpoints should be used for English speech recognition. For all other languages, one should use the multilingual checkpoints.

We recommend using the tiny model for rapid prototyping. We advise that the small or medium checkpoints are used for fine-tuning. These checkpoints achieve comparable performance to the large checkpoint, but can be trained much faster (and hence for much longer!).

There are three ways in which you can execute the fine-tuning code:

- Python Script

- Jupyter Notebook

- Google Colab

1 and 2 are applicable when running on a local GPU or cloud GPU instance (such as on our cloud GPUs). 3 applies if you have a Google Colab Pro/Pro+ subscription and want to run training in a Google Colab. The instructions for running each of these methods are quite lengthy. Feel free to read through each of them on the Fine-Tune Whisper GitHub README to get a better idea for which one you want to use for training. Once you've read through, we advise you pick one method and stick to it!

## Talks

We are quite excited to host talks from Open AI, Meta AI, and Hugging Face to help you get a better understanding of the Whisper architecture, datasets used for ASR and details about the event itself!

 | Speaker
 | Topic
 | Time
 | Video

 | Sanchit Gandhi, Hugging Face
 | Introduction to Whisper Fine Tuning Event
 | 7am PST / 10am EST, December 2nd, 2022
 | 

 | Jong Wook Kim, OpenAI
 | Whisper Model
 | 8:30am PST / 11:30am EST, December 5th, 2022
 | 

 | Changhan Wang, MetaAI
 | VoxPopuli Dataset
 | 9:30am PST / 12:30pm EST, December 5th, 2022
 | 

## AUTHORED BY

 Chuan Li

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
