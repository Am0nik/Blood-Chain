from django.contrib import admin
from django.urls import path
from .views import about, future, pricing, map,news

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about, name='about'),
    path('features/', future, name='features'),
    path('pricing/', pricing, name='pricing'),
    path('map/', map, name='map'),
    path('news/<int:id>/', news, name='news'),
]
