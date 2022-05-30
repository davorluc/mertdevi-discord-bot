# music.py
import discord
from discord.ext import commands


class Music(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def join(self, ctx):
        if(ctx.author.voice):
            channel = ctx.message.author.voice.channel
            await channel.connect()
            await ctx.send(f'AYO! We got a party in >>>{channel}<<<')
            print("Chadbot has connected to a voice channel")
            print("--------------------------------------")
        else:
            await ctx.send("Dipshit, you aren't in a voice channel... where do you expect me to join?")
            print("User not in any voice channel. Chadbot can't join")

    @commands.command(pass_context=True)
    async def leave(self, ctx):
        if(ctx.voice_client):
            await ctx.guild.voice_client.disconnect()
            await ctx.send("Bye, fucker")
            print("Chadbot left a voice channel")
            print("--------------------------------------")
        else:
            await ctx.send("Dipshit, how am I gonna leave a voice channel if I'm not in one?")
            print("User not in any voice channel. Chadbot can't leave")
            print("--------------------------------------")

    @commands.command()
    async def play(self, ctx):
        await ctx.send('Placeholder for play command')


def setup(client):
    client.add_cog(Music(client))
