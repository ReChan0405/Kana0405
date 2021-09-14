from discord import commands 
from discord import colour

class HelpCommands(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.group(invoke_without_command=True)
  async def help(self, ctx):
    em = discord.Embed(title = 'help', description = 'Use a!help command for extended information on the command.',color = ctx.author.color)

    em.add_field(name = 'economy', value = 'bag , balance , beg , buy , deposits , leaderboard , rob , sell , send , shop , slot , withdraw')
    em.add_field(name= 'stats' , value = 'ping , graph')
    em.add_field(name = 'moderation', value = 'kick , ban , mute , purge , unban , unmute , info ')
    
    await ctx.send(embed = em)
  
  
    
    
def setup(bot):
  bot.add_Cog(HelpCommands(bot))
