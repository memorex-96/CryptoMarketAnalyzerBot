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


# Daily Market Data Announcement 



# commands
@bot.command() 
async def cmd_help(ctx): 
    help_text = ( 
        "Welcome to the Crypto Market Analyzer Bot!\n", 
        "Here are the commands you can use: \n", 
        "/cmd_help - Show this help message\n",
        "/lookup <coin_name> - Get the current price of a cryptocurrency in USD\n",
        "To be added:\n", 
        "/project <coin_name> <amount> <timeframe> - Get coin investment details over a specified timeframe\n",   
    )
    await ctx.reply("".join(help_text))

 
@bot.command()          # need to fix, give parse JSON for coin profile, read docs  
async def lookup(ctx, coin:str): 
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

# /project command 
# access another file for mathmatical calculations 

bot.run(token, log_handler=handler, log_level=logging.DEBUG) 

