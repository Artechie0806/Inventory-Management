from django.db import models
from django.conf import settings

class OnlineOrder(models.Model):
    class Status(models.TextChoices):
        CART = 'CART', 'In Cart'
        PAID = 'PAID', 'Paid & Processing'
        SHIPPED = 'SHIPPED', 'Shipped'

    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, limit_choices_to={'role': 'CUSTOMER'})
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.CART)
    created_at = models.DateTimeField(auto_now_add=True)
    shipping_address = models.TextField(blank=True, null=True)

class OnlineOrderItem(models.Model):
    order = models.ForeignKey(OnlineOrder, on_delete=models.CASCADE, related_name='items')
    # We can link to the general Product here, and figure out which batch to deduct from at checkout
    product = models.ForeignKey('stock.Product', on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    price_at_sale = models.DecimalField(max_digits=10, decimal_places=2)