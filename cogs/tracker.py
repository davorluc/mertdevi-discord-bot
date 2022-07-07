# tracker.py
# this command will track the users current progression with the easter eggs

import discord
from discord.ext import commands
import json

# defining class
class Tracker(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def tracker(self, ctx):
        jojo = False
        racist = False
        sui = False
        username = str(ctx.message.author)
        with open("cogs/easteregghunters.json") as file:
            data = json.load(file)
        for i in range(len(data["jojo"])):
            if data["jojo"][i] == username:
                jojo = True
                return jojo
        for i in range(len(data["racist"])):
            if data["racist"][i] == username:
                racist = True
                return racist
        for i in range(len(data["sui"])):
            if data["sui"][i] == username:
                sui = True
                return sui

        print(f'{jojo} {racist} {sui}')
        print(username)

def setup(client):
    client.add_cog(Tracker(client))
