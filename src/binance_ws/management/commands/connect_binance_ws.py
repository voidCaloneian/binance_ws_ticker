import asyncio
import json
import logging
from decimal import Decimal
import websockets
from asgiref.sync import sync_to_async

from django.core.management import BaseCommand
from channels.layers import get_channel_layer

from api.models import Ticker

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
BINANCE_WS_URL = "wss://stream.binance.com:9443/ws/btcusdt@trade"


class Command(BaseCommand):
    """
    Команда для подключения к Binance WebSocket и обработки данных
    """

    help = "Подключается к Binance WebSocket и обрабатывает данные"

    def handle(self, *args, **kwargs):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.listen_binance())

    async def listen_binance(self):
        """
        Подключение к Binance WebSocket и обработка данных
        """
        channel_layer = get_channel_layer()
        last_ticker = None

        async with websockets.connect(BINANCE_WS_URL) as ws:
            logger.info("Подключение к **Binance WS** установлено")

            async def receive_messages():
                nonlocal last_ticker
                while True:
                    try:
                        message = await ws.recv()
                        data = json.loads(message)
                        price = Decimal(data.get("p", "0"))
                        symbol = data.get("s", "BTCUSDT")
                        # Обновляем last_ticker последними данными
                        last_ticker = {
                            "symbol": symbol,
                            "price": price,
                            "trade_time": data.get("T"),
                        }
                        payload = {
                            "symbol": symbol,
                            "price": str(price),
                            "trade_time": data.get("T"),
                        }
                        await channel_layer.group_send(
                            "prices",
                            {"type": "send_price_update", "data": json.dumps(payload)},
                        )
                    except Exception as e:
                        logger.error(f"Ошибка: {e}")
                        await asyncio.sleep(1)

            async def save_ticker_periodically():
                nonlocal last_ticker
                while True:
                    await asyncio.sleep(60)
                    if last_ticker:
                        # Сохраняем актуальный тикет раз в минуту
                        await sync_to_async(Ticker.objects.create)(
                            symbol=last_ticker["symbol"],
                            price=last_ticker["price"],
                        )
                        logger.info("Сохранён тикет")

            await asyncio.gather(receive_messages(), save_ticker_periodically())
