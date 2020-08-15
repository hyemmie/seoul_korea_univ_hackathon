from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50, blank=True)
    region = models.CharField(max_length=50, blank=True)
    building = models.CharField(max_length=50, blank=True)
    isAuth = models.BooleanField(default=False)

    def __str__(self):
        return self.nickname
