from django.db import models
from django.contrib.auth.models import User
from app.models import Profile
from django.dispatch import receiver

# Create your models here.
class Building(models.Model):
    residents = models.ManyToManyField(Profile, blank=True, related_name="residences", through='Live')
    name = models.CharField(max_length=15)
    location_str = models.CharField(max_length=50)
    loc_latitude = models.FloatField()
    loc_longitude = models.FloatField()
    score = models.FloatField()

    def __str__(self):
        return 'loc: %s / score: %s' % (self.location_str, self.score)


class BuildingScore(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    evaluated_by = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField() 


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    content = models.CharField(max_length=30, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Live(models.Model):
    residence = models.ForeignKey(Profile, on_delete=models.CASCADE)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s lives in %s' % (self.residence.username, self.building)