from django.contrib import admin
from django.utils.html import format_html
from .models import Product, Customer

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'discounted_price', 'category', 'display_product_image']  # Use a method

    def display_product_image(self, obj):
        if obj.product_image:  # Ensure image exists
            return format_html('<img src="{}" width="50" height="50" />', obj.product_image.url)
        return "No Image"

    display_product_image.short_description = 'Product Image'  # Column name in admin panel


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user','locality','city','state','zipcode']