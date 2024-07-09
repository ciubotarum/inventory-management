from django import views
from django.urls import path

urlpatterns = [
    path('', views.home_view, name='home'), 
    path('contact/', views.contact_view, name='contact'),
    path('contact/success', views.home_view, name='contact-success'),
]
