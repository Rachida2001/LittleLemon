from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),  # Default index path
    path('menu/items/', views.MenuItemView.as_view(), name='menu-list-create'),  # For menu items list and create
    path('menu/items/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-detail'),  # For individual menu items
]

