from django.urls import path

from .views import *
urlpatterns = [
    path('', index, name='homepage'),
    path('requests/', RequestView.as_view(), name='requests'),
    path('admin/', sotrudnic, name='sotrudnic'),
]