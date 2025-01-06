from django.urls import path
from . import views # import view.py

urlpatterns = [
    path('', views.posts_list), # homepage function in views.py
]