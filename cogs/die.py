# die.py
import discord
from discord.ext import commands


class Die(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def die(self, ctx):
        await ctx.send('Fuck You')
        await ctx.send('https://tenor.com/bKM4f.gif')


def setup(client):
    client.add_cog(Die(client))
