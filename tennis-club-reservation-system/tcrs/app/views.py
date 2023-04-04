from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import NewsFeed, MemberProfile, Object, Reservation
from .forms import UserSignupForm, MemberInformationForm
from .models import NewsFeed, MemberProfile
from .forms import UserSignupForm, MemberInformationForm, PaymentInformationForm, ReservationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
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

@login_required(login_url='signup')
def account_page(request):
    # template path
    template_name = 'accounts.html'

    # checks if member profile data exists, second level authentication for members only 
    is_member = True
    try:
        profile = MemberProfile.objects.get(first_name = request.user.memberprofile.first_name)
    except MemberProfile.DoesNotExist:
        is_member = False

    # checks if user has a reservation to display, if no reservation view does not display My Reservations box
    user_reservation = True
    try:
        user_reservation = Reservation.objects.filter(court = request.user.reservation.court)
    except Reservation.DoesNotExist:
        user_reservation = False
    
    # code to view profile info from the database
    profile = MemberProfile.objects.all()
    context = {
        'profile': profile,
        'is_member': is_member,
        'user_reservation': user_reservation,
    }
    # render the page
    return render(request, template_name, context)

@login_required(login_url='signup')
def reservation_page(request):
    # template path
    template_name = 'reservations.html'

    # checks if member profile data exists, second level authentication for members only 
    is_member = True
    try:
        profile = MemberProfile.objects.get(first_name = request.user.memberprofile.first_name)
    except MemberProfile.DoesNotExist:
        is_member = False

    reservations = Reservation.objects.all()
    context = {
        'reservations': reservations,
        'is_member': is_member,
    }

    if request.method == 'POST':
            
            form = ReservationForm(request.POST)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = request.user
                profile.save()
                # user.memberprofile.guest_count += user.reservation.number_of_guests
                context = {
                    'reservations': reservations,
                    'form': form,
                    'is_member': is_member,
                }
                return redirect('reservations')
                
    else:
        form = ReservationForm()
        context = {
            'reservations': reservations,
            'form': form,
            'is_member': is_member,
        }

    return render(request, template_name, context)

@login_required(login_url='signup')
def membership_page(request):
    # template path
    template_name = 'membership.html'

    # checks if member profile data exists, second level authentication for members only 
    is_member = True
    try:
        profile = MemberProfile.objects.get(first_name = request.user.memberprofile.first_name)
    except MemberProfile.DoesNotExist:
        is_member = False
    context = {
        'is_member': is_member,
    }

    if request.method == 'POST':
            
            form = MemberInformationForm(request.POST)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = request.user
                profile.save()
                context = {
                    'form': form,
                    'is_member': is_member,
                }
                return redirect('payment')
                
    else:
        form = MemberInformationForm()
        context = {
            'form': form,
            'is_member': is_member,
        }


    return render(request, template_name, context)

@login_required(login_url='signup')
def directory_page(request):
    # template path
    template_name = 'directory.html'

    # checks if member profile data exists, second level authentication for members only 
    is_member = True
    try:
        profile = MemberProfile.objects.get(first_name = request.user.memberprofile.first_name)
    except MemberProfile.DoesNotExist:
        is_member = False

    email = User.email

    # code to view accounts from the database
    profiles = MemberProfile.objects.all()
    context = {
        'profiles': profiles,
        'is_member': is_member,
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
                messages.success(request, f'Your account has been created!')
                return redirect('login')
    else:
        form = UserSignupForm()

    return render(request, template_name, {'form': form})

@login_required(login_url='signup')
def payment_page(request):
    # template path
    template_name = 'payment.html'

    # checks if member profile data exists, second level authentication for members only 
    is_member = True
    try:
        profile = MemberProfile.objects.get(first_name = request.user.memberprofile.first_name)
    except MemberProfile.DoesNotExist:
        is_member = False
    context = {
        'is_member': is_member,
    }

    if request.method == 'POST':
            
            form = PaymentInformationForm(request.POST)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = request.user
                profile.save()
                context = {
                    'form': form,
                    'is_member': is_member,
                }
                return redirect('home')
                
    else:
        form = PaymentInformationForm()
        context = {
            'form': form,
            'is_member': is_member,
        }


    return render(request, template_name, context)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {'form': form})
 
