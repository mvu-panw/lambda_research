# Running DeepSeek-R1 70B using Ollama - Lambda Docs

Source: https://docs.lambda.ai/education/large-language-models/deepseek-r1-ollama/

Skip to content

# Running DeepSeek-R1 70B using Ollama#

## Introduction#

This short tutorial teaches how to use a
Lambda Cloud on-demand instance
to run the
DeepSeek-R1 distilled Llama 3.3 70B model using Ollama
in a Docker container. Since
NVIDIA Container Toolkit
is preinstalled as part of
Lambda Stack
on all on-demand instances, Docker containers can use instance GPUs without any
additional configuration.

## Prerequisites#

For this tutorial, it's recommended that you use an instance type with more than
40 GB of VRAM, for example, a 1x GH200 or 1x H100.

## Download Ollama and start the Ollama server#

- 

Log into your instance using SSH or by opening a terminal in Jupyter Lab.

- 

Download Ollama and start the Ollama server:

sudo docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama

The download is complete once you see:

Status: Downloaded newer image for ollama/ollama:latest

- 

Confirm the Ollama server is running:

sudo docker ps

You should see output similar to:

CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES
3b27fdfbbfcc ollama/ollama "/bin/ollama serve" 2 hours ago Up 2 hours 0.0.0.0:11434->11434/tcp, :::11434->11434/tcp ollama

## Download and run the DeepSeek-R1 70B model#

Download and run the DeepSeek-R1 70B model:

sudo docker exec -it ollama ollama run deepseek-r1:70b

The model is over 40 GB in size and can take 10-15 minutes to download.

The model is running when you see:

success
>>> Send a message (/? for help)

## Test the DeepSeek-R1 70B model#

Test the DeepSeek-R1 70B model by submitting a prompt, for example:

What is the national anthem of France?

You should see output similar to:

<think>
Okay, so I need to figure out what the national anthem of France is. Hmm, I've heard a few national anthems before, but I'm not entirely sure about the French one. Let me think... I
remember that each country has its own song that represents them, often played during important events like sports games or official ceremonies.

I think the French national anthem might be called "La Marseillaise." That name rings a bell. It sounds familiar from movies or maybe history classes. But wait, am I confusing it with
something else? Maybe another country's anthem? No, I'm pretty sure "La Marseillaise" is French because Marseille is a city in France.

I should probably confirm what the lyrics are like. From what I recall, "La Marseillaise" has some strong, patriotic words. There's a part that goes something like "Allons enfants de
la Patrie," which translates to "Come, children of the Fatherland." That sounds right because it's a call to action, typical for national anthems trying to inspire people.

Also, I think it was written during the French Revolution, which makes sense because that period was crucial for France's identity. The song might have been adopted as the anthem after
the revolution gained momentum. Maybe it became official later on, but its origins are definitely tied to that time of significant change in France.

Wait, could there be another anthem? I don't think so. Most countries stick with one anthem unless they undergo major changes like a regime change or something. France has had "La
Marseillaise" for a long time now, so it's probably still their current national anthem.

I also remember that the melody is quite recognizable and grand, which fits the nature of a national anthem needing to be memorable and stirring. It's often played with orchestral
instruments, giving it that majestic feel that commands respect when it's performed.

To sum up my thoughts: the name "La Marseillaise" is linked to Marseille in France, the song has patriotic lyrics calling for unity and action, it originated during the French
Revolution, and its melody is well-known. All these points lead me to conclude confidently that the national anthem of France is indeed "La Marseillaise."
</think>

The national anthem of France is **"La Marseillaise."** It is a patriotic song with origins in the French Revolution, known for its stirring melody and lyrics that call for unity and
action. Adopted as the official anthem, it reflects the country's history and identity.

 Back to top
