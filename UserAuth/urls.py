from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import (PasswordResetCompleteView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView,
                                       PasswordResetView)
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('UserLogin.urls')),
    path('accounts/', include('allauth.urls')),
    path('password-reset/', PasswordResetView.as_view(
        template_name='account/password_reset.html'), name='password_reset'),
    path('password_reset_done', PasswordResetDoneView.as_view(
        template_name='account/password_reset_done.html'),
        name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='account/password_reset_confirm.html'),
        name='password_reset_confirm'),
    path('password_reset_complete', PasswordResetCompleteView.as_view(
        template_name='account/password_reset_complete.html'),
        name='password_reset_complete'),
]
