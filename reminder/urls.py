from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.register, name='register')
]