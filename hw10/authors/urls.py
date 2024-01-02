# authors/urls.py
from django.urls import path

from . import views

app_name = 'authors'

urlpatterns = [
    path('<str:author_id>/', views.main, name="root"),
    path('<int:author_id>/', views.author_list, name='author_list'),
]

