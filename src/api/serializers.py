from rest_framework import serializers
from api.models import Ticker


class TickerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticker
        fields = ["id", "symbol", "price", "trade_time"]
