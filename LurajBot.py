import discord
import pyjokes
import joke.quotes
from discord.ext import commands
from pyrandmeme import *
import random

client = commands.Bot(command_prefix=".l ")

@client.event
async def on_ready():
    print("Bot is ready")
@client.event
async def on_member_join(ctx):
    role = discord.utils.get(ctx.guild.roles, name="Members") #TODO
    await client.add_roles(member, role)

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
        description="A Server to Make Friends and have fun!",
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value="oGhostyyy", inline=True)
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
    await ctx.send(f'Pong! {round (client.latency * 1000)}ms ')
@client.command()
async def pp(ctx):
    pp_size = random.randint(1, 10)
    pps = discord.Embed(
        title = "pp size generator",
        description = "Your pp size: " + "8" + '=' * pp_size + "D",
        colour=discord.Colour.blue()
    )

    await ctx.send(embed = pps)
@client.command()
async def guess(ctx):
    await ctx.send("Guess the number from 1 to 10")
    def guess_check(m):
        return m.content.isdigit()
    guess = await client.wait_for('message')
    answer = random.randint(1, 10)
    if int(guess.content) == answer:
        await ctx.send('You are correct')
    else:
        await ctx.send('Sorry, it is actually {}.'.format(answer))

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

quote = random.choice(quotes_1)
@client.command()
async def quotes(ctx):
    await ctx.send(quote)


client.run("ODQwODYwOTU4NDA1NTU4MzAy.YJeWyg.wqw9TUN6oIrVG6pFonKrjtFUp1U")




