#Note: The openai-python library support for Azure OpenAI is in preview.
import os
import openai
openai.api_type = "azure"
openai.api_base = "https://polarbear-ai.openai.azure.com/"
openai.api_version = "2022-12-01"
openai.api_key = "0c805fd417a949b89566e28c9684f766"

response = openai.Completion.create(
    engine="bearCave",
    prompt="<|im_start|>system\nThe system is an AI assistant that helps people find information.\n<|im_end|>\n<|im_start|>user\nDoes Azure OpenAI support customer managed keys?\n<|im_end|>\n<|im_start|>assistant",
    temperature=1,
    max_tokens=800,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=["<|im_end|>"])

print(response['choices'][0]['text'])