from django.views.generic import *
from .models import *
from django.urls import reverse_lazy
from .forms import *


class ClientHomeView(TemplateView):
    template_name = 'clienttemplates/home.html'


class AdminHomeView(TemplateView):
    template_name = 'admintemplates/adminhome.html'


class AdminHomeTuitionSystemCreateView(CreateView):
    template_name = "admintemplates/adminhometuitionsystemcreate.html"
    form_class = HomeTuitionSystemCreateForm
    success_url = reverse_lazy(
        "hometuitionsystemapp:adminhometuitionsystemlist")


class AdminHomeTuitionSystemListView(ListView):
    template_name = "admintemplates/adminhometuitionsystemlist.html"
    queryset = HomeTuitionSystem.objects.all()
    context_object_name = "adminhometuitionsystemlist"


class AdminHomeTuitionSystemDetailView(DetailView):
    template_name = "admintemplates/adminhometuitionsystemdetail.html"
    model = HomeTuitionSystem
    context_object_name = "adminhometuitionsystemdetail"
