# gets embed data from CoinGecko API 
from pycoingecko import CoinGeckoAPI

def get_coin_data(coin: str): 
    cd = CoinGeckoAPI()
   # format for retrieval information:  
   # Crypto Daily Market Update:
   #- XRP: $0.50, (^ 2.3%) | Projected bullish next 7 days 
   #- ADA: $0.29, (\downarrow 1.1%) | projected neutral  
   #- HBAR: $0.06, (\uparrow 4.8%) | Strong bullish trend   
     
    try: 
        #get data 
        coin_data = cd.get_coin_by_id(coin.lower())
        name = coin_data['name'] 
        symbol = coin_data['symbol'].upper() 
        current_price = coin_data['market_data']['current_price']['usd']
        trend = coin_data['market_data']['trend_24h']  
        price_change = coin_data['market_data']['price_change_percentage_24h'] 
        
    except Exception as e: 
        print(f"Error fetching data for {coin}: {e}") 
        return None
    