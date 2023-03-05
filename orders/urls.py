from django.urls import path
from .views import OrderListView


app_name = 'product'

urlpatterns = [
    path('', OrderListView.as_view(),name='OrderList'),

]
