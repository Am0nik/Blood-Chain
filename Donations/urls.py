from django.contrib import admin
from django.urls import path
from .views import  map,news

urlpatterns = [
    path('admin/', admin.site.urls),
    path('map/', map, name='map'),
    path('news/<int:id>/', news, name='news'),
]
