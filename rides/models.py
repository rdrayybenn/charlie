import random
from django.db import models
from django.conf import settings
from django.utils import timezone


class Ride(models.Model):
    STATUS_CHOICES = (
        ('created', 'Created'),
        ('assigned', 'Assigned'),
        ('dropped', 'Dropped'),
    )

    rider = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='rides_as_rider', null=True, blank=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='rides_as_customer', on_delete=models.CASCADE)
    pickup_location = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    total_distance = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='created')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # If pickup and destination provided and total_distance is 0, generate a random distance
        if self.pickup_location and self.destination and (not self.total_distance or self.total_distance == 0):
            self.total_distance = random.randint(10, 30)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Ride #{self.pk} by {self.customer} ({self.status})"


class RideEvent(models.Model):
    ride = models.ForeignKey(Ride, related_name='events', on_delete=models.CASCADE)
    step_count = models.PositiveIntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['step_count']

    def __str__(self):
        return f"Event {self.step_count} for Ride {self.ride_id}: {self.description[:30]}"
