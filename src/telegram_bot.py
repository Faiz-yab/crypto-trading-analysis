import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from config import TELEGRAM_BOT_TOKEN, TIMEFRAMES, MESSAGE_LIMIT
from src.mexc_api import MexcAPI
from src.technical_analysis import TechnicalAnalysis
from src.message_formatter import MessageFormatter

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

class CryptoTradingBot:
    def __init__(self):
        self.mexc = MexcAPI()
        self.formatter = MessageFormatter()
        self.app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
        self.setup_handlers()
    
    def setup_handlers(self):
        self.app.add_handler(CommandHandler("start", self.start))
        self.app.add_handler(CommandHandler("help", self.help_command))
        self.app.add_handler(CommandHandler("analyze", self.analyze))
        self.app.add_handler(CommandHandler("symbols", self.list_symbols))
        self.app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))
    
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("🚀 Crypto Trading Analysis Bot\n\n✅ Support & Resistance (15m,1h,4h,1d)\n✅ EMA (9,21,50,200)\n✅ FVG & SMC\n✅ RSI\n\n/analyze BTC/USDT")
    
    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("/analyze <SYMBOL>\n/symbols\nOR just type: BTC, ETH, SOL")
    
    async def analyze(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if not context.args:
            await update.message.reply_text("❌ /analyze BTC/USDT")
            return
        
        symbol = context.args[0].upper()
        if not self.mexc.validate_symbol(symbol):
            await update.message.reply_text(f"❌ '{symbol}' not found")
            return
        
        status_msg = await update.message.reply_text(f"🔍 Analyzing {symbol}...")
        
        try:
            analysis_results = {}
            for timeframe in TIMEFRAMES:
                df = self.mexc.get_ohlcv(symbol, timeframe, limit=100)
                if df is not None:
                    ta = TechnicalAnalysis(df)
                    analysis_results[timeframe] = ta.get_all_analysis()
            
            if not analysis_results:
                await status_msg.edit_text(f"❌ Failed {symbol}")
                return
            
            formatted_message = self.formatter.format_analysis(symbol, analysis_results)
            
            if len(formatted_message) > MESSAGE_LIMIT:
                messages = self.formatter.split_message(formatted_message)
                await status_msg.delete()
                for msg in messages:
                    await update.message.reply_text(msg)
            else:
                await status_msg.edit_text(formatted_message)
        
        except Exception as e:
            await status_msg.edit_text(f"❌ Error: {str(e)}")
    
    async def list_symbols(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            symbols = self.mexc.get_symbols()
            popular = [s for s in symbols if any(coin in s for coin in ['BTC', 'ETH', 'BNB', 'SOL', 'XRP', 'DOGE'])][:15]
            message = "📈 Popular Pairs:\n\n" + "\n".join([f"{i}. {s}" for i, s in enumerate(popular, 1)])
            await update.message.reply_text(message)
        except Exception as e:
            await update.message.reply_text(f"❌ Error: {str(e)}")
    
    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        text = update.message.text.upper()
        for ending in ['/USDT', '/USDC', '/BNB']:
            symbol = f"{text}{ending}"
            if self.mexc.validate_symbol(symbol):
                context.args = [symbol]
                await self.analyze(update, context)
                return
        await update.message.reply_text(f"❌ Not found. Use /analyze <SYMBOL>")
    
    def run(self):
        logger.info("🤖 Bot started...")
        self.app.run_polling()

def start_bot():
    bot = CryptoTradingBot()
    bot.run()

if __name__ == '__main__':
    start_bot()