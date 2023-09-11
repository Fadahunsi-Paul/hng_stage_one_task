from django.urls import path
from . import views

urlpatterns = [
    path('json_endpoint/', views.json_endpoint, name='endpoint'),  
]
