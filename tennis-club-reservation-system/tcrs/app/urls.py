from django.urls import re_path, include
from django.urls import path
from django.contrib import admin
from . import views

# from .views import HomePageView, AccountPageView, ReservationPageView, PaymentPageView

# defines url extensions for each page

urlpatterns = [ 

    # URLS FOR class-based views (LEGACY DO NOT USE)

    # path("account/", AccountPageView.as_view(), name="account"),
    # path("reservations/", ReservationPageView.as_view(), name="reservations"),
    # path("payment/", PaymentPageView.as_view(), name="payment"),
    # path("", HomePageView.as_view(), name="home"), # default page, no extension specified

    # URLS for function-based views
    path("", views.home_page, name='home'),
    path("account/", views.account_page, name='account'),
    path("reservations/", views.reservation_page, name='reservations'),
    path("payment/", views.payment_page, name='payment'),
    path("directory/", views.directory_page, name='directory'),
    path("login/", views.login_page, name='login'),
]

