
from django.urls import path
from . import views

urlpatterns = [
    path('', views.CategoryListView.as_view(), name='category-create-view'),
    path('<int:pk>/', views.CategoryUpdateView.as_view(), name='category-update-view'),
]


