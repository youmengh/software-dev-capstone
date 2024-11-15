from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class NewsFeed(models.Model):  # This model is for displaying updates and news on the home page
    title = models.TextField()
    text = models.TextField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f'{self.title}'



class MemberProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Delete profile when user is deleted, this is username/password/email
    last_name = models.CharField(max_length=100, default="")
    first_name = models.CharField(max_length=100, default="")
    address = models.CharField(max_length=100, default="")
    phone_number = models.CharField(max_length=100, default="")
    date_of_birth = models.DateField(max_length=100, default="mm/dd/yy")
    in_directory = models.BooleanField()


    def __str__(self):
        return f'{self.user.username}\'s Profile' #show how we want it to be displayed
    
class PaymentInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=16, blank=True)
    CVV = models.CharField(max_length=3, blank=True)
    expiration_date = models.CharField(max_length=5, blank=True)
    payment_saved = models.BooleanField()
    initial_payment = models.BooleanField(default=False)
    yearly_payment_due = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user.username}\'s Payment Information' #show how we want it to be displayed

class Reservation(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    court = models.IntegerField(validators=[MaxValueValidator(12),MinValueValidator(1)])
    number_of_players = models.IntegerField(validators=[MaxValueValidator(4),MinValueValidator(1)])
    number_of_guests = models.IntegerField(validators=[MaxValueValidator(3),MinValueValidator(0)])
    is_tournament = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username}\'s Reservation' #show how we want it to be displayed
    
class Guest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=100, default="")
    first_name = models.CharField(max_length=100, default="")
    games_played = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.user.username}\'s Guest' #show how we want it to be displayed