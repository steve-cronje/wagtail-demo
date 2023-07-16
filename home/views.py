from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.views.generic import FormView
from .forms import RegisterForm, LoginForm
# from wagtail.url_routing import 
from django.contrib.auth import get_user_model, login, authenticate, logout

User = get_user_model()

class Register(FormView):

    form_class = RegisterForm
    template_name = "home/auth/register.html"
    success_url = "/redirect-1"
    # success_url "/my-details/"

    # I decided to make the redirect in Wagtail Admin's redirects page,
    # because I think its more accurate, incase the URL for the myDetailsPage is not "/my-details/" (default)

    def form_valid(self, form):

        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']

        # default django authentication system gets upset if you don't set a username.
        # just gonna set username as email and move on.

        user, created = User.objects.get_or_create(username=email)
        if created:
            user.email = email
            user.first_name = first_name
            user.last_name = last_name
            user.set_password(password)
            user.save()

            login(self.request, user)
            return super().form_valid(form)
        else:
            return HttpResponse("This email is taken!")   
      

class Login(FormView):

    form_class = LoginForm
    template_name = "home/auth/login.html"
    success_url = "/redirect-1"
    # success_url "/my-details/"

    # I decided to make the redirect in Wagtail Admin's redirects page,
    # because I think its more accurate, incase the URL for the myDetailsPage is not "/my-details/" (default)

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(username=email, password=password)
        if user:
            login(self.request, user)

        return super().form_valid(form)


def user_logout(request: HttpRequest):
    if request.POST:
        logout(request)
        return HttpResponseRedirect("/")
    else:
        return render(request, "home/auth/logout.html")
	

