from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'


class ProductCreateView(CreateView):
    model = Product
    template_name = 'product_form.html'
    fields = ['name', 'description', 'price']


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product_form.html'
    fields = ['name', 'description', 'price']


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('products') 


def all_products(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})
