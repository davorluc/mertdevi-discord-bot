#eastereggs.py
import discord
from discord.ext import commands

class Eastereggs(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    # If a user asks if this was a JoJo's reference, Chadbot confirm# If a user asks if this was a JoJo's reference, Chadbot confirms.
    
    @commands.Cog.listener("on_message")
    async def jojo(self, message):
        references = ["is this a jojo's reference?",
                "Is this a JoJo's reference?",
                "is this a jojo's reference?",
                "Is this a JoJo's reference",
                "is this a jojos reference",
                "Is this a JoJos reference?",
                "is this a jojos reference?",
                "Is this a Jojos reference"]
        if message.content in references:
            channel = message.channel
            await channel.send("https://c.tenor.com/vw7ogSgBWuYAAAAC/no-yes.gif")
            await self.client.process_commands(message)

    #more eastereggs to come :)

def setup(client):
    client.add_cog(Eastereggs(client))
