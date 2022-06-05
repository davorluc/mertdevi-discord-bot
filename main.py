# main.py
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

client = commands.Bot(command_prefix='$')


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    print("--------------------------------------")
    print(f'Cog {extension} loaded')
    print("--------------------------------------")


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    print("--------------------------------------")
    print(f'Cog {extension} unloaded')
    print("--------------------------------------")


@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    print("--------------------------------------")
    print(f'Cog {extension} reloaded')
    print("--------------------------------------")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run(TOKEN)
