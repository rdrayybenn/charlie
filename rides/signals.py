from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Ride, RideEvent


@receiver(post_save, sender=Ride)
def create_initial_event(sender, instance, created, **kwargs):
    if created:
        # Create initial event
        RideEvent.objects.create(ride=instance, step_count=1, description='User created a ride.')


@receiver(pre_save, sender=Ride)
def create_event_on_status_change(sender, instance, **kwargs):
    if not instance.pk:
        return
    try:
        old = Ride.objects.get(pk=instance.pk)
    except Ride.DoesNotExist:
        return
    if old.status != instance.status:
        # Determine next step count
        last = instance.events.order_by('-step_count').first()
        next_step = (last.step_count + 1) if last else 1
        desc = 'Ride status changed.'
        if instance.status == 'assigned':
            desc = 'Rider accepted the ride.'
        elif instance.status == 'dropped':
            desc = 'Ride Complete'
        RideEvent.objects.create(ride=instance, step_count=next_step, description=desc)
