# connect.py

# imports
import discord
from discord.ext import commands


# defining class
class Connect(commands.Cog):

    def __init__(self, client):
        self.client = client

    client = discord.Client()

    @commands.Cog.listener()
    # using pre-defined method on_ready from discord library to let us know when bot is online
    async def on_ready(self):
        print("--------------------------------------")
        print(f'Chadbot has connected')
        print("--------------------------------------")


# adds class to cogs
def setup(client):
    client.add_cog(Connect(client))
