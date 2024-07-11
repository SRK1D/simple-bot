import urllib
from settings import *
from discord.ext import commands

# I ain't even bothered to fix that code anymore :(
@bot.command(name="serverlist")
async def serverlist(message, gameid: int):
     print(f"{message.author} has requested for server list for game id: {gameid}")
     embed = discord.Embed(title="Server List", description=f"List of available servers for {gameid}:", color=0xe15453)
     a = 1
     with urllib.request.urlopen(f"https://api.infiniteyieldreborn.xyz/servers?gameId={gameid}") as url:
         data = json.load(url)
         for i, server in enumerate(data["data"], 1):
             a = a + 1
             if a == 12:
                 await message.send(embed=embed)
                 embed = discord.Embed(title="Server List", description=f"List of available servers for {gameid}:", color=0xe15453)
                 a = 0
 
 
             server_name = f"Server {i}"
             player_count = f"{server["playing"]}/{server["maxPlayers"]}"
             join_link = f"https://infiniteyieldreborn.xyz/game?placeId={gameid}&gameInstanceId={server["id"]}"
             embed.add_field(name=server_name, value=f"Players: {player_count} [Join]({join_link})", inline=True)
 
     if a <= 12:
         await message.send(embed=embed)
         
@serverlist.error
async def notserverlist(message, error):
     if isinstance(error, commands.MissingRequiredArgument):
         await message.send(f"<@{message.author.id}> you are missing a argument ( which is !serverlist <place/game ID> )")
     else:
         await message.send("An error occurred: {0}".format(error))
         raise error