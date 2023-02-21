from django.urls import path
from . import views
from .views import HomePageView, AccountPageView, ReservationPageView

# defines url extensions for each page

urlpatterns = [ 
    path("account/", AccountPageView.as_view(), name="account"),
    path("reservations/", ReservationPageView.as_view(), name="reservations"),
    path("", HomePageView.as_view(), name="home"),
]