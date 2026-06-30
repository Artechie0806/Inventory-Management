from django.db import models
from django.conf import settings

class POSReceipt(models.Model):
    cashier = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, limit_choices_to={'role': 'CASHIER'})
    created_at = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

class POSLineItem(models.Model):
    receipt = models.ForeignKey(POSReceipt, on_delete=models.CASCADE, related_name='items')
    # Linking to StockBatch instead of Product ensures we deduct from the correct expiring batch
    batch = models.ForeignKey('stock.StockBatch', on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    price_at_sale = models.DecimalField(max_digits=10, decimal_places=2)