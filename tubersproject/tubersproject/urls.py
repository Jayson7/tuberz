from apps import views
from apps.views import Home
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name='home'),
]
