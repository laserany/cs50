from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cart/", views.cart, name="cart"),
    path("place_order/", views.place_order, name="place_order"),
    path("view_orders/", views.view_orders, name="view_orders"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.register, name='register')
]
