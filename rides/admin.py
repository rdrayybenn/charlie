from django.contrib import admin
from .models import Ride, RideEvent


@admin.register(Ride)
class RideAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'rider', 'status', 'price', 'total_distance', 'created_at')
    list_filter = ('status',)


@admin.register(RideEvent)
class RideEventAdmin(admin.ModelAdmin):
    list_display = ('ride', 'step_count', 'description', 'created_at')
