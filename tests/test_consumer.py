import pytest
from channels.testing import WebsocketCommunicator
from core.asgi import application


@pytest.mark.asyncio
async def test_price_consumer():
    """
    Тестирование подключения к WebSocket
    """
    communicator = WebsocketCommunicator(application, "/ws/prices/")
    connected, _ = await communicator.connect()
    assert connected
    await communicator.disconnect()
