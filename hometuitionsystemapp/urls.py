from django.urls import path
from .views import *
app_name = 'hometuitionsystemapp'

urlpatterns = [
    path('', ClientHomeView.as_view(), name='clienthome'),
    path("login/", ClientLoginView.as_view(), name="clientlogin"),
    path("register/", ClientRegisterView.as_view(), name="clientregister"),
    path("system_admin/", AdminHomeView.as_view(), name='adminhome'),
    path("logout/", AdminLogoutView.as_view(), name="adminlogout"),
    path("system_admin/hometuitionsystem/create/",
         AdminHomeTuitionSystemCreateView.as_view(), name="adminhometuitionsystemcreate"),
    path('system_admin/hometuitionsystem/list/',
         AdminHomeTuitionSystemListView.as_view(), name="adminhometuitionsystemlist"),
    path('system_admin/<int:pk>/hometuitionsystem/detail/',
         AdminHomeTuitionSystemDetailView.as_view(), name="adminhometuitionsystemdetail"),
    path('system_admin/<int:pk>/hometuitionsystem/update/',
         AdminHomeTuitionSystemUpdateView.as_view(), name="adminhometuitionsystemupdate"),
    path('system_admin/<int:pk>/hometuitionsystem/delete/',
         AdminHomeTuitionSystemDeleteView.as_view(), name="adminhometuitionsystemdelete"),

]
