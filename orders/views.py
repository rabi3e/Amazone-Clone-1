from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Order, Cart, CartDetail
from product.models import Product


# Create Order List .

class OrderListView(ListView):
    model = Order
    
    def get_queryset(self):
        data = Order.objects.filter(user= self.request.user)
        return data


def add_to_cart(request):
    if request.method == 'POST' :
        product_id = request.POST['productid']
        quantity = request.POST['quantity']
        
        
        product = Product.objects.get(id=product_id)
        cart = Cart.objects.get(user=request.user , status='E')
        Cart_detail, created = CartDetail.objects.get_or_create(
            cart= cart,
            product = product
        )
        Cart_detail.quantity = int(quantity)
        Cart_detail.price = product.prix
        Cart_detail.total = int(quantity) * product.prix
        
        Cart_detail.save()
        
    return redirect (f'/products/{product.slug}')
        
        
        
        
    
   
def checkout(request):
    return render(request, 'orders/chekout.html', {})
    
    


