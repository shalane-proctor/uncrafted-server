from django.db import models
from .user import User


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    message_content = models.CharField(max_length=1000)
    is_new = models.BooleanField(default=False)
    connected_to_trade = models.BooleanField(default=False)

    def __str__(self):
        return self.subject
