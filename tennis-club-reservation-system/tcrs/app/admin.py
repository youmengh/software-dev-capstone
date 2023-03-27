from django.contrib import admin

# Register your models here.

from .models import NewsFeed, MemberProfile

admin.site.register(NewsFeed)
admin.site.register(MemberProfile)
