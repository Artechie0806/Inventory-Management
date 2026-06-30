from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Role(models.TextChoices):
        VENDOR = 'VENDOR', 'Vendor'
        MANAGER = 'MANAGER', 'Store Manager'
        CASHIER = 'CASHIER', 'Cashier'
        CUSTOMER = 'CUSTOMER', 'Customer'

    role = models.CharField(max_length=20, choices=Role.choices, default=Role.CUSTOMER)
    
    # Store vendor-specific info right on the user, or create a separate VendorProfile model
    company_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"