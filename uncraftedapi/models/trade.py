from django.db import models
from .user import User


class Post(models.Model):

    user_of_wanted = models.ForeignKey(User, on_delete=models.CASCADE)
    user_of_offered = models.ForeignKey(User, on_delete=models.CASCADE)
    item_wanted = models.ForeignKey(User, on_delete=models.CASCADE)
    item_offered = models.ForeignKey(User, on_delete=models.CASCADE)
    is_pending = models.BooleanField(default=True)
    objects = models.Manager()
