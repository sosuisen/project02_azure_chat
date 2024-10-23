import os
from openai import AzureOpenAI

# Initialize Azure OpenAI client with key-based authentication
client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_ENDPOINT_URL_CHAT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY_CHAT"),
    api_version="2024-05-01-preview",
)

completion = client.chat.completions.create(
    model="gpt-35-turbo",
    messages=[
        {
            "role": "system",
            "content": "You are an AI assistant that helps people find information.",
        },
        {
            "role": "user",
            "content": "Can you help me find some information about Python?",
        },
    ],
    temperature=0.7,
)

print(completion.to_json())
