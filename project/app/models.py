from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50, blank=True)
    region = models.CharField(max_length=50, blank=True)
    building = models.CharField(max_length=50, blank=True)
    isAuth = models.BooleanField(default=False)
    
    def __str__(self):
        return 'name: %s' % (self.username)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Rental(models.Model):
    title=models.CharField(max_length =100)
    content = models.TextField(null=True)
    author=models.CharField(max_length=50,null=True)
    region = models.CharField(max_length=50,null=True)
    deadline = models.CharField(max_length = 20, null=True)
    left = models.CharField(max_length = 20, null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post=models.ForeignKey(Rental,on_delete=models.CASCADE, related_name='comments')
    content=models.TextField(null=True)
    author=models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.post