from django.urls import path
from . import views

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('menu-items/', views.MenuItemView.as_view(), name='menu'),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view(), name='single_menu_item'),
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth')
]

