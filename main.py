import discord
from discord.ext import commands

import jishaku



from pymongo import MongoClient
import os

mongoClient = MongoClient(os.environ['mongolink']).ChainBot.ChainBot

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix = ['chain ', ':chains: ', '⛓️ ', '⛓️'], activity=discord.Game('dont break the chain ty'), status=discord.Status.idle, intents=intents)

@bot.event
async def on_message(message):
    try:
        channel_id = mongoClient.find_one({'_id': message.guild.id})['channel']
    except:
        channel_id = None
    if message.author == bot.user:
        pass
    else:
        if message.channel.id == channel_id:
            messages = await message.channel.history(limit=4).flatten()
            messages.remove(message)
            for ms in messages:
                if ms.content == messages[0].content:
                    pass
                else:
                    if message.content == messages[0].content:
                        pass
                    else:
                        try:
                            await message.delete()
                        except:
                            pass
                        await message.channel.send('You are breaking the chain!', delete_after=2)
        else:
            await bot.process_commands(message)

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

bot.load_extension('jishaku')

keep_alive()

bot.run(os.environ['ChainBotToken'])


