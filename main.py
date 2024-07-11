from dotenv import load_dotenv

# // -- For discord related stuff :?
import discord
import discord.ext.commands
from discord.ext import commands

# // -- Misc I need to filter
import os

# // -- To setup the bot env
import settings


load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

settings.setupSettings(bot, "configuration.json") # Make the bot variable global for all files imported
commandsFile = [i.replace(".py", "") for i in os.listdir("./commands/") if os.path.isfile(os.path.join("./commands/", i)) and i[-3:] == ".py"] # Filters all commands
for commandFile in commandsFile:
    __import__('commands.' + commandFile)
    
bot.run(TOKEN)