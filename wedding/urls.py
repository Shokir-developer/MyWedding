from django.urls import path
from .views import index, photos

urlpatterns = [
    path('', index, name='index'),
    path('photos/', photos, name='photos'),
]
