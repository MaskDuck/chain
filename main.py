import discord
from discord.ext import commands

import jishaku

from pymongo import MongoClient
import os

mongoClient = MongoClient(os.environ['mongolink']).ChainBot.ChainBot

bot = commands.Bot(command_prefix = 'chain ', activity=discord.Game('dont break the chain ty'), status=discord.Status.idle)\

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
                        await message.channel.send('You are breaking the chain!', delete_after=5)
        else:
            await bot.process_commands(message)




@bot.command()
@commands.has_permissions(administrator=True)
async def set(ctx, chain_channel: discord.TextChannel):
    result = mongoClient.find_one({'_id': ctx.guild.id})
    if result is None:
        data = {'_id': ctx.guild.id, 'channel': chain_channel.id}
        mongoClient.insert_one(data)
    else:
        mongoClient.upldate_one({'_id': ctx.guild.id}, {'$set': {'channel': chain_channel.id}})
    await ctx.send(f'The chain channel has been set to {chain_channel.mention}')
bot.load_extension('jishaku')
bot.run(os.environ['ChainBotToken'])

