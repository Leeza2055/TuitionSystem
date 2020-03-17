from django.urls import path
from .views import *
appname = 'hometuitionsystemapp'

urlpatterns = [
    path('', HomeView.as_view(), name='home')
]
