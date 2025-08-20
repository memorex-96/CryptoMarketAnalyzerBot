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
        trend = coin_data['market_data'].get('trend_24h', 'N/A') 
        price_change = coin_data['market_data']['price_change_percentage_24h'] 
        market_cap_rank = coin_data['market_data']['market_cap_rank'] 
        #embed_result = [name, symbol, current_price, trend, price_change, market_cap_rank]
        
        return {
            "name" : name, 
            "symbol" : symbol, 
            "current_price" : current_price, 
            "trend" : trend, 
            "price_change" : price_change, 
            "market_cap_rank" : market_cap_rank
        }    
         
    except Exception as e: 
        print(f"Error fetching data for {coin}: {e}") 
        return None
    