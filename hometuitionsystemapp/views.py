from django.views.generic import *
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from .forms import *


class ClientHomeView(TemplateView):
    template_name = 'clienttemplates/home.html'


class ClientLoginView(FormView):
    template_name = "clienttemplates/login.html"
    form_class = LoginForm
    success_url = reverse_lazy("hometuitionsystemapp:adminhome")

    def form_valid(self, form):
        uname = form.cleaned_data["username"]
        pword = form.cleaned_data["password"]
        user = authenticate(username=uname, password=pword)
        if user is not None:
            login(self.request, user)
        else:
            return render(self.request, "clienttemplates/login.html",
                          {
                              "error": "Invalid username or password", "form": form
                          })
        return super().form_valid(form)


class ClientRegisterView(TemplateView):
    template_name = "clienttemplates/register.html"


class AdminRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticted:
            return redirect("/login/")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sys'] = HomeTuitionSystem.object.first()
        return context


class AdminHomeView(TemplateView):
    template_name = 'admintemplates/adminhome.html'


class AdminLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("/")


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


class AdminHomeTuitionSystemUpdateView(UpdateView):
    template_name = "admintemplates/adminhometuitionsystemcreate.html"
    form_class = HomeTuitionSystemCreateForm
    success_url = reverse_lazy(
        "hometuitionsystemapp:adminhometuitionsystemlist")
    model = HomeTuitionSystem


class AdminHomeTuitionSystemDeleteView(DeleteView):
    template_name = "admintemplates/adminhometuitionsystemdelete.html"
    success_url = reverse_lazy(
        "hometuitionsystemapp:adminhometuitionsystemlist")
    model = HomeTuitionSystem
