from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    USER_ROLES = (
        ('customer', 'Customer'),
        ('rider', 'Rider'),
        ('staff', 'Staff'),
    )

    middle_name = models.CharField(max_length=150, blank=True)
    user_role = models.CharField(max_length=20, choices=USER_ROLES, default='customer')
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.username} ({self.user_role})"
