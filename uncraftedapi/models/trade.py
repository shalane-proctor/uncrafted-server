from django.db import models
from .user import User
from .post import Post

class Trade(models.Model):
    trade_by_user = models.ForeignKey(
        User, related_name='tradeuser', on_delete=models.CASCADE)
    item_wanted = models.ForeignKey(
        Post, related_name='post1', on_delete=models.CASCADE)
    item_offered = models.ForeignKey(
        Post, related_name='post2', on_delete=models.CASCADE)
    is_pending = models.BooleanField(default=True)
    objects = models.Manager()
