
from django.db import models
from django.conf import settings 

class Location(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='locations'
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    rating = models.FloatField()
    price = models.IntegerField()
    facilities = models.ManyToManyField('Facility')
    categories = models.ManyToManyField('Category')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class LocationImage(models.Model):
    location = models.ForeignKey(Location, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='location_images')

class Facility(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='facility_icons',null=True, blank=True)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name