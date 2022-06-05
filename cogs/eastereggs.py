#eastereggs.py
import discord
from discord.ext import commands

class Eastereggs(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def test(self, ctx):
        await ctx.send('This is a placeholder for this cog. Work in Progress')


def setup(client):
    client.add_cog(Eastereggs(client))
