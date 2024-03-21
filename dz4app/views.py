from datetime import timezone, timedelta
from django.shortcuts import render, redirect
from dz4app.forms import ProductForm
from .models import Product, Order


# Create your views here.
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('save-success')  # Перенаправление после сохранения
    else:
        form = ProductForm()

    return render(request, 'add_product.html', {'form': form})

def view_name(request):
    return render(request, 'success.html')

def save_success(request):
    return render(request, 'success.html')