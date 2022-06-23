# eastereggs.py

# imports
import discord
from discord.ext import commands
import json

"""
    # Blueprint for text/message based easter eggs (copy/paste is possible)
    # Code explanation: You fill the collection array with senteces or messages you want the easter egg to trigger
    # if-statement checks if sent message is in the collection. If so, Chadbot could send a gif with a follow up
    # message that an easter egg has been found.
    # check code below for examples

    # makes the Cog.listener listen for on_messsge events
    @commands.Cog.listener("on_message")
    # replace placeholder with your desired quote on quote command name. parameters stay the same
    async def placeholder(self, message):
        # String array with on_message event triggers. you may change array name
        collection = []
        # check if sent message in array
        if message.content in collection:
            # saves user from sent message in variable username
            username = message.author
            # sends easteregg response as dm. replace something with desired message (e.g. link to gif from tenor)
            await message.author.send("something")
            await message.author.send("Congrats sucker, you just found an easter egg. Go tell your mom or something. And tell her I said hi ;)")
            await self.client.process_commands(message)
            # boolean variable that checks if user in Json file. False by default
            inJson = False
            # opens easteregghunters.json as file
            with open("cogs/easteregghunters.json") as file:
                data = json.load(file)
                # only selects the easter egg we want to check. replace <json> with right list in json file. check in json file if not sure what to insert
                temp = data["<json>"]
            # loops through temp
            for i in range (len(temp)):
                # check if username at index i
                if temp[i]['username'] == username:
                    # returns true if it is in the file
                    inJson = True
                    return inJson
            # appends to dictionary/json file if user not found
            if inJson == False:
                y = {"username": username}
                temp.append(y)
                write_json(data)
"""

def write_json(data, filename = "cogs/easteregghunters.json"):
    with open (filename, "w") as f:
        json.dump(data, f, indent = 4)

class Eastereggs(commands.Cog):


    def __init__(self, client):
        self.client = client
    
    # all code explanation will be in the blueprint above, since it is the same for every easter egg
    # if easter egg is based on a different blueprint, it will be in the code directly

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
                "Is this a Jojos reference",
                "Is this a Jojos reference?"]
        if message.content in references:
            username = str(message.author)
            await message.author.send("https://c.tenor.com/vw7ogSgBWuYAAAAC/no-yes.gif")
            await message.author.send("Congrats sucker, you just found an easter egg. Go tell your mom or something. And tell her I said hi ;)")
            await self.client.process_commands(message)
            inJson = False
            with open("cogs/easteregghunters.json") as file:
                data = json.load(file)
                temp = data["jojo"]
            for i in range (len(temp)):
                if temp[i]['username'] == username:
                    inJson = True
                    return inJson
            if inJson == False:
                y = {"username": username}
                temp.append(y)
                write_json(data)


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
            username = str(message.author)
            await message.author.send("https://c.tenor.com/4qD3O4fICuYAAAAC/ok-and.gif")
            await message.author.send("Congrats sucker, you just found an easter egg. Go tell your mom or something. And tell her I said hi ;)")
            await self.client.process_commands(message)
            inJson = False
            with open("cogs/easteregghunters.json") as file:
                data = json.load(file)
                temp = data["racist"]
            for i in range (len(temp)):
                if temp[i]['username'] == username:
                    inJson = True
                    return inJson
            if inJson == False:
                y = {"username": username}
                temp.append(y)
                write_json(data)

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
            username = str(message.author)
            await message.author.send("https://c.tenor.com/5tMQDJlcOcYAAAAC/siuuu.gif")
            await message.author.send("Congrats sucker, you just found an easter egg. Go tell your mom or something. And tell her I said hi ;)")
            await self.client.process_commands(message)
            inJson = False
            with open("cogs/easteregghunters.json") as file:
                data = json.load(file)
                temp = data["sui"]
            for i in range (len(temp)):
                if temp[i]['username'] == username:
                    inJson = True
                    return inJson
            if inJson == False:
                y = {"username": username}
                temp.append(y)
                write_json(data)

def setup(client):
    client.add_cog(Eastereggs(client))
