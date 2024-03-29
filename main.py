import discord
from discord.ext import commands
import asyncio
import tokenID as token #create a file named tokenID.py and write TOKEN
import dexscreenerAPI 
import time


TOKEN = token.TOKEN
dex = dexscreenerAPI.DexScreenerAPI()
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

durum = False

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user.name}')


commands = ["p", "ss", "selamla", "join", "play"]

@bot.command()
async def fonksiyonlar(ctx):
    for i in commands:
        await ctx.send(i)

@bot.command()
async def coin(ctx):
    global durum
    if durum:
        durum = False
    else:
        durum = True
    print(durum)

    while durum == False:
        price = dex.get_price_data()    
        if temp_price < price:
            print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
            await ctx.send(f"Price: {ctx.author.mention}")
        elif temp_price > price:
            print("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
            await ctx.send(f"Price: {ctx.author.mention}")
        temp_price = price
        time.sleep(1)



@bot.command()
async def ss(ctx):
    global durum
    if durum:
        durum = False
    else:
        durum = True
    print(durum)

@bot.command()
async def selamla(ctx):
    await ctx.send(f"Selam, {ctx.author.mention}")

@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()


# Botu başlatma
bot.run(TOKEN)
