from django.contrib import admin

# Register your models here.
from . models import *


@admin.register(Category) 
class CategoryAdmin(admin.ModelAdmin):
    list_filter = ('created_at',)
    list_display = ('name','slug', 'created_at')
    search_fields = ['name',]
    prepopulated_fields = {'slug':('name',) }


@admin.register(Product) 
class ProductAdmin(admin.ModelAdmin):
    list_filter = ('category','created_at')
    list_display = ('name','image_tag','category','price','slug', 'created_at')
    search_fields = ['name',]
    prepopulated_fields = {'slug':('name',) }

