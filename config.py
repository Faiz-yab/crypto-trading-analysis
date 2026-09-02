import os
from dotenv import load_dotenv

load_dotenv()

# Telegram Configuration
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

# MEXC Configuration
MEXC_API_KEY = os.getenv('MEXC_API_KEY')
MEXC_API_SECRET = os.getenv('MEXC_API_SECRET')

# Analysis Configuration
TIMEFRAMES = ['15m', '1h', '4h', '1d']
EMA_PERIODS = [9, 21, 50, 200]

# Technical Analysis Parameters
SUPPORT_RESISTANCE_LOOKBACK = 20
FVG_THRESHOLD = 0.002  # 0.2% for FVG
SMC_LOOKBACK = 50

# Telegram Settings
MESSAGE_LIMIT = 4096  # Telegram message character limit