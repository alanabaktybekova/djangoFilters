from django.shortcuts import render, redirect
from .models import *
from .filters import ProductFilter
from .forms import ProductForm


def home(request):
    query = Product.objects.all()
    filter = ProductFilter(request.GET, queryset=query)
    query = filter.qs
    form = ProductFilter(request.GET, queryset=query).form
    return render(request, 'index.html', {'products': query, 'form': form})


def create_product(request):
    form = ProductForm
    if request.method == 'POST':
        form = ProductForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print(form.errors)
    return render(request, 'create.html', {'form': form})