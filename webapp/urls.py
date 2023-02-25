from django.contrib import admin
from django.urls import path

from webapp.views import *

urlpatterns = [
    path('', index),
    # path('company/', company, name='company'),
    path('company/', CompanyView.as_view(), name='company'),
    # path('company/<int:pk>/', company_detail, name='company_detail'),
    path('company/<int:pk>/', CompanyDetailView.as_view(), name='company_detail'),
    # path('about/', about, name='about'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('login/', CRMLogin.as_view(), name='login'),
]