# music.py
import discord
from discord.ext import commands


class Music(commands.Cog):

    def __init__(self, client):
        self.client = client

        @commands.command()
        async def play(self, ctx):
            await ctx.send('Placeholder for play command')


def setup(client):
    client.add_cog(Music(client))
