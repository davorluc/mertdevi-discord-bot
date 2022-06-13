# die.py

# imports
import discord
from discord.ext import commands


# defining class
class Die(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    # basic command. if command is called, it sends two strings
    async def die(self, ctx):
        await ctx.send('Fuck You')
        await ctx.send('https://tenor.com/bKM4f.gif')


# adds class to cogs
def setup(client):
    client.add_cog(Die(client))
