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

    # someone calls someone else out as a racist. Chadbot responds in the most based way
    @commands.Cog.listener("on_message")
    async def racist(self, message):
        allegations = ["you are a racist",
                "u are a racist",
                "u r a racist",
                "you are such a racist",
                "u are such a racist",
                "u r such a racist",
                "racist",
                "racist...",
                "Racist",
                "Racist...",
                "you are racist",
                "u are racist",
                "u r racist",
                "You are a racist",
                "You are such a racist",
                "U are a racust",
                "U r a racist2",
                "You are racist",
                "U are racist",
                "U r racist"]
        if message.content in allegations:
            channel = message.channel
            await channel.send("https://c.tenor.com/4qD3O4fICuYAAAAC/ok-and.gif")
            await self.client.process_commands(message)

def setup(client):
    client.add_cog(Eastereggs(client))
