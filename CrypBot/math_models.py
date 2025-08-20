from pycoingecko import CoinGeckoAPI
import numpy as np 
import math 


# functions for projection calculation pipeline 

#coin_prices arg = dictionary
def log_returns(coin_prices): return 0 # place-holder  

#Normalize Z-Score
def normalize(r_series): return 0 # place-holder 

# ADF 
def stationary_check(r_series): return 0 # place-holder 

#Smoothig for trend estimation 
def EMA(r_series): return 0 # place-holder 

# Volatility Measurement (standard dev)
def standard_deviation(r_series): return 0 # place-holder 


def projections(coin: str, inv_amt, timeframe):
    #build the output here 
    print("This function will calculate invesment return projection")  