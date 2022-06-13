# ping.py

# imports
import discord
from discord.ext import commands


# define class
class Ping(commands.Cog):

    def __init__(self, client):
        self.client = client

    # simple command that responds with pong and latency
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.client.latency * 1000)}ms')


# add class to cogs
def setup(client):
    client.add_cog(Ping(client))
