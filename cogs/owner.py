import discord
from discord.ext import commands

import os
import asyncio

class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.is_owner()
    async def shutdown(self, ctx):
        await ctx.send('bye...')
        
        await self.bot.close()
        

def setup(bot):
    bot.add_cog(Owner(bot))
