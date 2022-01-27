import os
import json
import base64
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
  @commands.command(name='terraria', help='Checks if terrara commands are online! (ex: !terraria) ')
  async def terraria(self, ctx):
    await ctx.send('Terraria commands online!')
  
  # Terraria Server Status
  @client.command(name='t_status', help='Terraria Server Status (ex: !t_status) ')
  async def t_status(self, ctx):
    url = "https://46xbqzxllc.execute-api.us-east-1.amazonaws.com/default/terraria/status"
    payload={}
    headers = {
      'x-api-key': os.getenv('terraria')
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200:
      resp = json.loads(response.text)
      #return response.json()
      #print(resp['body'])
      embed = discord.Embed(title="Terraria server status:", description="current status: **{}**".format(resp['body']), color = 0xadd8e6, inline = False)
      await ctx.channel.send(embed = embed)
    else:
      print(response.status_code)
      embed = discord.Embed(title="Terraria server status:", description="current status: **{}**".format(response.status_code), color = 0xadd8e6, inline = False)
      await ctx.channel.send(embed = embed)

  # Terraria Server Status
  @client.command(name='t_stop', help='Terraria Server STOP (ex: !t_stop) ')
  async def t_stop(self, ctx):
    url = "https://46xbqzxllc.execute-api.us-east-1.amazonaws.com/default/terraria/stop"
    payload={}
    headers = {
      'x-api-key': os.getenv('terraria')
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200:
      resp = json.loads(response.text)
      #return response.json()
      #print(resp['body'])
      embed = discord.Embed(title="Terraria server STOP:", description="current status: **{}**".format(resp['body']), color = 0xadd8e6, inline = False)
      await ctx.channel.send(embed = embed)
    else:
      print(response.status_code)
      embed = discord.Embed(title="Terraria server STOP:", description="current status: **{}**".format(response.status_code), color = 0xadd8e6, inline = False)
      await ctx.channel.send(embed = embed)
  
  # Terraria Server Start
  @client.command(name='t_start', help='Terraria Server START (ex: !t_start) ')
  async def t_start(self, ctx):
    url = "https://46xbqzxllc.execute-api.us-east-1.amazonaws.com/default/terraria/start"
    payload={}
    headers = {
      'x-api-key': os.getenv('terraria')
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200:
      resp = json.loads(response.text)
      #return response.json()
      #print(resp['body'])
      embed = discord.Embed(title="Terraria server START:", description="current status: **{}**".format(resp['body']), color = 0xadd8e6, inline = False)
      await ctx.channel.send(embed = embed)
    else:
      print(response.status_code)
      embed = discord.Embed(title="Terraria server START:", description="current status: **{}**".format(response.status_code), color = 0xadd8e6, inline = False)
      await ctx.channel.send(embed = embed)

def setup(client):
  client.add_cog(Terraria(client))

#os.getenv('terraria') x-api-key