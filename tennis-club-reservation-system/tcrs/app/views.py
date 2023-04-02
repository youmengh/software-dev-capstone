from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import NewsFeed, MemberProfile, Object
from .forms import UserSignupForm, MemberInformationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from calendar import HTMLCalendar
from datetime import datetime
# Create your views here.

class Calendar(HTMLCalendar):
    def __init__(self, objects):
        super().__init__()
        self.objects = objects

    def formatday(self, day, weekday): 
        if day == 0:
            return '<td class="noday">&nbsp;</td>' #day outside the appropriate month
        else:
            cssclass = self.cssclasses[weekday]
            if datetime.now().day == day and datetime.now().month == self.month:
                cssclass += ' today'
            objects_html = ''
            for obj in self.objects:
                if obj.date.day == day and obj.date.month == self.month:
                    objects_html += f'<li>{obj.title}</li>'
            return f'<td class="{cssclass}"><span class="day-number">{day}</span><ul>{objects_html}</ul></td>'

def calendar_view(request, year, month):
    objects = Object.objects.filter(date__year=year, date__month=month)
    cal = ObjectCalendar(objects).formatmonth(int(year), int(month))
    return render(request, 'reservations.html', {'calendar': cal})

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
    
    # code to view profile info from the database
    profile = MemberProfile.objects.all()
    context = {
        'profile': profile,
        'is_member': is_member,
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
    context = {
        'is_member': is_member,
    }

    return render(request, template_name, context)

@login_required(login_url='signup')
def membership_page(request):
    # template path
    template_name = 'membership.html'

    if request.method == 'POST':
            
            form = MemberInformationForm(request.POST)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = request.user
                profile.save()
                return redirect('home')
    else:
        form = MemberInformationForm()

    return render(request, template_name, {'form': form})

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