from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse

# Create your views here.

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/')
  
        form = AuthenticationForm()
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
            form = UserCreationForm(request.POST)
            if form.is_valid():
                messages.add_message(request,messages.SUCCESS,'registeration is  successful!')
                form.save()
                return redirect('/accounts/login/')
            else:
                messages.add_message(request,messages.ERROR,'registeration is not successful!')
                return render(request, 'accounts/signup.html',{'form':form})
        else:
            form = UserCreationForm()
            return render(request, 'accounts/signup.html', {'form': form})
    else:
        return redirect('/')

