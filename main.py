#!/usr/bin/env python3
import os
import sys
from dotenv import load_dotenv

load_dotenv()

required_vars = ['TELEGRAM_BOT_TOKEN', 'MEXC_API_KEY', 'MEXC_API_SECRET']
missing = [v for v in required_vars if not os.getenv(v)]

if missing:
    print(f"❌ Missing: {', '.join(missing)}")
    print("\n📝 Create .env from .env.example")
    sys.exit(1)

from src.telegram_bot import start_bot

if __name__ == '__main__':
    print("="*60)
    print("🚀 Crypto Trading Analysis Bot")
    print("="*60)
    print("\n✅ Environment loaded")
    print("🤖 Starting bot...")
    print("\nCommands: /start, /analyze BTC/USDT, /symbols, /help")
    print("\n" + "="*60)
    try:
        start_bot()
    except KeyboardInterrupt:
        print("\n👋 Bot stopped")
        sys.exit(0)