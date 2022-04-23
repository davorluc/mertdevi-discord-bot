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
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_member_join(member):
    print(f'{member} has joined.')


async def on_member_remove(member):
    print(f'{member} has left.')


@client.command()
async def marco(ctx):
    await ctx.send('Polo!')


@client.command()
async def die(ctx):
    await ctx.send('Fuck you')
    await ctx.send('https://tenor.com/bKM4f.gif')

client.run(TOKEN)
