import os.path
import openai
from src import keys


#     prompt=f"Test123\nHuman:{input}\nAI:",

def prompt_read() -> str:
    file = "src/prompt.txt"
    if os.path.exists(file):

        with open(file, 'r') as f:
            return f.read()

    else:
        print("File not found")
        return ""


def interact(memory: str,user_input: str, tempt: float = 0.8):

    # print("DEBUG INFO: ", memory, user_input)

    openai.api_key = keys.OpenAI

    return openai.Completion.create(
        engine="davinci",
        prompt=prompt_read() + "\n" + memory + "\nHuman:" + user_input + "\nAI:",
        temperature=tempt,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=["\n", " Human:", " AI:"]
    )
