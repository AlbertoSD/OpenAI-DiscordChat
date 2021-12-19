from src.OpenAI import interact

memory = []

while True:
    human_in = input("Human: ")
    response = interact("\n".join(memory), human_in)
    AI_out = ("AI: " + response.choices[0].text)
    print(AI_out)
    memory.append("Human: " + human_in + "\n" + AI_out)

    if len(memory) > 20:
        memory.pop(0)