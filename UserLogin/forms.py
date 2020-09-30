from allauth.account.forms import ChangePasswordForm, LoginForm, SignupForm
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User


class CustomSignupForm(SignupForm):

    class Meta:
        fields = '__all__'

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.save()
        return user

    def clean(self):
        super(CustomSignupForm, self).clean()
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and password != confirm_password:
            self._errors['password'] = self.error_class(
                ['Passwords don\'t match']
                )
        return self.cleaned_data


class MyCustomLoginForm(LoginForm):

    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)

    def login(self, *args, **kwargs):
        # Add your own processing here.
        # You must return the original result.
        return super(MyCustomLoginForm, self).login(*args, **kwargs)


class UpdateProfileForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super(UpdateProfileForm, self).__init__(*args, **kwargs)
