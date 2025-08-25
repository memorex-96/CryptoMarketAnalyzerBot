from pycoingecko import CoinGeckoAPI
import numpy as np 
import math 


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
def normalize(r_series): return 0 # place-holder 
    
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
         
    
         