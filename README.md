# 🚀 Crypto Trading Analysis Bot

A comprehensive cryptocurrency trading analysis tool with Telegram bot integration. Get real-time technical analysis for any cryptocurrency on MEXC exchange.

## ✨ Features

### Technical Analysis
- **Support & Resistance Levels** - Across 15m, 1h, 4h, and daily timeframes
- **EMA Indicators** - 9, 21, 50, and 200 period EMAs
- **Fair Value Gaps (FVG)** - Identify bullish and bearish gaps
- **Smart Money Concepts (SMC)** - Swing highs/lows and breaker levels
- **RSI Analysis** - Relative Strength Index for overbought/oversold conditions
- **Price Action Analysis** - Real-time price movements

### Integration
- **Telegram Bot** - Easy-to-use Telegram interface
- **MEXC Exchange API** - Real-time data from MEXC
- **Multi-Timeframe Analysis** - Analyze 15m, 1h, 4h, 1d simultaneously

## 📋 Requirements

- Python 3.8+
- MEXC Account (for API keys)
- Telegram Bot Token (create via @BotFather)

## 🔧 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Faiz-yab/crypto-trading-analysis.git
cd crypto-trading-analysis
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Setup Environment Variables
```bash
cp .env.example .env
```

Edit `.env` and add your credentials:
```
TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_CHAT_ID=your_chat_id_here
MEXC_API_KEY=your_mexc_api_key_here
MEXC_API_SECRET=your_mexc_api_secret_here
```

### 4. Get Required Credentials

#### Telegram Bot Token
1. Open Telegram and chat with @BotFather
2. Send `/newbot`
3. Follow the instructions to create a new bot
4. Copy the bot token to `.env`

#### MEXC API Keys
1. Login to [MEXC](https://www.mexc.com)
2. Go to Account > API Management
3. Create new API key
4. Copy API Key and Secret to `.env`

#### Telegram Chat ID
1. Chat with @userinfobot on Telegram
2. Send any message and get your Chat ID
3. Add to `.env`

## 🚀 Usage

### Start the Bot
```bash
python main.py
```

### Telegram Commands

```
/start - Welcome message and instructions
/analyze BTC/USDT - Get full technical analysis
/symbols - List popular trading pairs
/help - Show help information
```

### Examples

```
/analyze BTC/USDT
/analyze ETH/USDT
/analyze SOL/USDT
/analyze DOGE/USDT
```

Or just send the coin name:
```
BTC - Analyzes BTC/USDT
ETH - Analyzes ETH/USDT
```

## 📊 Analysis Components

### Price Action
- Current price
- Previous price
- Percentage change
- Trend direction (📈 UP / 📉 DOWN)

### Support & Resistance
- Main support level
- Main resistance level
- Multiple level identification

### EMA Indicators
- EMA 9 (Fast)
- EMA 21 (Medium)
- EMA 50 (Medium-Slow)
- EMA 200 (Slow - Trend)

### Fair Value Gaps
- Bullish FVG detection
- Bearish FVG detection
- Gap levels and timestamps

### Smart Money Concepts
- Recent swing highs
- Recent swing lows
- Breaker level identification

### RSI Indicator
- RSI 14 value
- Overbought (>70) warning
- Oversold (<30) warning
- Neutral zone indication

## 📁 Project Structure

```
crypto-trading-analysis/
├── main.py                      # Entry point
├── config.py                    # Configuration settings
├── requirements.txt             # Python dependencies
├── .env.example                # Environment variables template
├── README.md                   # This file
└── src/
    ├── __init__.py
    ├── mexc_api.py            # MEXC exchange integration
    ├── technical_analysis.py  # Technical analysis engine
    ├── telegram_bot.py        # Telegram bot implementation
    └── message_formatter.py   # Message formatting for Telegram
```

## 🔐 Security

⚠️ **Important:**
- Never commit `.env` file to repository
- Keep your API keys and bot token secret
- Use read-only API keys if possible
- Rotate API keys regularly

## 🛠️ Configuration

Edit `config.py` to customize:

```python
# Timeframes for analysis
TIMEFRAMES = ['15m', '1h', '4h', '1d']

# EMA periods
EMA_PERIODS = [9, 21, 50, 200]

# Support/Resistance lookback period
SUPPORT_RESISTANCE_LOOKBACK = 20

# FVG threshold (0.2% by default)
FVG_THRESHOLD = 0.002

# SMC lookback period
SMC_LOOKBACK = 50
```

## 📝 API Reference

### MexcAPI Class
```python
from src.mexc_api import MexcAPI

mexc = MexcAPI()

# Fetch OHLCV data
df = mexc.get_ohlcv('BTC/USDT', '1h', limit=100)

# Get current ticker
ticker = mexc.get_ticker('BTC/USDT')

# List all symbols
symbols = mexc.get_symbols()

# Validate symbol
is_valid = mexc.validate_symbol('BTC/USDT')
```

### TechnicalAnalysis Class
```python
from src.technical_analysis import TechnicalAnalysis

ta = TechnicalAnalysis(df)

# Get complete analysis
analysis = ta.get_all_analysis()

# Individual analyses
emas = ta.add_all_emas()
sr = ta.find_support_resistance()
fvg = ta.find_fvg()
smc = ta.find_smc_levels()
rsi = ta.calculate_rsi()
```

## 🐛 Troubleshooting

### "TELEGRAM_BOT_TOKEN not found"
- Check `.env` file exists
- Verify token is copied correctly
- Ensure no spaces around the token

### "Symbol not found on MEXC"
- Use `/symbols` to see available pairs
- Most pairs are in format: COIN/USDT
- Check MEXC website for available trading pairs

### "API Authentication Failed"
- Verify API Key and Secret are correct
- Check API key has appropriate permissions
- Ensure API key is enabled on MEXC

### No data returned
- Ensure cryptocurrency pair exists
- Check MEXC API status
- Verify internet connection
- Try with a different timeframe

## 🚀 Future Enhancements

- [ ] Multiple exchange support (Binance, Kraken, etc.)
- [ ] Alert system for specific conditions
- [ ] Backtesting functionality
- [ ] Advanced charting
- [ ] Signal notifications
- [ ] Database for historical analysis
- [ ] Web dashboard
- [ ] Discord bot integration
- [ ] Advanced SMC pattern recognition
- [ ] AI-powered predictions

## 📄 License

MIT License - feel free to use this project for personal and commercial purposes.

## ⚠️ Disclaimer

**This tool is for educational purposes only.** 

- Not financial advice
- Past performance doesn't guarantee future results
- Cryptocurrency trading carries high risk
- Always do your own research (DYOR)
- Only trade with money you can afford to lose

## 💬 Support

For issues, questions, or suggestions:
1. Check existing issues on GitHub
2. Open a new GitHub issue
3. Contact the developer

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests
- Improve documentation

## 👨‍💻 Developer

Created with ❤️ for crypto traders

---

**Start analyzing crypto like a pro! 🚀**
