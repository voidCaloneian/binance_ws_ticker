from django.urls import path
from api.views import TickerHistoryView

urlpatterns = [
    path("tickers/", TickerHistoryView.as_view(), name="ticker-history"),
]
