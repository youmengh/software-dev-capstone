from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import MemberProfile

class UserSignupForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User 
		fields = ['username', 'email', 'password1', 'password2']

class MemberInformationForm(forms.ModelForm):
	
	class Meta:
		model = MemberProfile
		fields = ['first_name', 'last_name', 'phone_number', 'address', 'date_of_birth']