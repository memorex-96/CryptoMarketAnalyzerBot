import discord 
from discord.ext import commands, tasks
import logging 
from dotenv import load_dotenv
import os
from pycoingecko import CoinGeckoAPI
from datetime import datetime 
from market_scraper import get_coin_data
#from math_models import projections  ; going to be openai implementation
#from math_models import print_analysis 
from openai import OpenAI

# going to need prompting and processing. not sure where to separate it 
#from llama_cpp import Llama 
from pathlib import Path 
import json 

load_dotenv()

''' going to use llama, open source  
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
response = client.responses.create( 
    model="gpt-4.1-mini", 
    input="Write a one sentence summary about cryptocurrency market trends." 
)
print(response.output_text)
'''


cg = CoinGeckoAPI() 

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
@tasks.loop(seconds=1)
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
            await channel.send("Good morning! Here is your daily crypto market update.\n") 
            #embed data here, maybe use a function to get market data 
            btc = get_coin_data("BitCoin")
            ADA = get_coin_data("Cardano")
            XRP = get_coin_data("XRP")
            HBAR = get_coin_data("Hedera") 
            # add more if necessary (make it so if coins get more popular, they get automatically announced) 
            # Change this to one embed
            # convert to correct format 
            if btc: 
                btc_embed = discord.Embed(
                    title=f"{btc['name']} ({btc['symbol'].upper()})", 
                    description=f"Rank #{btc['market_cap_rank']}"
                )
                btc_embed.add_field(name='Price', value=f"${btc['current_price']:.2f}", inline=True)
                btc_embed.add_field(name='24h Change', value=f"{btc['price_change']}%", inline=True)
                btc_embed.add_field(name='Trend', value=btc['trend'], inline=True) 
                await channel.send(embed=btc_embed)
            if ADA: 
                ada_embed = discord.Embed(
                    title=f"{ADA['name']} ({ADA['symbol'].upper()})", 
                    description=f"Rank #{ADA['market_cap_rank']}"
                )
                ada_embed.add_field(name='Price', value=f"${btc['current_price']:.2f}", inline=True)
                ada_embed.add_field(name='24h Change', value=f"{btc['price_change']}%", inline=True)
                ada_embed.add_field(name='Trend', value=btc['trend'], inline=True) 
                await channel.send(embed=ada_embed) 
           
           # remove/fix, they are not recognized in CoinGecko  
            
            if XRP: 
                xrp_embed = discord.Embed(
                    title=f"{XRP['name']} ({XRP['symbol'].upper()})", 
                    description=f"Rank #{ADA['market_cap_rank']}"
                )
                xrp_embed.add_field(name='Price', value=f"${btc['current_price']:.2f}", inline=True)
                xrp_embed.add_field(name='24h Change', value=f"{btc['price_change']}%", inline=True)
                xrp_embed.add_field(name='Trend', value=btc['trend'], inline=True) 
                await channel.send(embed=xrp_embed) 
            if HBAR: 
                hbar_embed = discord.Embed(
                    title=f"{HBAR['name']} ({HBAR['symbol'].upper()})", 
                    description=f"Rank #{HBAR['market_cap_rank']}"
                )
                hbar_embed.add_field(name='Price', value=f"${btc['current_price']:.2f}", inline=True)
                hbar_embed.add_field(name='24h Change', value=f"{btc['price_change']}%", inline=True)
                hbar_embed.add_field(name='Trend', value=btc['trend'], inline=True) 
                await channel.send(embed=hbar_embed) 
                
            

# commands
@bot.command() 
async def cmd_help(ctx): 
    help_text = ( 
        "Welcome to the Crypto Market Analyzer Bot!\n", 
        "Here are the commands you can use: \n", 
        "/cmd_help - Show this help message\n",
        "/lookup <coin_name> - Get the current price of a cryptocurrency in USD\n",
        "\n**To be implemented with OpenAI:**\n", 
        "/project <coin_name> <amount> <timeframe> - Get coin investment details over a specified timeframe\n",   
    )
    await ctx.reply("".join(help_text))

 
@bot.command()            
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
'''
@bot.command() 
async def project(ctx, coin:str, amount, timescale): 
   temp = projections(coin, amount, timescale) 
   ctx.send(temp)  
'''
  
bot.run(token, log_handler=handler, log_level=logging.DEBUG) 
