from discord.ext import commands 

class administrator(commands.Cog):
  def __init__(self, bot):
    self.bot = bot 
    
  @commands.commands()
  async def ban(self, ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)
    
def setup(bot):
  bot.add_cog(administrator(bot))
