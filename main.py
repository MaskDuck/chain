import discord
from discord.ext import commands

import jishaku

from pymongo import MongoClient
import os

mongoClient = MongoClient(os.environ['mongolink']).ChainBot.ChainBot

bot = commands.Bot(command_prefix = 'chain ', activity=discord.Game('dont break the chain ty'), status=discord.Status.idle)
@bot.event
async def on_message(m):
    channel_id = mongoClient.find_one({'_id': m.guild.id})['channel']
    if m.channel.id == channel_id:
        messages = await m.channel.history(limit=4).flatten()
        messages.pop(m)
        for ms in messages:
            if ms.content == messages[0].content:
                pass
            else:
                if m.content == messages[0].content:
                    pass
                else:
                    await m.delete()
                    await m.channel.send('You are breaking the chain!', delete_after=5)
    else:
        await bot.process_commands(m)




@bot.command()
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

