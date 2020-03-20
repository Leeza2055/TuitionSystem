from django.urls import path
from .views import *
app_name = 'hometuitionsystemapp'

urlpatterns = [
    path('', ClientHomeView.as_view(), name='clienthome'),



    path("system_admin/", AdminHomeView.as_view(), name='adminhome'),
    path("system_admin/hometuitionsystem/create/",
         AdminHomeTuitionSystemCreateView.as_view(), name="adminhometuitionsystemcreate"),

    path('system_admin/hometuitionsystem/list/',
         AdminHomeTuitionSystemListView.as_view(), name="adminhometuitionsystemlist"),
    path('system_admin/<int:pk>/hometuitionsystem/detail/',
         AdminHomeTuitionSystemDetailView.as_view(), name="adminhometuitionsystemdetail"),

]
