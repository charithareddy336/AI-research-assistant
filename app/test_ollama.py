from langchain_ollama import OllamaLLM

# Connect to your local Ollama model
llm = OllamaLLM(model="mistral")

# Ask it a question
question = "What is RAG in AI in simple terms?"
print("Asking Mistral:", question)
print("---")

# Get the response
response = llm.invoke(question)
print(response)