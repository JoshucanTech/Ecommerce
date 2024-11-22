
from django.urls import path
from . import views

urlpatterns = [
    path('', views.OrderListView.as_view(), name='order-create-view'),
    path('<int:pk>/', views.OrderUpdateView.as_view(), name='order-update-view'),
    path('items/', views.OrderItemListView.as_view(), name='order-item-create-view'),
    path('items/<int:pk>/', views.OrderItemUpdateView.as_view(), name='order-item-update-view'),
]


