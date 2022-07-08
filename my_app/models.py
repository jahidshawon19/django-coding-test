
from django.db import models

# Create your models here.

class ProductImage(models.Model):
    title = models.CharField(max_length=150)
    photo = models.ImageField(blank=True, upload_to='images/', default='', null=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title) 

class ProductVarients(models.Model):
  
    color = models.CharField(max_length=150)
    size = models.CharField(max_length=50)


    def __str__(self):
        return str(self.color+"/"+self.size)


class Products(models.Model):
   
    title = models.CharField(max_length=150)
    sku = models.CharField(max_length=150)
    description = models.TextField()
    varients = models.ForeignKey(ProductVarients, on_delete=models.SET_NULL, null=True, default='') 
    price = models.FloatField()
    stock = models.IntegerField()
    photo = models.ForeignKey(ProductImage, on_delete=models.SET_NULL, null=True, default='') 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title) 

