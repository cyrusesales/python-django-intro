from django.urls import path
from . import views # import view.py

app_name = 'posts'

urlpatterns = [
    path('', views.posts_list, name="list"), # homepage function in views.py
    path('<slug:slug>', views.post_page, name="page"), # use slug path converted, left and parameter
]