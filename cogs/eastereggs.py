#eastereggs.py
import discord
from discord.ext import commands

"""
    # Blueprint for text/message based easter eggs (copy/paste is possible)
    # Code explanation: You fill the collection array with senteces or messages you want the easter egg to trigger
    # if-statement checks if sent message is in the collection. If so, Chadbot could send a gif with a follow up
    # message that an easter egg has been found.
    # check code below for examples

    @commands.Cog.listener("on_message")
    async def placeholder(self, message):
        collection = []
        if message.content in collection:
            channel = message.channel
            await channel.send("something")
            await channel.send("Congrats sucker, you just found an easter egg. Go tell your mom or something. And tell her I said hi ;)")
            await self.client.process_commands(message)
"""

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
            await channel.send("Congrats sucker, you just found an easter egg. Go tell your mom or something. And tell her I said hi ;)")
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
                "U are a racist",
                "U r a racist",
                "You are racist",
                "U are racist",
                "U r racist"]
        if message.content in allegations:
            channel = message.channel
            await channel.send("https://c.tenor.com/4qD3O4fICuYAAAAC/ok-and.gif")
            await channel.send("Congrats sucker, you just found an easter egg. Go tell your mom or something. And tell her I said hi ;)")
            await self.client.process_commands(message)

    # if someonw mentions that Messi (Pessi) is finished, Chadbot sends a SIUUU gif
    @commands.Cog.listener("on_message")
    async def goat(self, message):
        factos = ["Pessi finished",
                "pessi finished",
                "Messi finished",
                "messi finished",
                "Pessi is finished",
                "pessi is finished",
                "Messi is finished",
                "messi is finished",
                "ronaldo > messi",
                "Ronaldo > Messi",
                "ronaldo > Messi",
                "Ronaldo > messi",
                "CR7 > Messi",
                "cr7 > messi",
                "CR7 > messi",
                "cr7 > Messi",
                "CR7 > LM10",
                "cr7 > lm10",
                "cr7 > LM10",
                "CR7 > lm10",
                ]
        if message.content in factos:
            channel = message.channel 
            await channel.send("https://c.tenor.com/5tMQDJlcOcYAAAAC/siuuu.gif")
            await channel.send("Congrats sucker, you just found an easter egg. Go tell your mom or something. And tell her I said hi ;)")
            await self.client.process_commands(message)

def setup(client):
    client.add_cog(Eastereggs(client))
