import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '!')

class Tarkov(commands.Cog):
  
  def __init__(self, client):
    self.client = client
  
  # Events
  @commands.Cog.listener()
  async def on_ready(self):
    print('Bot is online')
  
  # Commands
  @commands.command()
  async def tarkov(self, ctx):
    await ctx.send('Tarkov commands online!')


def setup(client):
  client.add_cog(Tarkov(client))
