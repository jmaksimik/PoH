"""poh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_app.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/login/', include('django.contrib.auth.urls'), name='login'),
    # path('accounts/logout/', include('django.contrib.auth.urls'), name='logout'),
    # path('accounts/password_change/', include('django.contrib.auth.urls'), name='password_change'),
    # path('accounts/password_change/done/', include('django.contrib.auth.urls'), name='password_change_done'),
    # path('accounts/password_reset/', include('django.contrib.auth.urls'), name='password_reset'),
    # path('accounts/password_reset/done/', include('django.contrib.auth.urls'), name='password_reset_done'),
    # path('accounts/reset/<uidb64>/<token>/', include('django.contrib.auth.urls'), name='password_reset_confirm'),
    # path('accounts/reset/done/', include('django.contrib.auth.urls'), name='password_reset_complete'),
]
