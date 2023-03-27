from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import NewsFeed, Account
from .forms import UserSignupForm
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

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

def membership_page(request):
    # template path
    template_name = 'membership.html'
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

def signup_page(request):
    # template path
    template_name = 'registration/signup.html'
    if request.method == 'POST':
            
            form = UserSignupForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Your account has been created! You are now able to log in.')
                return redirect('login')
    else:
        form = UserSignupForm()

    return render(request, template_name, {'form': form})


 