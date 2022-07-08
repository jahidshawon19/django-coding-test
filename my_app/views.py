
from django.shortcuts import redirect, render
from my_app.models import *
from .forms import *

# Create your views here.

def index(request):
    all_products = Products.objects.all()
    context ={
        'products':all_products,
    }
    return render( request, 'index.html', context) 


def addImage(request):
    form = ProductImageForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    
    context = {
        'form':form
    }
    return render(request, 'add_image.html', context)



def addProduct(request):
    form = ProductCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    
    context = {
        'form':form
    }
    return render(request, 'add_product.html', context)