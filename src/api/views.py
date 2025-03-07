from rest_framework import generics
from api.models import Ticker
from api.serializers import TickerSerializer


class TickerHistoryView(generics.ListAPIView):
    """
    Вьюха для получения истории тикеров
    """

    queryset = Ticker.objects.all().order_by("-trade_time")  # pylint: disable=no-member
    serializer_class = TickerSerializer
