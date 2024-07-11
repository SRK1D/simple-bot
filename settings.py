import os
import io
import json
import discord.ext.commands
import wrappers

@wrappers.exceptionWrapper(json.JSONDecodeError)
def parseJson(file: io.FileIO):
    return json.load(file)

def setupSettings(_bot: discord.ext.commands.Bot, _settings: str):
    # -- Check if the file even exists
    if not os.path.isfile('./' + _settings):
        raise FileNotFoundError("Could not find the configuration.json file containing the program's configurations")
    
    global bot, configuration
    bot = _bot
    configuration = parseJson(open(_settings, "r"))
    #pprint(configuration)