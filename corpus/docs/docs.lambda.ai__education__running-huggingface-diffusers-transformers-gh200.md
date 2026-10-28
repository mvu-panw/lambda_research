# Running Hugging Face Transformers and Diffusers on an NVIDIA GH200 instance - Lambda Docs

Source: https://docs.lambda.ai/education/running-huggingface-diffusers-transformers-gh200/

Skip to content

# Running Hugging Face Transformers and Diffusers on an NVIDIA GH200 instance#

Hugging Face provides
several powerful Python libraries that provide easy access to a wide range of
pre-trained models. Among the most popular are
Diffusers,
which focuses on diffusion-based generative AI, and
Transformers,
which supports common AI/ML tasks across several different modalities. This
tutorial demonstrates how to use these libraries to generate images and
chatbot-style responses on an On-Demand Cloud (ODC) instance backed with the
NVIDIA GH200 Grace Hopper Superchip.

## Setting up your environment#

### Launch your GH200 instance#

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

### Set up your Python virtual environment#

Next, create a new Python virtual environment and install the required
libraries:

- In the Lambda Cloud console, navigate to the
 Instances page,
 find the row for your instance, and then click Launch in the
 Cloud IDE column. JupyterLab opens in a new window.

- In JupyterLab's Launcher tab, under Other, click Terminal to
 open a new terminal.

- 

In your terminal, create a Python virtual environment:

python -m venv --system-site-packages hf-tests

- 

Activate the virtual environment:

source hf-tests/bin/activate

- 

Install the Hugging Face Transformers library, Diffusers library, and
 other dependencies:

pip install transformers diffusers["torch"] tf-keras==2.17.0 accelerate

## Using Hugging Face Transformers and Diffusers#

Now that you've set up your environment, you can create and run Python
programs based on Hugging Face Transformers and Diffusers. This section provides
a few example programs to get you started.

### Generate a chatbot response with the Transformers library#

To generate a chatbot-style response with the Hugging Face Transformers library:

- 

Open a new Python file named test_transformers.py for editing:

nano test_transformers.py

- 

Paste the following Hugging Face Transformers test script into the file:

import transformers
import torch

model_id = "facebook/opt-1.3b"

pipeline = transformers.pipeline(
 "text-generation", model=model_id, model_kwargs={"torch_dtype": torch.bfloat16}, device_map="auto"
)

output = pipeline("How is ice cream made?")
print(output)

- 

Save and exit.

- 

Run the script:

python test_transformers.py

You should get a result similar to the following:

[{'generated_text': 'How is ice cream made?\n\nIce cream is made by mixing milk, sugar, and'}]

To learn more about how to use the Transformers library, see the
Transformers section
in the Hugging Face docs.

### Generate an image with the Diffusers library#

To generate a prompt-based image with the Hugging Face Diffusers library:

- 

Open a new Python file named test_diffusers.py for editing:

nano test_diffusers.py

- 

Paste the following Hugging Face Diffusers test script into the file.
 Feel free to change the prompt if desired:

from diffusers import DiffusionPipeline
import torch

pipeline = DiffusionPipeline.from_pretrained("stable-diffusion-v1-5/stable-diffusion-v1-5", torch_dtype=torch.float16)
pipeline.to("cuda")
image = pipeline("An image of an elephant in the style of Matisse").images[0]
image.save("elephant_matisse.png")

- 

Save and exit.

- 

Run the script:

python test_diffusers.py

The resulting image file appears in JupyterLab's left nav. Double-click
it to view the image:

To learn more about how to use the Diffusers library, see the
Diffusers section
in the Hugging Face docs.

## Cleaning up#

When you're done with your instance, terminate it to avoid incurring unnecessary
costs:

- In the Lambda Cloud console, navigate to the
 Instances page.

- Select the checkboxes of the instances you want to delete.

- Click Terminate. A dialog appears.

- Follow the instructions and then click Terminate instances to
 terminate your instances.

## Next steps#

- To learn how to benchmark your GH200 instance against other instances, see
 Running a PyTorch®-based benchmark on an NVIDIA GH200 instance.

- To explore more Hugging Face libraries, see
 Libraries
 in the Hugging Face docs.

- For more tips and tutorials, visit the Education landing page.

 Back to top
