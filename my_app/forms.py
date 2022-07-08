from dataclasses import field
from django import forms 
from .models import ProductImage, Products 

class ProductImageForm(forms.ModelForm):
    class Meta: 
        model = ProductImage 
        fields = ['title', 'photo']



class ProductCreateForm(forms.ModelForm):
    class Meta: 
        model = Products 
        fields = ['title', 'sku', 'description', 'varients', 'price', 'stock', 'photo']


class ProductUpdateForm(forms.ModelForm):
    class Meta: 
        model = Products 
        fields = ['title', 'sku', 'description', 'varients', 'price', 'stock', 'photo']


class productSearchForm(forms.ModelForm):
    class Meta:
        model = Products 
        fields = ['title', 'varients']