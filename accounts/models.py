from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    coin = models.IntegerField(default=5000)
    nickname = models.CharField(max_length=32)