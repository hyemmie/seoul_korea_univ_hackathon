from django.contrib import admin

from building.models import Building, Review, Live

# Register your models here.
admin.site.register(Building),
admin.site.register(Review),
admin.site.register(Live),