
from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', views.CustomUserListView.as_view(), name='register-user-view'),
    path('register/', views.RegisterCustomUserView.as_view(), name='register-user-view'),
    path('<int:pk>/', views.CustomUserDetailView.as_view(), name='user-update-view'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]


