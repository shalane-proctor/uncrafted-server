from django.db import models
from .user import User


class Post(models.Model):

    posted_by_user = models.ForeignKey(
        User, related_name='user1', on_delete=models.CASCADE)
    owner_profile = models.ForeignKey(
        User, related_name='user2', on_delete=models.CASCADE)
    item_name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    amount = models.CharField(max_length=50)
    image_url = models.URLField(max_length=200)
    trade_preferences = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    is_draft = models.BooleanField(default=False)
    is_pending = models.BooleanField(default=False)
    objects = models.Manager()

    def __str__(self):
        return self.item_name
