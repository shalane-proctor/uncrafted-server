from django.db import models
from .message import Message
from .trade import Trade


class TradeMessage(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    trade = models.ForeignKey(Trade, on_delete=models.CASCADE)

    def __str__(self):
        return self.trade_message
