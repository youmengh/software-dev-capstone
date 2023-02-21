from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):   # method call for home page template
    template_name = "home.html"

class AccountPageView(TemplateView):  # method call for account page template
    template_name = "accounts.html"

class ReservationPageView(TemplateView):  # method call for reservation page template
    template_name = "reservations.html"

class PaymentPageView(TemplateView):  # method call for payment page template
    template_name = "payment.html"