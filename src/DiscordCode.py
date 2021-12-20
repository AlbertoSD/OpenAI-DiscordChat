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

    if message.channel.id == 817473346743959565:
        print(interact(user_input=message.content, memory=""))
        await message.channel.send(interact(user_input=message.content, memory="").choices[0].text)
        if interact(user_input=message.content, memory="").choices[0].text == "":
            await message.channel.send('<Empty>')

client.run('OTIyMjU5NDc1MzQyMTY0MDA5.Yb-3EQ.0VSetwXeDOIeTvK7OpGISdLGbpA')
