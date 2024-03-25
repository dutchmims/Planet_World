from django.contrib import admin
from .models import Item, Customer, Order

# Register your models here.

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'address')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'total_price', 'created_at')
    readonly_fields = ('total_price',)
    filter_horizontal = ('items',)  # Allows selecting items in a more user-friendly way
