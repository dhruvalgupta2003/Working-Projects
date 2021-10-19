import discord
from discord.ext import commands
client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready():
  print("{0.user} is online __!".format(client))

@client.event
async def on_member_join(member):
  print(f"{member} has joined a server.")

@client.event
async def on_member_remove(member):
  print(f"{member} has left the server.")




client.run('ODk4OTYwMjcwMDEyMDY3ODky.YWrz_g.BFkc9wHwyeZ2Yyp1kc9cFPBs8xs')