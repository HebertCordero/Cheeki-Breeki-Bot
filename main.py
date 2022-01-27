import discord
from discord.ext import commands
import os
import requests
import json
from keep_alive import keep_alive
import os

client = commands.Bot(command_prefix = '!')

@client.command()
async def load(ctx, extension):
  client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
  client.unload_extension(f'cogs.{extension}')
  
for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')

# PURGE CHANNEL MESSAGES
@client.command(name='clear', help='Deletes X messages (ex: !clear X) ')
async def clear(ctx, amount = 5):
    await ctx.channel.purge(limit=amount)

# PURGE CHANNEL MESSAGES
@client.command(name='author', help='Returns the f*** awsome crack author of this bot (ex: !author) ')
async def scav(ctx):
  embed = discord.Embed(title="HebertCordero", description="**{}**".format("https://github.com/HebertCordero"), color = 0xadd8e6, inline = False)
  await ctx.channel.send(embed = embed)

# ON READY RUN:
print(discord.__version__)

# EVENTS
@client.event
async def on_ready():
  print('We have logged in as {0.user}'
  .format(client))

keep_alive()
client.run(os.getenv('TOKEN'))