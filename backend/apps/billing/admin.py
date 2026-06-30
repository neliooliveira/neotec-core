from django.contrib import admin
from .models import Invoice, InvoiceLine
@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoice_number', 'project', 'status', 'total_amount', 'issue_date')
@admin.register(InvoiceLine)
class InvoiceLineAdmin(admin.ModelAdmin):
    list_display = ('invoice', 'description', 'quantity', 'unit_price', 'amount')
