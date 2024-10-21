from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm
from django.views.generic import ListView
from .models import Product


def home_view(request):
    return render(request, template_name='sweet_market_place14_app/home.html')


def upload_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ProductForm()
    return render(request, 'sweet_market_place14_app/upload_product.html', {'form': form})


class ProductListView(ListView):
    model = Product
    template_name = 'sweet_market_place14_app/products.html'


def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['product'] = context['object_list']
    return context


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'sweet_market_place14_app/product.html', {'product': product})
