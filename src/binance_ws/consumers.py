import json
from channels.generic.websocket import AsyncWebsocketConsumer


class PriceConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("prices", self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard("prices", self.channel_name)

    async def send_price_update(self, event):
        await self.send(text_data=event["data"])
