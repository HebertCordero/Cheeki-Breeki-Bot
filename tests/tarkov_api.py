import requests
import json

def run_query(name):
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
      print(response.json())
  else:
    print(response.status_code)
    
run_query("m855a1")