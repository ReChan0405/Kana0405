from discord import commands 

class HelpCommands(commands.Cog):
  def __init__(self, bot):
    self.bot = bot 
    
    
def setup(bot):
  bot.add_Cog(HelpCommands(bot))
