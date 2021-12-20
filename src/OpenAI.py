import os.path
import openai
from src import keys


def prompt_read() -> str:
    """
    Reads the prompt from the prompt text file in the src module. More about the prompt in the README
    :return: The contents of prompt.txt
    """
    file = "src/prompt.txt"
    if os.path.exists(file):
        with open(file, 'r') as f:
            return f.read()
    print(f"{file} not found. Returning empty string.")
    return ""


def interact(memory: str,user_input: str, tempt: float = 0.6, engine: str = "babbage"):
    """
    Interacts with the bot
    :param memory: Previous messages with the bot. Should be in this format: "\nHuman: Hello\nAI: Hello\n"
    :param user_input: The input that the user wants to give to the bot
    :param tempt: The temperature (randomness) of the responses. Default value is 0.6
    :param engine: The engine for GPT-3 to use. Default value is "davinci"
    :return: The OpenAI object response from OpenAI
    """
    openai.api_key = keys.OpenAI  # If not found, python will raise an error
    return openai.Completion.create(
        engine=engine,
        prompt=prompt_read() + "\n" + memory + "\nHuman:" + user_input + "\nAI:",
        temperature=tempt,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=["\n", " Human:", " AI:"]
    )
