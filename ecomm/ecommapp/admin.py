from django.contrib import admin
from .models import *
# from .models import Product
# from .models import ProductImage
# # Register your models here.

admin.site.register(Category)
# list_display=['category_name']

class ProductImageAdmin(admin.StackedInline):
    model=ProductImage

class ProductAdmin(admin.ModelAdmin):
    list_display=['product_name','price']
    inlines=[ProductImageAdmin]

admin.site.register(Product,ProductAdmin)



admin.site.register(ProductImage)


