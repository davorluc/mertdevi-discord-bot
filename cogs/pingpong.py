from discord.ext import commands
import discord
import os

class Ping(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx: commands.Context):
        await ctx.send(f'Pong! {round(self.bot.latency * 1000)}ms')


def setup(bot: commands.Bot):
    bot.add_cog(Ping(bot))
