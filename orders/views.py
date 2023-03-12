from django.shortcuts import render
from django.views.generic import ListView
from .models import Order

# Create Order List .

class OrderListView(ListView):
    model = Order
    
    def get_queryset(self):
        data = Order.objects.filter(user= self.request.user)
        return data
    
def checkout(request):
    return render(request, 'orders/chekout.html', {})
    
    


