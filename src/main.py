from src.OpenAI import interact


def conversation_cli(memory_size: int = 5, temperature: float = 0.5):
    """
    Starts an indefinitely long conversation with GPT-3 based on a prompt
    :param memory_size: How many of the previous messages the bot should remember
    :param temperature: The temperature (randomness) of the bot's responses
    :return: None
    """
    memory: list[str] = []
    while True:
        human_in: str = input("Human: ")
        response = interact("\n".join(memory), human_in, tempt=temperature)
        AI_out: str = ("AI: " + response.choices[0].text)
        print(AI_out)
        memory.append("Human: " + human_in + "\n" + AI_out)
        if len(memory) > memory_size:
            memory.pop(0)


if __name__ == '__main__':
    conversation_cli(
        memory_size=5,
        temperature=0.6
    )
