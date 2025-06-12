from django.contrib import admin
from .models import Location, LocationImage, Facility, Category

admin.site.register(Location)
admin.site.register(LocationImage)
admin.site.register(Facility)
admin.site.register(Category)