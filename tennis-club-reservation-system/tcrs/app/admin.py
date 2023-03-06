from django.contrib import admin

# Register your models here.

from .models import NewsFeed, User

admin.site.register(NewsFeed)
admin.site.register(User)
