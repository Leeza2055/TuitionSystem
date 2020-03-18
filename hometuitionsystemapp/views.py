from django.views.generic import *
from .models import *


class ClientHomeView(TemplateView):
    template_name = 'clienttemplates/home.html'


class AdminHomeView(TemplateView):
    template_name = 'admintemplates/adminhome.html'


class AdminHomeTuitionSystemListView(ListView):
    template_name = "admintemplates/adminhometuitionsystemlist.html"
    queryset = HomeTuitionSystem.objects.all()
    context_object_name = "adminhometuitionsystemlist"
