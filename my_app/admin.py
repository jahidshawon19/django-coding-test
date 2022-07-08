from django.contrib import admin
from .models import ProductImage
from .models import ProductVarients
from .models import Products
# Register your models here.

admin.site.register(ProductImage)
admin.site.register(ProductVarients)
admin.site.register(Products)
