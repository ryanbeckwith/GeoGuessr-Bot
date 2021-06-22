
#imports
from discord.ext.commands.errors import *
from geoguessr import *
from dev import *
import discord
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType, CommandOnCooldown


client = commands.Bot(command_prefix = '-')

@client.event
async def on_ready():
    print('Discord Bot Initiated')

@client.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Invalid command! Please check !help for all available GeoGuessr bot commands!")
        ctx.command.reset_cooldown(ctx)
    if isinstance(error, CommandOnCooldown):
        await ctx.send(f"Slow down! Use the bot in {error.retry_after:,.2f} seconds!")
        

@client.command()
@commands.cooldown(1,30, BucketType.user)
async def geo(ctx, arg1, arg2):
    user_map = arg1
    rule = arg2

    if user_map in maps and rule in options:
        await ctx.send("Game found! " + user_map + " " + rule)
        game_link = game.map_generator(user_map, rule)
        await ctx.send("Enjoy the game! " + game_link)          
    else:
        await ctx.send("Uh oh! Game link could not be generated based on your input. Reference !help for help!")
        ctx.command.reset_cooldown(ctx)

@geo.error
async def geo_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("You forgot to add a required option! Remember the format is !geo [map] [game rule]")
        ctx.command.reset_cooldown(ctx)


game = GeoGuessorBot()
print("Game Installed")
game.login()
client.run(token)
