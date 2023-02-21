from django.urls import path
from . import views
from .views import HomePageView, AccountPageView 

# defines url extensions for each page

urlpatterns = [ 
    path("account/", AccountPageView.as_view(), name="account"),
    path("", HomePageView.as_view(), name="home"),
]