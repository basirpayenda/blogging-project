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

    # change password
    path('change-password/', auth_views.PasswordChangeView.as_view(
        template_name='users/password_change.html'), name='password_change'),
    path('change-password/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='users/password_change_done.html'), name='password_change_done')
]
