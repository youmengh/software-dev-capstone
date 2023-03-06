from django.db import models

class NewsFeed(models.Model):  # This model is for displaying updates and news on the home page
    text = models.TextField()

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=100, default="lastname")
    first_name = models.CharField(max_length=100, default="firstname")
    address = models.CharField(max_length=100, default="address")
    phone_number = models.CharField(max_length=100, default="phone")
    email = models.CharField(max_length=100, default="email")
    date_of_birth = models.CharField(max_length=100, default="dob")

# returns name of entry in model lists instead of <model>_object
def __str__(self):  # new
        return self.text[:50]

