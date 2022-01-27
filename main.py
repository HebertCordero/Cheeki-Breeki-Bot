import discord
from discord.ext import commands
import os
import requests
import json
import random
import csv
from tabulate import tabulate
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

# COMMAND: CREATE CUSTOM CHANNEL
@client.command(name='init', help='Creates a Cheeki Breeki Text-Channel! (Requires Admin permission) ')
@commands.has_permissions(administrator = True)
async def init(ctx):
  guild = ctx.guild
  await guild.create_text_channel(name='Cheeki Breeki')
  embed = discord.Embed(title="New Text channel was created!", description="Name: **{}**".format('Cheeki Breeki'), color = 0xadd8e6, inline = False)
  await ctx.channel.send(embed = embed)
  
# COMMAND: RANDOM SCAV LINE
@client.command(name='scav', help='Returns a random Scav line! (ex: !scav) ')
async def scav(ctx):
  scav_line = ['Kefka!', 'prjamo bertsi', 'Cheeki breeki', 'Opachki', 'Vanon suka!', 'Paskuda!', 'Vot khuy!', 'Urod!', 'Davay mochi ikh!', 'Pidoras!', 'Khana te, ponyal!?']
  embed = discord.Embed(title=random.choice(scav_line), description="-scav 2021-".format(), color = 0xadd8e6, inline = False)
  await ctx.channel.send(embed = embed)

# COMMAND: Bullet Data
@client.command(name='bullet', help='Returns caliver info (ex: !bullet 5.56x45) ')
async def bullet(ctx, name):
  b_dataRaw = './assets/bullet_data.csv'
  with open(b_dataRaw, encoding="utf8") as f:
      csv_reader = csv.reader(f)
      temp_arr = []
      for line in csv_reader:
        if line[0] == name:
          temp_arr.append(line)
      print(tabulate(temp_arr, headers=['B.Type', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6','Dmg','Frag %','A.Type' ]))
      embed = discord.Embed(title=name, description=tabulate(temp_arr, headers=['B.Type', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6','Dmg','Frag %','A.Type']).format(), color = 0xadd8e6, inline = False)
      await ctx.channel.send(embed = embed)

@client.command(name='test', help='Returns a sample text (ex: !test TEXT RETURN) ')
async def test(ctx, name):
  embed = discord.Embed(title=name, description=name.format(), color = 0xadd8e6, inline = False)
  await ctx.channel.send(embed = embed)

# COMMAND: GET DAMAGE DATA
@client.command(name='item', help='Shows info of the item (ex: !item soap) ')
async def item(ctx, name):
  #EXAMPLE: m855a1
  new_query = """
  {
      itemsByName(name: "%s") {
          id
          name
          shortName
      }
  }
  """
  new_query = new_query % (name)
  response = requests.post('https://tarkov-tools.com/graphql', json={'query': new_query})
  if response.status_code == 200:
      #return response.json()
      embed = discord.Embed(title="query", description=response.json(), color = 0xadd8e6,inline = False)
      await ctx.channel.send(embed = embed)
      print(response.json())
  else:
    print(response.status_code)
    raise Exception("Query failed to run by returning code of {}. {}".format(response.status_code))

# COMMAND: GET ITEM DATA
@client.command(name='price', help='Shows price of the item (ex: !price soap) ')
async def price(ctx, name):
  #EXAMPLE: m855a1
  new_query = """
  {
      itemsByName(name: "%s") {
          name
          shortName
          basePrice
          imageLink
          traderPrices {
            price
            trader{
              name
            }
          }
      }
  }
  """
  new_query = new_query % (name)
  response = requests.post('https://tarkov-tools.com/graphql', json={'query': new_query})
  if response.status_code == 200:
      #return response.json()
      #print(response.json()['data']['itemsByName'][0]['imageLink'])
      imageURL = response.json()['data']['itemsByName'][0]['imageLink']
      embed = discord.Embed(title=response.json()['data']['itemsByName'][0]['shortName'], description=response.json(), color = 0xadd8e6,inline = False)
      embed.set_image(url=imageURL)
      await ctx.channel.send(embed = embed)
      print(response.json())
  else:
    print(response.status_code)
    raise Exception("Query failed to run by returning code of {}. {}".format(response.status_code))

# PURGE CHANNEL MESSAGES
@client.command(name='clear', help='Deletes X messages (ex: !clear X) ')
async def clear(ctx, amount = 5):
    await ctx.channel.purge(limit=amount)

# Terraria Server Status
@client.command(name='t_status', help='Terraria Server Status (ex: !t_status) ')
async def t_status(ctx):
  response = requests.post('https://46xbqzxllc.execute-api.us-east-1.amazonaws.com/default/terraria/status')
  if response.status_code == 200:
    #return response.json()
    print("done")
  else:
    print(response.status_code)
    raise Exception("Query failed to run by returning code of {}. {}".format(response.status_code))


# ON READY RUN:
print(discord.__version__)

# EVENTS
@client.event
async def on_ready():
  print('We have logged in as {0.user}'
  .format(client))

keep_alive()
client.run(os.getenv('TOKEN'))