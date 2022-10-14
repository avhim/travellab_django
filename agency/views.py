from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View

from .forms import AgencyForm, form_validation_error, LoginForm, SignUpForm
from .models import Agency


@method_decorator(login_required(login_url='login'), name='dispatch')
class AgencyDetailView(View):
    agency = None

    def dispatch(self, request, *args, **kwargs):
        self.agency, __ = Agency.objects.get_or_create(user=request.user)
        return super(AgencyDetailView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        context = {'agency': self.agency, 'segment': 'agency'}
        return render(request, 'agency/profile.html', context)

    def post(self, request):
        form = AgencyForm(request.POST, instance=self.agency)

        if form.is_valid():
            agency = form.save()
            agency.user.email = form.cleaned_data.get('email')
            agency.user.save()

            messages.success(request, 'Профиль успешно обновлен')
        else:
            messages.error(request, form_validation_error(form))
        return redirect('agency-profile')


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/agency/profile/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "registration/login.html", {"form": form, "msg": msg})


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "registration/register.html", {"form": form, "msg": msg, "success": success})
