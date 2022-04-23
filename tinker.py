# File für Tinkering von Commands
import discord
from main import TOKEN
from discord.ext import commands

client = commands.Bot(command_prefix='$')


@client.command()
async def die(ctx):
    await ctx.send('*dies from cringe*')

client.run(TOKEN)
