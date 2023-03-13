from django.urls import path
from .views import OrderListView, checkout


app_name = 'product'

urlpatterns = [
    path('', OrderListView.as_view(),name='OrderList'),
    path('chekout', checkout,name='checkout'),

]
