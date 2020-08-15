from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    region = models.CharField(max_length=50)
    isAuth = models.BooleanField(default=False)




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