import discord
import pyjokes
import joke.quotes
from discord.ext import commands
from pyrandmeme import *

client = commands.Bot(command_prefix=".l ")
@client.event
async def on_ready():
    print("Bot is ready")
@client.command()
async def server(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)

    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(
        title=name + " Server Information",
        description=description,
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)

    await ctx.send(embed=embed)

@client.command()
async def hi(ctx):
    await ctx.send("Hi im Luraj")
@client.command()
async def joke(ctx):
    await ctx.send(pyjokes.get_joke())
@client.command()
async def meme(ctx):
    await ctx.send(embed=await pyrandmeme())
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round (bot.latency * 1000)}ms ')



client.run("ODQwODYwOTU4NDA1NTU4MzAy.YJeWyg.wqw9TUN6oIrVG6pFonKrjtFUp1U")






