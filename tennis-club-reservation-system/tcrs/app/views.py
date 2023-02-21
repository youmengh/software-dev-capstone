from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):   # method call for home page template
    template_name = "home.html"

class AccountPageView(TemplateView):  # method call for account page template
    template_name = "accounts.html"