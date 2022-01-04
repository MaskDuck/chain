import discord, os
from discord.ext import commands

from pymongo import MongoClient

mongoClient = MongoClient(os.environ['mongolink']).ChainBot.ChainBot

class Config(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.mongoClient = mongoClient

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def set(self, ctx, chain_channel: discord.TextChannel):
        result = self.mongoClient.find_one({'_id': ctx.guild.id})
        if result is None:
            data = {'_id': ctx.guild.id, 'channel': chain_channel.id}
            self.mongoClient.insert_one(data)
        else:
            self.mongoClient.update_one({'_id': ctx.guild.id}, {'$set': {'channel': chain_channel.id}})
        await ctx.send(f'The chain channel has been set to {chain_channel.mention}')

    @commands.command()
    async def unset(self, ctx):
        result = self.mongoClient.find_one({'id': ctx.guild.id})

def setup(bot):
    bot.add_cog(Config(bot))

