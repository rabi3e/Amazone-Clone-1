from django.urls import path
from .views import OrderListView, checkout, add_to_cart


app_name = 'product'

urlpatterns = [
    path('', OrderListView.as_view(),name='OrderList'),
    path('chekout', checkout,name='checkout'),
    path('add-to-cart', add_to_cart,name='add_to_cart'),

]
