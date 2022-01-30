from apps import views
from apps.views import Home
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name='home'),
    path('high', views.Large, name='large'),
    path('low', views.Small, name='small'),
    
]
