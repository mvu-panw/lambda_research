# How To Fine Tune Stable Diffusion: Naruto Character Edition

Source: https://lambda.ai/blog/how-to-fine-tune-stable-diffusion-naruto-character-edition

Skip to main content

# How To Fine Tune Stable Diffusion: Naruto Character Edition

 November 2, 2022

 (Updated on July 24, 2023)

 • 4 min read

Fine tuning is the common practice of taking a model which has been trained on a wide and diverse dataset, and then training it a bit more on the dataset you are specifically interested in. This is common practice on deep learning and has been shown to be tremendously effective all manner of models from standard image classification networks to GANs. In this example we'll show how to fine tune Stable Diffusion on a Naruto anime character dataset to create a text to image model which makes custom Naruto inspired images based on any text prompt.

If you want more details on how to train your own Stable Diffusion variants, see Justin Pinkney's example on how we made the text-to-pokemon model at Lambda. 

If you're just after the model, code, or dataset, see:

- Lambda Diffusers

- Captioned Naruto dataset

- Model weights in Diffusers format

- Original model weights

- Naruto diffusers repo

If you just want to generate your own Naruto-like images, try the live text-to-naruto demo here!

## Example Stable Diffusion Outputs

Here are some examples of the sort of outputs the trained model can produce, and the prompt used:

"Bill Gates with a hoodie", "John Oliver with Naruto style", "Hello Kitty with Naruto style", "Lebron James with a hat", "Michael Jackson as a ninja", "Banksy Street art of ninja"

Put in a text prompt and generate your own Naruto style image!

#### Game of Thrones to Naruto

#### Marvel to Naruto

## Prompt Engineering Matters

We find that prompt engineering does help produce compelling and consistent Naruto style portraits. For example, writing prompts such as 'person_name ninja portrait' or 'person_name in the style of Naruto' tends to produce results that are closer to the style of Naruto character with the characteristic headband and other elements of costume.

Here are a few examples of prompts with and without prompt engineering that will illustrate that point.

#### Bill Gates

Without prompt engineering

With prompt engineering

#### A Cute Bunny

Without prompt engineering

With prompt engineering

## Usage

To run model locally:

!pip install diffusers==0.3.0
!pip install transformers scipy ftfy

import torch
from diffusers import StableDiffusionPipeline
from torch import autocast

pipe = StableDiffusionPipeline.from_pretrained("lambdalabs/sd-naruto-diffusers", torch_dtype=torch.float16) 
pipe = pipe.to("cuda")

prompt = "Yoda"
scale = 10
n_samples = 4

# Sometimes the nsfw checker is confused by the Naruto images, you can disable
# it at your own risk here
disable_safety = False

if disable_safety:
 def null_safety(images, **kwargs):
 return images, False
 pipe.safety_checker = null_safety

with autocast("cuda"):
 images = pipe(n_samples*[prompt], guidance_scale=scale).images

for idx, im in enumerate(images):
 im.save(f"{idx:06}.png")

##  

## Model Description

Trained on BLIP captioned Naruto images using 2xA6000 GPUs on Lambda GPU Cloud for around 30,000 step (about 12 hours, at a cost of about $20).

Trained by Eole Cervenka (@eoluscvka) after the work of Justin Pinkney (@Buntworthy)

## AUTHORED BY

 Eole Cervenka

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
