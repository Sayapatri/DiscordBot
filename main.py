import discord 
import os
import requests
import json
import random

client = discord.Client()

sad_words = ["sad", "unhappy", "miserable","sorrowful"]
starter_encoragements = ["he is fine", "have a good one"]

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)

    quote = json_data[0]['q'] + "-" + json_data[0]['a']
    return(quote)

@client.event
async def on_ready():
        print("..........")
        print("Bot is online {0.user}".format(client))
        print("..........")
@client.event 
async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith('$inspire'):
            quote = get_quote()
            await message.channel.send(quote)    
        if any (word in message.content for word in sad_words):
            await message.channel.send(random.choice(starter_encoragements))    
 
client.run('OTc5MzMxMjMzNzM5ODM3NDgx.G5ytqP.Bc8KwjMvq3tALn76enqjF7nAb2kHtp8rf9mEgM')