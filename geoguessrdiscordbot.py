
#imports
import asyncio
import os
import discord
from os import environ
from geoguessr import *
from inputs import africa, asia, na, sa, europe, oceania, misc, custom, definitions
from discord import embeds
from discord.ext.commands.errors import *
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType, CommandOnCooldown

# Variables for setting up the bot.
TOKEN = environ['TOKEN']
client = commands.Bot(command_prefix = '-')
client.remove_command('help')

@client.event
async def on_ready():
    # Tells user that the bot is ready to be used
    print('Discord Bot Initiated')

@client.command(aliases = ["maps"])
async def mapsinfo(ctx):
    # A help command that tells the user of the maps available for the bot to use.
    page_count = 0
    buttons = [u"\u23EA", u"\u2B05", u"\u27A1", u"\u23E9"]
    remove_char = ["{", "}", "'"]
    
    africa_list = (', '.join(sorted(filter(lambda i: i not in remove_char, africa))))
    asia_list = (', '.join(sorted(filter(lambda i: i not in remove_char, asia))))
    na_list = (', '.join(sorted(filter(lambda i: i not in remove_char, na))))
    sa_list = (', '.join(sorted(filter(lambda i: i not in remove_char, sa))))
    europe_list = (', '.join(sorted(filter(lambda i: i not in remove_char, europe))))
    oceania_list = (', '.join(sorted(filter(lambda i: i not in remove_char, oceania)))) 
    misc_list = (', '.join(sorted(filter(lambda i: i not in remove_char, misc))))
    custom_list = (', '.join(sorted(filter(lambda i: i not in remove_char, custom))))

    page1 = discord.Embed(
        color = discord.Color.red(),
        title = "Maps",
        description = "Flip through all the pages to find all official GeoGuessr maps. Custom Maps are on the last page."

    )
    page2 = discord.Embed(
        color = discord.Color.red(),
    )
    page3 = discord.Embed(
        color = discord.Color.red(),
    )
    page4 = discord.Embed(
        color = discord.Color.red(),
    )
    page5 = discord.Embed(
        color = discord.Color.red(),
    )
    page6 = discord.Embed(
        color = discord.Color.red(),
    )
    page7 = discord.Embed(
        color = discord.Color.red(),
    )
    page8 = discord.Embed(
        color = discord.Color.red(),
    )
    page9 = discord.Embed(
        color = discord.Color.red(),
    )
    page1.add_field(name = "Note:" , value = "You can use any of these maps listed in this message with the -geo command. Use -help to learn the correct syntax.")
    
    page2.add_field(name = "Africa Maps", value = africa_list, inline = True)
    page2.add_field(name = "Example of playing an Africa Map", value = "-geo madagascar nm", inline = True)
    
    page3.add_field(name = "Asia Maps", value = asia_list, inline = True)
    page3.add_field(name = "Example of playing an Asia Map", value = "-geo india nm", inline = True)
    
    page4.add_field(name = "Europe Maps", value = europe_list, inline = True)
    page4.add_field(name = "Example of playing an Europe Map", value = "-geo uk nm", inline = True)
    
    page5.add_field(name = "Miscellaneous Maps", value = misc_list, inline = True)
    page5.add_field(name = "Example of playing a Miscellaneous Map", value = "-geo famous-places nm", inline = True)
    
    page6.add_field(name = "North America Maps", value = na_list, inline = True)
    page6.add_field(name = "Example of playing a North America Map", value = "-geo usa nm", inline = True)

    page7.add_field(name = "South America Maps", value = sa_list, inline = True)
    page7.add_field(name = "Example of playing a South America Map", value = "-geo peru nm", inline = True)

    page8.add_field(name = "Oceania Maps", value = oceania_list, inline = True)
    page8.add_field(name = "Example of playing an Oceania Map", value = "-geo australia nm", inline = True)
    
    page9.add_field(name = "Custom Maps", value = custom_list, inline = True)
    page9.add_field(name = "Example of playing a Custom Map", value = "-geo urban-world-nobrr nm", inline = True)


    help_pages = [page1, page2, page3, page4, page5, page6, page7, page9, page9]
    message = await ctx.send(embed = help_pages[page_count])

    for button in buttons:
        await message.add_reaction(button)
    
    while True:
        try: 
            reaction, user = await client.wait_for("reaction_add", check = lambda reaction, user: user == ctx.author and reaction.emoji in buttons, timeout = 60.0)
        except asyncio.TimeoutError:
            pass

        else:
            prev_page = page_count
            
            if reaction.emoji == u"\u23EA":
                page_count = 0

            elif reaction.emoji  == u"\u2B05":
                if page_count > 0:
                    page_count -= 1

            elif reaction.emoji == u"\u27A1":
                if page_count < len(help_pages)-1:
                    page_count += 1

            elif reaction.emoji == u"\u23E9":
                page_count = len(help_pages)-1
            
            for button in buttons:
                await message.remove_reaction(button, ctx.author)
            
            if page_count != prev_page:
                await message.edit(embed = help_pages[page_count])

