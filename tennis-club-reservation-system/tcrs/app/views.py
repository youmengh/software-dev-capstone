from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import NewsFeed
from .models import Account
# Create your views here.
# Function-based views defined here

def home_page(request):
    # template path
    template_name = 'home.html'

    # DISPLAYING NEWS FEED
    messages = NewsFeed.objects.all()
    context = {
        'messages': messages
    }

    return render(request, template_name, context)

def account_page(request):
    # template path
    template_name = 'accounts.html'
    return render(request, template_name)

def reservation_page(request):
    # template path
    template_name = 'reservations.html'
    return render(request, template_name)

def payment_page(request):
    # template path
    template_name = 'payment.html'
    return render(request, template_name)

def directory_page(request):
    # template path
    template_name = 'directory.html'

    # code to view accounts from the database
    accounts = Account.objects.all()
    context = {
        'accounts': accounts
    }
    # render the page
    return render(request, template_name, context)

def login_page(request):
    # template path
    template_name = 'login.html'
    return render(request, template_name)




# class-based views (LEGACY DO NOT USE)

# class HomePageView(TemplateView):   # method call for home page template
#     model = TestModel
#     template_name = "home.html"

# class AccountPageView(TemplateView):  # method call for account page template
#     template_name = "accounts.html"

# class ReservationPageView(TemplateView):  # method call for reservation page template
#     template_name = "reservations.html"

# class PaymentPageView(TemplateView):  # method call for payment page template
#     template_name = "payment.html"

 