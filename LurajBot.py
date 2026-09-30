import asyncio
import os

import discord
import pyjokes
from discord.ext import commands
from pyrandmeme import pyrandmeme
import random

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix=".l ", intents=intents)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('Cake!'))
    print("Bot is ready")
   

@client.command()
@commands.guild_only()
async def server(ctx):
    guild = ctx.guild
    embed = discord.Embed(title=f"{guild.name} Server Information", color=discord.Color.blue())
    if guild.icon:
        embed.set_thumbnail(url=guild.icon.url)
    embed.add_field(name="Owner", value=str(guild.owner or guild.owner_id), inline=True)
    embed.add_field(name="Server ID", value=str(guild.id), inline=True)
    embed.add_field(name="Member Count", value=str(guild.member_count), inline=True)
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
    await ctx.send(f'Pong! {round (client.latency * 1000)}ms ')
@client.command()
@commands.max_concurrency(1, per=commands.BucketType.user, wait=False)
async def guess(ctx):
    await ctx.send("Guess a number from 1 to 10. You have 30 seconds.")
    def guess_check(message):
        return (message.author == ctx.author and message.channel == ctx.channel
                and message.content.isdigit() and 1 <= int(message.content) <= 10)
    try:
        response = await client.wait_for("message", check=guess_check, timeout=30)
    except asyncio.TimeoutError:
        await ctx.send("Time expired. Start a new game with .l guess.")
        return
    answer = random.randint(1, 10)
    await ctx.send("Correct!" if int(response.content) == answer else f"The answer was {answer}.")

quotes_1 = ["People often say that motivation doesn't last. Well, neither does bathing ﹘ that's why we recommend it daily.",

"Sales are contingent upon the attitude of the salesman ﹘ not the attitude of the prospect.",

"You can waste your lives drawing lines. Or you can live your life crossing them.",

"Always do your best. What you plant now, you will harvest later." ,

"Everyone lives by selling something.",

"Develop success from failures. Discouragement and failure are two of the surest stepping stones to success.",

"I’d rather regret the things I’ve done than regret the things I haven’t done.",

"Action is the foundational key to all success.",

"If you are not taking care of your customer, your competitor will.",

"The golden rule for every businessman is this: Put yourself in your customer's place.",

"Hire character. Train skill.",

"The secret of joy in work is contained in one word ﹘ excellence. To know how to do something well is to enjoy it.",

"Nothing is really work unless you would rather be doing something else.",

"Without a customer, you don’t have a business ﹘ all you have is a hobby.",

"To be most effective in sales today, it's imperative to drop your 'sales' mentality and start working with your prospects as if they've already hired you.",

"Formula for success: rise early, work hard, strike oil.",

"Pretend that every single person you meet has a sign around his or her neck that says, 'Make me feel important.' Not only will you succeed in sales, you will succeed in life.",

"Don't let the fear of losing be greater than the excitement of winning.",

"The difference between a successful person and others is not a lack of strength, not a lack of knowledge, but rather a lack of will.",

"Without hustle, talent will only carry you so far.",

"Working hard for something we don't care about is called stressed; working hard for something we love is called passion.",

"Move out of your comfort zone. You can only grow if you are willing to feel awkward and uncomfortable when you try something new.",

"Obstacles are those frightful things you see when you take your eyes off your goal.",

"It's not just about being better. It's about being different. You need to give people a reason to choose your business.",

"How dare you settle for less when the world has made it so easy for you to be remarkable?",

"Someday is not a day of the week.",

"If you cannot do great things, do small things in a great way.",

"Your time is limited, so don't waste it living someone else's life.",

"Being good in business is the most fascinating kind of art. Making money is art and working is art and good business is the best art.",

"Challenges are what make life interesting and overcoming them is what makes life meaningful.",

"Be patient with yourself. Self-growth is tender; it’s holy ground. There’s no greater investment.",]

@client.command()
async def quotes(ctx):
    await ctx.send(random.choice(quotes_1))


if __name__ == "__main__":
    token = os.environ.get("DISCORD_BOT_TOKEN")
    if not token:
        raise SystemExit("Set DISCORD_BOT_TOKEN before starting the bot.")
    client.run(token)
