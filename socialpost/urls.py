from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Ensure 'home' is defined in views.py
    path('post/', views.post_view, name='post'),  # Ensure 'post_view' is defined in views.py
    path('success/', views.success, name='success'),
]
