from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import MemberProfile, PaymentInfo, Reservation, Guest


class UserSignupForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User 
		fields = ['username', 'email', 'password1', 'password2']

class MemberInformationForm(forms.ModelForm):
	
	class Meta:
		model = MemberProfile
		fields = ['first_name', 'last_name', 'phone_number', 'address', 'date_of_birth', 'in_directory']

class PaymentInformationForm(forms.ModelForm):
	
	class Meta:
		model = PaymentInfo
		fields = ['card_number', 'CVV', 'expiration_date', 'payment_saved']


class ReservationForm(forms.ModelForm):
	
	class Meta:
		model = Reservation
		fields = ['date', 'time', 'court', 'number_of_players', 'number_of_guests']

class GuestForm(forms.ModelForm):
	
	class Meta:
		model = Guest
		fields = ['first_name', 'last_name']