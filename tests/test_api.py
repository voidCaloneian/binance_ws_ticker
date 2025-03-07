from decimal import Decimal
import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from django.utils import timezone
from api.models import Ticker


@pytest.mark.django_db
def test_ticker_history_api():
    """
    Тестирование API для получения истории тикеров
    """
    Ticker.objects.create(  # pylint: disable=no-member
        symbol="BTCUSDT", price=Decimal("50000"), trade_time=timezone.now()
    )
    client = APIClient()
    url = reverse("ticker-history")
    response = client.get(url)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert data[0]["symbol"] == "BTCUSDT"
