import discord 
from discord.ext import commands, tasks
import logging 
from dotenv import load_dotenv
import os
from pycoingecko import CoinGeckoAPI
from datetime import datetime 
from market_scraper import get_coin_data
from math_models import projections  

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
    daily.start() 

# Daily Market Data Announcement 
@tasks.loop(minutes=1)
async def daily():
   # format for retrieval information:  
   # Crypto Daily Market Update:
   #- XRP: $0.50, (^ 2.3%) | Projected bullish next 7 days 
   #- ADA: $0.29, (\downarrow 1.1%) | projected neutral  
   #- HBAR: $0.06, (\uparrow 4.8%) | Strong bullish trend  
    
     
    now = datetime.now()
    if now.hour == 9 and now.minute == 0:
        print("Time hit!")  
        channel = bot.get_channel(1406712918590095421) 
        if channel: 
            await channel.send("Good morning! Here is your daily crypto market update.") 
            #embed data here, maybe use a function to get market data
    
 

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

 
@bot.command()          # need to fix, give parse JSON for coin profile, read docs, make embed   
async def lookup(ctx, coin:str): 
    try:
        
       c = cg.get_coin_by_id(coin.lower())
       embed = discord.Embed(
           title=f"{c["name"]} ({c["symbol"].upper()})",
           description=f"Rank #{c['market_cap_rank']}"
        )
        
       embed.add_field(name="Current Price (USD)", value=f"${c['market_data']['current_price']['usd']:.2f}", inline=False) 
       embed.add_field(name="Market Cap (USD)", value=f"${c["market_data"]['market_cap']['usd']:.2f}", inline=False) 
       embed.add_field(name="Price Change (24h)", value=f"{c['market_data']['price_change_percentage_24h']:.2f}%", inline=False)
       embed.add_field(name="All Time High (USD)", value=f"${c['market_data']['ath']['usd']:.2f}", inline=False) 
      
       await ctx.reply(embed=embed) 
       
    except Exception as e: 
        await ctx.reply(f"Error fetching coin data.")
        print(e) 

# /project command 
# access another file for mathmatical calculations 

bot.run(token, log_handler=handler, log_level=logging.DEBUG) 

