# main.py
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

client = commands.Bot(command_prefix='$')


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(';help for a list of Commands'))
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


client.run(TOKEN)
