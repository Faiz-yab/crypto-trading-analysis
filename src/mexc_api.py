import ccxt
import pandas as pd
from config import MEXC_API_KEY, MEXC_API_SECRET

class MexcAPI:
    def __init__(self):
        """Initialize MEXC exchange"""
        self.exchange = ccxt.mexc({
            'apiKey': MEXC_API_KEY,
            'secret': MEXC_API_SECRET,
            'enableRateLimit': True,
        })
    
    def get_ohlcv(self, symbol, timeframe='1h', limit=100):
        """Fetch OHLCV data from MEXC"""
        try:
            ohlcv = self.exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
            df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
            df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
            return df
        except Exception as e:
            print(f"Error fetching OHLCV data: {e}")
            return None
    
    def get_ticker(self, symbol):
        """Get current ticker information"""
        try:
            ticker = self.exchange.fetch_ticker(symbol)
            return ticker
        except Exception as e:
            print(f"Error fetching ticker: {e}")
            return None
    
    def get_symbols(self):
        """Get all available trading symbols"""
        try:
            markets = self.exchange.load_markets()
            return list(markets.keys())
        except Exception as e:
            print(f"Error fetching symbols: {e}")
            return []
    
    def validate_symbol(self, symbol):
        """Validate if symbol exists on MEXC"""
        try:
            markets = self.exchange.load_markets()
            return symbol in markets
        except Exception as e:
            print(f"Error validating symbol: {e}")
            return False