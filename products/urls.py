
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='list-create-view'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='update-view'),
]


