from django.db import models
from django.conf import settings
from locations.models import Location

class Schedule(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    adults = models.PositiveIntegerField(default=1)
    children = models.PositiveIntegerField(default=0)
    babies = models.PositiveIntegerField(default=0)
    rental_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    service_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    payment_status = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.user} - {self.location} ({self.start_date} to {self.end_date})"
