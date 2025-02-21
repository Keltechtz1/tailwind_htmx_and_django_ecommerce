from django.contrib import admin

# Register your models here.
from . models import *


@admin.register(Order) 
class OrderAdmin(admin.ModelAdmin):
    list_filter = ('is_paid','status')
    list_display = ('user','status', 'paid_amount','is_paid','created_at')
    search_fields = ['first_name','last_name']


class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ('product','quantity','price')


@admin.register(OrderItem) 
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order','product','quantity','price')
    

