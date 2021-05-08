import sys
import os
import argparse
import subprocess
import asyncio
import aiofiles
import json
import getpass
import shutil
import random

print(""" _____                    _____            _____                    _____                _____                    _____          
         /\    \                  /\    \          /\    \                  /\    \              /\    \                  /\    \         
        /::\    \                /::\____\        /::\____\                /::\    \            /::\    \                /::\    \        
       /::::\    \              /:::/    /       /:::/    /               /::::\    \           \:::\    \              /::::\    \       
      /::::::\    \            /:::/    /       /:::/    /               /::::::\    \           \:::\    \            /::::::\    \      
     /:::/\:::\    \          /:::/    /       /:::/    /               /:::/\:::\    \           \:::\    \          /:::/\:::\    \     
    /:::/__\:::\    \        /:::/    /       /:::/    /               /:::/__\:::\    \           \:::\    \        /:::/__\:::\    \    
   /::::\   \:::\    \      /:::/    /       /:::/    /               /::::\   \:::\    \          /::::\    \      /::::\   \:::\    \   
  /::::::\   \:::\    \    /:::/    /       /:::/    /      _____    /::::::\   \:::\    \        /::::::\    \    /::::::\   \:::\    \  
 /:::/\:::\   \:::\ ___\  /:::/    /       /:::/____/      /\    \  /:::/\:::\   \:::\    \      /:::/\:::\    \  /:::/\:::\   \:::\    \ 
/:::/__\:::\   \:::|    |/:::/____/       |:::|    /      /::\____\/:::/__\:::\   \:::\____\    /:::/  \:::\____\/:::/__\:::\   \:::\____\
\:::\   \:::\  /:::|____|\:::\    \       |:::|____\     /:::/    /\:::\   \:::\   \::/    /   /:::/    \::/    /\:::\   \:::\   \::/    /
 \:::\   \:::\/:::/    /  \:::\    \       \:::\    \   /:::/    /  \:::\   \:::\   \/____/   /:::/    / \/____/  \:::\   \:::\   \/____/ 
  \:::\   \::::::/    /    \:::\    \       \:::\    \ /:::/    /    \:::\   \:::\    \      /:::/    /            \:::\   \:::\    \     
   \:::\   \::::/    /      \:::\    \       \:::\    /:::/    /      \:::\   \:::\____\    /:::/    /              \:::\   \:::\____\    
    \:::\  /:::/    /        \:::\    \       \:::\__/:::/    /        \:::\   \::/    /    \::/    /                \:::\   \::/    /    
     \:::\/:::/    /          \:::\    \       \::::::::/    /          \:::\   \/____/      \/____/                  \:::\   \/____/     
      \::::::/    /            \:::\    \       \::::::/    /            \:::\    \                                    \:::\    \         
       \::::/    /              \:::\____\       \::::/    /              \:::\____\                                    \:::\____\        
        \::/____/                \::/    /        \::/____/                \::/    /                                     \::/    /        
         ~~                       \/____/          ~~                       \/____/                                       \/____/         
                                                                                                                                          """)

print("Welcome To BlueTE, A CLI To Generate A Discord.py Bot Project!")
print("Note: It's recommended to move the project folder when created.")
TokenValue = input("Enter Your Token:")
PrefixValue = input("Enter Your Prefix:")
print('Success! Token will be saved in your-project/config/.env after choice is given.')

for i in range(0, 1):

    print("1. Create!\n")

    choice = int(input('Choice:'))

    if (choice == 1):
      if sys.platform.startswith('linux'):
        os.system(f'mkdir your-project')
        os.system('cd your-project')
        os.system('mkdir your-project/cogs/')
        os.system('mkdir your-project/config/')
        os.system('touch your-project/config/.env')
        os.system('touch your-project/cogs/moderation.py')
        os.system('touch your-project/cogs/fun.py')
        os.system('touch your-project/cogs/miscellaneous.py')
        os.system('touch your-project/bot.py')

      elif sys.platform.startswith('win32'):
        os.system('mkdir your-project')
        os.system('cd your-project')
        os.system('mkdir your-project/cogs/')
        os.system('mkdir your-project/config/')
        os.system('echo file > your-project/cogs/moderation.py')
        os.system('echo file > your-project/cogs/fun.py')
        os.system('echo file > your-project/cogs/miscellaneous.py')
        os.system('echo file > your-project/config/.env')
        os.system('echo file > your-project/bot.py')
        
      elif sys.platform.startswith('darwin'):
        os.system('mkdir your-project')
        os.system('cd your-project')
        os.system('mkdir your-project/cogs/')
        os.system('mkdir your-project/config/')
        os.system('touch your-project/cogs/moderation.py')
        os.system('touch your-project/cogs/fun.py')
        os.system('touch your-project/cogs/miscellaneous.py')
        os.system('touch your-project/config/.env')
        os.system('touch your-project/bot.py')
        
      elif sys.platform.startswith('cygwin'):
        os.system('mkdir your-project')
        os.system('cd your-project')
        os.system('mkdir your-project/cogs/')
        os.system('touch your-project/config/.env')
        os.system('touch your-project/cogs/moderation.py')
        os.system('touch your-project/cogs/fun.py')
        os.system('touch your-project/cogs/miscellaneous.py')
        os.system('mkdir your-project/config/')
        os.system('touch your-project/bot.py')

      with open('./your-project/bot.py', 'w') as f:
        f.write("""import discord
import json
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")
PREFIX = os.getenv("PREFIX")

client = commands.Bot(command_prefix = PREFIX, intents=discord.Intents.all())

@client.event
async def on_ready():
  print("Bot is ready!")

client.load_extension('cogs.moderation')
client.load_extension('cogs.fun')
client.load_extension('cogs.miscellaneous')
print('Loaded Cogs: Fun, Moderation and Miscellaneous')                  
client.run(TOKEN)""")
        f.close()
  
      with open('./your-project/config/.env', 'w') as f:
        f.write(f"""TOKEN={TokenValue}
PREFIX={PrefixValue}""")
        f.close()

      with open('./your-project/cogs/moderation.py', 'w') as f:
        f.write(f"""import discord
from discord.ext import commands
import json

class Moderation(commands.Cog):
  def __init__(self, client):
    self.client = client
    
    
def setup(client):
  client.add_cog(Moderation(client))""")
      f.close()

      with open('./your-project/cogs/fun.py', 'w') as f:
        f.write(f"""import discord
from discord.ext import commands
import json
import random

class Fun(commands.Cog):
  def __init__(self, client):
    self.client = client


def setup(client):
  client.add_cog(Fun(client))""")
      f.close()

      with open('./your-project/cogs/miscellaneous.py', 'w') as f:
        f.write(f"""import discord
from discord.ext import commands
import json

class Miscellaneous(commands.Cog):
  def __init__(self, client):
    self.client = client
    
    
def setup(client):
  client.add_cog(Miscellaneous(client))""")

      f.close()

print('Stored config in your-project/config/.env')
