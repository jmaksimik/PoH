from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dash_index, name='index'),
    path('dashboard/profile', views.update_profile, name='profile_update'),
    path('appointments/', views.appointments_index, name='appointments_index'),
    path('appointments/<int:pk>/', views.AppointmentDetail.as_view(), name='appointments_detail'),
    path('appointments/create/', views.AppointmentCreate.as_view(), name='appointments_create'),
	path('appointments/<int:pk>/update/', views.AppointmentUpdate.as_view(), name='appointments_update'),
	path('appointments/<int:pk>/delete/', views.AppointmentDelete.as_view(), name='appointments_delete'),
    path('prescriptions/', views.prescriptions_index, name='prescriptions_index'),
    path('prescriptions/create/', views.PrescriptionCreate.as_view(), name='prescriptions_create'),
    path('prescriptions/<int:user_id>/add_prescription/', views.add_prescription, name='add_prescription'),
    path('documents/', views.documents_index, name='documents_index'),
    path('accounts/signup', views.signup, name='signup'),
    path('provider/', views.provider_search, name='provider_search'),
    path('insurance/', views.insurance_index, name='insurance_index'),

    
]