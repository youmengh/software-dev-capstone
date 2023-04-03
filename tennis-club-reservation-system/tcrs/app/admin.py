from django.contrib import admin

# Register your models here.

from .models import NewsFeed, MemberProfile, PaymentInfo

admin.site.register(NewsFeed)
admin.site.register(MemberProfile)
admin.site.register(PaymentInfo)
