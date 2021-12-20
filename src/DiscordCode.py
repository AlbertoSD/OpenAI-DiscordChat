import discord
from src.OpenAI import interact

client = discord.Client()


@client.event
async def on_ready():
    print('Bot is ready.')


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.channel.id == 817473346743959565:
        await print(interact(memory="", user_input=""))
        #message.channel.send(interact[0].text)


client.run('OTIyMjU5NDc1MzQyMTY0MDA5.Yb-3EQ.0VSetwXeDOIeTvK7OpGISdLGbpA')
