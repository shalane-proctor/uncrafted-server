from django.db import models
from .user import Message
from .trade import Trade


class Message(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    trade = models.ForeignKey(Trade, on_delete=models.CASCADE)

    def __str__(self):
        return self.message
