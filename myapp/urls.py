
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/', views.post_view, name='post'),
    path('success/', views.success, name='success'),
]
