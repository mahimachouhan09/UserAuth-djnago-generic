from django.contrib.auth.views import (PasswordResetCompleteView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView,
                                       PasswordResetView)
from django.urls import path

from . import views
from .views import (ChangePasswordView, Index, LoginView, LogoutView,
                    SignUpView, UpdateProfileView)

app_name = 'UserLogin'
urlpatterns = [
  path('', Index.as_view(), name='index'),
  path('signup/', SignUpView.as_view(), name='signup'),
  path('login/', LoginView.as_view(), name='login'),
  path('logout/', LogoutView.as_view(), name='logout'),
  path(
    'change_password/', ChangePasswordView.as_view(), name='change_password'),
  path('update-profile/', UpdateProfileView.as_view(), name='profile_update'),
]
