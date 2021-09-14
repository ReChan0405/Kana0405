import discord
from discord.ext import commands 

Bot = commands.Bot(command_prefix = '#')

@Bot.event
async def on_ready():
    print(f'{client.user} is ready ')
    
Bot.load_extension('cogs.CommandEvents')
Bot.run('TOKEN')
