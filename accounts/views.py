from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from accounts.forms import SignupForm, LoginForm, ForgotPasswordForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse

# Create your views here.

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username_or_email = form.cleaned_data['username_or_email']
                password = form.cleaned_data['password']
                user = User.objects.filter(email=username_or_email).first()
                if user:
                    username = user.username
                else:
                    username = username_or_email

                user = authenticate(
                    request,
                    username=username,
                    password=password
                )
                if user is not None:
                    login(request, user)
                    return redirect('/')
  
        form = LoginForm()
        context = {'form':form}
        return render(request, 'accounts/login.html',context)
    else:
        return redirect('/')
        
@login_required
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')


def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                messages.add_message(request,messages.SUCCESS,'registeration is  successful!')
                form.save()
                return redirect('/accounts/login/')
            else:
                messages.add_message(request,messages.ERROR,'registeration is not successful!')
                return render(request, 'accounts/signup.html',{'form':form})
        else:
            form = SignupForm()
            return render(request, 'accounts/signup.html', {'form': form})
    else:
        return redirect('/')

def forgot_password(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            new_password = form.cleaned_data['password1']

            try:
                user = User.objects.get(username=username)
                user.set_password(new_password)
                user.save()
                messages.success(request, 'Password reset successful!')
                return redirect('/accounts/login/')
            except User.DoesNotExist:
                messages.error(request, 'User not found.')
        else:
            messages.error(request, 'Please correct the errors.')
    else:
        form = ForgotPasswordForm()

    return render(request, 'accounts/forgot_password.html', {'form': form})

