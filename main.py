import discord
from discord.ext import commands
import os
import requests
import json
import random

client = discord.Client()


def get_scav():
  scav_line = ['Kefka!', 'prjamo bertsi', 'Cheeki breeki', 'Opachki', 'Vanon suka!', 'Paskuda!', 'Vot khuy!', 'Urod!', 'Davay mochi ikh!', 'Pidoras!', 'Khana te, ponyal!?']
  return (random.choice(scav_line))

def run_query(query):
  response = requests.post('https://tarkov-tools.com/graphql', json={'query': query})
  if response.status_code == 200:
      return response.json()
  else:
      raise Exception("Query failed to run by returning code of {}. {}".format(response.status_code, query))


#CODE
print(discord.__version__)
new_query = """
{
    itemsByName(name: "m855a1") {
        id
        name
        shortName
    }
}
"""
result = run_query(new_query)
print(result)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'
  .format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
      return
  if message.content.startswith('-cheeki'):
    await message.channel.send(get_scav())
  if message.content.startswith('-query'):
    await message.channel.send(run_query(new_query))

client.run(os.getenv('TOKEN'))