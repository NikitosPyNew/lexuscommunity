import discord, os
from discord.ext import commands, bridge
bot = commands.Bot(command_prefix = '/', 
                   case_insensitive = True, 
                   intents = discord.Intents.all(),
                  help_command = None)
if __name__ =="__main__":
  bot.run(os.getenv('TOKEN'))
