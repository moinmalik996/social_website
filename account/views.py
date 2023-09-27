from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import (LoginView, LogoutView, PasswordChangeView,
                                       PasswordChangeDoneView, PasswordResetView,
                                       PasswordResetDoneView, PasswordResetConfirmView,
                                       PasswordResetCompleteView)

from .models import Profile

from .forms import UserForm, UserRegistrationForm, UserEditForm, ProfileEditForm


def home(request):
    return render(request, 'accounts/home.html')

def user_login(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request,
                username=cd['username'],
                password=cd['password']
            )
            if user and user.is_active:
                login(request, user)
                return HttpResponse('User Authenticated')
            else:
                return HttpResponse('Disabeled Account')
        else:
            return HttpResponse('Invalid Form')
    else:
        form = UserForm()
    
    return render(request, 'accounts/login.html', {'form':form})

@login_required
def dashboard(request):

    data = dict()
    data['section'] = 'dashboard'
    return render(request, 'accounts/dashboard.html', data)

def register(request):

    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # set the new password
            new_user.set_password(user_form.cleaned_data['password'])

            # Now Saving It To Database
            new_user.save()

            # creating User Profile
            Profile.objects.create(user=new_user)
            data = {
                'new_user':new_user
            }
            return render(request, 'accounts/register_done.html', data)
    else:
        form = UserRegistrationForm()
        data = {
            'form':form
        }
    return render(request, 'accounts/register.html', data)

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')

            return redirect('dashboard')

        else:
            messages.error(request, 'Error updating your profile.')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)


    return render(
        request,
        'accounts/edit.html',
        {'userr_form':user_form,
         'profile_form': profile_form}
    )

class UserLoginView(LoginView):
    pass

class UserLogoutVieew(LogoutView):
    pass

class UserPasswordChangeView(PasswordChangeView):
    pass

class UserPasswordChangeDoneView(PasswordChangeDoneView):
    pass

class UserPasswordResetView(PasswordResetView):
    pass

class UserPasswordResetDoneView(PasswordResetDoneView):
    pass

class UserPasswordResetConfirmView(PasswordResetConfirmView):
    pass

class UserPasswordResetCompleteView(PasswordResetCompleteView):
    pass