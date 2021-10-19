import discord
from discord.ext import commands
import requests
import json
intents = discord.Intents.default()
intents.members=True
client = discord.Client(intents=intents)

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return (quote)


@client.event
async def on_ready():
  print("{0.user} is online __!".format(client))

@client.event
async def on_member_join(member):
  print(f"{member} has joined a server.")

@client.event
async def on_member_remove(member):
  print(f"{member} has left the server.")
  
@client.event 
async def on_message(message):
  if message.content.startswith("$inspire"):
    quote = get_quote()
    await message.channel.send(quote)




client.run('ODk4OTYwMjcwMDEyMDY3ODky.YWrz_g.BFkc9wHwyeZ2Yyp1kc9cFPBs8xs')
