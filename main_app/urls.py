from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dash_index, name='index'),
    path('dashboard/profile', views.update_profile, name='profile_update'),
    path('appointments/', views.appointments_index, name='appointments_index'),
    path('accounts/signup', views.signup, name='signup'),
]