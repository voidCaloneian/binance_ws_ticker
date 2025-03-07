from django.db import models


class Ticker(models.Model):
    """
    Модель хранения данных о паре валют
    """

    symbol = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=20, decimal_places=10)
    trade_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.symbol}: {self.price} at {self.trade_time}"
