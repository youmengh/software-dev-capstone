from django.db import models
from django.contrib.auth.models import User

class NewsFeed(models.Model):  # This model is for displaying updates and news on the home page
    text = models.TextField()


class MemberProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Delete profile when user is deleted, this is username/password/email
    last_name = models.CharField(max_length=100, default="lastname")
    first_name = models.CharField(max_length=100, default="firstname")
    address = models.CharField(max_length=100, default="address")
    phone_number = models.CharField(max_length=100, default="phone")
    date_of_birth = models.DateField(max_length=100, default="dob")

    def __str__(self):
        return f'{self.user.username} Profile' #show how we want it to be displayed

class Object(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    
    def __str__(self):
        return self.title
    
class PaymentInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=16)
    cvv = models.CharField(max_length=3)
    expiration_date = models.CharField(max_length=5)
    payment_saved = models.BooleanField()
