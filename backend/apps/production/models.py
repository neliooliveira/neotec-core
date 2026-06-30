from django.db import models
from core.models import BaseModel

class Order(BaseModel):
    """Customer orders."""
    STATUS_CHOICES = [('pending', 'Pending'), ('processing', 'Processing'), ('shipped', 'Shipped'), ('delivered', 'Delivered'), ('cancelled', 'Cancelled')]
    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE, related_name='orders')
    order_number = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    currency = models.CharField(max_length=3, default='EUR')
    created_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, related_name='created_orders')
    class Meta:
        ordering = ['-created_at']
    def __str__(self):
        return self.order_number

class OrderItem(BaseModel):
    """Items in an order."""
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('products.Product', on_delete=models.SET_NULL, null=True, related_name='order_items')
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=12, decimal_places=2)
    unit_cost = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    class Meta:
        unique_together = ('order', 'product')
    def __str__(self):
        return f"{self.order} - {self.product}"
