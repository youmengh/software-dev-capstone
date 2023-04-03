from django.contrib import admin

# Register your models here.

from .models import NewsFeed, MemberProfile, PaymentInfo, Reservation

admin.site.register(NewsFeed)
admin.site.register(MemberProfile)
admin.site.register(PaymentInfo)
admin.site.register(Reservation)
