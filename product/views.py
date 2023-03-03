from django.shortcuts import render, redirect
from .models import *
from django.views.generic import ListView, DetailView
from .forms import ProductReviewForm

class ProductList(ListView):
    model = Product
    paginate_by = 50
    extra_context = {'all_prod': Product.objects.all().count()}
  

class ProductDetail(DetailView):
    model = Product
    
    def get_context_data(self, **kwargs):
        product = self.get_object()
        context = super().get_context_data(**kwargs)
        context["related_product"] = Product.objects.filter(brand=product.brand )[:10] #pour limiter le nombre des produits cible a 10
        return context
    
    
    
def add_review (request,slug):
    product =  Product.objects.get(slug=slug)
    if request.method == 'POST':
        form = ProductReviewForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user =  request.user
            myform.product = product
            myform.save()
    
    return redirect(f'/products/{product.slug}')
    
class BrandList(ListView):
    model = Brand
    paginate_by = 20
    extra_context = {'all_brand': Brand.objects.all().count()}
  


