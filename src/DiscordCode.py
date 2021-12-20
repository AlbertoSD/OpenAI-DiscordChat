import discord
from src.OpenAI import interact

client = discord.Client()
cat = []

@client.event
async def on_ready():
    print('Bot is ready.')


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.channel.id == <channel_id_here>:
        print(interact(user_input=message.content, memory=""))
        await message.channel.send(interact(user_input=message.content, memory="").choices[0].text)
        if interact(user_input=message.content, memory="").choices[0].text == "":
            await message.channel.send('<Empty>')

client.run(<bot_token_here>)
