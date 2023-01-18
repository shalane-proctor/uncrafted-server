from django.db import models

class User(models.Model):
    uid = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    about = models.CharField(max_length=1000)
    profile_image_url = models.URLField(max_length=200)
    instagram = models.URLField(max_length=200)
    etsy = models.URLField(max_length=200)

    def __str__(self):
        return self.username
