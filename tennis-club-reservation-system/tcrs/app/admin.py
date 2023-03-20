from django.contrib import admin

# Register your models here.

from .models import NewsFeed, Account

admin.site.register(NewsFeed)
admin.site.register(Account)
