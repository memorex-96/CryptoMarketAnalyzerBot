from pycoingecko import CoinGeckoAPI
import numpy as np 
import math 
from openai import OpenAI 
import os 
from llamma_cpp import Llama
from pathlib import Path
import json 
'''
    Turn Math Models into Open AI area for usibng GPT to help with analysis and predictions
'''


# TODO: get input from user, and use openai to generate anaylsis based on that input
#   Way to do that is to just use func params as user input, and format into prompt for openai

# function: coin info from coingecko, convert to json for llama 
# use llama in this file and not main 


#resolve llama model path
BASE_DIR = Path(__file__).resolve().parent 
MODEL_PATH = BASE_DIR / "models" / "REPLACE_WITH_MODEL.gguf"    # rememebr to replace with model when downloaded  

llm = Llama(
    model_path=str(MODEL_PATH), 
    n_ctx=2048,
    n_threads=os.cpu_count() // 2   
)



# to be deleted and turned into openai implementation
'''
# functions for projection calculation pipeline 

#coin_prices arg = arr of prices not dict 
def log_returns(coin_prices): 
    # r_t = ln({P_t}/{P_{t-1}})
    log_return = 0  
     
    for i in coin_prices: 
        if i == 0:               
            curr = coin_prices[i] 
            continue 
        curr = temp              
        curr = coin_prices[i]    
        
        log_return[i] = np.log(curr / temp)
              
    return log_return   

#Normalize Z-Score
def normalize(r_series): 
    z_score = 0
    r_mean = np.mean(r_series) 
    r_series_dev = np.standard_deviation(r_series) 
    for i in r_series: 
        z_score = ((r_series[i] - r_mean) / r_series_dev) 
    return 0 # place-holder 
    
# ADF 
def stationary_check(r_series): return 0 # place-holder 

#Smoothig for trend estimation 
def EMA(r_series): return 0 # place-holder 

# Volatility Measurement (standard dev)
def standard_deviation(r_series): return 0 # place-holder 


def projections(coin: str, inv_amt, timeframe):
    cd = CoinGeckoAPI() 
    coin = cd.get_coin_by_id(coin.lower())
    try:
        # need to get history of prices for a coin
        print("Placeholder, calculating return")
    except Exception as e:
        print(f"Error fetching data for {coin}. Message: {e}")
        return None  
         
    
'''       