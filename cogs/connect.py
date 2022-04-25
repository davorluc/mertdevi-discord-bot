# connect.py
import discord
from discord.ext import commands


class Connect(commands.Cog):

    def __init__(self, client):
        self.client = client

        @commands.Cog.listener()
        async def on_ready(self):
            print(f'bot has connected to Discord!')


def setup(client):
    client.add_cog(Connect(client))
