import discord 
from discord.ext import commands
import logging 
from dotenv import load_dotenv
import os
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI() 

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default() 
intents.message_content = True
intents.members = True 

bot = commands.Bot(command_prefix= '/', intents=intents) 

@bot.event
async def on_ready(): 
    print(f"We are ready to go, in {bot.user.name}!")  # modify 

# commands
@bot.command() 
async def cmd_help(ctx): 
    help_text = ( 
        "Welcome to the Crypto Market Analyzer Bot!\n", 
        "Here are the commands you can use: \n", 
        "/cmd_help - Show this help message\n"
        "/curr_price <coin_name> - Get the current price of a cryptocurrency in USD\n"   
    )
    await ctx.reply("".join(help_text))

 
@bot.command() 
async def curr_price(ctx, coin:str): 
    try:
        data = cg.get_price(ids=coin, vs_currencies='usd')
        if coin.lower() in data: 
            price = data[coin.lower()]['usd']
            await ctx.reply(f"The current price of {coin} is ${price:.2f} USD.") 
        else: 
            await ctx.reply(f"Could not find data for {coin}. Please check the coin name and try again.")  
    except Exception as e: 
        await ctx.reply(f"Error fetching coin data.")
        print(e) 

bot.run(token, log_handler=handler, log_level=logging.DEBUG) 

