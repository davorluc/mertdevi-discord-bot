# main.py

# imports
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

# get discord token from environmental variables
TOKEN = os.getenv("DISCORD_TOKEN")

# setting prefix for commands
client = commands.Bot(command_prefix='$')


@client.command()
async def load(ctx, extension):
    # method for loading a command/cog
    client.load_extension(f'cogs.{extension}')
    print("--------------------------------------")
    print(f'Cog {extension} loaded')
    print("--------------------------------------")


@client.command()
async def unload(ctx, extension):
    # method for unloading a command/cog
    client.unload_extension(f'cogs.{extension}')
    print("--------------------------------------")
    print(f'Cog {extension} unloaded')
    print("--------------------------------------")


@client.command()
async def reload(ctx, extension):
    # combines the load and unload method
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    print("--------------------------------------")
    print(f'Cog {extension} reloaded')
    print("--------------------------------------")


# iterates through all files in cogs directory with ending .py (loads all commands when script is run)
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


# runs the client
client.run(TOKEN)
