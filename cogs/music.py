# music.py

# imports
import discord
from discord.ext import commands
from youtube_dl import YoutubeDL


# define class
class Music(commands.Cog):

    def __init__(self, client):
        self.client = client

        # boolean variables to check if bot is playing or paused
        self.is_playing = False
        self.is_paused = False

        # music queue as 2d array
        self.music_queue = []
        # misc. options for ydl and ffmpeg. ignore, copied from internet
        self.YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
        self.FFMPEG_OPTIONS = {
            'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

        self.vc = None

    # search yt class
    def search_yt(self, item):
        with YoutubeDL(self.YDL_OPTIONS) as ydl:
            try:
                # extracts infos from youtube video
                info = ydl.extract_info("ytsearch:%s" %
                                        item, download=False)['entries'][0]
            except Exception:
                return False

        # returns data as dictionary
        return {'source': info['formats'][0]['url'], 'title': info['title']}

    # play next function
    def play_next(self):
        # check if music queue not 0
        if len(self.music_queue) > 0:
            self.is_playing = True

            #get the first url
            m_url = self.music_queue[0][0]['source']

            #remove the first element as you are currently playing it
            self.music_queue.pop(0)

            # plays the next song
            self.vc.play(discord.FFmpegPCMAudio(
                m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
        else:
            self.is_playing = False

    # play music function
    async def play_music(self, ctx):
        # check if music queue not 0
        if len(self.music_queue) > 0:
            self.is_playing = True

            # gets url from music queue array
            m_url = self.music_queue[0][0]['source']

            #try to connect to voice channel if you are not already connected
            if self.vc == None or not self.vc.is_connected():
                self.vc = await self.music_queue[0][1].connect()

                #in case we fail to connect
                if self.vc == None:
                    await ctx.send("Could not connect to the voice channel")
                    return
            else:
                await self.vc.move_to(self.music_queue[0][1])

            #remove the first element as you are currently playing it
            self.music_queue.pop(0)

            self.vc.play(discord.FFmpegPCMAudio(
                m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
        else:
            self.is_playing = False

    # join command
    @commands.command(pass_context=True)
    async def join(self, ctx):
        # check if author is connected to a voice channel
        if(ctx.author.voice):
            # saves channel from author in variable
            channel = ctx.message.author.voice.channel
            # connects to voice channel
            await channel.connect()
            await ctx.send(f'AYO! We got a party in >>>{channel}<<<')
            print("--------------------------------------")
            print("Chadbot has connected to a voice channel")
            print("--------------------------------------")
        else:
            await ctx.send("Dipshit, you aren't in a voice channel... where do you expect me to join?")
            print("--------------------------------------")
            print("User not in any voice channel. Chadbot can't join")
            print("--------------------------------------")

    # leave command
    @commands.command(pass_context=True)
    async def leave(self, ctx):
        # check if bot in a voice channel
        if(ctx.voice_client):
            self.is_paused = False
            self.is_playing = False
            # bot disconnets from voice channel
            await ctx.guild.voice_client.disconnect()
            await ctx.send("Bye, fucker")
            print("--------------------------------------")
            print("Chadbot left a voice channel")
            print("--------------------------------------")
        else:
            await ctx.send("Dipshit, how am I gonna leave a voice channel if I'm not in one?")
            print("--------------------------------------")
            print("User not in any voice channel. Chadbot can't leave")
            print("--------------------------------------")

    # play command
    @commands.command()
    async def play(self, ctx, *args):
        # takes argument from sent message and stores it in query variable
        query = " ".join(args)

        # saves authors voice channel in variable
        voice_channel = ctx.author.voice.channel
        # checks if user is connected to voice channel
        if voice_channel is None:
            await ctx.send("How do you expect me to play music when I'm not in a voice channel? Use $join. Or don't. I don't give a shit")
        elif self.is_paused:
            self.vc.resume()
        else:
            # uses search_yt function defined above with query variable as parameter
            song = self.search_yt(query)
            # checks if it a valid request
            if type(song) == type(True):
                await ctx.send("WTF is this shit? I can't use this format. Give me something else ffs")
            else:
                await ctx.send("Found your song. Added id to your queue, it's lame as shit tho")
                # adds song to music queue
                self.music_queue.append([song, voice_channel])

                if self.is_playing == False:
                    await self.play_music(ctx)

    # pause command
    @commands.command()
    async def pause(self, ctx, *args):
        if self.is_playing:
            self.is_playing = False
            self.is_paused = True
            # pauses the bot
            self.vc.pause()
        elif self.is_paused:
            self.vc.resume()

    # resume command
    @commands.command()
    async def resume(self, ctx, *args):
        if self.is_paused:
            self.is_paused = True
            self.is_playing = False
            # resumes the bot
            self.vc.resume()

    # skip command
    @commands.command()
    async def skip(self, ctx, *args):
        if self.vc != None and self.vc:
            # bot stops playing
            self.vc.stop()
            # play music function get called
            await self.play_music(ctx)

    # queue command
    @commands.command()
    async def queue(self, ctx):
        retval = ""

        # iterates through loop
        for i in range(0, len(self.music_queue)):
            if i > 4:
                break
            retval += self.music_queue[i][0]['title'] + '\n'

        if retval != "":
            # sends return value
            await ctx.send(retval)
        else:
            await ctx.send("Queue is empty... dipshit")

    # clear command
    @commands.command()
    async def clear(self, ctx, *args):
        if self.vc != None and self.is_playing:
            # stops playing music
            self.vc.stop()
        # sets music queue as empty array
        self.music_queue = []
        await ctx.send("Queue has been deleted... F in the chat boys")


# adds class to cogs
def setup(client):
    client.add_cog(Music(client))
