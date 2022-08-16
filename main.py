import discord
import os

token = os.environ('MTAwOTEwMzkyMDcyNDk3MTU5Mg.GFZ8uf.ayK8KBqfs6eL6dlSD6SoFmpkkTy3t9tmtyo0Zw')

client = discord.Client()

@client.event

async def on_ready():
  print("Discord bot config")
  
async def on_message(message):
  print("Discord bot config")
  if message.author == client.user:
    return
  if message.content.startswith('$hello'):
    await message.channel.send('Hello!!')

client.run(token)