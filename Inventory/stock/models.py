from django.db import models
from django.conf import settings
from datetime import date

class Product(models.Model):
    vendor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'role': 'VENDOR'})
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=100, unique=True)
    barcode = models.CharField(max_length=100, unique=True)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name

class StockBatch(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='batches')
    quantity = models.PositiveIntegerField(default=0)
    received_date = models.DateField(auto_now_add=True)
    expiry_date = models.DateField(null=True, blank=True)

    @property
    def is_expiring_soon(self):
        # Example logic: if expiring in less than 7 days
        if self.expiry_date:
            return (self.expiry_date - date.today()).days <= 7
        return False

class PurchaseOrder(models.Model):
    class Status(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        DISPATCHED = 'DISPATCHED', 'Dispatched'
        RECEIVED = 'RECEIVED', 'Received'

    manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='po_created')
    vendor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='po_received')
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)

class PurchaseOrderItem(models.Model):
    order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    requested_quantity = models.PositiveIntegerField()