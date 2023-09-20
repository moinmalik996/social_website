from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

from .forms import UserForm


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
    return render(request, 'registration/dashboard.html', data)

class UserLoginView(LoginView):
    pass

class UserLogoutVieew(LogoutView):
    pass