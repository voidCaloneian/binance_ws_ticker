from django.urls import re_path
from binance_ws.consumers import PriceConsumer

websocket_urlpatterns = [
    re_path(r"ws/prices/$", PriceConsumer.as_asgi()),
]
