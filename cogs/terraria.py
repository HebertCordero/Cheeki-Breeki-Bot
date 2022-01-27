import discord
import requests
from discord.ext import commands

client = commands.Bot(command_prefix = '!')

class Terraria(commands.Cog):
  
  def __init__(self, client):
    self.client = client
  
  # Events
  @commands.Cog.listener()
  async def on_ready(self):
    print('Bot is online')
  
  # Commands
  @commands.command()
  async def terraria(self, ctx):
    await ctx.send('Terraria commands online!')


def setup(client):
  client.add_cog(Terraria(client))
