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
async def ping(ctx):
    await ctx.send("ponggggg!!!")
@client.command()
async def hi(ctx):
    await ctx.send("Hi im Luraj")
@client.command()
async def pp(ctx):
    await ctx.send("8==============================================D")
@client.command()
async def joke(ctx):
    await ctx.send(pyjokes.get_joke())
@client.command()
async def meme(ctx):
    await ctx.send(embed=await pyrandmeme())


client.run("ODQwODYwOTU4NDA1NTU4MzAy.YJeWyg.wqw9TUN6oIrVG6pFonKrjtFUp1U")






