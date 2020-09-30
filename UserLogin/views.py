from allauth.account.forms import ChangePasswordForm, LoginForm, SignupForm
from django.contrib import messages
from django.contrib.auth import (authenticate, login, logout,
                                 update_session_auth_hash)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import (HttpResponse, HttpResponseRedirect, redirect,
                              render)
from django.urls import reverse, reverse_lazy
from django.views import generic

from .forms import (ChangePasswordForm, CustomSignupForm, LoginForm,
                    MyCustomLoginForm, UpdateProfileForm)


class LoginView(generic.CreateView):
    form_class = MyCustomLoginForm
    template_name = 'account/login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(request=request)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request=request, data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'logged in successfully')
                return redirect('/')
            else:
                pass
        else:
            return HttpResponseRedirect('/')


class Index(generic.TemplateView):
    template_name = 'index.html'


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('UserLogin:login')
    template_name = 'account/signup.html'


class LogoutView(generic.View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect('/')


class ChangePasswordView(LoginRequiredMixin, generic.View):
    form_class = PasswordChangeForm
    template_name = 'account/change_password.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(user=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST, user=request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return HttpResponseRedirect('/')
        else:
            form = PasswordChangeForm(request.user)

        return render(request, self.template_name, {'form': form})


class UpdateProfileView(LoginRequiredMixin, generic.UpdateView):
    form_class = UpdateProfileForm
    template_name = 'account/profile_update.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial, instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UpdateProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
        else:
            form = UpdateProfileForm(instance=request.user)
        return render(request, self.template_name, {'form': form})
