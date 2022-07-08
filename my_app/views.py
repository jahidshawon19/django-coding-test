
from math import prod
from django.shortcuts import redirect, render
from my_app.models import *
from .forms import *

# Create your views here.

def index(request):
    all_products = Products.objects.all()
    form = productSearchForm(request.POST or None)
    if request.method == 'POST':
        all_products = Products.objects.filter(title__icontains=form['title'].value(), varients__icontains=form['varients'].value())
    context ={
        'products':all_products,
        'form':form,
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

def updateProduct(request, pk):
    query = Products.objects.get(id=pk)
    form = ProductUpdateForm(instance=query)
    if request.method == 'POST':
        form = ProductUpdateForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context ={
        'form':form,
    }
    return render(request, 'add_product.html', context)


def deleteProduct(request, pk):
    query = Products.objects.get(id=pk)
    if request.method == 'POST':
        query.delete()
        return redirect('home')
    return render(request, 'delete.html')