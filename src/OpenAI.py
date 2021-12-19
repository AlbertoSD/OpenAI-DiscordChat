import openai
from src import keys

# Load your API key from an environment variable or secret management service
openai.api_key = keys.OpenAI


input = input("Enter what you want to the chatbot: ")

response = openai.Completion.create(
  engine="davinci",
  prompt=f"Test123\nHuman:{input}\nAI:",
  temperature=0.1,
  max_tokens=150,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.6,
  stop=["\n", " Human:", " AI:"]
)

print(response)