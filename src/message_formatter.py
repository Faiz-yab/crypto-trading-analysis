from config import MESSAGE_LIMIT

class MessageFormatter:
    def format_analysis(self, symbol, analysis_results):
        message = f"<b>📊 TECHNICAL ANALYSIS - {symbol}</b>\n"
        for timeframe, analysis in analysis_results.items():
            message += self.format_timeframe_analysis(timeframe, analysis)
            message += "\n" + "-" * 50 + "\n\n"
        message += "<i>⚠️ Educational purposes only. Not financial advice.</i>"
        return message
    
    def format_timeframe_analysis(self, timeframe, analysis):
        message = f"<b>⏱️ {timeframe.upper()}</b>\n\n"
        pa = analysis['price_action']
        message += f"<b>💹 Price:</b> ${pa['current_price']:.8f} ({pa['change_percent']:.2f}%) {pa['direction']}\n\n"
        
        sr = analysis['support_resistance']
        message += f"<b>🎯 S/R:</b>\nR: ${sr['main_resistance']:.8f}\nS: ${sr['main_support']:.8f}\n\n"
        
        emas = analysis['emas']
        message += f"<b>📈 EMA:</b> "
        for period in sorted(emas.keys()):
            message += f"{period}:${emas[period]:.8f} "
        message += "\n\n"
        
        message += f"<b>📊 RSI:</b> {analysis['rsi']:.2f}"
        if analysis['rsi'] > 70:
            message += " ⚠️ Overbought"
        elif analysis['rsi'] < 30:
            message += " ⚠️ Oversold"
        message += "\n"
        return message
    
    def split_message(self, message):
        parts = []
        current = ""
        for line in message.split('\n'):
            if len(current) + len(line) + 1 > MESSAGE_LIMIT:
                if current:
                    parts.append(current)
                current = line + "\n"
            else:
                current += line + "\n"
        if current:
            parts.append(current)
        return parts