import pandas as pd
import numpy as np
from ta.momentum import RSIIndicator
from config import EMA_PERIODS, SUPPORT_RESISTANCE_LOOKBACK, FVG_THRESHOLD

class TechnicalAnalysis:
    def __init__(self, df):
        self.df = df.copy()
        self.df = self.df.reset_index(drop=True)
    
    def calculate_ema(self, period):
        return self.df['close'].ewm(span=period, adjust=False).mean()
    
    def add_all_emas(self):
        for period in EMA_PERIODS:
            self.df[f'EMA_{period}'] = self.calculate_ema(period)
        return self.df
    
    def find_support_resistance(self):
        high = self.df['high'].tail(SUPPORT_RESISTANCE_LOOKBACK)
        low = self.df['low'].tail(SUPPORT_RESISTANCE_LOOKBACK)
        
        resistance = high.max()
        support = low.min()
        
        resistances = sorted(high.nlargest(3).values, reverse=True)
        supports = sorted(low.nsmallest(3).values)
        
        return {'main_resistance': resistance, 'main_support': support, 'resistance_levels': resistances, 'support_levels': supports}
    
    def find_fvg(self):
        fvgs = []
        for i in range(2, len(self.df) - 1):
            if self.df.loc[i, 'low'] > self.df.loc[i-2, 'high']:
                gap_size = self.df.loc[i, 'low'] - self.df.loc[i-2, 'high']
                if gap_size > self.df.loc[i, 'close'] * FVG_THRESHOLD:
                    fvgs.append({'type': 'Bullish', 'top': self.df.loc[i, 'low'], 'bottom': self.df.loc[i-2, 'high'], 'candle': i, 'timestamp': self.df.loc[i, 'timestamp']})
            
            if self.df.loc[i, 'high'] < self.df.loc[i-2, 'low']:
                gap_size = self.df.loc[i-2, 'low'] - self.df.loc[i, 'high']
                if gap_size > self.df.loc[i, 'close'] * FVG_THRESHOLD:
                    fvgs.append({'type': 'Bearish', 'top': self.df.loc[i-2, 'low'], 'bottom': self.df.loc[i, 'high'], 'candle': i, 'timestamp': self.df.loc[i, 'timestamp']})
        return fvgs
    
    def find_smc_levels(self):
        smc = {'highs': [], 'lows': [], 'broken_levels': []}
        for i in range(1, len(self.df) - 1):
            if self.df.loc[i, 'high'] > self.df.loc[i-1, 'high'] and self.df.loc[i, 'high'] > self.df.loc[i+1, 'high']:
                smc['highs'].append({'price': self.df.loc[i, 'high'], 'index': i, 'timestamp': self.df.loc[i, 'timestamp']})
            
            if self.df.loc[i, 'low'] < self.df.loc[i-1, 'low'] and self.df.loc[i, 'low'] < self.df.loc[i+1, 'low']:
                smc['lows'].append({'price': self.df.loc[i, 'low'], 'index': i, 'timestamp': self.df.loc[i, 'timestamp']})
        return smc
    
    def calculate_rsi(self, period=14):
        rsi = RSIIndicator(close=self.df['close'], window=period)
        return rsi.rsi()
    
    def get_price_action(self):
        current = self.df.iloc[-1]['close']
        previous = self.df.iloc[-2]['close']
        change = ((current - previous) / previous) * 100
        return {'current_price': current, 'previous_price': previous, 'change_percent': change, 'direction': '📈 UP' if change > 0 else '📉 DOWN'}
    
    def get_all_analysis(self):
        self.add_all_emas()
        analysis = {
            'price_action': self.get_price_action(),
            'support_resistance': self.find_support_resistance(),
            'fvg': self.find_fvg(),
            'smc': self.find_smc_levels(),
            'rsi': self.calculate_rsi().iloc[-1],
            'latest_candle': {'open': self.df.iloc[-1]['open'], 'high': self.df.iloc[-1]['high'], 'low': self.df.iloc[-1]['low'], 'close': self.df.iloc[-1]['close'], 'volume': self.df.iloc[-1]['volume']},
            'emas': {period: self.df[f'EMA_{period}'].iloc[-1] for period in EMA_PERIODS}
        }
        return analysis