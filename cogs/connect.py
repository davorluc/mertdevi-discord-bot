# connect.py
import discord
from discord.ext import commands


class Connect(commands.Cog):

    def __init__(self, client):
        self.client = client

    client = discord.Client()

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Chadbot has connected')


def setup(client):
    client.add_cog(Connect(client))
