# main.py
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
cogs = ["cogs.pingpong", ]

client = commands.Bot(command_prefix='$')

@client.event
# Terminal: Notification when bot connects to server/guild
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    print("Loading cogs")

    for cog in cogs:
        try:
            client.load_extension(cog)
            print(cog + " was loaded.")
        except Exception as e:
            print(e)


@client.event
# Terminal: Notification when someone joins and  leaves server/guild
async def on_member_join(member):
    print(f'{member} has joined.')


async def on_member_remove(member):
    print(f'{member} has left.')

# The following block of code is temporary. All subject to change.


@client.command()
# Discord: Bot responds with "Polo!" and latency
async def marco(ctx):
    await ctx.send(f'Polo! You just wasted {round(client.latency * 1000)} ms of my life. Congrats!')


@client.command()
# Discord: Bot dies
async def die(ctx):
    await ctx.send('Fuck you')
    await ctx.send('https://tenor.com/bKM4f.gif')
    # Maybe one day add feature where bot goes offline (literally dies)


@client.event
# Discord: Bot responds with Daniel and a gif when someone mentions damn
async def on_message(message):
    if message.content == 'damn':
        channel = message.channel
        await channel.send('Daniel')
        await channel.send('https://tenor.com/bMaK0.gif')
# temporary until here

client.run(TOKEN)
