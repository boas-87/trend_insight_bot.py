import asyncio
from telegram import Bot
from datetime import datetime
import os

TELEGRAM_BOT_TOKEN = os.environ["TREND_BOT_TOKEN"]
TELEGRAM_CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

def get_trend_insight():
    today = datetime.now().strftime("%Y-%m-%d")
    return f"""📊 {today} 트렌드 인사이트 큐레이션

📌 경제
- 글로벌 금리 및 환율 흐름 요약
- 주요 증시 체크 포인트

📚 도서
- 최근 주목받는 인문·경제 도서 키워드

🎨 미술
- 국내외 전시·미술계 트렌드 한 줄 요약
"""

async def send_telegram_message(msg):
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=msg)

if __name__ == "__main__":
    asyncio.run(send_telegram_message(get_trend_insight()))
