from django.urls import path
from .views import upload_csv, search_csv

urlpatterns = [
    path('upload/', upload_csv, name='upload_csv'),
    path('search/', search_csv, name='search_csv'),
]
