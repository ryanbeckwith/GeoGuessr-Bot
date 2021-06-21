
#imports
from geoguessr import *
from dev import *
import discord
from discord.ext import commands
import time


client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('Discord Bot Initiated')
""" 
@client.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Invalid command! Please check !help for all available GeoGuessr bot commands!")
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send("Invalid command! Remember to type the map and rule! Please check !help for all available GeoGuessr bot commands!") """

@client.command()
async def geo(ctx, arg1, arg2):
    user_map = arg1
    rule = arg2

    if user_map in maps and rule in options:
        await ctx.send("Game found! " + user_map + " " + rule)
        game_link = game.map_generator(user_map, rule)
        await ctx.send("Enjoy the game! " + game_link)          
    else:
        await ctx.send("Uh oh! Game link could not be generated based on your input. Please try again! Reference !help for help!")


game = GeoGuessorBot()
print("Game Installed")
game.login()
client.run(token)
