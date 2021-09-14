import discord
from discord.ext import commands 

Bot = commands.Bot(command_prefix = '#', help_command = None)

@Bot.event
async def on_ready():
    print(f'{client.user} is ready ')
    
extensions = ['cogs.CommandEvents', 'cogs.HelpCommands']

if __name__ = '__main__':
    for ext in extensions:
        client.load_extensions(ext)
   
Bot.run('TOKEN')
