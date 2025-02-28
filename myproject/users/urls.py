from django.urls import path
from . import views # import view.py

app_name = 'users'

urlpatterns = [
    path('register/', views.register_view, name="register"), # homepage function in views.py
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
]