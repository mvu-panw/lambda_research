# Deploying a Llama 3 inference endpoint - Lambda Docs

Source: https://docs.lambda.ai/education/large-language-models/deploying-a-llama-3-inference-endpoint/

Skip to content

# Deploying a Llama 3 inference endpoint#

Meta's Llama 3 large language models (LLMs) feature generative text models recognized for their state-of-the-art performance in common industry benchmarks.

This guide covers the deployment of a Meta Llama 3 inference endpoint using Lambda On-Demand Cloud. This tutorial uses the Llama 3 models hosted by Hugging Face.

The model is available in 8B and 70B sizes:

 | Model Size
 | Characteristics

 | 8B (8 billion parameters)
 | More efficient and accessible, suitable for tasks where resources are constrained. The 8B model requires a 1x A100 or H100 GPU node.

 | 70B (70 billion parameters)
 | Superior performance and capabilities ideal for complex or high-stakes applications. The 70B model requires an 8x A100 or H100 GPU node.

### Prerequisites#

This tutorial assumes the following prerequisites:

- Lambda On-Demand Cloud instances appropriate for the Llama 3 model size you want to run.

- Model 8B (meta-llama/Meta-Llama-3-8B) requires 1x A100 or H100 GPU node.

- Model 70B (meta-llama/Meta-Llama-3-70B) requires 8x A100 or H100 GPU nodes.

- A Hugging Face user account.

- An approved Hugging Face user access token that includes repository read permissions for the meta-llama-3 model repository you wish to use.

JSON outputs in this tutorial are formatted using jq.

### Set up the inference point#

Once you have the appropriate Lambda On-Demand Cloud instances and Hugging Face permissions, begin by setting up an inference point. 

- Launch your Lambda On-Demand Cloud instance.

- Add or generate an SSH key to access the instance.

- SSH into your instance.

- 

Create a dedicated python environment.

Llama3 8bLlama3 70b

python3 -m venv Meta-Llama-3-8B
source Meta-Llama-3-8B/bin/activate
python3 -m pip install vllm==0.4.3 huggingface-hub==0.23.2 torch==2.3.0 numpy==1.26.4

python3 -m venv Meta-Llama-3-70B
source Meta-Llama-3-70B/bin/activate
python3 -m pip install vllm==0.4.3 huggingface-hub==0.23.2 torch==2.3.0 numpy==1.26.4

- 

Log in to Hugging Face:

huggingface-cli login

- 

Start the model server (download/cache as necessary). 

Llama3 8BLlama3 70B

python3 -m vllm.entrypoints.openai.api_server \
 --host=0.0.0.0 \
 --port=8000 \
 --model=meta-llama/Meta-Llama-3-8B &> api_server.log &

 python3 -m vllm.entrypoints.openai.api_server \
 --host=0.0.0.0 \
 --port=8000 \
 --model=meta-llama/Meta-Llama-3-70B \
 --tensor-parallel-size 8 &> api_server.log &

// The API server may take several minutes to start.

### Interact with the Model#

The following request delivers language prompts to the Llama 3 model:

Llama3 8BLlama3 70B

curl -X POST http://localhost:8000/v1/completions \
 -H "Content-Type: application/json" \
 -d '{
 "prompt": "What is the name of the capital of France?",
 "model": "meta-llama/Meta-Llama-3-8B",
 "temperature": 0.0,
 "max_tokens": 1 // sets the response length
 }'

curl -X POST http://localhost:8000/v1/completions \
 -H "Content-Type: application/json" \
 -d '{
 "prompt": "What is the name of the capital of France?",
 "model": "meta-llama/Meta-Llama-3-70B",
 "temperature": 0.0,
 "max_tokens": 1 // sets the response length
 }'

Llama 3 responds to requests in the following format:

Llama3 8BLlama3 70B

{
 "id": "cmpl-d898e2089b7b4855b48e00684b921c95",
 "object": "text_completion",
 "created": 1718221710,
 "model": "meta-llama/Meta-Llama-3-8B",
 "choices": [
 {
 "index": 0,
 "text": " Paris",
 "logprobs": null,
 "finish_reason": "length",
 "stop_reason": null
 }
 ],
 "usage": {
 "prompt_tokens": 11,
 "total_tokens": 12,
 "completion_tokens": 1
 }
}

{
 "id": "cmpl-d898e2089b7b4855b48e00684b921c95",
 "object": "text_completion",
 "created": 1718221710,
 "model": "meta-llama/Meta-Llama-3-70B",
 "choices": [
 {
 "index": 0,
 "text": " Paris",
 "logprobs": null,
 "finish_reason": "length",
 "stop_reason": null
 }
 ],
 "usage": {
 "prompt_tokens": 11,
 "total_tokens": 12,
 "completion_tokens": 1
 }
}

 Back to top
