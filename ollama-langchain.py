# Import Ollama module from Langchain
from langchain_community.llms import Ollama

# Initialize an instance of the Ollama model
llm = Ollama(model="llama3")

# Invoke the model to generate responses
response = llm.invoke("Why the sky is blue?")
print(response)