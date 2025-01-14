"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views # import view.py
from django.conf.urls.static import static # import to upload image
from django.conf import settings # import to upload image

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage), # homepage function in views.py
    path('about/', views.about), # about page function in views.py
    path('posts/', include('posts.urls')) # to look inside posts app
]

# used both imported at the top to use in url patterns
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)