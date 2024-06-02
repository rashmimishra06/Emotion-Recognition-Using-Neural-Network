from django.urls import path
from django.conf.urls.static import static
from .views import handler, uploading

urlpatterns = [
    path('home/', handler, name='homepage'),
    path('home/upload', uploading, name='upload')
    ]