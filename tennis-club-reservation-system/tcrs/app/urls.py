from django.urls import path
from . import views
from .views import HomePageView, AccountPageView, ReservationPageView, PaymentPageView

# defines url extensions for each page

urlpatterns = [ 
    path("account/", AccountPageView.as_view(), name="account"),
    path("reservations/", ReservationPageView.as_view(), name="reservations"),
    path("payment/", PaymentPageView.as_view(), name="payment"),
    path("", HomePageView.as_view(), name="home"), # default page, no extension specified
]