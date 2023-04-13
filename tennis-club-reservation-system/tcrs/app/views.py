from django.shortcuts import render, redirect
from .models import NewsFeed, MemberProfile, Reservation, PaymentInfo
from .forms import UserSignupForm, MemberInformationForm, PaymentInformationForm, ReservationForm, GuestForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
# Create your views here.


def home_page(request):
    # template path
    template_name = 'home.html'

    # DISPLAYING NEWS FEED
    messages = NewsFeed.objects.order_by('-date')
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
        profile = MemberProfile.objects.filter(first_name = request.user.memberprofile.first_name)
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
        profile = MemberProfile.objects.filter(first_name = request.user.memberprofile.first_name)
    except MemberProfile.DoesNotExist:
        is_member = False

    reservations = Reservation.objects.order_by('date')
    context = {
        'reservations': reservations,
        'is_member': is_member,
    }

    reservation_failed = False

    if request.method == 'POST':
            
            form = ReservationForm(request.POST)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = request.user
                selected_date = form.cleaned_data.get('date')
                selected_time = form.cleaned_data.get('time')
                selected_court = form.cleaned_data.get('court')
                if Reservation.objects.filter(date = selected_date).exists() and Reservation.objects.filter(time = selected_time).exists() and Reservation.objects.filter(court = selected_court).exists():
                    reservation_failed = True
                    messages.info(request, 'This reservation has already been taken!')
                else:
                    profile.save()
                # user.memberprofile.guest_count += user.reservation.number_of_guests
                context = {
                    'reservations': reservations,
                    'form': form,
                    'is_member': is_member,
                    'reservation_failed': reservation_failed
                }
                
                if profile.number_of_guests > 0 and not reservation_failed:
                    return redirect('guest_info')
                
    else:
        form = ReservationForm()
        context = {
            'reservations': reservations,
            'form': form,
            'is_member': is_member,
            'reservation_failed': reservation_failed
        }

    return render(request, template_name, context)

@login_required(login_url='signup')
def cancel_reservation(request):
    reservation = request.user.reservation
    reservation.delete()
    return redirect('account')


@login_required(login_url='signup')
def membership_page(request):
    # template path
    template_name = 'membership.html'

    # checks if member profile data exists, second level authentication for members only 
    is_member = True
    try:
        profile = MemberProfile.objects.filter(first_name = request.user.memberprofile.first_name)
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
def cancel_membership(request):
    profile = request.user.memberprofile
    profile.delete()
    return redirect('home')

@login_required(login_url='signup')
def directory_page(request):
    # template path
    template_name = 'directory.html'

    # checks if member profile data exists, second level authentication for members only 
    is_member = True
    try:
        profile = MemberProfile.objects.filter(first_name = request.user.memberprofile.first_name)
    except MemberProfile.DoesNotExist:
        is_member = False

    email = User.email

    # code to view accounts from the database
    profiles = MemberProfile.objects.order_by('last_name')
    users = User.objects.order_by('first_name')
    context = {
        'profiles': profiles,
        'users': users,
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
        profile = MemberProfile.objects.filter(first_name = request.user.memberprofile.first_name)
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
                profile.initial_payment = True
                profile.save()
                payment = PaymentInfo.objects.all()
                context = {
                    'form': form,
                    'is_member': is_member,
                    'payment': payment,
                }
                return redirect('home')
                
    else:
        form = PaymentInformationForm()
        payment = PaymentInfo.objects.all()
        context = {
            'form': form,
            'is_member': is_member,
            'payment': payment,
        }


    return render(request, template_name, context)

@login_required(login_url='signup')
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
 
@login_required(login_url='signup')
def billing_page(request):
     # template path
    template_name = 'billing.html'

    # checks if member profile data exists, second level authentication for members only 
    is_member = True
    try:
        profile = MemberProfile.objects.filter(first_name = request.user.memberprofile.first_name)
    except MemberProfile.DoesNotExist:
        is_member = False
    context = {
        'is_member': is_member,
    }

    # checks if user has a reservation to display, if no reservation view does not display My Reservations box
    user_reservation = True
    try:
        user_reservation = Reservation.objects.filter(court = request.user.reservation.court)
    except Reservation.DoesNotExist:
        user_reservation = False

    fee = 400
    if user_reservation:
        guest = (request.user.reservation.number_of_guests * 10)
    else:
        guest = 0
    total = fee + guest

    if request.method == 'POST':
            
            form = PaymentInformationForm(request.POST, instance=request.user.paymentinfo)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = request.user
                profile.yearly_payment_due = False
                profile.save()
                payment = PaymentInfo.objects.all()
                context = {
                    'form': form,
                    'is_member': is_member,
                    'payment': payment,
                    'fee': fee,
                    'guest': guest,
                    'total': total,
                }
                return redirect('home')
                
    else:
        form = PaymentInformationForm()
        payment = PaymentInfo.objects.all()
        context = {
            'form': form,
            'is_member': is_member,
            'payment': payment,
            'fee': fee,
            'guest': guest,
            'total': total,
        }


    return render(request, template_name, context)

@login_required(login_url='signup')
def guest_info_page(request):
    # template path
    template_name = 'guest_info.html'

    # checks if member profile data exists, second level authentication for members only 
    is_member = True
    try:
        profile = MemberProfile.objects.get(first_name = request.user.memberprofile.first_name)
    except MemberProfile.DoesNotExist:
        is_member = False
    context = {
        'is_member': is_member,
    }

    GuestFormSet = formset_factory(GuestForm, extra = request.user.reservation.number_of_guests)

    if request.method == 'POST':
            
        formset = GuestFormSet(request.POST)
      
        # print formset data if it is valid
        if formset.is_valid():
            for form in formset:
                if form.is_valid():
                    profile = form.save(commit=False)
                    profile.user = request.user
                    profile.save()
                    context = {
                        'formset': formset,
                        'is_member': is_member,
                    }
            return redirect('reservations')
                
    else:
        formset = GuestFormSet(request.POST or None)
        context = {
            'formset': formset,
            'is_member': is_member,
        }


    return render(request, template_name, context)