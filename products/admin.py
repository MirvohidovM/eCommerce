from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Products, ProductsCategory


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):

    list_display = ['name', 'author', 'image_tag']
    readonly_fields = ['image_tag']

admin.site.register(ProductsCategory)