@client.command(aliases = ["options", "game-rules"])
async def optioninfo(ctx):
    # a help command that tells the user of all the options the bot can use.
    remove_char = ["{", "}", "'"]
    options_list = (', '.join(sorted(filter(lambda i: i not in remove_char, options))))
    definitions_list = ('\n'.join(sorted(filter(lambda i: i not in remove_char, definitions))))

    
    options_page = discord.Embed(
        color = discord.Color.red(),
        title = "Options",
        description = "You can make a game with custom game rules that GeoGuessr has to offer."
    )
    options_page.add_field(name = "Options:", value = options_list, inline = True)
    options_page.add_field(name = "Game Setting Explainations:", value = definitions_list, inline = True)
    options_page.add_field(name = "Example of using an option (game rule):", value = "-geo diverse-world nm", inline = False)
    options_page.add_field(name = "Note:", value = "The time rule has not been implemented yet. It will be implemented in a future update :)", inline = False)

    await ctx.send(embed = options_page)

@client.command(aliases = ["help"])
async def help_command(ctx):
    # a help command that gives instructions on how to use the bot on discord.
    help_page = discord.Embed(
        color = discord.Color.red(),
        title = "Help Page",
        description = "Welcome to the help page! Learn about all the commands for this bot below!"
    )

    help_page.add_field(name = "-geo", value = "The -geo command is how you can start a GeoGuessr game.\n Alternatively you can use -g or -game! \n -geo [map] [rule]" , inline = True)
    help_page.add_field(name = "Example of using the -geo command", value = "-geo usa nm \n -g usa nm \n -game usa nm", inline = True)
    help_page.add_field(name = "Note:" , value = "You must put in a map and game rule! See -maps and -options for more details.", inline = True)
    help_page.add_field(name = "-maps", value = "The -maps command will list all the available maps to play!", inline = False)
    help_page.add_field(name = "-options", value = "The -options command will list all the game rule options you can use!", inline= False)
    help_page.add_field(name = "-author", value = "Learn about who made this bot :)", inline= False)
    await ctx.send(embed = help_page)

@client.command(aliases = ["author"])
async def credits(ctx):
    # a command that tells the user of who made this bot.
    about = discord.Embed(
        color = discord.Color.red(),
        title = "Credits:",
        description = "This bot was made by #senn0526" 
    )
    about.set_thumbnail(url = "https://cdn.discordapp.com/avatars/239941463717314560/a_5199b98813b8a9c90327c033b3440f9e.gif?size=1024")
    await ctx.send(embed = about)

@client.command(aliases = ["g", "game"])
@commands.cooldown(1,30, BucketType.user)
async def geo(ctx, arg1, arg2):
    # this command is the call for using the GeoGuessr.py functions. It takes in two arugments from the user in discord: map and rule
    user_map = arg1.lower()
    rule = arg2.lower()

    if user_map in maps and rule in options:
        await ctx.send("Link is being generated for the map: " + user_map + " with the game rule: " + rule)
        game_link = game.map_generator(user_map, rule)
        await ctx.send("Enjoy the game! " + game_link)          
    else:
        await ctx.send("Uh oh! Game link could not be generated based on your input. Reference -help for help!")
        ctx.command.reset_cooldown(ctx)

#Error Checking
""" @client.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Invalid command! Please check -help for all available GeoGuessr bot commands!")

    if isinstance(error, CommandOnCooldown):
        await ctx.send(f"Slow down! Use the bot in {error.retry_after:,.2f} seconds!")

@geo.error
async def geo_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("You forgot to add a required option! Remember the format is -geo [map] [game rule]")
        ctx.command.reset_cooldown(ctx) """



game = GeoGuessorBot()
game.login()
print("Game Installed")
client.run(TOKEN)