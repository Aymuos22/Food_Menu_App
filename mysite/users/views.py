from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages
from django.views import View
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import RegisterForm,ProfileEditForm

def register(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'welcome {username}, Your Account is Created')
            return redirect('food:index')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')  
    else:
        form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'users/edit_profile.html', {'form': form})

@login_required
def profilepage(request):
    return render(request,'users/profile.html')