from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from users.forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, RegisterForm
from django.contrib.auth.models import User

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account created successfuly, log in as {username}')
            return redirect('users:login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')


@login_required
def UpdateProfile(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST, instance=request.user)
        profile_form = ProfileForm(
            request.POST, request.FILES, instance=request.user.profile)

        if register_form.is_valid() and profile_form.is_valid():
            register_form.save()
            profile_form.save()
            messages.success(request, 'Profile has been updated successfully!')
            return redirect('users:profile')
    else:
        register_form = RegisterForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    context = {
        'register_form': register_form,
        'profile_form': profile_form
    }

    return render(request, 'users/edit_profile.html', context)
