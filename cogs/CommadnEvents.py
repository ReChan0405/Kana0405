import discord
from discord.ext import commands 

class CommandEvents(commands.Cog):
  def __init__(self, bot):
    self.bot = bot 
    
  @bot.Cog.listener()
  async def on_command_error(ctx, error):
    print(ctx.command.name +' was called incorrectly')
  
  @bot.Cog.listener()
  async def on_command(ctx):
    if ctx.command is not None:
      if ctx.command.name in commands_tally:
        commands_tally[ctx.command.name] += 1
      else:
        commands_tally[ctx.command.name] = 1
      
  @bot.Cog.listener()
  async def on_command_completion(ctx):
    print(ctx.command.name + 'was called successfully')
def setup(bot):
  bot.add_cog(CommandEvents(bot))
    
