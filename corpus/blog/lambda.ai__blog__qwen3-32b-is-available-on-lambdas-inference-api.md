# Qwen3 32B is available on Lambda's Inference API

Source: https://lambda.ai/blog/qwen3-32b-is-available-on-lambdas-inference-api

Skip to main content

# Qwen3 32B is available on Lambda's Inference API

 May 29, 2025

 • 7 min read

Alibaba released one of the most advanced models to date, Qwen3-32B, which can now be integrated into your applications with Lambda’s Inference API. With its dense model architecture, hybrid reasoning, multilingual support, and agentic capacilities, Qwen3-32B is designed for complex tasks that would otherwise require human intervention.

## What is the model architecture of Qwen3 32B? 

Qwen3-32B is a dense model, a term used to describe neural networks whose neurons are structured in layers that are interconnected with each neuron in the next layer. These models can easily learn about interactions between input features and non-linear functions because of the large volume of data that can be embedded in its parameters. As the name suggests, Qwen3-32B is an LLM with 32 billion total parameters.

Qwen3-32B competes with larger models like DeepSeek-R1, xAI’s Grok-3, OpenAI’s o1 and o3-mini on benchmarks for coding, math, and logic. You can use our guides to reproduce evaluations for the coding benchmark LiveCodeBench and GPQA, a graduate-level Google-proof Q&A benchmark.

Multi-disciplinary performance benchmarks for Qwen3. Image courtesy of Qwen.

## What are the capabilities of Qwen3 32B?

With its STEM and logical reasoning proficiency, Qwen3-32B has two problem-solving modes, commonly known as hybrid reasoning. Thinking mode, which is enabled by default, helps a model process the inquiry and reason sequentially before responding. In non-thinking mode, the model answers simple questions instantly. Developers can switch modes by changing the open-source code, and users can enter /think or /nothink commands to toggle between the two options. 

Not only is Qwen3-32B capable of hybrid reasoning, but it also excels in code generation and tasks that previously required human-performance – like creative writing, role-playing, instruction following, and multi-turn dialogue. Additionally, Qwen3-32B supports 119 of the most widely-spoken languages and nuanced dialects.

Qwen3 provides multi-lingual support for 119 languages and dialects. Image courtesy of Qwen.

Qwen3-32B can execute agentic actions, enabling developers to call their tools of choice and to modify Model Context Protocol (MCP) configuration files, which are standards that define how LLMs integrate with data sources or third-party applications. Here is an example of a Python script that lets you define functions and deploy agents with access to Qwen3-32B provided by Lambda’s Inference API.

from qwen_agent.agents import Assistant

# Define LLM
llm_cfg = {
    'model': 'Qwen3-32B',

    # Use Lambda's Inference API:
    'model_server': 'https://api.lambdalabs.com/api/v1/inference',  # Replace with the actual endpoint URL
    'api_key': 'YOUR_LAMBDA_API_KEY',  # Replace with your actual API key

    # Other parameters:
    # 'generate_cfg': {
    #         # Add: When the response content is `<think>this is the thought</think>this is the answer;
    #         # Do not add: When the response has been separated by reasoning_content and content.
    #         'thought_in_content': True,
    #     },
}

# Define Tools
tools = [
    {'mcpServers': {  # You can specify the MCP configuration file
            'time': {
                'command': 'uvx',
                'args': ['mcp-server-time', '--local-timezone=Asia/Shanghai']
            },
            "fetch": {
                "command": "uvx",
                "args": ["mcp-server-fetch"]
            }
        }
    },
  'code_interpreter',  # Built-in tools
]

# Define Agent
bot = Assistant(llm=llm_cfg, function_list=tools)

# Streaming generation
messages = [{'role': 'user', 'content': 'https://qwenlm.github.io/blog/ Introduce the latest developments of Qwen'}]
for responses in bot.run(messages=messages):
    pass
print(responses)

## How was Qwen3 32B trained?

Qwen3-32B was pre-trained with 36 trillion tokens from online sources and PDF documents. The legacy multi-modal Qwen2.5-VL model extracted and improved the text quality of these files, while Qwen2.5-Math and Qwen2.5-Coder generated synthetic math and coding data from textbooks, code snippets, and question-answer pairs. 

Compared to the Qwen2.5 base models, the smaller Qwen3-32B model delivers similar performance, and therefore operates more efficiently due to the following pre-training processes: 

- Qwen3-32B was taught basic language skills and general knowledge with 30 trillion tokens at a context length of four thousand tokens. 

- Training datasets were improved with an additional five trillion tokens for STEM, coding, and reasoning tasks. 

- Context lengths were extended to 32 thousand tokens with high-quality, long-context datasets. 

Models with hybrid-thinking functions were developed using a four-stage post-training pipeline. 

- In the first stage, models were fine-tuned with long Chain-of-Thought (CoT) data, describing its thought-process before undergoing various tasks and disciplines. 

- The second stage required scaling computational resources for reinforcement learning to enhance the models’ ability to explore knowledge and exploit rules-based rewards. 

- During stage three, the Qwen team integrated non-thinking capabilities by fine-tuning models with instruction-tuning and additional long CoT data generated by the thinking model to develop quick, but well-thought responses. 

- Lastly, reinforcement learning was applied to 20 generic tasks to rectify unwanted model behavior and improve instruction and format following as well as agentic actions. 

Post-training process for hybrid thinking models. Image courtesy of Qwen.

## How to start testing and using Qwen3 32B

API calls for Qwen3-32B are priced at $0.10 per million input tokens and $0.30 per million output tokens. It’s available with an FP8 weight precision level, and context windows can reach up to 41,000 tokens in length. This makes Qwen3-32B and Lambda’s Inference API as cost-efficient as possible, with no rate limits. Qwen3-32B can now be integrated into applications with an API key. Review our technical documentation for more details.

## AUTHORED BY

 Anthony Walsh

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
