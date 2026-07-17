from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('patients/', views.patients_view, name='patients'),
    path('delete-patient/<int:id>/', views.delete_patient, name='delete_patient'),

    path('doctors/', views.doctors_view, name='doctors'),
    path('delete-doctor/<int:id>/', views.delete_doctor, name='delete_doctor'),

    path('appointments/', views.appointments_view, name='appointments'),
    path('delete-appointment/<int:id>/', views.delete_appointment, name='delete_appointment'),
]