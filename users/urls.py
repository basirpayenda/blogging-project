from django.urls import path
from . import views as users_view
from django.contrib.auth import views as auth_views


app_name = 'users'
urlpatterns = [
    path('register/', users_view.register, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', users_view.profile, name='profile'),
    path('update_profile/', users_view.UpdateProfile, name='update-profile'),

    # password reset
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='users/password_reset_complete.html'), name='password_reset_complete'),

    # change password
    path('change-password/', auth_views.PasswordChangeView.as_view(
        template_name='users/password_change.html'), name='password_change'),
    path('change-password/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='users/password_change_done.html'), name='password_change_done')
]
