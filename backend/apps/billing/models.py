from django.db import models
from core.models import BaseModel

class Invoice(BaseModel):
    """Invoice model."""
    STATUS_CHOICES = [('draft', 'Draft'), ('sent', 'Sent'), ('paid', 'Paid'), ('overdue', 'Overdue'), ('cancelled', 'Cancelled')]
    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE, related_name='invoices')
    invoice_number = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    issue_date = models.DateField()
    due_date = models.DateField()
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    paid_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    currency = models.CharField(max_length=3, default='EUR')
    created_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, related_name='created_invoices')
    class Meta:
        ordering = ['-created_at']
    def __str__(self):
        return self.invoice_number

class InvoiceLine(BaseModel):
    """Invoice line items."""
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='lines')
    description = models.CharField(max_length=255)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    class Meta:
        ordering = ['id']
    def __str__(self):
        return f"{self.invoice} - {self.description}"
