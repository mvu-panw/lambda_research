# Lambda Demos: Simplifying ML Demo Hosting

Source: https://lambda.ai/blog/lambda-demos-simplifying-ml-demo-hosting

Skip to main content

# Lambda Demos: Simplifying ML Demo Hosting

 May 24, 2023

 • 2 min read

Lambda Demos streamlines the process of hosting your own machine learning demos. With a user-friendly interface, you can effortlessly host a demo built with Gradio using your existing repository URL in just a few clicks.

We wanted to provide machine learning practitioners with a unified platform for training and sharing their work. With Lambda Cloud, you can access the latest generation of NVIDIA GPUs, including powerful H100 instances for training and smaller instance types like the 1x A10 for hosting demos.

While our machine learning team at Lambda trains models using Lambda GPU Cloud, they often rely on other services to share their demos with the world. We developed Lambda Demos initially with our own machine learning team in mind, but it has proven valuable to others who want to streamline their work.

I don’t build or train models myself but I do use demos hosted by others. Unfortunately, during peak demand, I often experience waiting queues. Having the ability to clone the repository and independently host the demo is a convenient option. With Lambda Demos, end-users like myself can do this with just a few clicks on Lambda Cloud.

Since Gradio is one of the more popular frameworks for building demos, we focused on enabling the hosting of Gradio apps in the first iteration of this feature, with some specific requirements:

- The app must be built using Gradio.

- The code must be in a git repository.

- The repository must contain a file called README.md with specific properties. If this file and these properties don’t exist, you will receive a Demo Misconfigured error.

- The README.md must have a YAML block at the top, containing the following:

---

sdk: gradio

sdk_version: GRADIO-VERSION

app_file: PATH-TO-APP-FILE

---

where GRADIO-VERSION is the version of Gradio your demo is built with, for example, 3.24.1 and PATH-TO-APP-FILE is the path to your Gradio application file (the file containing the Gradio interface code), relative to the root of your repository. For example, if your Gradio application file is named app.py and is located in the root directory of your repository, replace PATH-TO-APP-FILE with app.py.

To learn more about how to use Lambda Demos, check out our documentation page or read our earlier blog post about how to host Stable Diffusion using Lambda Demos.

If you are cloning someone else’s repository, please make sure that you understand the licensing and you have permissions to use the models before hosting them with Lambda Demos. 

Discover the ease and efficiency of hosting your models with Lambda Demos and streamline the way you share your work with the world!

Happy hosting!

Kathy

## AUTHORED BY

 Kathy Bui

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
