from django.urls import re_path as url
from .views import first_stage

urlpatterns = [
    url(r'', first_stage.as_view()),  
]
