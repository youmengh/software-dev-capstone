from django.urls import re_path, include
from django.urls import path
from django.contrib import admin
from . import views

# defines url extensions for each page

urlpatterns = [ 

    # URLS for function-based views
    path("", views.home_page, name='home'),
    path("account/", views.account_page, name='account'),
    path("reservations/", views.reservation_page, name='reservations'),
    path("membership/", views.membership_page, name='membership'),
    path("directory/", views.directory_page, name='directory'),
    path("signup/", views.signup_page, name="signup"),

    
]

