from django.urls import path
from . import views

urlpatterns = [
    path('', views.Dashboard, name='Dashboard'),
    path('VaccinationCenter', views.VaccinationCenter, name='VaccinationCenter'),
    path('Statistics', views.Statistics, name='Statistics'),
    path('ContactForm', views.ContactForm, name='ContactForm'),
]
