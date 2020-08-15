from django.contrib import admin
from app.models import Profile, Rental, Comment
# Register your models here.
admin.site.register(Profile)
admin.site.register(Rental)
admin.site.register(Comment)