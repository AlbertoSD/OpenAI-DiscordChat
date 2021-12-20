import discord
from src.OpenAI import interact
from discord.ext import commands
import keys

bot = commands.Bot(command_prefix='!inigay')
client = discord.Client()
cat = []


@client.event
async def on_ready():
    print('Bot is ready.')


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.channel.id == keys.channelID:

        if message.content == "you forgor 💀":
            cat.clear()
            await message.channel.send("I forgor 💀")
            return

        richard = interact(user_input=message.content, memory="\n".join(cat), tempt= 0.5).choices[0].text
        cat.append(f"Human: {message.content} \n AI: {richard}")
        await message.channel.send(richard)
        if len(cat) > 5:
            cat.pop(0)


client.run(keys.bot)
